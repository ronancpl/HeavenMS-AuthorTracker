import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import AuthorScanJsonReader
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
import math
import os.path


result_path_name = AuthorGraphResultFile.ResultFile.CONTENT_FILE_COUNT_GROWTH


def fetchFileExtensionIndex(filename):
    return {
        '.java': 1,
        '.js': 2,
        '.xml': 3,
    }.get(os.path.splitext(filename)[1], 4)


def countGitTreeFiles(commitDate, treePath, fileTree, fileCount):
    for file in fileTree:
        if file['type'] != 'tree':
            idx = fetchFileExtensionIndex(file['path'])
            filePath = treePath + file['path']

            is_file_dump = scanner.isCommitFileDump(commitDate, filePath, True)
            if is_file_dump:
                continue

            fileCount[0] += 1
            fileCount[idx] += 1
        else:
            countGitTreeFiles(commitDate, treePath + file['path'] + '/', file['tree'], fileCount)


def countGitTree(commitDate, gitTree):
    fileCount = [0, 0, 0, 0, 0]             # ['Overall', 'Java', 'Javascript', 'XML', 'Others']

    countGitTreeFiles(commitDate, '', gitTree, fileCount)

    return fileCount


def updateFileGrowth(trees, idx, fileCount):
    if fileCount[0] > trees[idx][0]:        # evaluates the max total of files of each "season"
        for i in range(len(fileCount)):
            trees[idx][i] = fileCount[i]


def calculateFileGrowth():
    fs_vals = []
    for fs_key, fs_val in sorted(scanner.filesystem.items(), key=lambda kv: kv[0]):  # commit entries in chronological order
        fs_vals.append(fs_val)

    fs_db = scanner.generateTimeSectionDatabase(fs_vals, ['commit_time'], months=3, days=0, debug=False)

    repoFileCount = []
    for idx in range(len(fs_db)):
        repoFileCount.append([0, 0, 0, 0, 0])

    for idx in range(len(fs_db)):
        for fs_db_item in fs_db[idx]:
            fs_db_tree = fs_db_item['content'][0]['content']

            commit_date = AuthorScanJsonReader.AuthorScanJsonReader().getDateFilestamp(fs_db_item['commit_time'])
            fileCount = countGitTree(commit_date, fs_db_tree)
            updateFileGrowth(repoFileCount, idx, fileCount)

    return repoFileCount


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    treeCount = calculateFileGrowth()

    graph_content = treeCount

    print()
    print('File count growth')
    print(treeCount)

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
