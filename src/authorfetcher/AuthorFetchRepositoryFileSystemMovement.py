#### UNUSED ####

# from authorscanner import AuthorScanRepository
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta

import os.path
import base64
import math
import requests
import sys
import time
import traceback
import difflib
import json
import AuthorScanJsonReader


# exit values
EXIT_OK = 0
EXIT_FAIL = 7


MIN_DRCT = 0.5
MIN_FILE = 0.4


def loadAuthToken():
    file = open("C:/Nexon/auth.txt", 'r')
    tokens = file.read().splitlines()
    return tokens


def getNextLink(r):
    try:
        link = r.headers['link']
    except KeyError:
        link = None

    if link is None:
        return None

    # Should be a comma separated string of links
    links = link.split(',')

    for link in links:
        # If there is a 'next' link return the URL between the angle brackets, or None
        if 'rel="next"' in link:
            return link[link.find("<") + 1:link.find(">")]
    return None


def getRequestCall(nextLink, apiParams):
    global auth

    while True:
        try:
            reqGet = requests.get(nextLink, headers=apiParams, auth=(auth[1], auth[0]))

            if 'X-RateLimit-Remaining' in reqGet.headers and int(reqGet.headers['X-RateLimit-Remaining']) < 1:
                print('RateLimit exceeded for this hour...')

                time.sleep(max(20,float(reqGet.headers['X-RateLimit-Reset']) - float(datetime.utcnow().timestamp())))
                continue

            return reqGet
        except requests.exceptions.ConnectionError or ConnectionRefusedError:
            print('Connection lost. Retrying...')
            time.sleep(20)


def getRequest(nextLink, apiParams):
    global reqGet

    reqGet = getRequestCall(nextLink, apiParams)
    return reqGet


def levenshteinDistance(s1, s2):    # thanks to SalvadorDali at https://stackoverflow.com/questions/2460177/edit-distance-in-python
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


def fetchGitTreeDiff(missingContent, changedContent, pathStr, srcTree, dstTree):
    # unpack tree by definition
    srcTree = srcTree[0]
    dstTree = dstTree[0]

    for key, value in srcTree.items():     # locating removed, moved or renamed contents within source versions
        if key in dstTree:
            dstVal = dstTree[key]
            if isinstance(dstVal, list):    # assumption: there will not have the case where a file and a directory will share the same path
                nextPathStr = pathStr + key + '.'
                fetchGitTreeDiff(missingContent, changedContent, nextPathStr, value, dstVal)
            else:
                if value['size'] != dstVal['size']:
                    changedContent[pathStr + key] = (value, abs(value['size'] - dstVal['size']))    # tuple: file descriptor, changed bytes
        else:
            missingContent[pathStr + key] = value


apiParams = {'per_page': '100'}


def decodeGitBlobContent(content):
    return str(base64.b64decode(content), encoding='UTF-8', errors='replace')


def getGitBlobContent(item):
    global apiParams

    r = getRequest(item['url'], apiParams)

    # extracting data in json format
    data = r.json()

    if data['encoding'] == 'base64':
        return decodeGitBlobContent(data['content'])
    else:
        print('Encoding ' + data['encoding'] + ' for url ' + item['url'] + ' not supported')
        return ''


def getGitTreeItemContent(cachedContents, pathItem, item):
    if pathItem in cachedContents:
        content = cachedContents[pathItem]
    else:
        content = getGitBlobContent(item)
        cachedContents[pathItem] = content

    return content


previousContents = {}
currentContents = {}


def getItemLikelihood(pathItem, previousItem, currentItem, currentMatch):
    if previousItem['size'] == currentItem['size']:
        return 1.0

    prevContent = getGitTreeItemContent(previousContents, pathItem, previousItem)
    currContent = getGitTreeItemContent(currentContents, currentMatch, currentItem)

    editDistance = levenshteinDistance(prevContent, currContent)        # likelihood measured based in edit-distance
    textLength = max(len(prevContent), len(currContent))

    return 1.0 - (math.log(editDistance, 2.25) / math.log(textLength, 2.25))


