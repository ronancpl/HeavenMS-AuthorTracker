import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authorscanner import AuthorScanRepository

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.COMMIT_FILE_LINE_GROWTH


def loadTimesectionGraphDataset(graph_content):
    rls_file_db = scanner.generateSequenceSectionDatabase(graph_content, ["commit_time"], scanner.getReleaseTimestamps())
    return rls_file_db


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    rls_line_growth_db = loadTimesectionGraphDataset(result_type.readGraphFile())

    for rls_line_growth_range_idx in range(len(rls_line_growth_db)):
        rls_line_growth_range = rls_line_growth_db[rls_line_growth_range_idx]

        graph_dataset = []
        graph_idx = []
        graph_ts = []

        for rls_line_item in rls_line_growth_range:
            rls_line_ts = rls_line_item['commit_time']

            idx = scanner.fetchRepositoryTimeSectionFromTimestamp(rls_line_ts, days=1)
            graph_idx.append(idx)
            graph_ts.append(rls_line_ts)

            graph_item = []
            for i in range(5):
                graph_item.append([0, 0, 0])    # all 3 change types

            graph_data = []
            graph_dataset.append(graph_data)
            graph_data.append(rls_line_ts)

            commit_diff_count = rls_line_item['diff_count']
            for ftype_idx in range(len(commit_diff_count)):
                commit_ftype_diff_count = commit_diff_count[ftype_idx]

                for diff_idx in range(len(commit_ftype_diff_count)):
                    diff_count = commit_ftype_diff_count[diff_idx]
                    graph_item[ftype_idx][diff_idx] = diff_count

            graph_data.extend(graph_item)

        graph_content = grapher.loadGraphDatasetFormat(['commit', 'all', 'java', 'js', 'xml', 'other'], graph_dataset)
        grapher.writeGraphDataset(result_type.value, graph_content, rls_line_growth_range_idx)
