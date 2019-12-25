import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os
import re
import pathvalidate
from pathvalidate.error import NullNameError

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.PATRONS_WORD
unit_result_type = AuthorGraphResultFile.ResultFile.PATRONS_WORD_UNIT


def patronFileName(file_path, patron_name):
    idx = file_path.rfind('/') + 1

    try:
        patron_fname = pathvalidate.sanitize_filename(patron_name)
    except NullNameError:
        print('>' + str(patron_name) + ' ' + str(type(patron_name)))    # SHORTCUT -
        patron_fname = 'err' + str(hash(patron_name))

    return file_path[0:idx] + patron_fname + '_' + file_path[idx:]


def runPatronsWords(graph_content):
    for patron_name, patron_wordrank in graph_content:
        graph_ds = grapher.loadGraphDatasetFormat(['word', 'weight', 'count'], patron_wordrank)
        grapher.writeGraphDataset(patronFileName(unit_result_type.value, patron_name), graph_ds)


def run():
    global scanner
    scanner = AuthorGraphResultPrinter.grapher

    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_content = result_type.readGraphFile()
    graph_ds = grapher.loadGraphDatasetFormat(['word', 'count'], graph_content)
    grapher.writeGraphDataset(result_type.value, graph_ds)

    graph_content = unit_result_type.readGraphFile()
    runPatronsWords(graph_content)
