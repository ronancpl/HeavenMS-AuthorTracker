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
import requests
import sys
import errno
import time
import traceback
import AuthorScanJsonReader
from authorscanner import AuthorScanRepository


apiParams = {'per_page': '100'}


def existsDir(filename):
    return os.path.exists(os.path.dirname(filename))


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


def getRequestDirectory(dir_link, repoApiParams):
    r = getRequest(dir_link, repoApiParams)

    # extracting data in json format
    data = r.json()

    dir_node = {}
    for tree_node in data['tree']:
        dir_node[tree_node['path']] = tree_node

    return dir_node


def processCommitFileSystemDirectory(commitDirectoryUrl, pathList, repoApiParams):
    dir_link = commitDirectoryUrl

    for path in pathList:
        dir_node = getRequestDirectory(dir_link, repoApiParams)
        dir_link = dir_node[path]['url']

    return getRequestDirectory(dir_link, repoApiParams)


def decodeGitBlobContent(content):
    return str(base64.b64decode(content), encoding='UTF-8', errors='replace')


def getGitBlobContent(item, repoApiParams):
    r = getRequest(item['url'], repoApiParams)

    # extracting data in json format
    data = r.json()

    if data['encoding'] == 'base64':
        return decodeGitBlobContent(data['content'])
    else:
        print('Encoding ' + data['encoding'] + ' for url ' + item['url'] + ' not supported')
        return ''


def fetchCommitCurrentFile(content_path, changed_file, changed_file_name, dir_node, repoApiParams):
    content = getGitBlobContent(dir_node[changed_file], repoApiParams)

    setupDir(content_path + 'a.txt')
    file = open(content_path + changed_file_name + ".txt", 'w', encoding='UTF-32')
    file.write(content)

    file.close()


def fetchCommitFilePatches(content_path, changed_file_path, changed_file_name, commitSha):
    content = ''
    for line in scanner_commit_file_diffs[commitSha][changed_file_path]:
        content += line

    setupDir(content_path + 'a.txt')
    file = open(content_path + changed_file_name + ".txt", 'w', encoding='UTF-32')
    file.write(content)

    file.close()


def fetchRepoCommitFileSystem(commitSha, commitTreeUrl, directory_path, commitChangedFiles, repoApiParams):
    contentPath = scanner.lib_path + '/diffquests/commit/' + commitSha + '/'
    if existsDir(contentPath):
        # do not refetch if diffquest for commit exists
        return

    pathList = directory_path.split('/')
    dir_node = processCommitFileSystemDirectory(commitTreeUrl, pathList, repoApiParams)

    for changed_file_name in commitChangedFiles:
        changed_file = changed_file_name + '.img.xml'

        fetchCommitCurrentFile(scanner.lib_path + '/diffquests/commit/' + commitSha + '/', changed_file, changed_file_name, dir_node, repoApiParams)
        fetchCommitFilePatches(scanner.lib_path + '/diffquests/diff/' + commitSha + '/', directory_path + '/' + changed_file, changed_file_name, commitSha)


def fetchRepositoryGitQuestMovement(repoApiParams):
    quest_path = scanner.repository_wz_path + '/Quest.wz'
    quest_files = ['Act', 'Check', 'QuestInfo', 'Say']
    quest_extension = '.img.xml'

    commit_quest_patches = {}

    for qfile in quest_files:
        qfile_metadata_key = quest_path + '/' + qfile + quest_extension

        if qfile_metadata_key in scanner_deltas:
            qfile_metadata = scanner_deltas[qfile_metadata_key]

            for commit_sha in qfile_metadata['modification_commit_shas']:
                if commit_sha not in commit_quest_patches:
                    commit_quest_patches[commit_sha] = set()

                commit_quest_patches[commit_sha].add(qfile)

    global reqCount
    global reqLast
    for commit_sha, commit_quest_files in commit_quest_patches.items():
        commit_tree_url = scanner_commits[commit_sha]['commit']['tree']['url']
        reqCount = 0
        reqLast = -1

        fetchRepoCommitFileSystem(commit_sha, commit_tree_url, quest_path, commit_quest_files, repoApiParams)
        # print('Request count ' + str(reqCount))

    return commit_quest_patches


def loadCommitGitQuestContents(content_path, commitSha, changed_file_name):
    file = open(content_path + commitSha + '/' + changed_file_name + ".txt", 'r', encoding='UTF-32')
    patch_contents = file.read()
    file.close()

    return patch_contents


def parseCommitGitQuestSectionMovement(quest_content, section_content, ref_content_line):
    patch_lines = []
    in_patch = False

    cur_content_line = ref_content_line
    for line in section_content[1:-1]:
        if line[0] == '+':
            if not in_patch:
                patch_lines.append(cur_content_line)
                in_patch = True
        else:
            in_patch = False

        cur_content_line += 1

    patch_questids = set()

    pidx = len(patch_lines) - 1
    while pidx >= 0:
        qidx = patch_lines[pidx]

        qline = quest_content[qidx]
        while True:
            if qline.startswith('  <imgdir name="'):
                qline = qline[16:]
                qid = int(qline[:qline.find('"')])

                patch_questids.add(qid)

                pidx -= 1
                while pidx >= 0 and patch_lines[pidx] >= qidx:
                    pidx -= 1

                break
            elif qidx < 1:
                pidx = -1
                break

            qidx -= 1
            qline = quest_content[qidx]

    return patch_questids


def parseCommitGitQuestMovement(quest_content, patch_content):
    sections = []
    line_buffer = []
    for line in patch_content.split('\n'):
        if line.startswith('@@'):
            sections.append(line_buffer)
            line_buffer = []

        line_buffer.append(line)

    sections.append(line_buffer)
    sections.pop(0)

    quests = set()
    for patch in sections:
        line = patch[0]
        line = line[line.find('+') + 1:]
        line = line[:line.find(' ')].split(',')

        ref_content_line = int(line[0])
        qids = parseCommitGitQuestSectionMovement(quest_content, patch, ref_content_line)
        quests.update(qids)

    return quests


def scanRepositoryGitQuestMovement(commit_quest_patches):
    quest_movements = {}
    for commit_sha, commit_quest_files in commit_quest_patches.items():
        commit_quest_movements = set()
        quest_movements[commit_sha] = commit_quest_movements

        for qfile in commit_quest_files:
            quest_content = loadCommitGitQuestContents(scanner.lib_path + '/diffquests/commit/', commit_sha, qfile)
            patch_content = loadCommitGitQuestContents(scanner.lib_path + '/diffquests/diff/', commit_sha, qfile)

            commit_quest_movements.update(parseCommitGitQuestMovement(quest_content, patch_content))

        if len(commit_quest_movements) > 0:
            print('commit ' + commit_sha + ' : ' + str(commit_quest_movements))

    return quest_movements


class AuthorScanGitQuestMovement:

    def scanRepositoryGitQuestMovement(self, commits, deltas, commit_file_diffs):
        global auth
        auth = loadAuthToken()

        global scanner
        scanner = AuthorScanRepository.scanner

        global scanner_commits
        scanner_commits = commits

        global scanner_deltas
        scanner_deltas = deltas

        global scanner_commit_file_diffs
        scanner_commit_file_diffs = commit_file_diffs

        quest_patches = fetchRepositoryGitQuestMovement(apiParams)
        return scanRepositoryGitQuestMovement(quest_patches)


if __name__ == '__main__':
    AuthorScanGitQuestMovement().scanRepositoryGitQuestMovement(scanner.commits, scanner.deltas, scanner.commit_file_diffs)