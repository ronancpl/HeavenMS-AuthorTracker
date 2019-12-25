import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
import math
import os.path


result_path_name = AuthorGraphResultFile.ResultFile.ATOMIC_FILE


def countFileActivityType(stats):
    ceil_count = 0
    total_count = 0

    for stat in stats.values():
        if ceil_count < stat:
            ceil_count = stat

        total_count += stat

    return ceil_count, total_count


def countFileActivities(deltas):
    file_activities = {}

    for file_delta in deltas.values():
        file_activity = {}
        file_activity['modification_count'] = file_delta['modification_count']

        add_c, add_t = countFileActivityType(file_delta['stats']['add_count'])
        del_c, del_t = countFileActivityType(file_delta['stats']['del_count'])
        chg_c, chg_t = countFileActivityType(file_delta['stats']['change_count'])

        upper_stats = {'add_count': add_c, 'del_count': del_c, 'change_count': chg_c}
        file_activity['upper_stats'] = upper_stats

        total_stats = {'add_count': add_t, 'del_count': del_t, 'change_count': chg_t}
        file_activity['total_stats'] = total_stats

        file_activities[file_delta['path']] = file_activity

    return file_activities


def run():
    scanner = AuthorScanRepository.scanner

    file_activities = countFileActivities(scanner.deltas)

    graph_content = sorted(file_activities.items(), key=lambda kv: kv[1]['modification_count'], reverse=True)

    print()
    print('file mod')

    i = 0
    for file, diff in graph_content:
        print(str(file) + ' : ' + str(diff))
        i += 1

        if i == 100:
            break

    scanner.writeGraphFile(result_path_name, graph_content)

if __name__ == '__main__':
    run()
