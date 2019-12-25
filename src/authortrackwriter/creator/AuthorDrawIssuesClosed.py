import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.CREATOR_ISSUES_CLOSED


def run():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_content = result_type.readGraphFile()

    graph_ds = []
    for idx in range(len(graph_content)):
        graph_item = {}
        graph_item['month'] = 2 * idx     # interval: 2 months
        graph_item.update(graph_content[idx])

        graph_ds.append(graph_item)

    grapher.writeGraphDataset(result_type.value, graph_ds)
