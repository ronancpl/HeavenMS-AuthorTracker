import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import nltk
import seaborn as sns
import errno
import os

from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

import base64
import datetime
import requests
import time
from datetime import datetime
from datetime import timedelta
from authorfinder import AuthorFetchPatrons

stopwords = set(nltk.corpus.stopwords.words())
wordcloud_path = '../../wordcloud'


def loadAuthToken():
    file = open("C:/Nexon/auth.txt", 'r')
    tokens = file.read().splitlines()
    return tokens


file_url = 'https://api.github.com/repos/ronancpl/HeavenMS/git/blobs/918a2d06d12340e8eb2ef1fd30a3606016de5698'
auth = loadAuthToken()


def decodeGitBlobContent(content):
    return str(base64.b64decode(content), encoding='UTF-8', errors='replace')


def getGitBlobContent(data):
    try:
        if data['encoding'] == 'base64':
            return decodeGitBlobContent(data['content'])
        else:
            print('Encoding ' + data['encoding'] + ' not supported')
            return ''
    except KeyError:
        print(data)
        raise


def fetchFileBlobContent(file_blob):
    file_content = getGitBlobContent(file_blob)
    return file_content


def getRequestCall(nextLink, apiParams):
    global auth

    while True:
        try:
            reqGet = requests.get(nextLink, headers=apiParams, auth=(auth[1], auth[0]))

            if 'X-RateLimit-Remaining' in reqGet.headers and int(reqGet.headers['X-RateLimit-Remaining']) < 1:
                print('RateLimit exceeded for this hour...')

                time.sleep(max(20,float(reqGet.headers['X-RateLimit-Reset']) - float(datetime.utcnow().timestamp())))
                continue

            return reqGet
        except requests.exceptions.ConnectionError or ConnectionRefusedError:
            print('Connection lost. Retrying...')
            time.sleep(20)


def getRequest(nextLink, apiParams):
    global reqGet

    reqGet = getRequestCall(nextLink, apiParams)
    return reqGet


def run():
    apiParams = {'per_page': '100'}
    file_blob = getRequest(file_url, apiParams).json()

    if file_blob is not None:
        file_content = fetchFileBlobContent(file_blob)
        print(file_content)
        print('----------------')

        file_patrons = AuthorFetchPatrons.AuthorFetchPatrons().authorFetchFileContentPatrons(file_content)

        for patron_names, patron_type in file_patrons:
            print(patron_names[0] + str(patron_type))


def plotfy():
    fig = plt.figure(dpi=1000, figsize=(10.00, 10.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    m = mpimg.imread(wordcloud_path + '/assets/weather-cloud-flat.png')
    # mask = m,
    wordcloud = WordCloud(font_path=wordcloud_path + '/fonts/Bitstream-Cyberbit_7170.ttf', width=1000, height=1000,
                          background_color='white', stopwords=stopwords,
                          min_font_size=10).generate('頼案 aaa sc asw er 頼案 頼案 頼案 頼案')
    plt.imshow(wordcloud)

    plt.show()
    plt.close(fig)


def calcWordValue(overall_word_count, len_word_patrons, count_word_patron):
    word_tf = count_word_patron

    word_patrons_count = len_word_patrons
    word_presence_count = overall_word_count
    word_idf = max(word_patrons_count * math.log(word_presence_count, 7.77), 0.777)

    return word_tf / word_idf


import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import seaborn as sns
import errno
import nltk
import os

from authorscanner import AuthorScanRepository
from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.PATRONS_WORD

stopwords = set(nltk.corpus.stopwords.words())


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def plotfy2(patron_words, csv_filename, doc_index=-1):
    # plot_img = grapher.fetchGraphFilename(csv_filename, doc_index)

    fig = plt.figure(dpi=1000, figsize=(10.00,10.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    m = mpimg.imread(scanner.wordcloud_path + '/assets/weather-cloud-flat.png')
    # mask = m,
    wordcloud = WordCloud(font_path=scanner.wordcloud_path + '/fonts/Bitstream-Cyberbit_7170.ttf', width=1000, height=1000,
                          background_color='white', stopwords=stopwords, min_font_size=10).generate_from_frequencies(frequencies=patron_words)
    plt.imshow(wordcloud)

    # grapher.savePlot(fig, plot_img)
    plt.show()
    # plt.close(fig)


def plotPatronWords(csv_filename, word_content, weight_idx):
    patron_words = {}
    for word_item in word_content:
        word = str(word_item[0])
        weight = word_item[weight_idx]

        patron_words[word] = weight

    plotfy2(patron_words, csv_filename)


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    csv_filename = result_type.value
    column_names, graph_content = grapher.readGraphDataset(csv_filename)

    setupDir(grapher.fetchGraphFilename(csv_filename[0:csv_filename.rfind('/')] + '/a.txt', -1))
    plotPatronWords(csv_filename, graph_content, 1)


def printTimesections():
    start_time = datetime(2015, 7, 12)
    finish_time = datetime(2019, 12, 31)
    days_interval = 20

    total_days = (finish_time - start_time).days

    time_set = start_time

    for i in range(0, math.ceil(total_days / days_interval)):
        print(str(i) + ': ' + str(time_set))
        time_set = time_set + timedelta(days=20)


import math
if __name__ == '__main__':
    # print(stopwords)
    # plot()
    printTimesections()