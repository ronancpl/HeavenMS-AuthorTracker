import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.SURVEY_QUESTION

def run():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    graph_content = result_type.readGraphFile()

    graph_dataset = []
    for survey_question in graph_content:
        graph_dataset.append(survey_question['options'])

    graph_ds = grapher.loadGraphDatasetFormat(['survey_answers'], [[graph_dataset]])
    grapher.writeGraphDataset(result_type.value, graph_ds)
