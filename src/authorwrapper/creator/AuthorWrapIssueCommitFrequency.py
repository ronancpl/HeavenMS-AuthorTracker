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

issues_type = AuthorGraphResultFile.ResultFile.CREATOR_ISSUES_CLOSED
commit_type = AuthorGraphResultFile.ResultFile.CREATOR_COMMIT_FREQUENCY
graph_activity_type = AuthorGraphResultFile.ResultFile.CREATOR_COMMIT_GRAPH_ACTIVITY
graph_avg_time_type = AuthorGraphResultFile.ResultFile.CREATOR_COMMIT_GRAPH_AVG_TIME


def plotfy(x, y1, y2, y3, y4, y_names, activity_csv_filename, avg_time_csv_filename):
    plot_img = grapher.fetchGraphFilename(avg_time_csv_filename)

    fig = plt.figure(dpi=1000, figsize=(6.40,7.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    ax = sns.barplot(x=x, y=y1)
    ax.set_ylabel(y_names[4])

    grapher.savePlot(fig, plot_img)
    # plt.show()
    plt.close(fig)

    # -------------------

    plot_img = grapher.fetchGraphFilename(activity_csv_filename)

    fig = plt.figure(dpi=1000, figsize=(6.40, 7.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    data = {"months (4)": x, "issues_closed_by_creator": y2, "issues_closed": y3, "commits": y4}
    df = pd.DataFrame(data=data)

    ax2 = sns.lineplot(x='months (4)', y='value', hue='variable', data=pd.melt(df, ['months (4)']))
    ax2.set_ylabel(y_names[5])

    grapher.savePlot(fig, plot_img)
    # plt.show()
    plt.close(fig)


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    issues_column_names, issues_graph_content = grapher.readGraphDataset(issues_type.value)
    issues_csv_filename = issues_type.value

    issues_closed_by_creator_values = []
    issues_count_values = []
    average_open_time_values = []
    for issues_graph_item in issues_graph_content:
        issues_closed_by_creator_values.append(issues_graph_item[1])
        issues_count_values.append(issues_graph_item[2])
        average_open_time_values.append(issues_graph_item[3])

    commits_column_names, commits_graph_content = grapher.readGraphDataset(commit_type.value)
    commits_csv_filename = commit_type.value

    commits_count_values = []
    for count_uniques_ts in commits_graph_content:
        commits_count_values.append(count_uniques_ts[1])

    y_names = [issues_column_names[2], issues_column_names[0], issues_column_names[1], 'commit_' + commits_column_names[0], issues_column_names[3], 'count']
    # print(average_open_time_values)
    plotfy(list(range(len(average_open_time_values))), average_open_time_values, issues_closed_by_creator_values, issues_count_values, commits_count_values, y_names, graph_activity_type.value, graph_avg_time_type.value)
