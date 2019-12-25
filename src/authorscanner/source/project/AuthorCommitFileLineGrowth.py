import AuthorScanJsonReader
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
from authorconstants import AuthorConstantLimit
import os.path


result_path_name = AuthorGraphResultFile.ResultFile.COMMIT_FILE_LINE_GROWTH


def fetchFileExtensionIndex(filename):
    return {
        '.java': 1,
        '.js': 2,
        '.xml': 3,
    }.get(os.path.splitext(filename)[1], 4)


def updateFileChanges(commitTypeCount, commit_file, is_file_dump):
    if is_file_dump:
        commitTypeCount[0] += 1
        commitTypeCount[1] += 1
        commitTypeCount[2] += 1
    else:
        commitTypeCount[0] += commit_file['add_count']
        commitTypeCount[1] += commit_file['del_count']
        commitTypeCount[2] += commit_file['change_count']


def updateCommitFileChanges(commitFileGrowth, commit_date, commit_file, commit_file_dump_count):
    file_path = commit_file['path']

    file_type = fetchFileExtensionIndex(file_path)
    is_file_dump = scanner.isCommitFileDump(commit_date, file_path, False)
    if is_file_dump:
        commit_file_dump_count[0] += 1
        # print('File dump "' + commit_file['path'] + '" on commit ' + commit_file_dump_count[1])   # SHORTCUT?

    commit_count = commitFileGrowth['diff_count']
    updateFileChanges(commit_count[0], commit_file, is_file_dump)
    updateFileChanges(commit_count[file_type], commit_file, is_file_dump)


def generateEmptyCommitChangesGrowth(value):
    commitLineGrowth = []
    for i in range(5):  # all file types
        commitLineGrowth.append([value, value, value])  # add, delete, change

    return commitLineGrowth


def calculateCommitChanges():
    fs_vals = []
    for fs_key, fs_val in sorted(scanner.diffs.items(), key=lambda kv: kv[0]):   # commit entries in chronological order
        fs_vals.append(fs_val)

    fs_db = scanner.generateSequenceSectionDatabase(fs_vals, ['commit_time'], scanner.getCommitTimestamps('commits/'), debug=False)

    commitFileGrowth = []
    for fs_db_range in fs_db:
        if len(fs_db_range) == 0:
            commitFileGrowth.append({})
            continue

        commitLineGrowth = generateEmptyCommitChangesGrowth(0)
        commitFileGrowth.append({'commit_time': fs_db_range[0]['commit_time'], 'diff_count': commitLineGrowth})

    for idx in range(len(fs_db)):
        fs_db_range = fs_db[idx]
        commitFileGrowthItem = commitFileGrowth[idx]

        for fs_db_item in fs_db_range:
            if fs_db_item['commit_time'] in scanner.authoredTimestamps:
                item_ct = fs_db_item['content']

                commit_date = AuthorScanJsonReader.AuthorScanJsonReader().getDateFilestamp(fs_db_item['commit_time'])
                commit_file_dump_count = [0, commit_date]
                for commit_file in item_ct:
                    updateCommitFileChanges(commitFileGrowthItem, commit_date, commit_file, commit_file_dump_count)

                if commit_file_dump_count[0] > AuthorConstantLimit.WrapLimit.WARN_COMMIT_FILE_DUMPS_COUNT.getValue():
                    # print('Commit dump ' + commit_file_dump_count[1])
                    commitFileGrowthItem['diff_count'] = generateEmptyCommitChangesGrowth(0)

    return commitFileGrowth


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    commitGrowthCount = calculateCommitChanges()

    graph_content = commitGrowthCount
    print()
    print('file line')

    for commitCount in commitGrowthCount:
        if len(commitCount) == 0:
            continue

        print(str(commitCount['commit_time']) + ' : ' + str(commitCount['diff_count']))

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
