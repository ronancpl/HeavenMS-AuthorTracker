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

# exit values
EXIT_OK = 0
EXIT_FAIL = 7


import sys

from datetime import datetime
import json
import requests
import os
import errno
import time
import traceback


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


def processLink(todayString, nextLink, repoApiParams, repoApiHeader, fileName):
    setupDir(fileName)  # make sure the FS path is available before downloading data

    if repoApiHeader is not None:
        apiParams = repoApiParams.copy()
        apiParams.update(repoApiHeader)
    else:
        apiParams = repoApiParams

    print('Requesting \'' + nextLink + '\'')
    jsonArray = []
    while True:
        r = getRequest(nextLink, apiParams)

        # extracting data in json format
        data = r.json()
        jsonArray.append(data)

        nextLink = getNextLink(r)
        if nextLink is None:
            break

    # saving new content
    blob = {'fetchDate': todayString, 'content': jsonArray}

    file = open(fileName, 'a')  # appending new data
    file.write("" + json.dumps(blob) + ",\n")


def main():
    # getting timestamp
    today = datetime.today()
    todayStr = "{}-{}-{}".format(today.year, today.month, today.day)

    global auth
    auth = loadAuthToken()

    repoApiParams = {'per_page': '100'}
    repoApiUrl = "https://api.github.com/repos/ronancpl/HeavenMS"

    processLink(todayStr, repoApiUrl, repoApiParams, None, '../../lib/repo/HeavenMS.txt')

    repoApiSubpath = "/"
    repoApiEndpoints = ['commits', 'languages', 'releases', 'forks', 'subscribers', 'contributors',
                        ['stargazers', '', {'Accept': 'application/vnd.github.v3.star+json'}],
                        ['commit_activity', 'stats/'], ['contributors', 'stats/'], ['participation', 'stats/']]

    for apiEndpoint in repoApiEndpoints:
        header = None

        if isinstance(apiEndpoint, str):
            subpath = ""
            endpoint = apiEndpoint
        else:
            if len(apiEndpoint) > 2:
                header = apiEndpoint[2]

            subpath = apiEndpoint[1]
            endpoint = apiEndpoint[0]

        filename = '../../lib' + repoApiSubpath + subpath + endpoint + '.txt'
        processLink(todayStr, repoApiUrl + repoApiSubpath + subpath + endpoint, repoApiParams, header, filename)


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
