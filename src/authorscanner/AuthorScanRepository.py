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

import errno
import inspect
import json
import pickle
import math
import os
from datetime import datetime
from datetime import timedelta
import AuthorScanJsonReader

from authorconstants import AuthorConstantLimit
from authorscanner import AuthorScanGitFileMovement
from authorscanner import AuthorScanGitTreeMovement
from authorscanner import AuthorScanGitTreePatrons
from authorscanner import AuthorScanGitQuestMovement
from authorscanner.patrons import AuthorPatronElement
from authorscanner.patrons import AuthorPatronManager
from authorscanner.patrons import AuthorScanGithubPatrons
from authorscanner.patrons import AuthorScanSocialPatrons
from authorscanner.patrons import AuthorScanSourcePatrons
from authorscanner.patrons import AuthorScanSurveyPatrons
from authorscanner.survey import AuthorSurveyQuestion


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def writableTimestamp(ts):
    return ts.isoformat() + 'Z' # matches with github timestamps


def parseScanElement(index, scan):
    cache = {}

    if index is not None:
        if not isinstance(index, list):
            index = [index]

        for scanData in scan:
            scanItem = scanData['content']
            for scanIt in scanItem:
                if len(scanIt) > 0:
                    cacheKey = scanIt
                    for idx in index:
                        cacheKey = cacheKey[idx]

                    cache[cacheKey] = scanIt

    else:   # non-indexed content are always stored as list
        for scanData in scan:
            scanKey = scanData['fetchDate']
            scanItem = scanData['content']

            cache[scanKey] = scanItem

    return cache


def parseScanCommitsInfo(commits_info_path):
    commits_info = AuthorScanJsonReader.AuthorScanJsonReader().readFile(commits_info_path, False)[0]['content']
    commits_info.reverse()  # fetch commits in publish order

    return commits_info


def parseScanCommits(dir_path):
    ret = {}

    for filename in os.listdir(dir_path):
        commit_data = parseScanElement('sha', scanFile(dir_path + '/' + filename, True))
        ret.update(commit_data)

    return ret


def parseScanFilesystem(dir_path):
    ret = {}

    for filename in os.listdir(dir_path):
        commit_fs = AuthorScanJsonReader.AuthorScanJsonReader().readFileRaw(dir_path + '/' + filename)
        commit_timestamp = filename.rsplit('.txt', 2)[0]

        # SHORTCUT - use SHA to get commit info, get timestamp from within commit, directly from file not needed
        commit_fs = {'commit_time': scanner.parseFileTimestampToStringTimestamp(commit_timestamp), 'content': commit_fs}
        ret[commit_timestamp] = commit_fs

    return ret


def parseScanFileDiffs():
    return AuthorScanGitTreeMovement.AuthorScanGitTreeMovement().scanRepositoryGitMovement()


def parseScanFileDeltas():
    return AuthorScanGitFileMovement.AuthorScanGitFileMovement().countRepositoryGitFileMovement()


def parseScanQuestDiffs(commits, deltas, commit_file_diffs):
    return AuthorScanGitQuestMovement.AuthorScanGitQuestMovement().scanRepositoryGitQuestMovement(commits, deltas, commit_file_diffs)


def isFileDump(commit_file, file_type):
    if 'is_binary' in commit_file:
        return True

    if file_type == 3:
        wrap_limit_type = AuthorConstantLimit.WrapLimit.XML_DUMP_DIFF_MINSIZE
    elif file_type == 4 and commit_file['type'] == 2 and os.path.splitext(commit_file['path'])[1] == '.txt':
        wrap_limit_type = AuthorConstantLimit.WrapLimit.TXT_DUMP_DIFF_MINSIZE
    elif file_type != 4:
        wrap_limit_type = AuthorConstantLimit.WrapLimit.CODE_DUMP_DIFF_MINSIZE
    else:
        wrap_limit_type = AuthorConstantLimit.WrapLimit.FILE_DUMP_DIFF_MINSIZE

    max_count = wrap_limit_type.getValue()

    if commit_file['add_count'] > max_count:
        return True

    if commit_file['del_count'] > max_count:
        return True

    if commit_file['change_count'] > max_count:
        return True

    return False


