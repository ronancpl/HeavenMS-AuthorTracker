# from authorscanner import AuthorScanRepository
from datetime import datetime
import errno
import os.path
import requests
import time
import base64
import json
import AuthorScanJsonReader
from authorfinder import AuthorFetchPatrons
from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager
from authorscanner.patrons import AuthorPatronType
from authorconstants import AuthorPatronableDocumentChecker, AuthorConstantLimit

patronhistoryDir = '../../lib/patrons_history/'

apiParams = {'per_page': '100'}


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


def decodeGitBlobContent(content):
    return str(base64.b64decode(content), encoding='UTF-8', errors='replace')


def getGitBlobContent(data):
    try:
        if data['encoding'] == 'base64':
            return decodeGitBlobContent(data['content'])
        else:
            print('Encoding ' + data['encoding'] + ' not supported')
            return ''
    except KeyError:
        print('Encoding not found on ' + str(data))
        raise


def parseDirectoryPath(string_path):
    return string_path.split('/')


def getRequestGithubNode(github_tree_link):
    while True:
        github_node = getRequest(github_tree_link, apiParams).json()
        if 'tree' in github_node:
            return github_node

        print('No "tree" node in ' + github_tree_link + ' . Retrying...')
        time.sleep(20)


def fetchGithubDirectoryNode(github_tree_link):
    github_node = getRequestGithubNode(github_tree_link)

    github_directory_tree = {}
    for node_item in github_node['tree']:
        if 'size' in node_item:
            file_size = node_item['size']
        else:
            file_size = None

            # don't account for patronability ignored directories
            if not AuthorPatronableDocumentChecker.isPatronableRepositoryDirectory(node_item['path']):
                continue

        github_directory_tree[node_item['path']] = node_item['url'], file_size

    return github_directory_tree


def fetchGithubNodeElement(github_tree_cache, file_structure, file_structure_idx, file_structure_len):
    current_path = file_structure[file_structure_idx]
    if file_structure_idx >= file_structure_len:  # reached blob content
        file_url, file_size = github_tree_cache[current_path]

        if AuthorPatronableDocumentChecker.isPatronableRepositoryFile(file_url, file_size):
            return getRequest(file_url, apiParams).json()
        else:
            print('Git location out: ' + file_url)
            return None
    else:
        if current_path in github_tree_cache:
            next_github_tree = github_tree_cache[current_path]

            if isinstance(next_github_tree, tuple):   # convert directory link to reachable directory
                directory_url, directory_size = next_github_tree
                next_github_tree = fetchGithubDirectoryNode(directory_url)
                github_tree_cache[current_path] = next_github_tree

            return fetchGithubNodeElement(next_github_tree, file_structure, file_structure_idx + 1, file_structure_len)
        else:
            if not AuthorPatronableDocumentChecker.isPatronableRepositoryDirectory(current_path):
                print('Git location error: Could not find ' + current_path + ' in ' + str(file_structure) + ' at Git-tree: ' + str(github_tree_cache))

            return None


def initGithubCommitRootNode(commit_tree_link):
    initial_node = fetchGithubDirectoryNode(commit_tree_link)
    return initial_node


def fetchFileFromGithubCommitTree(github_tree_cache, file_path):
    directory_structure = parseDirectoryPath(file_path)
    return fetchGithubNodeElement(github_tree_cache, directory_structure, 0, len(directory_structure) - 1)


def addPatronItem(fetched_patrons, patron_name, patron_type_str):
    fetched_patrons_type = fetched_patrons[AuthorPatronType.AuthorPatronType(patron_type_str)]
    if patron_name not in fetched_patrons_type:
        fetched_patrons_type[patron_name] = 1
    else:
        fetched_patrons_type[patron_name] += 1


def fetchFileBlobContent(file_blob):
    file_content = getGitBlobContent(file_blob)
    return file_content


def fetchCommitFilePatronsFromGithubTree(github_commit_tree_cache, file_path):
    file_blob = fetchFileFromGithubCommitTree(github_commit_tree_cache, file_path)

    fetched_patrons = getEmptyFilePatronsStructure()
    if file_blob is not None:
        file_content = fetchFileBlobContent(file_blob)

        file_patrons = AuthorFetchPatrons.AuthorFetchPatrons().authorFetchFileContentPatrons(file_content)

        for patron_names, patron_type in file_patrons:
            for patron in patronManager.getPatron(patron_names[0]):
                addPatronItem(fetched_patrons, patron.name, patron_type)

    return fetched_patrons


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def getPatronFilePath(commit_sha, file_path):
    return scanner.lib_path + '/patrons_diff/' + commit_sha + '/' + file_path + '.txt'


