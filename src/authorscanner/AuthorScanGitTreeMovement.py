# from authorscanner import AuthorScanRepository
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import math
import os.path
import base64
import json
import AuthorScanJsonReader
from authorconstants import AuthorConstantLimit
from authorscanner import AuthorScanRepository


def readGitCommitTreeFile(diffDirPath, commitSha):
    lines = []
    for line in open(diffDirPath + commitSha + '.txt', encoding='UTF-8'):
        lines.append(line)

    return lines


def generateGitCommitFilesDiff(commitDiffData):
    fileDiff = []
    commitFilesDiff = []
    for line in commitDiffData:
        if line.startswith('diff --git '):
            commitFilesDiff.append(fileDiff)
            fileDiff = [line]
        else:
            fileDiff.append(line)

    commitFilesDiff.append(fileDiff)
    commitFilesDiff.pop(0)

    return commitFilesDiff


def generateGitCommitFallbackFile(filePath):
    fileDiff = []
    fileDiff.append('diff --git a/' + filePath + ' b/' + filePath)
    fileDiff.append('similarity index 100% (diff too long)')
    fileDiff.append('rename from ' + filePath + '\n')
    fileDiff.append('rename to ' + filePath + '\n')

    return fileDiff


def generateGitCommitFallbackTree(fallbackFileDiffs, treePath, fileTree):
    for file in fileTree:
        if file['type'] != 'tree':
            filePath = treePath + file['path']
            fallbackFileDiffs.append(generateGitCommitFallbackFile(filePath))
        else:
            generateGitCommitFallbackTree(fallbackFileDiffs, treePath + file['path'] + '/', file['tree'])


def generateGitCommitFallback(commitSha):
    gitDate = AuthorScanJsonReader.AuthorScanJsonReader().getDateFilestamp(scanner.commits[commitSha]['commit']['author']['date'])
    gitTree = scanner.filesystem[gitDate]['content'][0]['content']

    scanner.commitdump_fallback_date.add(gitDate)

    fallbackFileDiffs = []
    generateGitCommitFallbackTree(fallbackFileDiffs, '', gitTree)

    return fallbackFileDiffs


def generateGitCommitTree(diffDirPath, commitSha):
    commitDiffData = readGitCommitTreeFile(diffDirPath, commitSha)
    if len(commitDiffData) == 1 and commitDiffData[0].startswith('error: too big or took too long to generate'):
        commitFilesDiff = generateGitCommitFallback(commitSha)
    else:
        commitFilesDiff = generateGitCommitFilesDiff(commitDiffData)

    return commitFilesDiff


def processFileDiffType(fileDiffHeader):
    indexType = fileDiffHeader[1]

    if indexType.startswith('new file'):
        return 2
    elif indexType.startswith('similarity index'):
        return 3
    elif indexType.startswith('deleted file'):
        return 1

    return 0


def processFileDiff(fileDiff, commitNextTreeFiles):
    fileRes = {}

    headerLines = []
    i = 0
    diffLen = len(fileDiff)
    while i < diffLen:
        line = fileDiff[i]
        i += 1

        if line.startswith('@@'):
            i += 1
            break

        headerLines.append(line)

    fileRes['type'] = processFileDiffType(headerLines)
    if fileRes['type'] == 3:
        fileRes['fromPath'] = headerLines[2][12:-1]     # removing line-feed
        fileRes['path'] = headerLines[3][10:-1]

        commitNextTreeFiles.append((fileRes['path'], fileRes['fromPath']))
    else:
        basePath = headerLines[0]
        a_idx = basePath.find(' a/') + 3
        b_idx = basePath.find(' b/', a_idx)

        fileRes['path'] = basePath[a_idx:b_idx]

        if fileRes['type'] != 1:
            toPath = basePath[b_idx + 3:-1]
        else:
            toPath = 'dev/null'

        commitNextTreeFiles.append((toPath, toPath))

    rawAdd = 0
    rawDel = 0

    while i < diffLen:
        if fileDiff[i][0] == '+':
            rawAdd += 1
        elif fileDiff[i][0] == '-':
            rawDel += 1

        i += 1

    if rawAdd > rawDel:
        fileAdd = rawAdd - rawDel
        fileDel = 0
        fileChange = rawDel
    else:
        fileAdd = 0
        fileDel = rawDel - rawAdd
        fileChange = rawAdd

    diff_rate_limit_type = AuthorConstantLimit.WrapLimit.FILE_EMPTY_DIFFS_MAXRATE
    diff_rate_limit = diff_rate_limit_type.getValue()

    rawAddDel = rawAdd + rawDel
    if (rawAddDel != 0 and abs((rawAdd / rawAddDel) - 0.5) < diff_rate_limit):  # possible empty diff
        fileChange = 0

    fileRes['add_count'] = fileAdd
    fileRes['del_count'] = fileDel
    fileRes['change_count'] = fileChange

    if diffLen == 1 and fileDiff[0].startswith('Binary file'):
        fileRes['is_binary'] = 1

    return fileRes


def processCommitFileDiff(commitFilesDiff, gitCommitSha):
    commitFileDeltas = []
    commitNextTreeFiles = []
    commitFilesDiffNotes = {}

    for fileDiff in commitFilesDiff:
        fileRes = processFileDiff(fileDiff, commitNextTreeFiles)
        commitFileDeltas.append(fileRes)
        commitFilesDiffNotes[fileRes['path']] = fileDiff

    return commitFileDeltas, commitNextTreeFiles, commitFilesDiffNotes


def parseRepositoryGitTreeMovement():
    gitCommitTreeMovement = {}
    gitCommitUpdatedFiles = {}
    gitCommitFilesDiffs = {}

    gitCommits = scanner.commits_info
    for gitCommit in gitCommits:
        gitDate = AuthorScanJsonReader.AuthorScanJsonReader().getDateFilestamp(gitCommit['commit']['author']['date'])
        gitDiff = generateGitCommitTree('../../lib/diffs/', gitCommit['sha'])

        gitCommitDelta, gitCommitNextTreeFiles, gitCommitFilesDiffNotes = processCommitFileDiff(gitDiff, gitCommit['sha'])

        gitCommitTreeMovement[gitDate] = {'sha': gitCommit['sha'], 'commit_time': scanner.parseFileTimestampToStringTimestamp(gitDate), 'content': gitCommitDelta}
        gitCommitUpdatedFiles[gitCommit['sha']] = gitCommitNextTreeFiles

        gitCommitFilesDiffs[gitCommit['sha']] = gitCommitFilesDiffNotes

    return gitCommitTreeMovement, gitCommitUpdatedFiles, gitCommitFilesDiffs


class AuthorScanGitTreeMovement:

    def scanRepositoryGitMovement(self):

        global scanner
        scanner = AuthorScanRepository.scanner

        return parseRepositoryGitTreeMovement()

