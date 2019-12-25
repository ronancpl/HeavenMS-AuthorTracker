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

result_path_name = AuthorGraphResultFile.ResultFile.SURVEY_QUESTION


def readSurveyQuestionEntry(survey_file_path):
    file = open(survey_file_path, 'r', encoding='UTF-8')

    survey_question_list = []

    survey_question = None
    survey_options = None

    state = 0

    for line in file:
        line = line.strip()

        if state == 0:
            if line.endswith('<td colspan="6" valign="middle" class="QuestionBackground">'):
                state = 1
                current_question = {'meta': {}, 'options': []}
                survey_question_list.append(current_question)

                survey_question = current_question['meta']
                survey_options = current_question['options']
        else:
            if line.startswith('<td><input id="SurveyPage_SurveyQuestions_ct'):
                en = line.rfind('</label>')
                st = line.rfind('</span>', None, en) + 7

                option = line[st:en]
                survey_options.append(option)
            elif line.endswith('</td>'):
                state = 0
            elif line.startswith('<span id="'):
                name_en = line.find('"', 10)
                qst_value_st = line.find('>', name_en) + 1
                qst_value_en = line.rfind('</span>')

                name_ct = line[10:name_en]
                name_st = name_ct.rfind('_')
                qst_name = name_ct[name_st+1:]
                qst_value = line[qst_value_st:qst_value_en]

                survey_question[qst_name] = qst_value
            elif line.startswith('<option value="'):
                st = line.find('>', 15) + 1
                en = line.rfind('</option>')

                option = line[st:en]
                survey_options.append(option)

    file.close()

    return survey_question_list


def fetchSurveyQuestions(survey_meta_path):
    survey_questions = []
    for file in os.listdir(survey_meta_path):
        survey_file_path = survey_meta_path + '/' + file

        file_questions = readSurveyQuestionEntry(survey_file_path)
        survey_questions.extend(file_questions)

    return survey_questions


def fetchSurveyQuestionList(survey_path):
    global scanner
    scanner = AuthorScanRepository.scanner

    survey_data = fetchSurveyQuestions(survey_path)
    graph_content = survey_data

    print()
    print('Survey questions')

    for survey_item in survey_data:
        print('Question #' + str(survey_item['meta']['LblQuestionNumber']) + '" : ' + str(survey_item['options']))

    print('Survey has ' + str(len(survey_data)) + ' questions')

    scanner.writeGraphFile(result_path_name, graph_content)


class AuthorSurveyQuestion:

    def fetchSurveyQuestionList(self):
        return fetchSurveyQuestionList('../../lib/survey/meta')


if __name__ == '__main__':
    fetchSurveyQuestionList('../../../lib/survey/meta')
