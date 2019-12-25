import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import AuthorScanJsonReader
from authorscanner import AuthorScanRepository
from authorscanner.words import AuthorWordManager
from authortrackwriter import AuthorGraphResultFile
import math
import os.path
import re


result_path_name = AuthorGraphResultFile.ResultFile.CONTENT_REPOSITORY_KEYWORD

lib_commit_path = "../../lib/commits/"


def getCommitKeywordList(commit_filename):
    commit_data = AuthorScanJsonReader.AuthorScanJsonReader().readFileRaw(lib_commit_path + commit_filename)[0]['content']
    keyword_list = []

    for commit_item in commit_data:
        word_list = wordManager.generateWordList(commit_item['commit']['message'])
        keyword_list.extend(word_list)

    return keyword_list


def sortRecurringKeywords():
    recurring_keywords = {}

    for file_name in os.listdir(lib_commit_path):
        wordManager.updateKeywordFrequency(recurring_keywords, getCommitKeywordList(file_name))

    return sorted(recurring_keywords.items(), key=lambda kv: kv[1], reverse=True)


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    global wordManager
    wordManager = AuthorWordManager.wordManager

    keywords_ts = sortRecurringKeywords()

    graph_content = keywords_ts

    print()
    print('Repo keywords')

    for ts_words in keywords_ts:
        ts_str = ''
        j = 0
        for ts_item in ts_words:
            ts_str += str(ts_item) + ', '
            j += 1

            if j == 20:
                break

        print(ts_str)

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
