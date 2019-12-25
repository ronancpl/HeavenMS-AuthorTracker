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

result_type = AuthorGraphResultFile.ResultFile.COMMIT_FILE_SIZE_GROWTH


def fetchSegments(x, num_file_types):
    ret = []
    for i in range(math.ceil(len(x) / num_file_types)):
        ret.append([])

    for idx in range(len(x)):
        ret[idx % num_file_types].append(x[idx])

    return ret


def plotfy(x, y, y_names, csv_filename, doc_index):
    plot_img = grapher.fetchGraphFilename(csv_filename, doc_index)

    data = {"commits": x, "file_size": y}
    df = pd.DataFrame(data)

    fig = plt.figure(dpi=1000, figsize=(6.40,7.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    ax = sns.pointplot(x='commits', y='file_size', data=df, scale=0.4)
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
        file_size_values = []
        for graph_item in graph_content:
            commit_values.append(graph_item[0])

            for i in range(1, len(graph_item)):
                file_size_values.append(graph_item[i])

        file_size_segments = fetchSegments(file_size_values, 5)  # all file types
        y_names = column_names

        file_types = ['all', 'java', 'js', 'xml', 'other']
        for i in range(5):
            plotfy(commit_values, file_size_segments[i], y_names, csv_filename, 'jn' + str(release_idx) + '_' + file_types[i])

