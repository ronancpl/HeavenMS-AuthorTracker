from authortrackprocessor import AuthorTrackRepository
from authorscanner.patrons import AuthorPatronManager
from authorscanner.patrons import AuthorPatronFeatType


def processSocialActivities():
    for patron_name, patron_data in tracker.social.items():
        for patron in patronManager.getPatron(patron_name):
            i = 0
            for timely_item in patron_data:
                # timely_item['word_table']
                is_public_stream = timely_item['public_stream']

                patron.addFeat(AuthorPatronFeatType.FeatType.SOCIAL_CHARACTER, timely_item['character_count'], i, is_public_stream)
                patron.addFeat(AuthorPatronFeatType.FeatType.SOCIAL_QUESTION, timely_item['question_count'], i, is_public_stream)
                patron.addFeat(AuthorPatronFeatType.FeatType.SOCIAL_CODE, timely_item['code_count'], i, is_public_stream)

                i += 1


def scoreSocial():
    global tracker
    tracker = AuthorTrackRepository.tracker

    global patronManager
    patronManager = AuthorPatronManager.patronManager

    processSocialActivities()


def run():
    scoreSocial()


if __name__ == '__main__':
    run()
