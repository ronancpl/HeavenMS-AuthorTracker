import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import AuthorScanJsonReader
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
import math
import os.path
import re


result_path_name = AuthorGraphResultFile.ResultFile.TRAFFIC_CLONES


def updateDailyEntry(dailies, log_item):
    if log_item['timestamp'] not in dailies:
        dailies[log_item['timestamp']] = (log_item['count'], log_item['uniques'])
    else:
        daily_item = dailies[log_item['timestamp']]
        if daily_item[0] < log_item['count']:
            dailies[log_item['timestamp']] = (log_item['count'], log_item['uniques'])


def generateCloneLogList():
    clone_dailies = {}
    for log_clones in scanner.traffic_clones.values():
        for log_item in log_clones[0]['clones']:
            updateDailyEntry(clone_dailies, log_item)

    clone_items = []
    for clone_time, clone_count in clone_dailies.items():
        clone_items.append({'logged_at': clone_time, 'content': clone_count})

    return sorted(clone_items, key=lambda kv: kv['logged_at'])  # commit entries in chronological order


def scanClonePopularity():
    clone_list = generateCloneLogList()
    clone_db = scanner.generateSequenceSectionDatabase(clone_list, ['logged_at'], scanner.getCommitTimestamps('commits/'), debug=False)

    clone_contents = []
    for clone_ts in clone_db:
        clone_content_item = [[], []]

        for clone_it in clone_ts:
            clone_ct = clone_it['content']
            clone_content_item[0].append(clone_ct[0])   # 'count'
            clone_content_item[1].append(clone_ct[1])   # 'uniques'

        clone_contents.append(clone_content_item)

    return clone_contents


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    clone_traffic = scanClonePopularity()

    graph_content = clone_traffic

    print()
    print('Traffic Clones')

    i = 0
    for clone_count in clone_traffic:
        print('Commit ' + str(i) + ': ' + str(clone_count))
        i += 1

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
