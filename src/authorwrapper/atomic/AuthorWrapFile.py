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

result_type = AuthorGraphResultFile.ResultFile.ATOMIC_FILE


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    csv_filename = result_type.value

    column_names, graph_content = grapher.readGraphDataset(csv_filename)
    grapher.replicateGraphDataset(csv_filename, column_names, graph_content)
