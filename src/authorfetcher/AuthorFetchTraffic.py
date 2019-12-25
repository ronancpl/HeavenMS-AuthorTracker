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

import sys

from datetime import datetime
import errno
import json
import requests
import os
import traceback
import time

# exit values
EXIT_OK = 0
EXIT_FAIL = 7


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def loadAuthToken():
    file = open("C:/Nexon/auth.txt", 'r')
    return file.read().splitlines()[0]


def main():
    # getting timestamp
    today = datetime.today()
    todayStr = "{}-{}-{}".format(today.year, today.month, today.day)

    repoApiParams = {'access_token': loadAuthToken()}
    repoApiUrl = "https://api.github.com/repos/ronancpl/HeavenMS"
    repoApiSubpath = "/traffic/"
    repoApiEndpoints = [['referrers', 'popular/'], ['paths', 'popular/'], 'views', 'clones']

    for apiEndpoint in repoApiEndpoints:
        if isinstance(apiEndpoint, str):
            subpath = ""
            endpoint = apiEndpoint
        else:
            subpath = apiEndpoint[1]
            endpoint = apiEndpoint[0]

        filename = '../../lib' + repoApiSubpath + subpath + endpoint + '.txt'
        setupDir(filename)      # make sure the FS path is available before downloading data

        while True:
            try:
                reqGet = requests.get(repoApiUrl + repoApiSubpath + subpath + endpoint, repoApiParams)
                print(reqGet.status_code)

                break
            except requests.exceptions.ConnectionError or ConnectionRefusedError:
                print('Connection lost. Retrying...')
                time.sleep(20)


        # extracting data in json format
        data = reqGet.json()
        print(data)

        # saving new content
        blob = {'fetchDate': todayStr, 'content': data}

        file = open(filename, 'a')  # appending new data
        file.write("" + json.dumps(blob) + ",\n")


def run():
    global reqGet
    reqGet = None
    try:
        main()
        exit_code = EXIT_OK
    except TypeError:
        if 'X-RateLimit-Remaining' in reqGet.headers and int(reqGet.headers['X-RateLimit-Remaining']) > 0:
            traceback.print_exc(file=sys.stdout)

        exit_code = EXIT_FAIL

    return exit_code


if __name__ == '__main__':
    sys.exit(run())