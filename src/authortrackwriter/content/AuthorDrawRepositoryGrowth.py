import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authorscanner import AuthorScanRepository

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.CONTENT_REPOSITORY_GROWTH


def generateEmptyGraphDataset():
    line_dataset = []

    for i in range(5):  # all github action types
        line_dataset.append([])

    return line_dataset


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_db = result_type.readGraphFile()

    graph_range = graph_db[4]   # comments, div 20 to fit radarplot
    for range_item_idx in range(len(graph_range)):
        graph_range[range_item_idx] = math.ceil(graph_range[range_item_idx] / 20.0)

    graph_dataset = []
    for graph_range_idx in range(len(graph_db)):
        graph_item = []
        graph_dataset.append(graph_item)

        graph_range = graph_db[graph_range_idx]
        for range_item_idx in range(len(graph_range)):
            range_item = graph_range[range_item_idx]
            graph_item.append(range_item)

    graph_content = grapher.loadGraphDatasetFormat(['fork', 'star', 'issue', 'pull', 'comment (x10)'], graph_dataset)
    grapher.writeGraphDataset(result_type.value, graph_content)