def getDirectoryLikelihood(path, directoryItem, currentDirectory):
    containedItems = 0

    for itemPath in directoryItem.keys():
        if itemPath in currentDirectory:                                # likelihood measured based in same-named files
            containedItems += 1

    currentDirectoryLen = len(currentDirectory)

    return 1.0 - math.exp(1 - (1 / math.pow(currentDirectoryLen - containedItems, 2)))


def getCurrentGitTreeItemDirectoryMatch(pathTrace, path, item, directoryItem, matchableItem):
    for currentPath, currentItem in directoryItem.items():
        if not isinstance(currentItem, list):
            currentMatch = ''.join(pathTrace) + currentPath
            currentRank = getItemLikelihood(path, item, currentItem, currentMatch)

            if currentRank > matchableItem[1]:
                matchableItem[0] = currentMatch
                matchableItem[1] = currentRank
                matchableItem[2] = pathTrace.copy()
        else:
            pathTrace.append(currentPath + '.')
            getCurrentGitTreeItemDirectoryMatch(pathTrace, path, item, currentItem[0], matchableItem)
            pathTrace.pop()


def removePathTrace(pathTrace, matchable):
    return matchable.split(''.join(pathTrace),2)[1]


def getMatchedItem(pathTrace, matchable, currentAdditions):
    ret = currentAdditions

    for path in pathTrace:
        ret = ret[path[:-1]][0]

    return ret[removePathTrace(pathTrace, matchable)]


def getCurrentGitTreeItemMatch(path, item, currentAdditions):
    matchableItem = [None, 0.0, None]
    getCurrentGitTreeItemDirectoryMatch([], path, item, currentAdditions, matchableItem)

    matchable = matchableItem[0]
    matchableRank = matchableItem[1]
    matchablePathTrace = matchableItem[2]

    # print(path + ' : ' + str(matchable) + ' ' + str(matchableRank) + ' | ' + str(matchablePathTrace))

    if matchableRank > MIN_FILE:
        return [matchable, getMatchedItem(matchablePathTrace, matchable, currentAdditions), matchablePathTrace]
    else:
        return None


def getCurrentGitTreeDirectoryMatch(path, item, currentAdditions):
    matchable = None
    matchableRank = 0.0

    for currentPath, currentItem in currentAdditions.items():
        if isinstance(currentItem, list):
            currentRank = getDirectoryLikelihood(path, item, currentItem[0])

            if currentRank > matchableRank:
                matchable = currentPath
                matchableRank = currentRank

    print('dir: ' + str(matchable) + ' ' + str(matchableRank))

    if matchableRank > MIN_DRCT:
        return [matchable, currentAdditions[matchable], []]
    else:
        return None


def getCurrentGitTreeMatch(path, item, currentAdditions):
    if isinstance(item, list):
        return getCurrentGitTreeDirectoryMatch(path, item[0], currentAdditions)
    else:
        return getCurrentGitTreeItemMatch(path, item, currentAdditions)


def additionalContentsDeepCopy(additionalCurrentContents):
    ret = {}
    for key, val in additionalCurrentContents.items():
        if isinstance(val, list):
            valR = [additionalContentsDeepCopy(val[0])]
        else:
            valR = val.copy()

        ret[key] = valR

    return ret


def popFromAdditionalContentsCopy(pathTrace, pathItem, additionalCurrentContents):
    traceList = []

    ret = additionalCurrentContents
    retArray = [ret]
    for path in pathTrace:
        traceList.append(retArray)
        retArray = ret[path[:-1]]
        ret = retArray[0]

    ret.pop(removePathTrace(pathTrace, pathItem))

    if len(ret) == 0:   # back-removing empty nodes
        i = len(traceList) - 1

        while i >= 0 and len(ret) == 0:
            ret = traceList[i][0]
            ret.pop(retArray)

            retArray = traceList[i]
            i -= 1


