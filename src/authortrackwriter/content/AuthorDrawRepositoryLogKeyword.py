import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authorscanner.words import AuthorWordManager
from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.CONTENT_REPOSITORY_LOG_KEYWORD


def run():
    global wordManager
    wordManager = AuthorWordManager.wordManager

    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_content = result_type.readGraphFile()

    graph_words = {}
    for graph_ts in graph_content:  # merge timesectioned words from write log
        wordManager.updateKeywordFrequency(graph_words, dict(graph_ts))

    graph_content = grapher.loadGraphDatasetFormat(['word', 'count'], graph_words.items())

    grapher.writeGraphDataset(result_type.value, graph_content)
