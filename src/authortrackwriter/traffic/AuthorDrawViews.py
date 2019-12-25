import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.TRAFFIC_VIEWS


def run():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_content = result_type.readGraphFile()
    graph_content = grapher.loadGraphDatasetFormat(['count', 'uniques'], graph_content)

    grapher.writeGraphDataset(result_type.value, graph_content)
