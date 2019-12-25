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


result_path_name = AuthorGraphResultFile.ResultFile.CONTENT_SEARCHED_PATHS

lib_path = "../../lib/"


def sortTimesectionPopularPaths(searched_path_items):
    popular_paths = {}

    for path_item in searched_path_items:
        path_name = path_item['path']

        if path_name not in popular_paths:
            popular_paths[path_name] = [path_item['count'], path_item['uniques']]
        else:
            popular_paths[path_name][0] = max(popular_paths[path_name][0], path_item['count'])
            popular_paths[path_name][1] = max(popular_paths[path_name][1], path_item['uniques'])

    return sorted(popular_paths.items(), key=lambda kv: kv[1][1], reverse=True)


def sortPopularPaths():
    popular_paths = []

    for path_date, path_items in scanner.traffic_popular_paths.items():
        popular_paths.append({'fetchDate': scanner.writableTimestamp(path_date), 'content': path_items})

    popular_paths_db = scanner.generateTimeSectionDatabase(popular_paths, ['fetchDate'], months=2, days=0, debug=False)

    popular_paths = []
    for popular_paths_range in popular_paths_db:
        popular_paths_ts = []

        for popular_paths_item in popular_paths_range:
            popular_paths_ts.extend(popular_paths_item['content'])

        sorted_popular_paths = sortTimesectionPopularPaths(popular_paths_ts)
        popular_paths.append(sorted_popular_paths)

    return popular_paths


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    popular_paths_ts = sortPopularPaths()

    graph_content = popular_paths_ts

    print()
    print('Searched paths')

    i = 0
    for ts_popular_paths in popular_paths_ts:
        print('  Month: ' + str(2 * i))
        print(ts_popular_paths)
        print()
        i += 1

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