def getFileDiffPatrons(diff_patrons):
    file_diff_patrons = {}

    for patron_type, patron_names in diff_patrons.items():
        file_diff_patrons[patron_type.value] = patron_names

    return file_diff_patrons


def createPatronFile(commit_sha, file_path, diff_patrons, current_patrons):
    patron_file_path = getPatronFilePath(commit_sha, file_path)
    setupDir(patron_file_path)

    blob = {'diff': getFileDiffPatrons(diff_patrons), 'all': getFileDiffPatrons(current_patrons)}

    file = open(patron_file_path, 'w')
    file.write("" + json.dumps(blob) + ",\n")
    file.close()


def readPatronFile(commit_sha, file_path):
    patron_file_path = getPatronFilePath(commit_sha, file_path)

    try:
        patron_ret = {}

        for patron_diff_type, patron_file_content in AuthorScanJsonReader.AuthorScanJsonReader().readFileRaw(patron_file_path)[0].items():
            patron_file_ret = {}
            patron_ret[patron_diff_type] = patron_file_ret

            for patron_type_str, patron_names in patron_file_content.items():
                patron_file_ret[AuthorPatronType.AuthorPatronType(patron_type_str)] = patron_names

        return patron_ret
    except (IOError, IndexError):
        return None


def parsePatronsInSourceFile(commit_sha, commit_tree_cache, file_path):
    patron_cached_file = readPatronFile(commit_sha, file_path)
    if patron_cached_file is None:
        return (fetchCommitFilePatronsFromGithubTree(commit_tree_cache, file_path), True)   # boolean signalizing later patron file write (diff patrons not yet done)
    else:
        return (patron_cached_file['all'], False)


def findFileInRepositoryPatrons(directory_structure, repository_patrons_file_tree):
    directory_node = repository_patrons_file_tree

    for directory_item in directory_structure:
        if directory_item not in directory_node:
            return None
        else:
            directory_node = directory_node[directory_item]

    return directory_node


def getPatronFileInRepositoryPatrons(prior_file_path, repository_patrons_file_tree):
    directory_structure = parseDirectoryPath(prior_file_path)
    file_item = findFileInRepositoryPatrons(directory_structure, repository_patrons_file_tree)

    return file_item


# assumption: there is no "same-name" for files/folders between items in source version tree
def addFilePatronsInRepositoryPatrons(file_structure, file_structure_idx, file_structure_len, file_patrons, modified_patrons_file_tree):
    if file_structure_idx >= file_structure_len:
        file_patrons_copy = file_patrons.copy()     # markup this node as a 'file node'
        file_patrons_copy['/file'] = 1

        modified_patrons_file_tree[file_structure[file_structure_idx]] = file_patrons_copy
    else:
        if file_structure[file_structure_idx] not in modified_patrons_file_tree:
            modified_patrons_file_tree_node = {}
            modified_patrons_file_tree[file_structure[file_structure_idx]] = modified_patrons_file_tree_node
        else:
            modified_patrons_file_tree_node = modified_patrons_file_tree[file_structure[file_structure_idx]]

        addFilePatronsInRepositoryPatrons(file_structure, file_structure_idx + 1, file_structure_len, file_patrons, modified_patrons_file_tree_node)


def addFilePatronsCount(diff_file_patrons, patron, count):
    if patron not in diff_file_patrons:
        diff_file_patrons[patron] = count
    else:
        diff_file_patrons[patron] += count


def deductFilePatronsCount(diff_file_patrons, patron, count):
    if patron in diff_file_patrons:
        diff_file_patrons[patron] -= count
        if count < 1:
            diff_file_patrons.pop(patron)


def calcFilePatronsDiff(prior_file_patrons, current_file_patrons):
    diff_file_patrons_struct = {}
    for patron_type in AuthorPatronType.AuthorPatronType:
        diff_file_patrons = {}
        diff_file_patrons_struct[patron_type] = diff_file_patrons

        for patron, count in current_file_patrons[patron_type].items():
            addFilePatronsCount(diff_file_patrons, patron, count)

        for patron, count in prior_file_patrons[patron_type].items():
            deductFilePatronsCount(diff_file_patrons, patron, count)

    return diff_file_patrons_struct


