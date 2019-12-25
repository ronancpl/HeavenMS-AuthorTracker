import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authorscanner import AuthorScanRepository

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.CONTENT_ACCEPTED_PULL_REQUESTS


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    accepted_pr_db = result_type.readGraphFile()

    graph_dataset = []
    for pr_merged, pr_closed in accepted_pr_db:
        graph_dataset.append([pr_merged, pr_closed])

    graph_item_ct = grapher.loadGraphDatasetFormat(['accepted', 'closed'], graph_dataset)

    grapher.writeGraphDataset(result_type.value, graph_item_ct)

