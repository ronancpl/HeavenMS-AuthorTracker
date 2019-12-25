import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import AuthorScanJsonReader
from authorconstants import AuthorConstantLimit
from authorscanner import AuthorScanRepository
from authortrackprocessor import AuthorProcessWriteLogHistory
from authortrackwriter import AuthorGraphResultFile
import math
import os.path
import re
from googletrans import Translator
from unicodedata import normalize


result_path_name = AuthorGraphResultFile.ResultFile.CONTENT_REPOSITORY_LOG_KEYWORD


def scanRecurringKeywords():
    kw_res = {}

    for patron_name, patron_logs in AuthorProcessWriteLogHistory.fetchWriteLogEntries().items():
        kw_patron = []
        kw_res[patron_name] = kw_patron

        kw_db = scanner.generateTimeSectionDatabase(patron_logs, ['created_at'], months=2, days=0)

        for kw_ts in kw_db:
            kw_step = {}

            for kw_item in kw_ts:
                for kw_word, kw_count in kw_item['content'].items():
                    if kw_word not in kw_step:
                        kw_step[kw_word] = kw_count
                    else:
                        kw_step[kw_word] += kw_count

            kw_patron.append(sorted(kw_step.items(), key=lambda kv: kv[1], reverse=True))

    return kw_res


def getKeywordFromTranslation(translator, keyword):
    tl_word = translator.translate(keyword, dest='en', src='pt').text.lower()
    if tl_word.startswith('{'):
        r_word = keyword
    else:
        tl_list = tl_word.split()
        if len(tl_list) > 1:
            i = 0
            r_word = ''

            for w in tl_list:
                if len(w) > i:
                    i = len(w)
                    r_word = w
        else:
            r_word = tl_list[0]

    if r_word.endswith('.') or r_word.endswith(':'):
        r_word = r_word[:-1]

    print(str(keyword) + ' -> ' + str(r_word) + ' | ' + str(tl_word))
    return r_word


def sortKeywordCount(word_content, weight_idx):
    return sorted(word_content, key=lambda kv: kv[weight_idx], reverse=True)


def translateKeywords(keyword_ts):
    if not AuthorConstantLimit.WrapLimit.LOG_TRANSLATE.getValue():
        return keyword_ts

    translator = Translator()

    ret = []
    tl_keywords = {}

    for ts_words in keyword_ts:
        ts_ret = []
        ret.append(ts_ret)

        for keyword, count in ts_words:
            if keyword not in tl_keywords:
                tl_keyword = getKeywordFromTranslation(translator, keyword)
                tl_keywords[keyword] = tl_keyword
            else:
                tl_keyword = tl_keywords[keyword]

            ts_ret.append((tl_keyword, count))

    return ret


def run():
    global scanner
    scanner = AuthorScanRepository.scanner

    keyword_ts = None
    for patron_name, patron_kw in scanRecurringKeywords().items():
        keyword_ts = translateKeywords(patron_kw)  # SHORTCUT -
        break

    graph_content = keyword_ts

    print()
    print('Log keywords')

    for ts_words in keyword_ts:
        ts_str = ''
        j = 0
        for ts_item in ts_words:
            ts_str += str(ts_item) + ', '
            j += 1

            if j == 20:
                break

        if ts_str != '':
            print(ts_str)

    scanner.writeGraphFile(result_path_name, graph_content)


if __name__ == '__main__':
    run()
