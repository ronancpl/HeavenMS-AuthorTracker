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

question_result_type = AuthorGraphResultFile.ResultFile.SURVEY_QUESTION
result_type = AuthorGraphResultFile.ResultFile.SURVEY_TABLE

pie_labels = ['Answer', 'Count']
pie_colors = ['cornflowerblue', 'lightcoral', 'springgreen', 'lightgray', 'peru']
pie_explode = (0.1, 0, 0, 0, 0)  # explode 1st slice


def processSurveyAnswer(answer_count, answer):
    if answer == '-':   # left unanswered
        return

    answer_count[answer] += 1


def createAnswerCountDict(idx, answer_list):
    ret = {}

    for ans in answer_list[idx]:
        ret[ans] = 0

    return ret


def processGraphResults(survey_contents, answer_list):
    survey_question_results = []

    for idx in range(1, 7):
        answer_count = createAnswerCountDict(idx, answer_list)
        survey_question_results.append(answer_count)

        for survey_item in survey_contents:
            processSurveyAnswer(answer_count, survey_item[idx])

    return survey_question_results


def compileFixedColors(dicti_items, dicti_colors):
    print(dicti_items)
    c = 0
    for item in dicti_items:
        for i in range(len(dicti_items)):
            if item[0] == dicti_items[i][0]:
                dicti_colors[c] = pie_colors[i]
                break
        c += 1


def getDictiDfEntries(dicti, dicti_crop_size):
    dicti_items = list(dicti.items())
    dicti_items.sort(key=lambda kv: kv[1], reverse=True)

    dictidf_items = []
    i = 0

    print(str(dicti_crop_size) + ' ' + str(len(dicti_items)))
    crop_size = min(dicti_crop_size, len(dicti_items))
    while i < crop_size:
        dictidf_items.append(dicti_items[i])
        i += 1

    if i < len(dicti_items):
        other_count = 0
        for i in range(i, len(dicti_items)):
            other_count += dicti_items[i][1]

        dictidf_items.append(('Other', other_count))

    explode_list = []
    colors_list = []
    for i in range(len(dictidf_items)):
        j = i % len(pie_explode) | 0
        explode_list.append(pie_explode[j])

        k = i % len(pie_colors) | 0
        colors_list.append(pie_colors[k])

    compileFixedColors(dictidf_items, colors_list)

    return dictidf_items


def getCropAnswerResults(answer_results):
    ret = len(answer_results)   # past limit entries for the pie chart, set to get highest 4 and merge the rest
    if ret > len(pie_colors):
        ret = len(pie_colors) - 1

    return ret


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct


def fetchPieLabels(label_list):
    ret = []
    for label_item in label_list:
        if len(label_item) > 52:
            label_item = label_item[0:52] + '...'

        ret.append(label_item)

    return ret


def plotfy(answer_results, csv_filename, doc_index):
    plot_img = grapher.fetchGraphFilename(csv_filename, doc_index)

    fig = plt.figure(dpi=1000, figsize=(6.40, 7.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    pd_df = pd.DataFrame(getDictiDfEntries(answer_results, getCropAnswerResults(answer_results)))
    normalizeSurveyAnswers(pie_labels[0])
    pd_df.columns = (pie_labels[0], pie_labels[1])

    # Plot
    plt.pie(pd_df[pie_labels[1]], explode=pie_explode, colors=pie_colors, autopct=make_autopct(pd_df[pie_labels[1]]), shadow=False, startangle=140)
    plt.legend(loc='best', labels=fetchPieLabels(pd_df[pie_labels[0]]))

    plt.axis('equal')
    plt.tight_layout()

    grapher.savePlot(fig, plot_img)
    # plt.show()
    plt.close(fig)


def plotResults(csv_filename, survey_results):
    for idx in range(len(survey_results)):
        plotfy(survey_results[idx], csv_filename, idx)


def shouldNormalizeSurveyAnswers(answers_question):
    for idx in range(len(answers_question)):
        ans = answers_question[idx]
        if len(ans) > 40:
            return True

    return False


def normalizeSurveyAnswers(answers_list):
    if shouldNormalizeSurveyAnswers(answers_list):
        for idx in range(len(answers_list)):
            ans = 'Answer #' + str(idx + 1)
            answers_list[idx] = ans


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    csv_filename = question_result_type.value
    survey_column_names, survey_questions = grapher.readGraphDataset(csv_filename)

    print('Fetch survey answer')
    survey_answers = survey_questions[0][0]
    print(survey_answers)

    csv_filename = result_type.value
    lines_column_names, lines_graph_content = grapher.readGraphDataset(csv_filename)

    survey_results = processGraphResults(lines_graph_content, survey_answers)
    plotResults(csv_filename, survey_results)