def fetchFileExtensionIndex(filename):
    return {
        '.java': 1,
        '.js': 2,
        '.xml': 3,
    }.get(os.path.splitext(filename)[1], 4)


def parseDirectoryPath(string_path):
    return string_path.rsplit('/', 2)[0]


def createDirectoryPathEntry():
    file_dir_contents = []
    for t in range(5):  # file types
        file_dir_contents.append(set())

    return file_dir_contents


def updateCommitDiffDirectoryContents(directory_path_contents, file_path, file_type):
    file_dir_path = parseDirectoryPath(file_path)  # files in root folder gets to be their own "directory"

    if file_dir_path in directory_path_contents:
        dir_path_entry = directory_path_contents[file_dir_path]
    else:
        dir_path_entry = createDirectoryPathEntry()
        directory_path_contents[file_dir_path] = dir_path_entry

    dir_path_entry[file_type].add(file_path)


def getDirectoryNameFromFilePath(file_path, max_depth):
    try:
        return '/'.join(file_path.split('/', max_depth)[:-1])
    except:
        return ''


def mergeDirectoryContentsByDepth(directory_path_contents):
    merged_directory_path_contents = {}

    for dp_key, dp_val in directory_path_contents.items():
        dp_merge_dir_key = getDirectoryNameFromFilePath(dp_key, AuthorConstantLimit.WrapLimit.FILE_DUMP_DIRECTORY_MINDEPTH.getValue() + 1)

        if dp_merge_dir_key not in merged_directory_path_contents:
            dp_item = createDirectoryPathEntry()
            merged_directory_path_contents[dp_merge_dir_key] = dp_item
        else:
            dp_item = merged_directory_path_contents[dp_merge_dir_key]

        for file_type in range(len(dp_val)):
            file_type_directory_paths = dp_val[file_type]
            for file_path in file_type_directory_paths:
                dp_item[file_type].add(file_path)

    return merged_directory_path_contents


def parseScanCommitDumps(diffs):
    commit_dumps = {}
    filesystem_dumps = set()

    for fs_key, fs_val in diffs.items():
        directory_path_contents = {}
        file_dumps = set()
        commit_dumps[fs_key] = file_dumps

        for commit_diff_file in fs_val['content']:
            file_path = commit_diff_file['path']

            file_type = fetchFileExtensionIndex(file_path)
            if not isFileDump(commit_diff_file, file_type):
                updateCommitDiffDirectoryContents(directory_path_contents, file_path, file_type)
            else:
                file_dumps.add(file_path)  # SHORTCUT - make integer hash?
                filesystem_dumps.add(file_path)

        directory_path_contents = mergeDirectoryContentsByDepth(directory_path_contents)

        # files dumps as several files of the same extension changed within the same directory
        for dp_key, dp_val in directory_path_contents.items():
            for file_type in range(len(dp_val)):
                file_type_directory_paths = dp_val[file_type]

                if file_type == 3:
                    wrap_directory_limit_type = AuthorConstantLimit.WrapLimit.XML_DUMP_DIRECTORY_DIFF_MINSIZE
                elif file_type == 1 or file_type == 2:
                    wrap_directory_limit_type = AuthorConstantLimit.WrapLimit.CODE_DUMP_DIRECTORY_DIFF_MINSIZE
                else:
                    wrap_directory_limit_type = AuthorConstantLimit.WrapLimit.FILE_DUMP_DIRECTORY_DIFF_MINSIZE

                if len(file_type_directory_paths) > wrap_directory_limit_type.getValue():
                    for file_path in file_type_directory_paths:
                        file_dumps.add(file_path)
                        filesystem_dumps.add(file_path)

    return commit_dumps, filesystem_dumps


def parseScanSourcePatrons(lib_patrons_path):
    patrons_directory_info = []

    for patrons_directory_file in os.listdir(lib_patrons_path):
        patrons_directory_item = parseScanElement(None, scanFile(lib_patrons_path + patrons_directory_file, False))

        for patrons_directory_data in patrons_directory_item.values():
            patrons_directory_info.append(patrons_directory_data[0]['patrons'])

    return patrons_directory_info


