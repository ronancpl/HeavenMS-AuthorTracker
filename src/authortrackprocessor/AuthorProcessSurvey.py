from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager


def filteredSurveyContents():
    survey_entries = {}

    for survey_item in scanner.survey.values():
        for patron in patronManager.getPatron(survey_item['name']):
            if patron not in survey_entries or len(survey_entries[patron]['answer_list']) == 0:
                survey_entries[patron] = survey_item

    return survey_entries


def fetchSurveyContents():
    global scanner
    scanner = AuthorScanRepository.scanner

    global patronManager
    patronManager = AuthorPatronManager.patronManager

    survey_contents_db = filteredSurveyContents()
    return survey_contents_db


def run():
    fetchSurveyContents()


if __name__ == '__main__':
    run()
