import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from authorscanner import AuthorScanRepository
import AuthorScanJsonReader
import math
import os.path


def updateDiffStatIfNotZero(file_stat, mod_value, commit_time):
    if mod_value > 0:
        file_stat[commit_time] = mod_value


def parseCommitDiff(diff_items, diff_tree, commit_time, commit_sha):
    diff_tree_copy = diff_tree.copy()   # to avoid file glitch in "renaming file then creating new file with same previous name"
    added_files = {}

    for file_item in diff_items:
        if file_item['path'] in diff_tree_copy:  # tantamount to "if file_item['type'] != 2", but will break on non-processed (too large) diffs
            file_diff_blob = diff_tree_copy[file_item['path']]
        else:
            file_diff_blob = {'path': file_item['path'],
                              'path_history': [],
                              'modification_count': 0,
                              'modification_commit_times': [],
                              'modification_commit_shas': [],
                              'stats': {'add_count': {},
                                        'del_count': {},
                                        'change_count': {}
                                        }
                              }

        file_diff_stats = file_diff_blob['stats']
        updateDiffStatIfNotZero(file_diff_stats['add_count'], file_item['add_count'], commit_time)
        updateDiffStatIfNotZero(file_diff_stats['del_count'], file_item['del_count'], commit_time)
        updateDiffStatIfNotZero(file_diff_stats['change_count'], file_item['change_count'], commit_time)

        file_diff_blob['modification_count'] += 1
        file_diff_blob['modification_commit_times'].append(commit_time)
        file_diff_blob['modification_commit_shas'].append(commit_sha)

        file_diff_type = file_item['type']
        if file_diff_type == 3:     # file repositioned
            file_diff_blob['path_history'].append(file_item['fromPath'])
            next_file_path = file_item['path']

            rmv_item = file_item['fromPath']
            if rmv_item in diff_tree:
                diff_tree.pop(rmv_item)
        elif file_diff_type == 1:   # file deleted
            next_file_path = 'dev/null/' + file_item['path']

            rmv_item = file_item['path']
            if rmv_item in diff_tree:
                diff_tree.pop(rmv_item)
        elif file_diff_type == 2:   # file added
            next_file_path = file_item['path']
            added_files[next_file_path] = file_diff_blob
            continue
        else:
            next_file_path = file_item['path']

        file_diff_blob['path'] = next_file_path
        diff_tree[next_file_path] = file_diff_blob

    for file_path, file_diff_blob in added_files.items():
        diff_tree[file_path] = file_diff_blob


def calculateCommitChanges(except_deleted=False):
    fs_vals = []
    for fs_key, fs_val in sorted(scanner.diffs.items(), key=lambda kv: kv[0]):   # commit entries in chronological order
        fs_vals.append(fs_val)

    fs_db = generateSequenceSectionDatabase(fs_vals, ['commit_time'], scanner.getCommitTimestamps('commits/'), debug=False)
    diff_tree = {}

    for fs_db_range in fs_db:
        for fs_db_item in fs_db_range:
            if fs_db_item['commit_time'] in scanner.authoredTimestamps:
                item_ct = fs_db_item['content']
                parseCommitDiff(item_ct, diff_tree, fs_db_item['commit_time'], fs_db_item['sha'])

    if except_deleted:
        to_remove = []
        for key in diff_tree.keys():
            if key.startswith('dev/null'):
                to_remove.append(key)

        for key in to_remove:
            diff_tree.pop(key)

    return diff_tree


# \/\/\/\/\/\/ from AuthorScanRepository \/\/\/\/\/\/


def parseGranularTimestampDate(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')  # Datetime from timestamp string


def generateSequenceSectionDatabase(database, time_path_list, intervals, debug=False):
    intervals.append(datetime(7777, 7, 7))

    array = []
    for i in range(len(intervals)):
        array.append([])

    current_timestamp = intervals[0]
    idx = 0
    for database_item in database:
        database_date = database_item
        for path in time_path_list:
            database_date = database_date[path]

        timestamp = parseGranularTimestampDate(database_date)
        while timestamp >= current_timestamp:
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


# /\/\/\/\/\/\ from AuthorScanRepository /\/\/\/\/\/\


class AuthorScanGitFileMovement:

    def countRepositoryGitFileMovement(self):
        global scanner
        scanner = AuthorScanRepository.scanner

        repositoryFileEntries = calculateCommitChanges(except_deleted=True)

        return repositoryFileEntries
