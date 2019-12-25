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

from datetime import datetime
import errno
import json
import os
import sys


directoryMetadataStr = ''


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def directoryMetadataToString(dirPath, dirFileStats):
    msg = dirPath + ' :\n'
    for fileName, fileStat in dirFileStats:
        msg += '  ' + fileName + ' -- ' + str(fileStat)
        msg += '\n'

    msg += '\n'
    return msg


def fetchMetadataFromDirectory(dirPath):
    subdirs = []
    fileStats = []

    for fileName in os.listdir(dirPath):
        filePath = dirPath + '/' + fileName

        if os.path.isdir(filePath):
            subdirs.append(filePath)
        elif os.path.isfile(filePath):
            fileStats.append((fileName, os.stat(filePath)))
        else:
            print('Not a file: %s' + filePath)

    global directoryMetadataStr
    directoryMetadataStr += directoryMetadataToString(dirPath, fileStats)

    for subdirPath in subdirs:
        fetchMetadataFromDirectory(subdirPath)


def dumpFileSystemMetadata():
    global directoryMetadataStr
    fsData = directoryMetadataStr

    # getting timestamp
    today = datetime.today()
    todayStr = "{}-{}-{}".format(today.year, today.month, today.day)

    # saving new content
    blob = {'fetchDate': todayStr, 'content': '\n' + fsData + '\n'}

    fsMetaFilePath = "../../lib/filesystem_meta/fs_logs.txt"
    setupDir(fsMetaFilePath)
    file = open(fsMetaFilePath, 'w')
    # file.write("" + json.dumps(blob) + ",\n")
    file.write(fsData)


def run():
    fetchMetadataFromDirectory('../../../HeavenMS')
    dumpFileSystemMetadata()


if __name__ == '__main__':
    sys.exit(run())