def evaluateGitTreeChanges(missingPreviousContents, additionalCurrentContents):
    removedContent = {}
    repositionedContent = {}
    additionalContent = additionalContentsDeepCopy(additionalCurrentContents)

    for path, item in missingPreviousContents.items():
        bestMatchPath = getCurrentGitTreeMatch(path, item, additionalCurrentContents)

        if bestMatchPath is not None:
            repositionedContent[path] = bestMatchPath[0]
            popFromAdditionalContentsCopy(bestMatchPath[2], bestMatchPath[0], additionalContent)
        else:
            removedContent[path] = item

    return [repositionedContent, removedContent, additionalContent]


def printContent(dict):
    return str(dict.keys())


def parseGitTreeChanges(lastTree, currentTree):
    leftChangedContents = {}
    rightChangedContents = {}

    missingContents = {}
    additionalContents = {}

    fetchGitTreeDiff(missingContents, leftChangedContents, '', lastTree.copy(), currentTree.copy())
    fetchGitTreeDiff(additionalContents, rightChangedContents, '', currentTree.copy(), lastTree.copy())

    versionResults = evaluateGitTreeChanges(missingContents, additionalContents)

    changedContents = leftChangedContents       # non-repositioned changed contents
    repositionedContents = versionResults[0]    # key-value as from-path, to-path strings
    removedContents = versionResults[1]         # both add & remove as git item descriptors
    additionalContents = versionResults[2]
    print('CHANGED: ' + printContent(changedContents))
    print('REPOSIT: ' + printContent(repositionedContents))
    print('REMOVED: ' + printContent(removedContents))
    print('ADDITIO: ' + printContent(additionalContents))


def parseCommitGitTreeMovement(lastTree, currentTree):
    previousContents.clear()
    currentContents.clear()

    parseGitTreeChanges(lastTree, currentTree)


def generateCommitGitTree(gitTree):
    ret = {}

    for gitItem in gitTree:
        if gitItem['type'] == 'tree':
            item = generateCommitGitTree(gitItem['tree'])
        else:
            item = gitItem

        ret[gitItem['path']] = item

    return [ret]


myVal = None
auth = loadAuthToken()


def generateRepositoryGitTrees(libPath):
    global myVal

    ret = []
    gitCommits = AuthorScanJsonReader.AuthorScanJsonReader().readFile(libPath + 'commits.txt', False)[0]['content']
    gitCommits.reverse()

    i = 0
    for gitCommit in gitCommits:
        if gitCommit['sha'] == 'ad812de0012d48c28a8493d6205c62122bb2933a':
            myVal = i
        i += 1

        gitDate = AuthorScanJsonReader.AuthorScanJsonReader().getDateFilestamp(gitCommit['commit']['author']['date'])
        gitFileTree = AuthorScanJsonReader.AuthorScanJsonReader().readFileRaw(libPath + 'filesystem/' + gitDate + '.txt')

        gitTree = generateCommitGitTree(gitFileTree)
        ret.append(gitTree)

    return ret


def fetchRepositoryGitTreeMovement():
    global myVal
    gitTrees = generateRepositoryGitTrees('../../lib/')

    for i in range(1, len(gitTrees) - 1):
        if i == myVal - 1:
            parseCommitGitTreeMovement(gitTrees[i], gitTrees[i + 1])


def main():
    global auth
    auth = loadAuthToken()

    fetchRepositoryGitTreeMovement()


def run():
    reqGet = None
    try:
        main()
        exit_code = EXIT_OK
    except TypeError:
        if int(reqGet.headers['X-RateLimit-Remaining']) > 0:
            traceback.print_exc(file=sys.stdout)

        exit_code = EXIT_FAIL

    return exit_code


if __name__ == '__main__':
    sys.exit(run())