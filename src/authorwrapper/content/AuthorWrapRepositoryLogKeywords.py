import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import nltk
import pandas as pd
from wordcloud import WordCloud
import seaborn as sns
import errno
import os

from authorscanner import AuthorScanRepository
from authorscanner.words import AuthorWordManager
from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

result_type = AuthorGraphResultFile.ResultFile.CONTENT_REPOSITORY_LOG_KEYWORD
stopwords = set(nltk.corpus.stopwords.words())


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def plotfy(repo_words, csv_filename, doc_index=-1):
    plot_img = grapher.fetchGraphFilename(csv_filename, doc_index)
    setupDir(plot_img)

    wordManager = AuthorWordManager.wordManager

    fig = plt.figure(dpi=1000, figsize=(10.00, 10.00))
    plt.xticks(rotation=90, fontsize=4, fontweight=25)

    m = mpimg.imread(scanner.wordcloud_path + '/assets/weather-cloud-flat.png')
    # mask = m,
    wordcloud = WordCloud(font_path=scanner.wordcloud_path + '/fonts/Bitstream-Cyberbit_7170.ttf', width=1000, height=1000,
                          background_color='white', stopwords=stopwords, min_font_size=10).generate_from_frequencies(frequencies=wordManager.stripStopwords(repo_words))
    plt.imshow(wordcloud)

    grapher.savePlot(fig, plot_img)
    # plt.show()
    plt.close(fig)


def plotRepositoryWords(csv_filename, word_content, weight_idx):
    repo_words = {}
    for word_item in word_content:
        word = str(word_item[0])
        weight = word_item[weight_idx]

        repo_words[word] = weight

    plotfy(repo_words, csv_filename)


def plot():
    global grapher
    grapher = AuthorGraphResultPrinter.grapher

    global scanner
    scanner = AuthorScanRepository.scanner

    csv_filename = result_type.value
    column_names, graph_content = grapher.readGraphDataset(csv_filename)

    plotRepositoryWords(csv_filename, graph_content, 1)
