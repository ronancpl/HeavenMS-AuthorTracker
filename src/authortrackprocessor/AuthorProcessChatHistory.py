from authorscanner import AuthorScanRepository
from authorscanner.words import AuthorWordManager

last_author = ''
last_skip_count = -1


def generateWordTable(message_lines):
    words = {}

    for line in message_lines:
        keyword_list = wordManager.generateWordList(line)
        wordManager.updateKeywordFrequency(words, keyword_list)

    return words


def fetchCharacterCount(message_lines):
    count = 0
    for line in message_lines:
        count += len(line)

    return count


def fetchQuestionCount(message_author, message_lines):
    global last_skip_count

    if message_author != last_author:
        last_skip_count = -1

    count = 0
    for line in message_lines:
        message_snippets = line.split('?')

        for snippet in message_snippets:
            snippet = snippet.strip().split()

            snippet_len = len(snippet)
            last_skip_count -= snippet_len

            if last_skip_count < 0:
                count += 1
                last_skip_count = 5     # to remove question mark spamming

    return count - 1


def fetchCodeRemarkCount(message_lines):
    count = 0
    for line in message_lines:
        count += (len(line.split('`')) - 1)

    return count


def processSocialMessage(msg_metadata, message_content, is_public_stream):
    message_author = message_content['author']
    message_timestamp = message_content['created_at']
    message_lines = message_content['text_lines']

    msg_item = {}
    msg_item['public_stream'] = is_public_stream
    msg_item['created_at'] = message_timestamp
    msg_item['word_table'] = generateWordTable(message_lines)
    msg_item['character_count'] = fetchCharacterCount(message_lines)
    msg_item['question_count'] = fetchQuestionCount(message_author, message_lines)
    msg_item['code_count'] = fetchCodeRemarkCount(message_lines)

    if message_author in msg_metadata:
        msg_author_array = msg_metadata[message_author]
    else:
        msg_author_array = []
        msg_metadata[message_author] = msg_author_array

    msg_author_array.append(msg_item)


def readSocialContents():
    # fetching relations of assiduity (timestamp), character count and word-list of contributors

    social_metadata = {}

    for file_name, social_content in scanner.social.items():
        # msg_count = social_content['message_count']
        is_public_stream = file_name.startswith('1')

        for msg in social_content['chat_history']:
            processSocialMessage(social_metadata, msg, is_public_stream)

    return social_metadata


def addPatronWordTable(patron_wt, word_table):
    for word, count in word_table.items():
        if word in patron_wt:
            patron_wt[word] += count
        else:
            patron_wt[word] = count


def addPatronContents(patron_item, patron_data):
    addPatronWordTable(patron_item['word_table'], patron_data['word_table'])
    patron_item['public_stream'] = patron_data['public_stream']

    patron_item['character_count'] += patron_data['character_count']
    patron_item['question_count'] += patron_data['question_count']
    patron_item['code_count'] += patron_data['code_count']


def fetchTimeSectionSocialContents(social_metadata):
    social_contents = {}

    print('Fetch social channel patrons')
    for patron_name, patron_metadata in social_metadata.items():
        print('  ' + patron_name + ' ' + str(len(patron_metadata)))
        patron_timely_metadata = []
        social_contents[patron_name] = patron_timely_metadata

        patron_msg_db = scanner.generateTimeSectionDatabase(patron_metadata, ['created_at'], days=20)
        for patron_msg_db_range in patron_msg_db:
            patron_timely_item = {}
            patron_timely_metadata.append(patron_timely_item)

            patron_timely_item['word_table'] = {}
            patron_timely_item['public_stream'] = False

            patron_timely_item['character_count'] = 0
            patron_timely_item['question_count'] = 0
            patron_timely_item['code_count'] = 0

            for patron_msg_item in patron_msg_db_range:
                addPatronContents(patron_timely_item, patron_msg_item)

    return social_contents


def fetchSocialContents():
    global scanner
    scanner = AuthorScanRepository.scanner

    global wordManager
    wordManager = AuthorWordManager.wordManager

    social_metadata = readSocialContents()
    social_patron_db = fetchTimeSectionSocialContents(social_metadata)

    return social_patron_db


def run():
    fetchSocialContents()


if __name__ == '__main__':
    run()
