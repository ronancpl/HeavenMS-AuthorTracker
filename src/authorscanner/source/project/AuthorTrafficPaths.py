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


result_path_name = AuthorGraphResultFile.ResultFile.TRAFFIC_PATHS


def updatePathSearchEntry(log_paths, path_item, log_timestamp):
    path_name = path_item['path']

    if path_name in log_paths:
        path = log_paths[path_name]
    else:
        path = []
        log_paths[path_name] = path

    path.append({'logged_at': log_timestamp, 'count': path_item['count'], 'uniques': path_item['uniques']})


def generatePathSearchLogList():
    paths = {}

    for log_date, log_paths in scanner.traffic_popular_paths.items():
        log_timestamp = scanner.writableTimestamp(log_date)

        for log_path in log_paths:
            updatePathSearchEntry(paths, log_path, log_timestamp)

    return paths


def scanPathPopularity():
    path_list = generatePathSearchLogList()

    path_count = {}
    for path_name, path_data in path_list.items():
        path_db = scanner.generateTimeSectionDatabase(path_data, ['logged_at'], days=40)

        path_contents = []
        path_uniques = 0
        for path_ts in path_db:
            path_content_item = [0, 0]

            for path_ct in path_ts:
                path_content_item[0] += path_ct['count']
                path_content_item[1] += path_ct['uniques']
                path_uniques += path_content_item[1]

            path_contents.append(path_content_item)

        path_count[path_name] = path_uniques, path_contents

    return scanner.sortedTrafficEntries(path_count)


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    path_traffic = scanPathPopularity()
    graph_content = path_traffic

    print()
    print('Traffic paths')

    for path_item in path_traffic:
        path_name = path_item['name']
        path_uniques = path_item['uniques']
        print(str(path_name) + ': ' + str(path_uniques))

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
