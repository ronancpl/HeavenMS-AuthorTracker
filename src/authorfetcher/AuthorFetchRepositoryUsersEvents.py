import sys

# Run after 'AuthorFetchRepositoryUsers'

# exit values
EXIT_OK = 0
EXIT_FAIL = 7

from datetime import datetime
import json
import requests
import time
import traceback
import os
import errno
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


def processLink(nextLink, apiParams):
    idx = nextLink.find('{')
    if idx > -1:
        nextLink = nextLink[:idx]

    jsonArray = []
    while True:
        print('Requesting "' + nextLink + '"')
        r = getRequest(nextLink, apiParams)

        # extracting data in json format
        rContent = r.json()
        jsonArray.extend(rContent)

        nextLink = getNextLink(r)
        if nextLink is None:
            break

    return jsonArray


def fetchGithubUserData(todayString, nextEventsLink, nextReposLink, repoApiParams, dirPath, fileName):
    apiParams = repoApiParams

    jsonEventsArray = processLink(nextEventsLink, apiParams)
    jsonReposArray = processLink(nextReposLink, apiParams)

    # saving new content
    blob = {'fetchDate': todayString, 'content': {'events': jsonEventsArray, 'repos': jsonReposArray}}

    file = open(dirPath + '/' + fileName + ".txt", 'w')
    file.write("" + json.dumps(blob) + ",\n")


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


def fetchGithubUser(todayString, repoApiParams, lib_events_path, github_user):
    fetchGithubUserData(todayString, github_user['events_url'], github_user['repos_url'], repoApiParams, lib_events_path, github_user['login'])


def fetchGithubUsersData(lib_events_path, github_users):
    setupDir(lib_events_path + '/a.txt')

    # getting timestamp
    today = datetime.today()
    todayStr = "{}-{}-{}".format(today.year, today.month, today.day)

    repoApiParams = {'per_page': '100'}

    for user in github_users:
        fetchGithubUser(todayStr, repoApiParams, lib_events_path, user)


def main():
    global auth
    auth = loadAuthToken()

    lib_path = "../../lib"
    github_users = AuthorScanJsonReader.AuthorScanJsonReader().readFile(lib_path + '/users/users.txt', True)[0]['content']

    fetchGithubUsersData(lib_path + '/users/events', github_users)


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