def getEmptyFilePatronsStructure():
    file_patrons = {}
    for patron_type in AuthorPatronType.AuthorPatronType:
        file_patrons[patron_type] = {}

    return file_patrons


def parseCommitFile(commit_sha, commit_tree_cache, file_path, prior_file_path, repository_patrons_file_tree, modified_patrons_file_tree):
    prior_file_patrons = getPatronFileInRepositoryPatrons(prior_file_path, repository_patrons_file_tree)
    if prior_file_patrons is None:
        prior_file_patrons = getEmptyFilePatronsStructure()

    current_file_patrons, write_file_patrons = parsePatronsInSourceFile(commit_sha, commit_tree_cache, file_path)

    current_file_structure = parseDirectoryPath(file_path)
    addFilePatronsInRepositoryPatrons(current_file_structure, 0, len(current_file_structure) - 1, current_file_patrons, modified_patrons_file_tree)

    diff_file_patrons = calcFilePatronsDiff(prior_file_patrons, current_file_patrons)

    if write_file_patrons:
        createPatronFile(commit_sha, file_path, diff_file_patrons, current_file_patrons)

    return diff_file_patrons


def deepCopyRepositoryPatronsTree(modified_patrons_file_tree):
    ret_tree = {}

    if '/file' in modified_patrons_file_tree:
        modified_patrons_file_tree.pop('/file')  # dispose file node markup

    for key, value in modified_patrons_file_tree.items():
        if isinstance(value, dict):
            ret_tree[key] = deepCopyRepositoryPatronsTree(value)
        else:
            ret_tree[key] = value

    return ret_tree


def deepUpdateRepositoryPatronsTree(repository_patrons_file_tree, modified_patrons_file_tree):
    for key, value in modified_patrons_file_tree.items():
        if key not in repository_patrons_file_tree:
            repository_patrons_file_tree[key] = deepCopyRepositoryPatronsTree(value)
        else:
            if '/file' in value:
                value.pop('/file')  # dispose file node markup
                repository_patrons_file_tree[key].update(value)
            else:
                deepUpdateRepositoryPatronsTree(repository_patrons_file_tree[key], value)


def fetchRepositoryCommitPatrons(scanner_commits_file_changes):
    setupDir(patronhistoryDir + '/a.txt')

    diff_repository_patrons = {}
    repository_patrons_file_tree = {}

    gitCommits = scanner.commits_info
    for gitCommit in gitCommits:
        diff_commit_patrons = {}
        modified_patrons_file_tree = {}

        commit_changed_files = scanner_commits_file_changes[gitCommit['sha']]
        commit_tree_cache = initGithubCommitRootNode(gitCommit['commit']['tree']['url'])

        if len(commit_changed_files) < AuthorConstantLimit.WrapLimit.PATRON_COMMIT_FILES_MAXSIZE.getValue():
            print('Parsing patrons commit ' + gitCommit['sha'])

            for commit_file_path in commit_changed_files:
                diff_file_patrons = parseCommitFile(gitCommit['sha'], commit_tree_cache, commit_file_path[0], commit_file_path[1], repository_patrons_file_tree, modified_patrons_file_tree)
                diff_commit_patrons[commit_file_path[0]] = diff_file_patrons

            deepUpdateRepositoryPatronsTree(repository_patrons_file_tree, modified_patrons_file_tree)

        diff_commit_node = {'created_at': gitCommit['commit']['author']['date'], 'diff': diff_commit_patrons}
        diff_repository_patrons[gitCommit['sha']] = diff_commit_node

    return diff_repository_patrons


class AuthorScanGitTreePatrons:

    def fetchRepositoryCommitPatrons(self):
        global auth
        auth = loadAuthToken()

        global patronManager
        patronManager = AuthorPatronManager.patronManager

        global scanner
        scanner = AuthorScanRepository.scanner

        return fetchRepositoryCommitPatrons(scanner.commits_file_changes)


if __name__ == '__main__':
    AuthorScanGitTreePatrons().fetchRepositoryCommitPatrons()
