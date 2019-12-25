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
    jsonArray = []
    while True:
        print('Requesting "' + nextLink + '"')
        r = getRequest(nextLink, apiParams)

        # extracting data in json format
        rContent = r.json()
        jsonArray.append(rContent)

        nextLink = getNextLink(r)
        if nextLink is None:
            break

    return jsonArray


def fetchGithubPullCommits(nextPullCommitsLink, repoApiParams):
    apiParams = repoApiParams
    jsonPullCommitsArray = processLink(nextPullCommitsLink, apiParams)

    return jsonPullCommitsArray


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


def fetchGithubPullsCommits(lib_pulls_path, github_pulls):
    setupDir(lib_pulls_path + '/a.txt')

    # getting timestamp
    today = datetime.today()
    todayStr = "{}-{}-{}".format(today.year, today.month, today.day)

    repoApiParams = {'per_page': '100'}

    pull_commits = []
    for pull_request in github_pulls:
        if 'commits_url' in pull_request:
            pull_commits.append(fetchGithubPullCommits(pull_request['commits_url'], repoApiParams))
        else:
            pull_commits.append([])

    # saving new content
    blob = {'fetchDate': todayStr, 'content': {'commits': pull_commits}}

    file = open(lib_pulls_path + "/commits.txt", 'w')
    file.write("" + json.dumps(blob) + ",\n")


def main():
    global auth
    auth = loadAuthToken()

    lib_path = "../../lib"
    github_pulls = AuthorScanJsonReader.AuthorScanJsonReader().readFile(lib_path + '/users/pulls.txt', True)[0]['content']
    fetchGithubPullsCommits(lib_path + '/users/pulls', github_pulls)


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