def parseScanFilePatronMovements():
    return AuthorScanGitTreePatrons.AuthorScanGitTreePatrons().fetchRepositoryCommitPatrons()


def parseScanGithubEvents(lib_events_path, users_db):
    github_users_events = {}

    for user in users_db.values():
        user_events = parseScanElement(None, scanFile(lib_events_path + '/' + user['login'] + '.txt', False))

        for user_events_ct in user_events.values():
            github_users_events[user['login']] = user_events_ct[0]

    return github_users_events


def parseRecalledGithubContents():
    commit_pulls = set()
    commit_shas = set()

    print('Load recalled commits')
    for issue_comments in scanner.users_issue_comments.values():
        for comment in issue_comments:
            if comment['user']['login'] == 'ronancpl':
                comment_msg = comment['body']
                fidx = comment_msg.find('Recalled commit ')
                if fidx >= 0:
                    pull_number = comment['issue_url']
                    comment_msg = comment_msg[fidx + len('Recalled commit '):]
                    print('  Detected sha "' + comment_msg + '" PR: ' + str(int(pull_number[pull_number.rfind('/') + 1:])))
                    commit_shas.add(comment_msg.split()[0])
                    commit_pulls.add(int(pull_number[pull_number.rfind('/') + 1:]))

    return commit_shas, commit_pulls


def parseScanFilePatrons():
    return AuthorScanSourcePatrons.AuthorScanSourcePatrons().scanFilePatronAssociations()


def parseScanGithubPatrons(users_db):
    return AuthorScanGithubPatrons.AuthorScanGithubPatrons().scanGithubPatronAssociations(users_db)


def parseScanSurveyContent():
    return AuthorScanSurveyPatrons.AuthorScanSurveyPatrons().scanSurveyPatronAssociations()


def parseScanSocialContent():
    return AuthorScanSocialPatrons.AuthorScanSocialPatrons().scanSocialPatronAssociations()


def parseSurveyMetadata():
    return AuthorSurveyQuestion.AuthorSurveyQuestion().fetchSurveyQuestionList()


def scanFile(file_path, no_duplicates):
    return AuthorScanJsonReader.AuthorScanJsonReader().readFile(file_path, no_duplicates)


def applyInverseLinks(inverse_patron_aliases, patron_name, patron_aliases):
    for alias_name in patron_aliases:
        if alias_name != patron_name:
            inverse_patron_aliases[alias_name] = patron_name


def updateExistingPatron(patron_data, aliases, nationality, stats):
    patron_data.aliases.update(aliases)

    if patron_data.nationality is None:
        patron_data.nationality = nationality

    patron_data.stats.update(stats)


def processIndividualPatron(patron_aliases, patrons, nationality, patron_data):
    for patron_name in patron_aliases:
        if patron_name in patrons:
            # update existing

            existing_patron = patrons[patron_name]
            updateExistingPatron(existing_patron, set(patron_aliases), nationality, patron_data)
            return

    patron_name = patron_aliases[0]
    patrons[patron_name] = AuthorPatronElement.createPatron(patron_name, set(patron_aliases), nationality, patron_data)


def createIndividualPatrons(source_patrons, github_patrons, survey_patrons, social_patrons):
    patrons = {}

    for patron_name, patron_data in source_patrons:
        patron_aliases = set(patron_data)
        patrons[patron_name] = AuthorPatronElement.createPatron(patron_name, patron_aliases, None, {})

    for patron_name, patron_data in github_patrons:
        patron_data.pop('login')
        alias_name = patron_data.pop('name')
        nationality = patron_data.pop('nationality')

        patron_aliases = set()
        patron_aliases.add(patron_name)

        if alias_name is not None:
            patron_aliases.add(alias_name)  # an association of names for that github patron entry

        if patron_name not in patrons:
            patrons[patron_name] = AuthorPatronElement.createPatron(patron_name, patron_aliases, nationality, patron_data)
        else:   # update existing
            existing_patron = patrons[patron_name]
            updateExistingPatron(existing_patron, patron_aliases, nationality, patron_data)

    for patron_aliases, patron_nationality in survey_patrons:
        processIndividualPatron(patron_aliases, patrons, patron_nationality, {})

    for patron_data in social_patrons:
        processIndividualPatron(patron_data, patrons, None, {})

    inverse_patron_aliases = processInverseAliases(patrons)

    return (patrons, inverse_patron_aliases)


