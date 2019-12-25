from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager
from authortrackscorer import AuthorScoreHolder
from authortrackscorer import AuthorTrackChatHistory
from authortrackscorer import AuthorTrackGithub
from authortrackscorer import AuthorTrackSourceCode
from authortrackscorer import AuthorTrackSurvey
from authortrackwriter import AuthorGraphResultFile
import sys

# exit values
EXIT_OK = 0
EXIT_FAIL = 7

result_path_name = AuthorGraphResultFile.ResultFile.PATRONS_SCORE


class AuthorScoreRepository:

    def scoreRepository(self):
        print('Scoring patrons...')
        AuthorScoreHolder.loadScoreHolder()

        AuthorTrackChatHistory.scoreSocial()
        AuthorTrackGithub.scoreGithub()
        AuthorTrackSourceCode.scoreSourceCode()
        AuthorTrackSurvey.scoreSurvey()

        global patronManager
        patronManager = AuthorPatronManager.patronManager

        patrons_list = patronManager.exportPatronsList()
        for patron in patrons_list:
            patron.calcScore()

        global scanner
        scanner = AuthorScanRepository.scanner

        patrons_list = sorted(patrons_list, key=lambda k: k.score, reverse=True)    # top-down score ordering

        print()
        print('score patrons')
        i = 0
        for patron in patrons_list:
            print(patron)
            i += 1

            if i == 100:
                break

        graph_content = patrons_list
        scanner.writeGraphFile(result_path_name, graph_content)


def run():
    AuthorScoreRepository().scoreRepository()


if __name__ == '__main__':
    run()

    exit_code = EXIT_OK
    sys.exit(exit_code)