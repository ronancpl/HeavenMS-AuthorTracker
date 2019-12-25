# Heuristic binary/text file type detection thanks to Eli Bendersky
# src: https://stackoverflow.com/questions/1446549/how-to-identify-binary-and-text-files-using-python

from nltk.stem.snowball import SnowballStemmer
import nltk
import re

stm = SnowballStemmer("english")
stopwords = None

override_chars = list()
override_chars.extend(map(chr, range(0, 48)))
override_chars.extend(map(chr, range(58, 65)))
override_chars.extend(map(chr, range(91, 97)))
override_chars.extend(map(chr, range(123, 128)))
override_chars.extend(list("\n\r\t\b"))
override_characters = "".join(override_chars)

override_chars_table = str.maketrans(override_characters, ' ' * len(override_chars))

hex_p = re.compile('^([0-9a-f])*[0-9]([0-9a-f])*$')
digit_p = re.compile('[0-9]')

def getReadableCharacters(s):
    # Get the non-text characters (maps a character to itself then
    # use the 'override' option to get rid of the text characters.)

    t = s.translate(override_chars_table)   # thanks to Eli Bendersky, SparkAndShine, Peter Mortensen from StackOverflow
    return t


def getWordClausesFromSentence(text_sentence):
    return getReadableCharacters(text_sentence).split()


def isNumber(v):
    try:
        float(v)
        return True
    except ValueError:
        return False


def isNotValue(word):
    if word == '':          # check empty
        return False

    if isNumber(word):      # check plain number
        return False

    if hex_p.match(word):   # check hexadecimal content
        return False

    return True


def findWordStem(word):
    word_radical = stm.stem(word)
    if len(word_radical) > 4 and word_radical[1:-1] == word[1:-1] and digit_p.search(word):
        return None
    else:
        return word_radical   # avoid web URL codes or encoded numbers if possible


def generateWordlist(line):
    words = []

    line = line.lower()
    word_clauses = getWordClausesFromSentence(line)

    for word_clause in word_clauses:
        if isNotValue(word_clause):
            words.append(word_clause)

    return words


def updateKeywordFrequency(keywords_frequency, keyword_list):
    for keyword_item in keyword_list:
        if keyword_item not in keywords_frequency:
            keywords_frequency[keyword_item] = 1
        else:
            keywords_frequency[keyword_item] += 1


def stripStopwords(keywords_frequency):
    global stopwords

    ret = {}

    for keyword, count in keywords_frequency.items():
        if keyword not in stopwords:
            ret[keyword] = count

    return ret


class AuthorWordManager:

    def __init__(self):
        nltk.download('snowball_data')
        nltk.download('stopwords')

        global stopwords
        stopwords = set(nltk.corpus.stopwords.words())

        global wordManager
        wordManager = self

    def generateWordList(self, text):
        return generateWordlist(text)

    def updateKeywordFrequency(self, keywords_frequency, keyword_list):
        updateKeywordFrequency(keywords_frequency, keyword_list)

    def findWordStem(self, word):
        return findWordStem(word)

    def stripStopwords(self, keywords_frequency):
        return stripStopwords(keywords_frequency)

global wordManager
wordManager = None
