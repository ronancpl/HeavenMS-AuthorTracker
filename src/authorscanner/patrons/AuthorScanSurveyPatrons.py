from datetime import datetime
import os
import re

from authorscanner.patrons import AuthorPatronManager


def readSurveyTopicEntry(topic_item):
    return topic_item[topic_item.find('">') + 2 : topic_item.rfind('</p>')]

def readSurveyTopic(survey_topic):
    survey_item = {}

    topic_question = None
    topic_answer = None

    for topic_item in survey_topic:
        topic_item = topic_item.lstrip()
        if topic_item.startswith('<p class="question-title'):
            topic_question = readSurveyTopicEntry(topic_item)
        elif topic_item.startswith('<p class="question-answer'):
            topic_answer = re.sub('<br/>$', '', readSurveyTopicEntry(topic_item))

    if topic_question is not None and topic_answer is not None:
        survey_item[topic_question] = topic_answer

    return survey_item, topic_answer


def processPlatforms(platform_str):
    platforms_entries = platform_str.split(':')

    platforms = set()
    for entry in platforms_entries:
        for platform in entry.strip().split('/'):
            platforms.add(platform)

    return platforms


def processInternalName(internal_name, patron_entry):
    platforms = None

    idx = internal_name.find(':')
    if idx >= 0:
        platform_str = internal_name[0:idx]
        platforms = processPlatforms(platform_str)

    names_str = internal_name[idx + 1:]
    names = re.split(r'[,|]+', names_str)

    name_list = []
    for name in names:
        name = patronManager.processPatronName(re.sub('#\d{4}$', '', name))

        if name is not None:
            name_list.append(name)

    if platforms is not None:
        for platform in platforms:
            patron_entry[platform] = name_list

    patron_entry[''].extend(name_list)


def processSurveyNames(item_name):
    idx = 0
    internal_names = []

    while True:
        lastIdx = idx
        idx = item_name.find('(', idx)
        if idx < 0:
            internal_names.append(item_name[lastIdx:])
            break

        internal_names.append(item_name[lastIdx:idx])

        endIdx = item_name.find(')', idx)

        internal_name = item_name[idx + 1:endIdx]
        internal_names.append(internal_name)

        idx = endIdx + 1

    patron_entry = {'': []}
    for name in internal_names:
        processInternalName(name, patron_entry)

    platforms = set(patron_entry.keys())
    platforms.remove('')

    name_list = patron_entry['']

    name = None
    aliases = set()
    if len(name_list) > 0:
        name = name_list[0]

        for alias in name_list[1:]:
            aliases.add(alias)

    return name, aliases, platforms


def processSurveyTopicMetadata(survey_item, name, nationality, timestamp, survey_answers):
    survey_item['name'], survey_item['assoc'], survey_item['platforms'] = processSurveyNames(name)
    survey_item['nationality'] = nationality
    survey_item['created_at'] = timestamp
    survey_item['answer_list'] = survey_answers


def readSurveyEntry(survey_file_path):
    file = open(survey_file_path, 'r', encoding='UTF-8')

    survey_item = {}
    survey_answers = []
    survey_timestamp = None

    survey_topic = None
    countStart = 0

    for line in file:
        if survey_topic is not None:
            if line.startswith('</div>'):
                survey_topic_res, survey_topic_ans = readSurveyTopic(survey_topic)
                survey_item.update(survey_topic_res)
                survey_answers.append(survey_topic_ans)
                survey_topic = None
            else:
                survey_topic.append(line)
        else:
            if line.startswith('<div class="onecol question">'):
                survey_topic = []
            elif line.lstrip().startswith('<p class="sub-title-grey-small"><b>Survey Started:'):
                countStart = 3
            elif countStart > 0:
                if countStart == 1:
                    en = line.rfind(' GMT')
                    st = line.rfind('\">') + 2

                    date_str = line[st:en]
                    survey_timestamp = datetime.strptime(date_str, '%m/%d/%Y, %I:%M %p')

                countStart -= 1

    file.close()

    processSurveyTopicMetadata(survey_item, survey_answers[0], survey_answers[1], survey_timestamp, survey_answers)
    return survey_item


def interpretSurveyPatrons(patronsLibPath):
    survey_content = {}

    for file in os.listdir(patronsLibPath):
        survey_file_path = patronsLibPath + '/' + file
        if os.path.isfile(survey_file_path):
            survey_item = readSurveyEntry(survey_file_path)
            survey_content[survey_file_path] = survey_item

    return survey_content


def fetchSurveyPatronAliases(survey_content):
    survey_patrons = []

    for survey_item in survey_content.values():
        patron_alias = []

        patron_alias.append(survey_item['name'])
        for alias in survey_item['assoc']:
            patron_alias.append(alias)

        survey_patrons.append((patron_alias, survey_item['nationality']))

    return survey_patrons


class AuthorScanSurveyPatrons:

    def scanSurveyPatronAssociations(self):
        global patronManager
        patronManager = AuthorPatronManager.patronManager

        survey_content = interpretSurveyPatrons('../../lib/survey')
        return (survey_content, fetchSurveyPatronAliases(survey_content))


def main():
    AuthorScanSurveyPatrons().scanSurveyPatronAssociations()


if __name__ == '__main__':
    main()