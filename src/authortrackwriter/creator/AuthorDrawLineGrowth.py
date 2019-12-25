import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
import errno
import os

from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.CREATOR_LINE_GROWTH


def run():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    file_types = ['all', 'java', 'js', 'xml', 'other']
    graph_content = result_type.readGraphFile()

    graph_ds = []
    for graph_ts_idx in range(len(graph_content)):
        graph_ts = graph_content[graph_ts_idx]

        graph_ds_ts = {'month': 3 * graph_ts_idx}
        graph_ds.append(graph_ds_ts)
        for i in range(5):  # all file types
            graph_ds_ts[file_types[i]] = {'line_added': 0, 'line_removed': 0, 'line_changed': 0}

        for graph_file_type_idx in range(len(graph_ts)):
            graph_item = graph_ts[graph_file_type_idx]
            graph_ds_item = graph_ds_ts[file_types[graph_file_type_idx]]

            line_add = graph_item[0]
            line_del = graph_item[1]
            line_chg = graph_item[2]

            graph_ds_item['line_added'] += line_add
            graph_ds_item['line_removed'] += line_del
            graph_ds_item['line_changed'] += line_chg

    grapher.writeGraphDataset(result_type.value, graph_ds)
