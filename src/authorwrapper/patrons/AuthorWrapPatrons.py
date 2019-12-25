import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import squarify
import seaborn as sns
import errno
import os

from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.PATRONS_SCORE


def plotfy(names, scores, csv_filename, doc_index):
    plot_img = grapher.fetchGraphFilename(csv_filename, doc_index)

    sq_names = []
    sq_scores = []
    for idx in range(len(names)):
        if scores[idx] > 0:
            sq_scores.append(scores[idx])
            sq_names.append(names[idx])

    fig = plt.figure(dpi=1000, figsize=(6.40,7.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    squarify.plot(sizes=sq_scores, label=sq_names, alpha=0.777)
    plt.axis('off')

    grapher.savePlot(fig, plot_img)
    # plt.show()
    plt.close(fig)


def plotPatrons(name_values, score_values, csv_filename):
    st = 0
    en = len(score_values)
    limit = 15

    acc_scores_reverse = []
    acc = 0.0
    for i in reversed(range(en)):
        acc += score_values[i]
        acc_scores_reverse.append(acc)

    graph_idx = 0
    while st < en:
        graph_names = []
        graph_scores = []
        acc = 0.0

        next = min(st + limit, en)
        for i in range(st, next):
            graph_names.append(name_values[i])
            graph_scores.append(score_values[i])
            acc += score_values[i]

        i = next
        while i < en and (i - st) < 20 and (acc / (acc + acc_scores_reverse[i])) < 0.34:
            graph_names.append(name_values[i])
            graph_scores.append(score_values[i])
            acc += score_values[i]
            i += 1

        if i < en:
            graph_names.append('patrons_' + str(i))
            graph_scores.append(acc_scores_reverse[i])

        plotfy(graph_names, graph_scores, csv_filename, graph_idx)
        graph_idx += 1

        st = i


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    csv_filename = result_type.value

    column_names, graph_content = grapher.readGraphDataset(csv_filename)

    print('Patron scores')
    name_values = []
    score_values = []
    for graph_item in graph_content:
        name_values.append(graph_item[33])      # name
        score_values.append(graph_item[35])      # score
        print('  |' + str(graph_item[33]) + '| ' + str(graph_item[35]))

    plotPatrons(name_values, score_values, csv_filename)
