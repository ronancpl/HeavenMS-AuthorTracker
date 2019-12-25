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


result_path_name = AuthorGraphResultFile.ResultFile.CONTENT_REPOSITORY_GROWTH

lib_path = "../../lib/"


def getEventIndex(event_data):
    return {
        'fork': 0,
        'star': 1,
        'issue': 2,
        'pull': 3,
    }.get(event_data['type'], 4)


def calculateRepositoryGrowth(repo_data):
    fs_db = scanner.generateTimeSectionDatabase(repo_data, ["created_at"], months=3, days=0)

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


def getRepositoryEventFileData(scanner_event, timestamp_path, event_name):
    event_data = []

    repo_content = []
    for repo_item in scanner_event.values():
        if type(repo_item) is dict:
            repo_content.append(repo_item)
        else:
            repo_content.extend(repo_item)

    for repo_item in repo_content:
        if len(repo_item) > 0:
            event_data.append(createEventData(event_name, repo_item[timestamp_path]))

    return event_data


def getRepositoryEventData():
    repo_data = []

    repo_data.extend(getRepositoryEventFileData(scanner.forks, 'created_at', 'fork'))
    repo_data.extend(getRepositoryEventFileData(scanner.stargazers, 'starred_at', 'star'))
    repo_data.extend(getRepositoryEventFileData(scanner.users_issues, 'created_at', 'issue'))
    repo_data.extend(getRepositoryEventFileData(scanner.users_pulls, 'created_at', 'pull'))
    repo_data.extend(getRepositoryEventFileData(scanner.users_comments, 'created_at', 'comment'))
    repo_data.extend(getRepositoryEventFileData(scanner.users_issue_comments, 'created_at', 'comment'))

    return sorted(repo_data, key=lambda k: k['created_at'])


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    repo_data = getRepositoryEventData()
    repoMovementCount = calculateRepositoryGrowth(repo_data)

    graph_content = repoMovementCount

    print()
    print('Repo movement')
    print(repoMovementCount)

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
