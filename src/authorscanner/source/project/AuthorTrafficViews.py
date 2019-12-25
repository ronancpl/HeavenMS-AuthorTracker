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


result_path_name = AuthorGraphResultFile.ResultFile.TRAFFIC_VIEWS


def updateDailyEntry(dailies, log_item):
    if log_item['timestamp'] not in dailies:
        dailies[log_item['timestamp']] = (log_item['count'], log_item['uniques'])
    else:
        daily_item = dailies[log_item['timestamp']]
        if daily_item[0] < log_item['count']:
            dailies[log_item['timestamp']] = (log_item['count'], log_item['uniques'])


def generateViewLogList():
    view_dailies = {}
    for log_view in scanner.traffic_views.values():
        for log_item in log_view[0]['views']:
            updateDailyEntry(view_dailies, log_item)

    view_items = []
    for view_time, view_count in view_dailies.items():
        view_items.append({'logged_at': view_time, 'content': view_count})

    return sorted(view_items, key=lambda kv: kv['logged_at'])  # commit entries in chronological order


def scanViewPopularity():
    view_list = generateViewLogList()
    view_db = scanner.generateSequenceSectionDatabase(view_list, ['logged_at'], scanner.getCommitTimestamps('commits/'), debug=False)

    view_contents = []
    for view_ts in view_db:
        view_content_item = [[], []]

        for view_it in view_ts:
            view_ct = view_it['content']

            view_content_item[0].append(view_ct[0]) # 'count'
            view_content_item[1].append(view_ct[1]) # 'uniques'

        view_contents.append(view_content_item)

    return view_contents


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    view_traffic = scanViewPopularity()

    graph_content = view_traffic

    print()
    print('Traffic views')

    i = 0
    for view_count in view_traffic:
        print('Commit ' + str(i) + ': ' + str(view_count))
        i += 1

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
