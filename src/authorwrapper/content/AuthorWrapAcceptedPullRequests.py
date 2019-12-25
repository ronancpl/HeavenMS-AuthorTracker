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

result_type = AuthorGraphResultFile.ResultFile.CONTENT_ACCEPTED_PULL_REQUESTS


def plotfy(x, y1, y2, y_names, csv_filename):
    plot_img = grapher.fetchGraphFilename(csv_filename)
    fig = plt.figure(dpi=1000, figsize=(6.40,7.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    data = {"months (3)": x, y_names[0]: y1, y_names[1]: y2}
    df = pd.DataFrame(data=data)

    ax = sns.barplot(x='months (3)', y='value', hue='variable', data=pd.melt(df, ['months (3)']), dodge=True)
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

    column_names, graph_content = grapher.readGraphDataset(csv_filename)

    merged_values = []
    closed_values = []

    for graph_item in graph_content:
        merged_values.append(graph_item[0])     # merged
        closed_values.append(graph_item[1])     # closed

    plotfy(list(range(len(merged_values))), merged_values, closed_values, column_names, csv_filename)
