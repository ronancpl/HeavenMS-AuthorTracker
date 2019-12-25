import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
import math
import os.path


result_path_name = AuthorGraphResultFile.ResultFile.ATOMIC_DIRECTORY


def updateDirectoryStats(path, directory_activities, file_activities):
    if path in directory_activities:
        dir_activity = directory_activities[path]
    else:
        dir_activity = {'modification_count': 0, 'upper_stats': {'add_count': 0, 'del_count': 0, 'change_count': 0},
                                                 'total_stats': {'add_count': 0, 'del_count': 0, 'change_count': 0},
                        'participating_commits': set()}

        directory_activities[path] = dir_activity

    for commit_ts in file_activities['participating_commits']:
        if commit_ts not in dir_activity['participating_commits']:
            dir_activity['participating_commits'].add(commit_ts)
            dir_activity['modification_count'] += 1

    dir_upper_stats = dir_activity['upper_stats']
    file_upper_stats = file_activities['upper_stats']

    dir_upper_stats['add_count'] = max(dir_upper_stats['add_count'], file_upper_stats['add_count'])
    dir_upper_stats['del_count'] = max(dir_upper_stats['del_count'], file_upper_stats['del_count'])
    dir_upper_stats['change_count'] = max(dir_upper_stats['change_count'], file_upper_stats['change_count'])

    dir_total_stats = dir_activity['total_stats']
    file_total_stats = file_activities['total_stats']

    dir_total_stats['add_count'] += file_total_stats['add_count']
    dir_total_stats['del_count'] += file_total_stats['del_count']
    dir_total_stats['change_count'] += file_total_stats['change_count']


def updateUpperDirectories(path, directory_activities, file_stats):
    updateDirectoryStats(path, directory_activities, file_stats)

    ridx = path.rfind('/')
    if ridx != -1:
        updateUpperDirectories(path[:ridx], directory_activities, file_stats)


def countFileActivityType(stats, commit_mod_ts):
    ceil_count = 0
    total_count = 0

    for commit_ts, stat in stats.items():
        if ceil_count < stat:
            ceil_count = stat

        total_count += stat
        commit_mod_ts.add(commit_ts)

    return ceil_count, total_count


def countFileActivities(deltas):
    file_activities = {}

    for file_delta in deltas.values():
        file_activity = {}
        file_activity['modification_count'] = file_delta['modification_count']

        commit_mod_ts = set()
        add_c, add_t = countFileActivityType(file_delta['stats']['add_count'], commit_mod_ts)
        del_c, del_t = countFileActivityType(file_delta['stats']['del_count'], commit_mod_ts)
        chg_c, chg_t = countFileActivityType(file_delta['stats']['change_count'], commit_mod_ts)

        upper_stats = {'add_count': add_c, 'del_count': del_c, 'change_count': chg_c}
        file_activity['upper_stats'] = upper_stats

        total_stats = {'add_count': add_t, 'del_count': del_t, 'change_count': chg_t}
        file_activity['total_stats'] = total_stats

        file_activity['participating_commits'] = commit_mod_ts
        file_activities[file_delta['path']] = file_activity

    return file_activities


def run():
    scanner = AuthorScanRepository.scanner

    file_activities = countFileActivities(scanner.deltas)
    directory_activities = {}

    for file_path, file_stats in file_activities.items():
        ridx = file_path.rfind('/')
        if ridx != -1:
            updateUpperDirectories(file_path[:ridx], directory_activities, file_stats)

    graph_content = sorted(directory_activities.items(), key=lambda kv: kv[1]['modification_count'], reverse=True)

    print()
    print('directory mod')

    i = 0
    for file, diff in graph_content:
        print(str(file) + ' : ' + str(diff))
        i += 1

        if i == 100:
            break

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
