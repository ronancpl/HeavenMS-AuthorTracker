import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from authorconstants import AuthorConstantLimit
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
import AuthorScanJsonReader
import math
import os.path


result_path_name = AuthorGraphResultFile.ResultFile.COMMIT_FILE_SIZE_GROWTH


lastGitTreeStack = []


def fetchFileExtensionIndex(filename):
    return {
        '.java': 1,
        '.js': 2,
        '.xml': 3,
    }.get(os.path.splitext(filename)[1], 4)


def bsearch_tree(tree_data, search_path):
    st = 0
    en = len(tree_data) - 1

    while st <= en:
        m = math.floor((st + en) / 2)
        item_path = tree_data[m]['path']

        if search_path < item_path:
            en = m - 1
        elif search_path > item_path:
            st = m + 1
        else:
            return m

    return -1


def locateFilesystemItem(fileTree, path):
    if fileTree is None:
        return None

    idx = bsearch_tree(fileTree, path)
    if idx != -1:
        return fileTree[idx]
    else:
        return None


def calculateFileDelta(lastFile, thisFile, thisCommitDate, thisTreePath):
    if lastFile is not None:
        lastFile['parsed'] = 1
        ret = abs(thisFile['size'] - lastFile['size'])
    else:
        ret = thisFile['size']

    is_file_dump = scanner.isCommitFileDump(thisCommitDate, thisTreePath + thisFile['path'], True)
    if is_file_dump:
        return 0
    else:
        return ret


def countGitTreeFileChanges(commitDate, fileTree, changeCount, treePath):
    for file in fileTree:
        if file['type'] != 'tree':
            idx = fetchFileExtensionIndex(file['path'])

            lastGitFile = locateFilesystemItem(lastGitTreeStack[len(lastGitTreeStack) - 1], file['path'])
            delta = calculateFileDelta(lastGitFile, file, commitDate, treePath)

            changeCount[0] += delta
            changeCount[idx] += delta
        else:
            lastGitTreeCursor = locateFilesystemItem(lastGitTreeStack[len(lastGitTreeStack) - 1], file['path'])
            if lastGitTreeCursor is not None:
                lastGitTreeCursor = lastGitTreeCursor['tree']

            lastGitTreeStack.append(lastGitTreeCursor)
            countGitTreeFileChanges(commitDate, file['tree'], changeCount, treePath + file['path'] + '/')
            lastGitTreeStack.pop()


def resolveMissingFiles(commitDate, gitTree, changeCount, treePath):
    for item in gitTree:
        if item['type'] != 'tree':
            if 'parsed' not in item:
                idx = fetchFileExtensionIndex(item['path'])

                delta = calculateFileDelta(None, item, commitDate, treePath)
                changeCount[0] += delta
                changeCount[idx] += delta
        else:
            resolveMissingFiles(commitDate, item['tree'], changeCount, treePath + item['path'] + '/')


def countGitTreeChanges(commitDate, gitTree):
    changeCount = [0, 0, 0, 0, 0]

    countGitTreeFileChanges(commitDate, gitTree, changeCount, '')
    # resolveMissingFiles(commitDate, lastGitTree, changeCount, '') | don't count changes from removed files

    '''
        treeitems = ''
        for it in gitTree:
            treeitems += (it['path'] + ', ')
        print('this2 tree: (' + treeitems + ')')
    '''

    lastGitTreeStack.clear()
    lastGitTreeStack.append(gitTree)

    return changeCount


def updateFileChanges(commitTree, changeCount):
    for i in range(len(changeCount)):
        commitTree[i] += changeCount[i]


def sortFilesystemData(tree):
    new_tree = []

    sort_tree = sorted(tree, key=lambda k: k['path'])
    for item in sort_tree:
        if item['type'] == 'tree':
            item['tree'] = sortFilesystemData(item['tree'])

        new_tree.append(item)

    return new_tree


def limitFileGrowth(commitFileGrowthItem):
    for idx in range(len(commitFileGrowthItem)):
        if commitFileGrowthItem[idx] > AuthorConstantLimit.WrapLimit.COMMIT_DIFF_SIZE_LIMIT.getValue():
            commitFileGrowthItem[idx] = 0


def calculateCommitChanges():
    fs_vals = []
    for fs_key, fs_val in sorted(scanner.filesystem.items(), key=lambda kv: kv[0]):   # commit entries in chronological order
        fs_vals.append(fs_val)

    fs_db = scanner.generateSequenceSectionDatabase(fs_vals, ['commit_time'], scanner.getCommitTimestamps('commits/'), debug=False)

    commitFileGrowth = []

    lastGitTreeStack.clear()
    lastGitTreeStack.append([]) # before first commit is an empty filesystem

    for idx in range(len(fs_db)):
        fs_db_range = fs_db[idx]
        commitFileGrowthItem = [0, 0, 0, 0, 0]

        if len(fs_db_range) > 0:
            commitFileGrowth.append({'commit_time': fs_db_range[0]['commit_time'], 'diff_size_count': commitFileGrowthItem})

            for fs_db_item in fs_db_range:
                if fs_db_item['commit_time'] in scanner.authoredTimestamps:
                    item_ct = fs_db_item['content'][0]['content']
                    sorted_item_ct = sortFilesystemData(item_ct)

                    commit_date = AuthorScanJsonReader.AuthorScanJsonReader().getDateFilestamp(fs_db_item['commit_time'])
                    changeCount = countGitTreeChanges(commit_date, sorted_item_ct)
                    updateFileChanges(commitFileGrowthItem, changeCount)

            limitFileGrowth(commitFileGrowthItem)   # SHORTCUT -

    return commitFileGrowth


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    growthCount = calculateCommitChanges()

    graph_content = growthCount

    print()
    print('file size')
    for commitGrowthItem in growthCount:
        print(str(commitGrowthItem['commit_time']) + ' ' + str(commitGrowthItem['diff_size_count']))

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
