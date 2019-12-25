# Run after 'AuthorFetchRepository'

# from authorscanner import AuthorScanRepository
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import errno
import math
import os.path
import requests
import sys
import time
import traceback
import base64
import json
import AuthorScanJsonReader


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


def fetchGitCommitTree(libPath, commitSha):
    commitDiffLink = 'https://github.com/ronancpl/HeavenMS/commit/' + commitSha + '.diff'
    print('Fetching ' + commitDiffLink)
    r = getRequest(commitDiffLink, {'per_page': '100'})

    # extracting data in text format
    data = r.text

    # keep data in file
    file = open(libPath + 'diffs/' + commitSha + ".txt", 'w', encoding='UTF-8')
    file.write(data)


def fetchGitRepositoryDiffTree(libPath):
    gitCommits = AuthorScanJsonReader.AuthorScanJsonReader().readFile(libPath + 'commits.txt', False)[0]['content']
    gitCommits.reverse()

    for gitCommit in gitCommits:
        fetchGitCommitTree(libPath, gitCommit['sha'])


def main():
    global auth
    auth = loadAuthToken()

    libPath = '../../lib/'
    setupDir(libPath + 'diffs/a.txt')
    fetchGitRepositoryDiffTree(libPath)


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