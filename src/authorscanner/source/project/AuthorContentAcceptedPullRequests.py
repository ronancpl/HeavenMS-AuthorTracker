import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
import math


result_path_name = AuthorGraphResultFile.ResultFile.CONTENT_ACCEPTED_PULL_REQUESTS


def calculatePullResults():
    pulls_db = scanner.generateTimeSectionDatabase(scanner.users_pulls.values(), ['created_at'], months=3, days=0, debug=False)

    pulls_counts = []
    print('Accepted pulls')
    for ts_branch in pulls_db:
        merged = 0
        closed = 0

        for ts_item in ts_branch:
            if ts_item['merged']:
                merged += 1
            else:
                closed += 1

        pulls_counts.append((merged, closed))
        print((merged, closed))

    return pulls_counts


def run():
    global scanner
    scanner = AuthorScanRepository.scanner
    pullsCounts = calculatePullResults()

    graph_content = pullsCounts
    scanner.writeGraphFile(result_path_name, graph_content)

if __name__ == '__main__':
    run()
