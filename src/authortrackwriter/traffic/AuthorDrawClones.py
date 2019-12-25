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

result_type = AuthorGraphResultFile.ResultFile.TRAFFIC_CLONES


def run():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_content = result_type.readGraphFile()
    graph_content = grapher.loadGraphDatasetFormat(['count', 'uniques'], graph_content)

    grapher.writeGraphDataset(result_type.value, graph_content)
