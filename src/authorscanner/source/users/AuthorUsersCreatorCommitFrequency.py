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


result_path_name = AuthorGraphResultFile.ResultFile.CREATOR_COMMIT_FREQUENCY

lib_path = "../../lib/"


def generateTimeSectionCommitsList():
    commit_list = []

    git_commits = scanner.commits_info
    for commit_item in git_commits:
        if commit_item['author']['login'] == 'ronancpl':
            commit_list.append(commit_item)

    return scanner.generateTimeSectionDatabase(commit_list, ['commit', 'author', 'date'], months=2, days=0, debug=False)


def calculateCommitFrequency(commits_ts):
    commit_frequency_ts = []
    for commits_ts_range in commits_ts:
        commit_ts_count = len(commits_ts_range)
        commit_frequency_ts.append(commit_ts_count)

    return commit_frequency_ts


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    commit_list = generateTimeSectionCommitsList()
    commit_frequency_data = calculateCommitFrequency(commit_list)

    graph_content = commit_frequency_data

    print()
    print('Commit freq')
    i = 0
    for commit_freq in commit_frequency_data:
        print('Month' + str(2 * i) + ': ' + str(commit_freq))
        i += 1

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
