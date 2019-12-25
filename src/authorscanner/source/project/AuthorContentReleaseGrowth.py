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


result_path_name = AuthorGraphResultFile.ResultFile.CONTENT_RELEASE_GROWTH


def getEventIndex(event_data):
    return {
        'fork': 0,
        'star': 1,
        'issue': 2,
        'pull': 3,
    }.get(event_data['type'], 4)


def calculateReleaseGrowth(repo_data, release_intervals):
    fs_db = scanner.generateSequenceSectionDatabase(repo_data, ["created_at"], release_intervals)

    repoEventCount = []
    for idx in range(len(fs_db)):
        repoEventCount.append([0, 0, 0, 0, 0])   # forks, stars, issues, pulls, comments

    for idx in range(len(fs_db)):
        for fs_db_item in fs_db[idx]:
            type = getEventIndex(fs_db_item)
            repoEventCount[idx][type] += 1

    return repoEventCount


def createEventData(event_type, timestamp):
    return {'type': event_type, 'created_at': timestamp}


def getReleaseEventFileData(scanner_event, timestamp_path, event_name):
    event_data = []

    rls_content = []
    for rls_item in scanner_event.values():
        if type(rls_item) is dict:
            rls_content.append(rls_item)
        else:
            rls_content.extend(rls_item)

    for rls_item in rls_content:
        if len(rls_item) > 0:
            event_data.append(createEventData(event_name, rls_item[timestamp_path]))

    return event_data


def getReleaseEventData():
    rls_data = []

    rls_data.extend(getReleaseEventFileData(scanner.forks, 'created_at', 'fork'))
    rls_data.extend(getReleaseEventFileData(scanner.stargazers, 'starred_at', 'star'))
    rls_data.extend(getReleaseEventFileData(scanner.users_issues, 'created_at', 'issue'))
    rls_data.extend(getReleaseEventFileData(scanner.users_pulls, 'created_at', 'pull'))
    rls_data.extend(getReleaseEventFileData(scanner.users_comments, 'created_at', 'comment'))
    rls_data.extend(getReleaseEventFileData(scanner.users_issue_comments, 'created_at', 'comment'))

    return sorted(rls_data, key=lambda k: k['created_at'])


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    rls_ts = scanner.getReleaseTimestamps()
    rls_data = getReleaseEventData()

    releaseCount = calculateReleaseGrowth(rls_data, rls_ts)

    graph_content = releaseCount

    print()
    print('Release count')
    print(releaseCount)

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
