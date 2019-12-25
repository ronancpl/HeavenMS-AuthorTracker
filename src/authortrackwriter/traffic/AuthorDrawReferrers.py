import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.TRAFFIC_REFERRERS


def generateEmptyGraphStructure(graph_content):
    graph_ds = []
    for i in range(len(graph_content[0]['content'])):
        graph_ds.append([])

    return graph_ds


def run():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_content = result_type.readGraphFile()

    if len(graph_content) > 0:
        graph_overall_ds = []
        graph_ds = generateEmptyGraphStructure(graph_content)

        for graph_word_ct in graph_content:
            word = graph_word_ct['name']
            overall_uniques = graph_word_ct['uniques']

            graph_overall_ds.append([word, overall_uniques])

            graph_word_item = graph_word_ct['content']
            for graph_word_idx in range(len(graph_word_item)):
                graph_word_ts = graph_word_item[graph_word_idx]
                graph_ds[graph_word_idx].append([word, graph_word_ts[0], graph_word_ts[1]])

        for idx in range(len(graph_ds)):
            graph_ds = sorted(graph_ds, key=lambda k: k[2], reverse=True)  # order each timesection graph by 'uniques'

            graph_item_ct = grapher.loadGraphDatasetFormat(['name', 'count', 'uniques'], graph_ds[idx])
            grapher.writeGraphDataset(result_type.value, graph_item_ct, idx)
