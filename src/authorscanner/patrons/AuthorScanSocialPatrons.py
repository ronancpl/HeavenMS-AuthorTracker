from datetime import datetime
import os
import re

from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager


authorDifferentiator = {}

def parseAuthor(author):
    r = re.match('.*(#\d{4})( \(pinned\))?$', author)
    diff = r.group(1)

    if diff not in authorDifferentiator:
        diffGroup = []
        authorDifferentiator[diff] = diffGroup
    else:
        diffGroup = authorDifferentiator[diff]

    name = re.sub('(#\d{4})( \(pinned\))?$', '', author)
    diffGroup.append(name)

    return name


def getLineHeaderInfo(line):
    try:
        tokens = line.split(']', 1)
        message_timestamp = datetime.strptime(tokens[0][1:], '%d-%b-%y %I:%M %p')
        message_author = patronManager.processPatronName(parseAuthor(tokens[1][1:]))

        if message_author is not None:
            message_info = {'author': message_author, 'created_at': scanner.writableTimestamp(message_timestamp), 'text_lines': []}
        else:
            message_info = None

        return message_info

    except ValueError:
        return None


def readTextMessage(line, message_item):
    if len(line) > 0:
        message_item.append(line)


def readSocialEntry(social_file_path):
    file = open(social_file_path, 'r', encoding='UTF-8')
    file_lines = file.read().splitlines(keepends=False)

    social_item = {'chat_history': []}

    message_lines = None

    i = 0
    count = 0
    for line in file_lines:
        i += 1

        if line.startswith('=============================================================='):
            count += 1
            if count == 2:
                i += 1  # skip header empty line
                break
        else:
            r = re.match('Messages: ([%d]+)', line)
            if r is not None:
                social_item['message_count'] = int(r.group(1))

    for line in file_lines[i:]:   # skip exporter library file header
        header_item = getLineHeaderInfo(line)
        if header_item is not None:
            message_lines = header_item['text_lines']
            social_item['chat_history'].append(header_item)
        else:
            readTextMessage(line, message_lines)

    file.close()

    return social_item


def interpretSocialPatronsDirectory(dirPath, is_dm):
    social_content = {}

    for file in os.listdir(dirPath):
        social_file_path = dirPath + '/' + file

        if os.path.isdir(social_file_path):
            if re.match(r"^.*([0-9])$", file):
                continue

            social_content.update(interpretSocialPatronsDirectory(social_file_path, file == 'directmessages'))
        else:
            if is_dm:
                public_stream = '0'
            else:
                public_stream = '1'

            social_item = readSocialEntry(social_file_path)
            social_content[public_stream + social_file_path] = social_item

    return social_content


def interpretSocialPatrons(socialLibPath):
    return interpretSocialPatronsDirectory(socialLibPath, None)


def fetchSocialPatronAliases(social_content):
    patron_names = set()

    for social_item in social_content.values():
        for social_entry in social_item['chat_history']:
            patron_names.add(social_entry['author'])

    print('Located ' + str(len(social_content)) + ' social entries from ' + str(len(patron_names)) + ' patrons')

    patron_aliases = []
    for name in patron_names:
        patron_aliases.append([name])   # chat context only lets one name per account

    return patron_aliases


class AuthorScanSocialPatrons:

    def scanSocialPatronAssociations(self):
        global scanner
        scanner = AuthorScanRepository.scanner

        global patronManager
        patronManager = AuthorPatronManager.patronManager

        social_content = interpretSocialPatrons('../../lib/social')
        return (social_content, fetchSocialPatronAliases(social_content))


def main():
    AuthorScanSocialPatrons().scanSocialPatronAssociations()


if __name__ == '__main__':
    main()