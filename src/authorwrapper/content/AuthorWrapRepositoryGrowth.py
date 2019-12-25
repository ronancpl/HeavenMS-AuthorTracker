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
from authorwrapper import AuthorGraphRadarplot

result_type = AuthorGraphResultFile.ResultFile.CONTENT_REPOSITORY_GROWTH


def plotfy(data, csv_filename):
    AuthorGraphRadarplot.plot(data, csv_filename)


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    csv_filename = result_type.value

    column_names, graph_content = grapher.readGraphDataset(csv_filename)

    data = {}

    data['group'] = []
    for graph_item_idx in range(len(graph_content)):
        data['group'].append(graph_item_idx)

    for name in column_names:
        data[name] = []

    for graph_item_idx in range(len(graph_content)):
        graph_item = graph_content[graph_item_idx]

        for i in range(len(column_names)):
            name = column_names[i]
            data[name].append(graph_item[i])

    plotfy(data, csv_filename)
