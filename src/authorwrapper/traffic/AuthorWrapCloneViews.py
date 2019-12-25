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

clones_type = AuthorGraphResultFile.ResultFile.TRAFFIC_CLONES
views_type = AuthorGraphResultFile.ResultFile.TRAFFIC_VIEWS


def isEmptyPlot(arr):
    for i in arr:
        if i != 0:
            return False

    return True


def plotfy(x, y, y_names, csv_filename, doc_index):
    plot_img = grapher.fetchGraphFilename(csv_filename, doc_index)

    fig = plt.figure(dpi=1000, figsize=(7.00,10.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    y_elem = []
    for y_db_range in y:
        v = 0
        for y_item in y_db_range:
            if v < y_item:
                v = y_item

        y_elem.append(v)

    if isEmptyPlot(y_elem):
        return

    ax = sns.barplot(x=x, y=y_elem)
    ax.set_xlabel('commit')
    ax.set_ylabel(y_names[0])

    grapher.savePlot(fig, plot_img)
    # plt.show()
    plt.close(fig)


def plotGraphs(clones_uniques_values_all, views_uniques_values_all, y_names, clones_csv_filename, doc_index):
    i = 0
    graph = 0

    limit = len(clones_uniques_values_all)
    while True:
        next_i = i + 50
        if next_i > limit:
            next_i = limit
            plotfy(list(range(i, next_i)), clones_uniques_values_all[i:next_i], y_names, clones_csv_filename, doc_index + str(graph))
            plotfy(list(range(i, next_i)), views_uniques_values_all[i:next_i], y_names, clones_csv_filename, doc_index + str(graph))
            break

        plotfy(list(range(i, next_i)), clones_uniques_values_all[i:next_i], y_names, clones_csv_filename, doc_index + str(graph))
        plotfy(list(range(i, next_i)), views_uniques_values_all[i:next_i], y_names, clones_csv_filename, doc_index + str(graph))

        i = next_i
        graph += 1


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    clones_csv_filename = clones_type.value

    clones_column_names, clones_graph_content = grapher.readGraphDataset(clones_csv_filename)

    clones_count_values = []
    clones_uniques_values = []
    for count_uniques_ts in clones_graph_content:
        clones_count_values.append(count_uniques_ts[0])
        clones_uniques_values.append(count_uniques_ts[1])

    views_csv_filename = views_type.value
    views_column_names, views_graph_content = grapher.readGraphDataset(views_csv_filename)

    views_count_values = []
    views_uniques_values = []
    for count_uniques_ts in views_graph_content:
        views_count_values.append(count_uniques_ts[0])
        views_uniques_values.append(count_uniques_ts[1])

    y_names = views_column_names

    plotGraphs(clones_count_values, views_count_values, y_names, clones_csv_filename, 'count')
    plotGraphs(clones_uniques_values, views_uniques_values, y_names, clones_csv_filename, 'uniques')
