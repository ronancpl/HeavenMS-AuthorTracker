import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from authorscanner import AuthorScanRepository
from authortrackprocessor import AuthorTrackRepository
from authortrackwriter import AuthorGraphResultFile
import AuthorScanJsonReader
import math
import os.path

result_path_name = AuthorGraphResultFile.ResultFile.SURVEY_TABLE

def fetchSurveyData():
    survey_items = []
    for survey_item in tracker.survey.items():
        survey_items.append(survey_item)

    return survey_items


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    global tracker
    tracker = AuthorTrackRepository.tracker

    survey_data = fetchSurveyData()
    graph_content = survey_data

    print()
    print('Survey table')

    for survey_name, survey_item in survey_data:
        print(str(survey_name) + ' as ' + str(survey_item['name']) + ', ' + str(survey_item['nationality']) + ' : ' + str(survey_item['answer_list']))
    print('Survey has ' + str(len(survey_data)) + ' entries')

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
