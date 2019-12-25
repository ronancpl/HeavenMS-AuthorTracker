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

result_type = AuthorGraphResultFile.ResultFile.CONTENT_FILE_COUNT_GROWTH


def plotfy(data, csv_filename):
    plot_img = grapher.fetchGraphFilename(csv_filename)

    # x = 'months (3)', y = 'value', hue = 'variable', data = pd.melt(df, ['months (3)']), scale = 0.4
    fig = sns.catplot(x='timeset', y='count', col='filetype', kind='point', data=data, height=5, aspect=1)

    grapher.savePlot(fig, plot_img)
    # plt.show()
    # plt.close(fig)


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    csv_filename = result_type.value

    column_names, graph_content = grapher.readGraphDataset(csv_filename)

    dd = {'timeset': [], 'filetype': [], 'count': []}
    for graph_content_range_idx in range(len(graph_content)):
        graph_content_range = graph_content[graph_content_range_idx]

        for filetype_graph_content_idx in range(len(graph_content_range) - 1):  # not plotting last element (is 0)
            filetype_graph_content = graph_content_range[filetype_graph_content_idx]

            dd['timeset'].append(str(graph_content_range_idx).zfill(2))
            dd['filetype'].append(column_names[filetype_graph_content_idx])
            dd['count'].append(filetype_graph_content)

    graph_df = pd.DataFrame(data=dd)
    plotfy(graph_df, csv_filename)
