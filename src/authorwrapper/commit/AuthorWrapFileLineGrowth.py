import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import errno
import os

from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.COMMIT_FILE_LINE_GROWTH


def fetchSegments(x, num_file_types):
    ret = []
    for i in range(math.ceil(len(x) / num_file_types)):
        ret.append([])

    for idx in range(len(x)):
        ret[idx % num_file_types].append(x[idx])

    return ret


def plotfy(x, y1, y2, y3, y_names, csv_filename, doc_index):
    plot_img = grapher.fetchGraphFilename(csv_filename, doc_index)

    y = []
    for idx in range(len(y1)):
        modifs = y1[idx] + y2[idx] + y3[idx]
        y.append(modifs)

    data = {"commits": x, "modifications": y, "additions": y1}
    df = pd.DataFrame(data=data)

    fig = plt.figure(dpi=1000, figsize=(6.40,7.00))

    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    ax = sns.pointplot(x='commits', y='value', hue='variable', data=pd.melt(df, ['commits']), scale=0.4, dodge=True)
    ax.set_ylabel('count')

    grapher.savePlot(fig, plot_img)
    # plt.show()
    plt.close(fig)


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    csv_filename = result_type.value

    for release_idx in range(len(scanner.getReleaseTimestamps())):  # all releases
        column_names, graph_content = grapher.readGraphDataset(csv_filename, release_idx)

        commit_values = []
        additions_values = []
        deletions_values = []
        changes_values = []
        for graph_item in graph_content:
            commit_values.append(graph_item[0])

            for i in range(1, len(graph_item)):
                additions_values.append(graph_item[i][0])
                deletions_values.append(graph_item[i][1])
                changes_values.append(graph_item[i][2])

        additions_segments = fetchSegments(additions_values, 5)  # all file types
        deletions_segments = fetchSegments(deletions_values, 5)
        changes_segments = fetchSegments(changes_values, 5)
        y_names = column_names

        file_types = ['all', 'java', 'js', 'xml', 'other']
        for i in range(5):
            plotfy(commit_values, additions_segments[i], deletions_segments[i], changes_segments[i], y_names, csv_filename, 'jn' + str(release_idx) + '_' + file_types[i])

