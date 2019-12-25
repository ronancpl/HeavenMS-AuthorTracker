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

result_type = AuthorGraphResultFile.ResultFile.TRAFFIC_REFERRERS


def isEmptyPlot(arr):
    for i in arr:
        if i != 0:
            return False

    return True


def plotfy(x, y, y_names, csv_filename, doc_index):
    if isEmptyPlot(y):
        return

    plot_img = grapher.fetchGraphFilename(csv_filename, doc_index)

    fig = plt.figure(dpi=1000, figsize=(7.00,10.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    ax = sns.lineplot(x=x, y=y)
    ax.set_ylabel(y_names[2])

    grapher.savePlot(fig, plot_img)
    # plt.show()
    plt.close(fig)


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    csv_filename = result_type.value

    for idx in range(len(scanner.generateTimeSectionDatabase([], [], days=40))):
        column_names, graph_content = grapher.readGraphDataset(csv_filename, idx)
        graph_content = sorted(graph_content, key=lambda k: k[2], reverse=True)

        name_values = []
        count_values = []
        uniques_values = []
        for graph_item in graph_content:
            name_values.append(graph_item[0])       # path
            count_values.append(graph_item[1])      # count
            uniques_values.append(graph_item[2])    # uniques

        y_names = column_names
        plotfy(name_values, count_values, y_names, csv_filename, 'count_jn' + str(idx))
        plotfy(name_values, uniques_values, y_names, csv_filename, 'uniques_jn' + str(idx))
