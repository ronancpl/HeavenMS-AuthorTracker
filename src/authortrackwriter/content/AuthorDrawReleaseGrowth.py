import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authorscanner import AuthorScanRepository

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.CONTENT_RELEASE_GROWTH


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_db = result_type.readGraphFile()

    for graph_range in graph_db:    # comments, div 20 to fit radarplot
        graph_range[4] = math.ceil(graph_range[4] / 20.0)

    graph_dataset = []
    for graph_range_idx in range(len(graph_db)):
        graph_item = []
        graph_dataset.append(graph_item)

        graph_range = graph_db[graph_range_idx]
        for range_item_idx in range(len(graph_range)):
            range_item = graph_range[range_item_idx]
            graph_item.append(range_item)

    graph_content = grapher.loadGraphDatasetFormat(['fork', 'star', 'issue', 'pull', 'comment (x 10)'], graph_dataset)
    grapher.writeGraphDataset(result_type.value, graph_content)