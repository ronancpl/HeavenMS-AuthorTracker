import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.CONTENT_SEARCHED_PATHS


def run():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_content = result_type.readGraphFile()

    for graph_content_idx in range(len(graph_content)):
        graph_item_ct = graph_content[graph_content_idx]

        graph_item_ct = grapher.loadGraphDatasetFormat(['path', 'count'], graph_item_ct)

        grapher.writeGraphDataset(result_type.value, graph_item_ct, graph_content_idx)
