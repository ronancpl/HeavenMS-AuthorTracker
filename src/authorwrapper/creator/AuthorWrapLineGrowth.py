import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import errno
import os

from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.CREATOR_LINE_GROWTH


def plotfy(x, y1, y2, y3, y_names, csv_filename, doc_index):
    plot_img = grapher.fetchGraphFilename(csv_filename, doc_index)

    fig = plt.figure(dpi=1000, figsize=(6.40,7.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    data = {"months (3)": x, "additions": y1, "deletions": y2, "changes": y3}
    df = pd.DataFrame(data)

    ax = sns.barplot(x='months (3)', y='value', hue='variable', data=pd.melt(df, ['months (3)']))
    ax.set_ylabel('count')

    grapher.savePlot(fig, plot_img)
    # plt.show()
    plt.close(fig)


def fetchSegments(x, num_file_types):
    ret = []
    for i in range(math.ceil(len(x) / num_file_types)):
        ret.append([])

    for idx in range(len(x)):
        ret[idx % num_file_types].append(x[idx])

    return ret


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    csv_filename = result_type.value

    lines_column_names, lines_graph_content = grapher.readGraphDataset(csv_filename)

    month_values = []
    additions_values = []
    deletions_values = []
    changes_values = []
    for lines_graph_item in lines_graph_content:
        month_values.append(lines_graph_item[0])

        for i in range(1, len(lines_graph_item), 3):
            additions_values.append(lines_graph_item[i])
            deletions_values.append(lines_graph_item[i + 1])
            changes_values.append(lines_graph_item[i + 2])

    additions_segments = fetchSegments(additions_values, 5) # all file types
    deletions_segments = fetchSegments(deletions_values, 5)
    changes_segments = fetchSegments(changes_values, 5)
    y_names = lines_column_names

    file_types = ['all', 'java', 'js', 'xml', 'other']
    for i in range(5):
        plotfy(month_values, additions_segments[i], deletions_segments[i], changes_segments[i], y_names, csv_filename, file_types[i])