def processInverseAliases(patrons):
    inverse_patron_aliases = {}

    for patron in patrons.values():
        inverse_patron_aliases[patron.name] = patron.name

    for patron in patrons.values():
        applyInverseLinks(inverse_patron_aliases, patron.name, patron.aliases)

    return inverse_patron_aliases


class AuthorScanRepository():

    def writableTimestamp(self, ts):
        return writableTimestamp(ts)


    def isCommitFileDump(self, commit_timestamp, file_path, is_filesystem_check):
        if is_filesystem_check:
            ret = file_path in self.filesystem_dumps
            st = self.valid_commitfiles_fs
        else:
            ret = file_path in self.commit_dumps[commit_timestamp]
            st = self.valid_commitfiles_df[commit_timestamp]

        if ret: # SHORTCUT -
            st.add(file_path)

        if commit_timestamp in self.commitdump_fallback_date:   # SHORTCUT -
            ret = True

        return ret


    def printCommitDumps(self):
        for k, v in self.commit_dumps.items():
            commit_dump_path = self.lib_path + '/commitdump/' + str(k) + '.txt'
            setupDir(commit_dump_path)

            if len(v) > 0:
                file = open(commit_dump_path, 'w')
                for p in v:
                    file.write("'" + p + "'\n")

                file.close()


    def printCommitFileChecks(self, k, v):
        commit_fetch_path = self.lib_path + '/commitfetchs/' + str(k) + '.txt'
        setupDir(commit_fetch_path)

        if len(v) > 0:
            file = open(commit_fetch_path, 'w')
            for p in v:
                file.write("'" + p + "'\n")

            file.close()


    def printFileDumpChecks(self):
        for k, v in self.valid_commitfiles_df.items():
            self.printCommitFileChecks(k, v)

        self.printCommitFileChecks('filesystem', self.valid_commitfiles_fs)


    def getCommitTimestamps(self, commits_path):
        timestamps = []

        for filename in os.listdir(self.lib_path + '/' + commits_path):
            timestamps.append(self.parseFileTimestampDate(filename))

        return sorted(timestamps)


    def getCreatorCommitTimestamps(self):
        creator_ts = set()     # commit timestamps with "ronancpl" as author

        for commitData in self.commits_info:
            if commitData['author']['login'] == 'ronancpl':
                commit_timestamp = commitData['commit']['author']['date']
                creator_ts.add(commit_timestamp)

        return creator_ts


    def getDirectoryNameFromFilePath(self, file_path, max_depth):
        return getDirectoryNameFromFilePath(file_path, max_depth)


    '''
    def getCommitTimestamps(self):
        return self.commit_ts


    def getCreatorCommitTimestamps(self):
        return self.creator_ts
    '''


    def sortedTrafficEntries(self, traffic_entries):
        entries = []
        for name, content in traffic_entries.items():
            entries.append({'name': name, 'uniques': content[0], 'content': content[1]})

        return sorted(entries, key=lambda kv: kv['uniques'])


    def generateSequenceSectionDatabase(self, database, time_path_list, intervals, debug=False):
        intervals.append(datetime(7777, 7, 7))

        array = []
        for i in range(len(intervals)):
            array.append([])

        current_timestamp = intervals[0]
        idx = 0
        for database_item in database:
            if len(database_item) > 0:
                database_date = database_item
                for path in time_path_list:
                    database_date = database_date[path]

                timestamp = self.parseGranularTimestampDate(database_date)
                while timestamp > current_timestamp:
                    idx += 1
                    current_timestamp = intervals[idx]

                array[idx].append(database_item)

        if debug:
            print('--------------------------------------')
            print('Database content:')
            c = 0
            for item in array:
                print('Section ' + str(c) + ': ' + str(item) + '\n')
                c += 1

            print('--------------------------------------')

        return array


    def generateTimeSectionDatabase(self, database, time_path_list, months=0, days=0, debug=False):
        days_interval = self.getDayCount(months, days)
        if days_interval == 0:
            return None

        array = []
        for i in range(0, math.ceil(self.total_days / days_interval)):
            array.append([])

        for database_item in database:
            database_date = database_item
            for path in time_path_list:
                database_date = database_date[path]

            timestamp = self.parseTimestampDate(database_date)
            database_idx = self.fetchRepositoryTimeSection(timestamp, months, days)
            # print(str(len(array)) + ' ' + str(database_idx) + ' : ' + str(timestamp) + ' ' + str(months) + ' ' + str(days))
            array[database_idx].append(database_item)

        if debug:
            print('--------------------------------------')
            print('Database content:')
            c = 0
            for item in array:
                print('Section ' + str(c) + ': ' + str(item) + '\n')
                c += 1

            print('--------------------------------------')

        return array


    def parseTimestampDate(self, date_str):
        if type(date_str) is not str:   # SHORTCUT -
            return date_str

        return datetime.strptime(date_str[:date_str.find('T')], '%Y-%m-%d')  # Datetime from timestamp string


    def parseGranularTimestampDate(self, date_str):
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')    # Datetime from timestamp string


    def parseFileTimestampDate(self, date_str):
        return datetime.strptime(date_str[:14], '%Y%m%d%H%M%S')     # Datetime from timestamp string


    def parseFileTimestampToStringTimestamp(self, date_str):
        return self.writableTimestamp(self.parseFileTimestampDate(date_str))


    def fetchRepositoryTimeSectionFromTimestamp(self, timestamp, months=0, days=0):
        return self.fetchRepositoryTimeSection(self.parseTimestampDate(timestamp), months=months, days=days)


    def fetchRepositoryTimeSection(self, current_time, months=0, days=0):
        days_interval = self.getDayCount(months, days)
        if days_interval == 0:
            return -1

        elapsed_time = current_time - self.repository_start_time
        return math.floor(elapsed_time.days / days_interval)

    def getReleaseTimestamps(self):
        rls_data = scanner.releases.values()

        rls_ts = []
        for rls_item in sorted(rls_data, key=lambda k: k['created_at']):
            rls_ts.append(scanner.parseTimestampDate(rls_item['created_at']))

        return rls_ts


    def getDayCount(self, months, days):
        return 30 * months + days


    def normalizeEmptyUserEntry(self, github_user, user_info_key):
        if type(github_user) is dict:
            github_iter = [github_user]
        else:
            github_iter = github_user

        for github_item in github_iter:
            if github_item[user_info_key] is None:
                github_item[user_info_key] = {'login': '/null/'}


    def scanEmptyGithubUsers(self):
        for github_item in scanner.repo.values():
            self.normalizeEmptyUserEntry(github_item, 'owner')

        for github_item in scanner.forks.values():
            self.normalizeEmptyUserEntry(github_item, 'owner')

        for github_item in scanner.stargazers.values():
            self.normalizeEmptyUserEntry(github_item, 'user')

        # for github_item in scanner.subscribers.values():
        #     self.normalizeEmptyUserEntry(github_item, 'user')     already a git user node

        for github_item in scanner.users_issues.values():
            self.normalizeEmptyUserEntry(github_item, 'user')

        for github_item in scanner.users_pulls.values():
            self.normalizeEmptyUserEntry(github_item, 'user')

        for github_item in scanner.users_comments.values():
            self.normalizeEmptyUserEntry(github_item, 'user')

        for github_item in scanner.users_issue_comments.values():
            self.normalizeEmptyUserEntry(github_item, 'user')

        for github_item in self.commits.values():
            self.normalizeEmptyUserEntry(github_item, 'author')

        for github_item in self.commits_info:
            self.normalizeEmptyUserEntry(github_item, 'author')


    def writeGraphFile(self, file_path_name, content):
        file_graph_name = self.graph_path + '/' + file_path_name.value
        setupDir(file_graph_name)

        file = open(file_graph_name, 'wb')
        pickle.dump(content, file)
        file.close()


    def readGraphFile(self, file_path_name):
        file_graph_name = self.graph_path + '/' + file_path_name
        setupDir(file_graph_name)

        file = open(file_graph_name, 'rb')
        content = pickle.load(file)
        file.close()

        return content


    def loadJsonifiedScanRepository(self):
        try:
            with open(self.monolithic_file, 'rb') as file:
                print('Loading repository monolithic...')
                objfrom = pickle.load(file, encoding="UTF-32", errors="replace")

                for n, v in inspect.getmembers(objfrom):    # src: https://stackoverflow.com/questions/3818825/python-what-is-the-correct-way-to-copy-an-objects-attributes-over-to-another/3818861
                    try:
                        setattr(self, n, v)
                    except AttributeError:
                        pass

                global patronManager
                patronManager = AuthorPatronManager.patronManager
                patronManager.importPatrons(self.patrons_individuals, self.patrons_links, self.patrons_organizations)

                return True
        except (FileNotFoundError, EOFError):
            pass

        return False


    def dumpJsonifiedScanRepository(self):
        file = open(self.monolithic_file, 'wb')
        pickle.dump(self, file)
        file.close()


    def scanRepository(self):
        self.tracker_timesection_len = self.fetchRepositoryTimeSection(self.repository_finish_time, days=20) + 1

        self.repo = parseScanElement('id', scanFile(self.lib_path + '/repo/HeavenMS.txt', True))  # HeavenMS

        self.commits = parseScanCommits(self.lib_path + '/commits')
        self.commits_info = parseScanCommitsInfo(self.lib_path + '/commits.txt')

        self.contributors = parseScanElement('id', scanFile(self.lib_path + '/contributors.txt', True))
        self.forks = parseScanElement('id', scanFile(self.lib_path + '/forks.txt', True))
        self.languages = parseScanElement(None, scanFile(self.lib_path + '/languages.txt', False))    # not delete (progressive data)
        self.releases = parseScanElement('url', scanFile(self.lib_path + '/releases.txt', True))
        self.stargazers = parseScanElement(['user', 'id'], scanFile(self.lib_path + '/stargazers.txt', True))
        self.subscribers = parseScanElement('id', scanFile(self.lib_path + '/subscribers.txt', True))

        # stats -
        print('Loading stats...')
        self.stats_commit_activities = parseScanElement('week', scanFile(self.lib_path + '/stats/commit_activity.txt', True))     # not delete (1 year)
        self.stats_contributors = parseScanElement(['author', 'id'], scanFile(self.lib_path + '/stats/contributors.txt', True))   # not delete (1 year)
        self.stats_participations = parseScanElement(None, scanFile(self.lib_path + '/stats/participation.txt', False))           # not delete (1 year)

        # traffic -
        print('Loading traffic...')
        self.traffic_popular_paths = parseScanElement(None, scanFile(self.lib_path + '/traffic/popular/paths.txt', False))        # not delete (2 weeks)
        self.traffic_popular_referrers = parseScanElement(None, scanFile(self.lib_path + '/traffic/popular/referrers.txt', False))# not delete (2 weeks)
        self.traffic_clones = parseScanElement(None, scanFile(self.lib_path + '/traffic/clones.txt', False))                      # not delete (2 weeks)
        self.traffic_views = parseScanElement(None, scanFile(self.lib_path + '/traffic/views.txt', False))                        # not delete (2 weeks)

        # users -
        print('Loading users...')
        self.users_issue_comments = parseScanElement(None, scanFile(self.lib_path + '/users/issues/comments.txt', False))
        self.users_comments = parseScanElement(None, scanFile(self.lib_path + '/users/comments.txt', False))
        self.users_issues = parseScanElement('number', scanFile(self.lib_path + '/users/issues.txt', True))
        self.users_pulls = parseScanElement('number', scanFile(self.lib_path + '/users/pulls.txt', True))
        self.users_pulls_commits = parseScanElement(None, scanFile(self.lib_path + '/users/pulls/commits.txt', False))
        self.users_users = parseScanElement('id', scanFile(self.lib_path + '/users/users.txt', True))
        self.users_events_repos = parseScanGithubEvents(self.lib_path + '/users/events', self.users_users)

        print('Scanning user loadouts...')
        self.scanEmptyGithubUsers()

        print('Loading creator timestamps...')
        self.authoredTimestamps = self.getCreatorCommitTimestamps()

        print('Loading filesystem...')
        self.filesystem = parseScanFilesystem(self.lib_path + '/filesystem')

        print('Generating diffs...')
        self.commitdump_fallback_date = set()
        self.diffs, self.commits_file_changes, self.commit_file_diffs = parseScanFileDiffs()

        self.deltas = parseScanFileDeltas()

        self.commit_quests = parseScanQuestDiffs(self.commits, self.deltas, self.commit_file_diffs)

        print('Detecting commit file dumps...')
        self.commit_dumps, self.filesystem_dumps = parseScanCommitDumps(self.diffs)
        self.valid_commitfiles_fs = set()

        self.valid_commitfiles_df = {}
        for k in self.commit_dumps.keys():
            self.valid_commitfiles_df[k] = set()

        self.printCommitDumps()

        print('Loading patrons...')
        global patronManager
        patronManager = AuthorPatronManager.patronManager

        filePatrons = parseScanFilePatrons()
        self.patrons_organizations = filePatrons[0]

        githubPatrons = parseScanGithubPatrons(self.users_users)

        surveyContent = parseScanSurveyContent()
        self.survey = surveyContent[0]

        self.survey_metadata = parseSurveyMetadata()

        socialContent = parseScanSocialContent()
        self.social = socialContent[0]

        generatedPatrons = createIndividualPatrons(filePatrons[1], githubPatrons, surveyContent[1], socialContent[1])
        self.patrons_individuals = generatedPatrons[0]
        self.patrons_links = generatedPatrons[1]

        print('Organizations:')
        for name, assocs in self.patrons_organizations:
            print('  ' + name + ' : ' + str(assocs))

        print('Individuals:')
        for patron in self.patrons_individuals.values():
            print('  ' + str(patron))

        print('Inverse aliases:')
        for alias, name in self.patrons_links.items():
            print(alias + ' : ' + name)

        patronManager.importPatrons(self.patrons_individuals, self.patrons_links, self.patrons_organizations)

        self.patrons_directory_info = parseScanSourcePatrons(self.lib_path + '/patrons/')
        self.commit_patrons = parseScanFilePatronMovements()

        self.recalled_commits, self.recalled_pulls = parseRecalledGithubContents()

        print('Writing repository monolithic...')
        # self.dumpJsonifiedScanRepository()

        print('Load Repository COMPLETE')


    def routine_checkup(self):
        for git_commit_sha, git_commit_files in self.commit_file_diffs.items():
            git_commit_stats = self.commits[git_commit_sha]['stats']
            addt = git_commit_stats["additions"]
            delt = git_commit_stats["deletions"]
            chng = git_commit_stats["total"]

            n_idx = self.commits[git_commit_sha]["commit"]["message"].find('\n')
            if n_idx > -1:
                msg = self.commits[git_commit_sha]["commit"]["message"][:n_idx]
            else:
                msg = self.commits[git_commit_sha]["commit"]["message"]

            print(git_commit_sha + ' has ' + str(len(git_commit_files)) + ' changed files, ' + str(chng) + ' total, ' + str(addt) + '|' + str(delt) + ' : ' + msg)


    def __init__(self, scanner_load):   # "scanner_load" explicitly loads repository-analysis modules
        self.scanner_load = scanner_load

        self.lib_path = "../../lib"
        self.graph_path = "../../graph"
        self.tools_path = "../../tools"
        self.csv_path = '../../digest'
        self.plot_path = '../../chart'
        self.wordcloud_path = '../../wordcloud'
        self.wordpress_path = '../../wordpress/gen'

        self.repository_wz_path = "wz"
        self.repository_path = "../../../HeavenMS"
        self.wz_path = self.repository_path + '/' + self.repository_wz_path

        self.monolithic_file = self.lib_path + '/monolithic.txt'

        self.repository_start_time = datetime(2015, 7, 12)
        self.repository_finish_time = datetime(2019, 12, 31)

        self.total_days = (self.repository_finish_time - self.repository_start_time).days

        print('Loading repository database...')

        global scanner
        scanner = self

        if self.scanner_load is True:
            if not self.loadJsonifiedScanRepository():
                self.scanRepository()

            # self.routine_checkup()  # SHORTCUT -

        else:   # mandatory loads
            self.releases = parseScanElement('url', scanFile(self.lib_path + '/releases.txt', True))


global scanner
scanner = None