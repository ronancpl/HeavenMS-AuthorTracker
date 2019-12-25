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


result_path_name = AuthorGraphResultFile.ResultFile.TRAFFIC_REFERRERS


def updateReferrerEntry(log_referrers, referrer_item, log_timestamp):
    referrer_name = referrer_item['referrer']

    if referrer_name in log_referrers:
        referrer = log_referrers[referrer_name]
    else:
        referrer = []
        log_referrers[referrer_name] = referrer

    referrer.append({'logged_at': log_timestamp, 'count': referrer_item['count'], 'uniques': referrer_item['uniques']})


def generateReferrerLogList():
    referrers = {}

    for log_date, log_referrers in scanner.traffic_popular_referrers.items():
        log_timestamp = scanner.writableTimestamp(log_date)

        for log_referrer in log_referrers:
            updateReferrerEntry(referrers, log_referrer, log_timestamp)

    return referrers


def scanReferrerPopularity():
    ref_list = generateReferrerLogList()

    ref_count = {}
    for referrer_name, referrer_data in ref_list.items():
        ref_db = scanner.generateTimeSectionDatabase(referrer_data, ['logged_at'], days=40)

        ref_contents = []
        ref_uniques = 0
        for ref_ts in ref_db:
            ref_content_item = [0, 0]

            for ref_ct in ref_ts:
                ref_content_item[0] += ref_ct['count']
                ref_content_item[1] += ref_ct['uniques']
                ref_uniques += ref_content_item[1]

            ref_contents.append(ref_content_item)

        ref_count[referrer_name] = ref_uniques, ref_contents

    return scanner.sortedTrafficEntries(ref_count)


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    ref_traffic = scanReferrerPopularity()
    graph_content = ref_traffic

    print()
    print('Traffic referrers')

    for ref_item in ref_traffic:
        ref_name = ref_item['name']
        ref_uniques = ref_item['uniques']

        print(str(ref_name) + ': ' + str(ref_uniques))

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
