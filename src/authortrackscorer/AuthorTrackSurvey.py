from authortrackprocessor import AuthorTrackRepository
from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager
from authorscanner.patrons import AuthorPatronFeatType


def scorePatronActivity(patron, survey_item):
    answer_list = survey_item['answer_list']
    survey_timesection = scanner.fetchRepositoryTimeSectionFromTimestamp(survey_item['created_at'], days=20)

    patron.addFeat(AuthorPatronFeatType.FeatType.SURVEY_BASIC, 1, survey_timesection, True)

    if len(answer_list) > 0:
        patron.addFeat(AuthorPatronFeatType.FeatType.SURVEY_COMPLETE, 1, survey_timesection, True)


def processSurveyActivities():
    for survey_patron, survey_item in tracker.survey.items():
        scorePatronActivity(survey_patron, survey_item)


def scoreSurvey():
    global scanner
    scanner = AuthorScanRepository.scanner

    global tracker
    tracker = AuthorTrackRepository.tracker

    global patronManager
    patronManager = AuthorPatronManager.patronManager

    processSurveyActivities()


def run():
    scoreSurvey()


if __name__ == '__main__':
    run()
