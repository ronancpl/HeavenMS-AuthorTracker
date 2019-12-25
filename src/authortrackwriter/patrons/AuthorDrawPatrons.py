import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.PATRONS_SCORE


def run():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_content = result_type.readGraphFile()

    graph_ds = []
    for graph_patron in graph_content:
        graph_ds.append(graph_patron.exportScore())

    grapher.writeGraphDataset(result_type.value, graph_ds)
