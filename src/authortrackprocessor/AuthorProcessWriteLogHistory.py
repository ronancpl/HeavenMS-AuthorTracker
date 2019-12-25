import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import AuthorScanJsonReader
from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager
from authorscanner.words import AuthorWordManager
from authortrackwriter import AuthorGraphResultFile
import math
import os.path
import re
from unicodedata import normalize


repository_path = "../../../../../HeavenMS"

ptbr_months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
ptbr_months = dict(zip(ptbr_months, range(len(ptbr_months))))


def updateWordCount(recurring_keywords, keywords):
    for keyword_item, keyword_count in keywords.items():
        if keyword_item not in recurring_keywords:
            recurring_keywords[keyword_item] = keyword_count
        else:
            recurring_keywords[keyword_item] += keyword_count


def getMonthIndex(log_month):
    log_month = log_month.lower()

    if log_month in ptbr_months:
        return ptbr_months[log_month]
    else:
        print('Error parsing Month "' + log_month + '"')
        return -1


def processKeywordText(recurring_keywords, text):
    keyword_list = wordManager.generateWordList(text)
    wordManager.updateKeywordFrequency(recurring_keywords, keyword_list)


def fetchTimeSectionWriteLogContents(write_log_metadata):
    write_log_contents = {}

    print('Fetch log entries')
    for patron_name, patron_metadata in write_log_metadata.items():
        print('  ' + patron_name + ' ' + str(len(patron_metadata)))
        patron_timely_metadata = []
        write_log_contents[patron_name] = patron_timely_metadata

        patron_log_db = scanner.generateTimeSectionDatabase(patron_metadata, ['created_at'], days=20)
        for patron_log_db_range in patron_log_db:
            keywords_count = {}
            for patron_log_db_item in patron_log_db_range:
                updateWordCount(keywords_count, patron_log_db_item['content'])

            patron_timely_item = {}
            patron_timely_item['word_table'] = keywords_count

            patron_timely_metadata.append(patron_timely_item)

    return write_log_contents


def loadWriteLogKeywords(write_log_entries, patron_name, log_filepath):
    log_timestamp_p = re.compile('^(([\d]+)([\s]*[-]+[\s]*([\d]+))?)[\s]+([\w]+)[\s]+([\d]{4}),.*')
    log_keywords = []

    keywords_count = {}
    with open(log_filepath, encoding='UTF-8') as log_data:
        for line in log_data:
            timelog = log_timestamp_p.match(line)
            if timelog is None:
                processKeywordText(keywords_count, line)
            else:
                keywords_count = {}

                start_date = timelog.group(2)
                end_date = timelog.group(4)
                if end_date is None:
                    end_date = start_date

                month_date = str(getMonthIndex(timelog.group(5)) + 1).zfill(2)
                year_date = timelog.group(6)

                current_timestamp = year_date + '-' + month_date + '-' + start_date + 'T0000'
                end_timestamp = year_date + '-' + month_date + '-' + end_date + 'T0000'

                log_keywords.append({'content': keywords_count, 'created_at': current_timestamp, 'ended_at': end_timestamp})

    for patron in patronManager.getPatron(patron_name):
        write_log_entries[patron.name] = log_keywords


def loadWriteLogContents():
    write_log_entries = {}
    loadWriteLogKeywords(write_log_entries, 'ronancpl', scanner.repository_path + '/docs/mychanges_ptbr.txt')

    return write_log_entries


def fetchWriteLogEntries():
    global scanner
    scanner = AuthorScanRepository.scanner

    global patronManager
    patronManager = AuthorPatronManager.patronManager

    global wordManager
    wordManager = AuthorWordManager.wordManager

    write_log_entries = loadWriteLogContents()
    return write_log_entries


def fetchWriteLogContents():
    write_log_entries = fetchWriteLogEntries()
    write_log_contents_db = fetchTimeSectionWriteLogContents(write_log_entries)

    return write_log_contents_db


def run():
    fetchWriteLogContents()


if __name__ == '__main__':
    run()
