'''
    This file is part of the HeavenMS MapleStory Server
    Copyleft (L) 2016 - 2018 RonanLana

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation version 3 as published by
    the Free Software Foundation. You may not use, modify or distribute
    this program under any other version of the GNU Affero General Public
    License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# Run after 'AuthorFetchRepositoryCommits'

# exit values
EXIT_OK = 0
EXIT_FAIL = 7

REQUEST_UNIT = 0

import sys

from datetime import datetime
import json
import requests
import os
import errno
import time
import traceback
import AuthorScanJsonReader


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


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
    global REQUEST_UNIT

    while True:
        try:
            reqGet = requests.get(nextLink, headers=apiParams, auth=(auth[1], auth[0]))

            if REQUEST_UNIT % 200 == 0:
                print('Request unit ' + str(REQUEST_UNIT))

            REQUEST_UNIT += 1

            if 'X-RateLimit-Remaining' in reqGet.headers and int(reqGet.headers['X-RateLimit-Remaining']) < 1:
                print('RateLimit exceeded for this hour...')

                time.sleep(max(20,float(reqGet.headers['X-RateLimit-Reset']) - float(datetime.utcnow().timestamp())))
                continue

            return reqGet
        except requests.exceptions.ConnectionError or ConnectionRefusedError:
            print('Connection lost. Retrying...')
            time.sleep(20)


def getRequest(nextLink, apiParams):
    global reqCount
    global reqLast
    global reqGet

    try:
        reqGet = getRequestCall(nextLink, apiParams)
        reqCount += 1

        return reqGet

    except KeyError:
        print(traceback.print_exc(file=sys.stdout))
        print(str(reqLast) + ' excepted ' + nextLink + ' ' + str(reqGet.headers))
        time.sleep(20)
        return getRequest(nextLink, apiParams)


def processFileSystemDirectoryContents(rContent):
    dirItems = []

    for rItem in rContent:
        dirItems.append(rItem)

    return dirItems


def processFileSystemDirectoryNode(nextLink, repoApiParams):
    apiParams = repoApiParams

    jsonArray = []
    while True:
        r = getRequest(nextLink, apiParams)

        # extracting data in json format
        rContent = r.json()

        try:
            rTree = rContent['tree']
            jsonArray.append(processFileSystemDirectoryContents(rTree))
        except KeyError:
            print('[ERROR] No tree node on "' + nextLink + '"')
            time.sleep(120)
            continue

        nextLink = getNextLink(r)
        if nextLink is None:
            break

    return jsonArray


def processFileSystemDirectory(directoryUrl, repoApiParams):
    directoryContent = []
    directoryData = processFileSystemDirectoryNode(directoryUrl, repoApiParams)[0]
    for data in directoryData:
        if data['type'] == 'tree':  # DFT File System content retrieval
            data['tree'] = processFileSystemDirectory(data['url'], repoApiParams)

        directoryContent.append(data)

    return directoryContent


def processRepoCommitFileSystem(todayString, dirName, commitData, repoApiParams):
    fsData = processFileSystemDirectory(commitData['commit']['tree']['url'], repoApiParams)

    # saving new content
    blob = {'fetchDate': todayString, 'content': fsData}

    file = open(dirName + commitData['timestamp'] + ".txt", 'w')
    file.write("" + json.dumps(blob) + ",\n")


def processRepoCommitSetFiles(todayString, filesystemDir, commitSet, repoApiParams):
    global reqCount
    global reqLast
    for commitData in commitSet:
        print('Requesting FS commit ' + str(commitData['timestamp']))
        reqCount = 0
        reqLast = -1
        processRepoCommitFileSystem(todayString, filesystemDir, commitData, repoApiParams)
        print('Request count ' + str(reqCount))


def fetchRepoCommitSetFiles(dirPath):
    commitSet = []
    dirPath = dirPath + "/"

    for commitFile in os.listdir(dirPath):
        commitData = AuthorScanJsonReader.AuthorScanJsonReader().readFile(dirPath + commitFile, False)[0]['content'][0]
        commitData['timestamp'] = commitFile.partition('.')[0]

        commitSet.append(commitData)

    return commitSet


def main():
    global auth
    auth = loadAuthToken()

    # getting timestamp
    today = datetime.today()
    todayStr = "{}-{}-{}".format(today.year, today.month, today.day)

    dirName = '../../lib/filesystem'
    commitDirName = '../../lib/commits'
    repoApiParams = {'per_page': '100'}
    repoApiUrl = "https://api.github.com/repos/ronancpl/HeavenMS"
    repoApiSubpath = '/'
    repoApiEndpoint = 'trees'

    # getting commit SHAs from commit summary from AuthorFetchRepository
    commitSet = fetchRepoCommitSetFiles(commitDirName)
    if len(commitSet) == 0:
        print('Empty commit descriptor directory')
        return

    subpath = ""
    endpoint = repoApiEndpoint

    setupDir(dirName + repoApiSubpath + subpath + endpoint + '.txt')  # make sure the FS path is available before downloading data
    processRepoCommitSetFiles(todayStr, dirName + '/', commitSet, repoApiParams)


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