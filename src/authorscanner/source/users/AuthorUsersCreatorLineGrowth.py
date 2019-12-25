import AuthorScanJsonReader
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
from authorconstants import AuthorConstantLimit
import os.path


result_path_name = AuthorGraphResultFile.ResultFile.CREATOR_LINE_GROWTH

lib_path = "../../lib/"


def fetchFileExtensionIndex(filename):
    return {
        '.java': 1,
        '.js': 2,
        '.xml': 3,
    }.get(os.path.splitext(filename)[1], 4)


def updateFileTypeChanges(fileTypeCount, file_stats, is_file_dump):
    if is_file_dump:
        fileTypeCount[0] += 0
        fileTypeCount[1] += 0
        fileTypeCount[2] += 0
    else:
        fileTypeCount[0] += file_stats['add_count']
        fileTypeCount[1] += file_stats['del_count']
        fileTypeCount[2] += file_stats['change_count']


def updateFileTypeStats(fileTypeGrowth, commit_date, file_stats, commit_file_dump_count):
    file_path = file_stats['path']

    file_type = fetchFileExtensionIndex(file_path)
    is_file_dump = scanner.isCommitFileDump(commit_date, file_path, False)
    if is_file_dump:
        commit_file_dump_count[0] += 1
        # print('File dump "' + file_stats['path'] + '" on commit ' + commit_file_dump_count[1])    # SHORTCUT?

    updateFileTypeChanges(fileTypeGrowth[0], file_stats, is_file_dump)
    updateFileTypeChanges(fileTypeGrowth[file_type], file_stats, is_file_dump)


def generateEmptyCommitChangesGrowth(value):
    commitLineGrowth = []
    for i in range(5):  # all file types
        commitLineGrowth.append([value, value, value])  # add, delete, change

    return commitLineGrowth


def updateFileTypeRangeGrowth(rangeTypeGrowth, fileTypeGrowth):
    for i in range(len(rangeTypeGrowth)):
        for j in range(len(rangeTypeGrowth[i])):
            rangeTypeGrowth[i][j] += fileTypeGrowth[i][j]


def calculateCommitChanges():
    fs_vals = []
    for fs_key, fs_val in sorted(scanner.diffs.items(), key=lambda kv: kv[0]):   # commit entries in chronological order
        fs_vals.append(fs_val)

    fs_db = scanner.generateTimeSectionDatabase(fs_vals, ['commit_time'], months=3, days=0)

    repoFileTypeGrowth = []
    for fs_db_range in fs_db:
        rangeTypeGrowth = generateEmptyCommitChangesGrowth(0)    # changes from all commits for the same file type

        for fs_db_commit in fs_db_range:
            if fs_db_commit['commit_time'] in scanner.authoredTimestamps:
                item_ct = fs_db_commit['content']
                fileTypeGrowth = generateEmptyCommitChangesGrowth(0)

                commit_date = AuthorScanJsonReader.AuthorScanJsonReader().getDateFilestamp(fs_db_commit['commit_time'])
                commit_file_dump_count = [0, commit_date]
                for commit_diff_file in item_ct:
                    updateFileTypeStats(fileTypeGrowth, commit_date, commit_diff_file, commit_file_dump_count)

                if commit_file_dump_count[0] > AuthorConstantLimit.WrapLimit.WARN_COMMIT_FILE_DUMPS_COUNT.getValue():
                    print('Commit dump ' + commit_file_dump_count[1] + ' ' + str(commit_file_dump_count[0]))
                    fileTypeGrowth = generateEmptyCommitChangesGrowth(0)

                updateFileTypeRangeGrowth(rangeTypeGrowth, fileTypeGrowth)

        repoFileTypeGrowth.append(rangeTypeGrowth)

    return repoFileTypeGrowth


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    commitGrowthCount = calculateCommitChanges()

    graph_content = commitGrowthCount

    print()
    print('Line growth')

    i = 0
    for commit_time in commitGrowthCount:
        print('Month ' + str(3 * i) + ' :')
        print('  .all   -> add: ' + str(commit_time[0][0]) + ' del: ' + str(commit_time[0][1]) + ' change: ' + str(commit_time[0][2]))
        print('  .java  -> add: ' + str(commit_time[1][0]) + ' del: ' + str(commit_time[1][1]) + ' change: ' + str(commit_time[1][2]))
        print('  .js    -> add: ' + str(commit_time[2][0]) + ' del: ' + str(commit_time[2][1]) + ' change: ' + str(commit_time[2][2]))
        print('  .xml   -> add: ' + str(commit_time[3][0]) + ' del: ' + str(commit_time[3][1]) + ' change: ' + str(commit_time[3][2]))
        print('  .other -> add: ' + str(commit_time[4][0]) + ' del: ' + str(commit_time[4][1]) + ' change: ' + str(commit_time[4][2]))
        print()

        i += 1

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
