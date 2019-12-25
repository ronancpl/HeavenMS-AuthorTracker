from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager
from authorscanner.words import AuthorWordManager
from authortrackprocessor import AuthorTrackRepository
from authortrackwriter import AuthorGraphResultFile
from authortrackwriter import AuthorGraphResultPrinter

import math
import sys

# exit values
EXIT_OK = 0
EXIT_FAIL = 7

result_path_name = AuthorGraphResultFile.ResultFile.PATRONS_WORD
result_unit_path_name = AuthorGraphResultFile.ResultFile.PATRONS_WORD_UNIT


def updateWordCount(recurring_keywords, keywords):
    for keyword_item, keyword_count in keywords.items():
        if keyword_item not in recurring_keywords:
            recurring_keywords[keyword_item] = keyword_count
        else:
            recurring_keywords[keyword_item] += keyword_count


def fetchPatronWordsFromChannels(patron_name, ts_idx):
    wordlist_patron_ts = {}

    try:
        updateWordCount(wordlist_patron_ts, tracker.github[patron_name]['word_table'][ts_idx])
        updateWordCount(wordlist_patron_ts, tracker.social[patron_name][ts_idx]['word_table'])
        updateWordCount(wordlist_patron_ts, tracker.write_log[patron_name][ts_idx]['word_table'])
    except KeyError:
        pass    # ignore missing entries, no activities there

    return wordlist_patron_ts


def fetchPatronsWords(patrons_list):
    print('Fetching vocabulary...')

    overall_words = {}
    patrons_words = {}
    for patron in patrons_list:
        wordlist_patron = {}
        patrons_words[patron.name] = wordlist_patron

        for ts_idx in range(scanner.tracker_timesection_len):
            wordlist_patron_ts = fetchPatronWordsFromChannels(patron.name, ts_idx)
            updateWordCount(wordlist_patron, wordlist_patron_ts)

        updateWordCount(overall_words, wordlist_patron)

    return overall_words, patrons_words


def fetchInversePatronsWords(patrons_words):
    words_patrons = {}

    for patron_name, patron_words in patrons_words.items():
        for word in patron_words.keys():
            if word in words_patrons:
                patron_set = words_patrons[word]
            else:
                patron_set = set()
                words_patrons[word] = patron_set

            patron_set.add(patron_name)

    return words_patrons


def calcWordValue(word, overall_words, patron_words, words_patrons):
    if word not in patron_words:
        return 0.0

    word_tf = math.log(patron_words[word] + 1, 1.777)

    word_patrons_count = len(words_patrons[word])
    word_presence_count = overall_words[word]
    word_idf = word_patrons_count * math.log(word_presence_count, 7.77)

    if word_idf < 0.777:
        if patron_words[word] >= 3:    # normalize rate of expected words
            word_idf = 0.777
        elif word_idf < 0.1:
            word_idf = 0.1

    return word_tf / word_idf


def processPatronWordRank(patron_name, overall_words, patron_words, words_patrons):
    words = []
    for word, count in patron_words.items():
        word_v = calcWordValue(word, overall_words, patron_words, words_patrons)
        words.append((word, word_v, count))

    print('Wording ' + patron_name)
    word_contents = sorted(words, key=lambda k: k[1], reverse=True)
    return word_contents


def processPatronsWordRank(overall_words, patrons_words, words_patrons):
    patrons_wordranks = []

    for patron_name, patron_words in patrons_words.items():
        patron_wordrank = (patron_name, processPatronWordRank(patron_name, overall_words, patron_words, words_patrons))
        patrons_wordranks.append(patron_wordrank)

    scanner.writeGraphFile(result_unit_path_name, patrons_wordranks)


def stemVocabulary(vocabulary_words):
    stem_words = {}
    word_stem = {}
    for word, count in vocabulary_words.items():
        word_radical = wordManager.findWordStem(word)
        if word_radical is None:    # word not found
            continue

        word_stem[word] = word_radical
        if word_radical not in stem_words or stem_words[word_radical][1] < count:
            stem_words[word_radical] = (word, count)

    return stem_words, word_stem


def stemPatronVocabulary(word_stem, stem_words, patron_words):
    patron_stems = {}
    for word, count in patron_words.items():
        if word not in word_stem:
            continue

        common_word = stem_words[word_stem[word]][0]
        if common_word not in patron_stems:
            patron_stems[common_word] = count
        else:
            patron_stems[common_word] += count

    return patron_stems


def stemPatronsWords(overall_words, patrons_words):
    print('Stemming vocabulary...')

    stem_patrons_words = {}
    stem_words, word_stem = stemVocabulary(overall_words)
    for patron_name, patron_words in patrons_words.items():
        patron_stems = stemPatronVocabulary(word_stem, stem_words, patron_words)
        stem_patrons_words[patron_name] = patron_stems

    stem_overall_words = stemPatronVocabulary(word_stem, stem_words, overall_words)
    return stem_overall_words, stem_patrons_words


def fetchPatronsWordlist(patrons_list):
    overall_words, patrons_words = fetchPatronsWords(patrons_list)
    overall_words, patrons_words = stemPatronsWords(overall_words, patrons_words)

    words_patrons = fetchInversePatronsWords(patrons_words)
    processPatronsWordRank(overall_words, patrons_words, words_patrons)

    return overall_words


class AuthorWordifyRepository:

    def wordifyRepository(self):
        print('Wording patrons...')

        global grapher
        grapher = AuthorGraphResultPrinter.grapher

        global patronManager
        patronManager = AuthorPatronManager.patronManager

        global scanner
        scanner = AuthorScanRepository.scanner

        global tracker
        tracker = AuthorTrackRepository.tracker

        global wordManager
        wordManager = AuthorWordManager.wordManager

        patrons_list = patronManager.exportPatronsList()
        word_list = fetchPatronsWordlist(patrons_list)

        word_frequency = sorted(list(word_list.items()), key=lambda k: k[1], reverse=True)  # top-down score ordering

        print()
        print('count words')
        i = 0
        for word, count in word_frequency:
            print('  ' + word + ' : ' + str(count))
            i += 1

            if i == 200:
                break

        scanner.writeGraphFile(result_path_name, word_frequency)


def run():
    AuthorWordifyRepository().wordifyRepository()


if __name__ == '__main__':
    run()

    exit_code = EXIT_OK
    sys.exit(exit_code)