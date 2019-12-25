import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
import AuthorScanJsonReader
import math
import os.path


result_path_name = AuthorGraphResultFile.ResultFile.CREATOR_ISSUES_CLOSED

lib_path = "../../lib/"


def generateTimeSectionIssueList():
    issue_list = []

    for issue_item in scanner.users_issues.values():
        if len(issue_item) > 0:
            issue_list.append(issue_item)


    return scanner.generateTimeSectionDatabase(issue_list, ['created_at'], months=2, days=0, debug=False)


def calculateClosedIssues(ts_issues):
    ts_closed_issues = []

    for ts_range in ts_issues:
        closed_timeframes = []
        closed_by_creator = 0

        for issue_data in ts_range:
            if issue_data['state'] == 'closed':
                issue_opened = scanner.parseGranularTimestampDate(issue_data['created_at'])
                issue_closed = scanner.parseGranularTimestampDate(issue_data['closed_at'])

                issue_timeframe = issue_closed - issue_opened
                closed_timeframes.append(issue_timeframe.seconds)

                issue_closed_by_key = 'closed_by'
                if issue_closed_by_key in issue_data:
                    issue_closed_by = issue_data[issue_closed_by_key]
                    if issue_closed_by is not None and issue_closed_by['login'] == 'ronancpl':
                        closed_by_creator += 1

        # calc average timeframe from closed issues
        average_timeframe = 0.0
        closed_timeframes_len = len(closed_timeframes)
        if closed_timeframes_len > 0:
            for tf in closed_timeframes:
                average_timeframe += tf

            average_timeframe /= closed_timeframes_len

        closed_issues_res = {'closed_by_creator_count': closed_by_creator, 'issues_count': len(closed_timeframes), 'average_time_frame': average_timeframe}
        ts_closed_issues.append(closed_issues_res)

    return ts_closed_issues


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    closed_issues_data = calculateClosedIssues(generateTimeSectionIssueList())

    graph_content = closed_issues_data

    print()
    print('Issues closed')

    i = 0
    for closed_issue in closed_issues_data:
        print('Month' + str(2 * i) + ': ' + str(closed_issue))
        i += 1

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
