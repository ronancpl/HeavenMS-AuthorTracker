from authorscanner import AuthorScanRepository
from authorscanner.words import AuthorWordManager
from authortrackwriter import AuthorGraphResultPrinter

from authortrackwriter.atomic import AuthorDrawDirectory
from authortrackwriter.atomic import AuthorDrawFile
from authortrackwriter.commit import AuthorDrawFileLineGrowth
from authortrackwriter.commit import AuthorDrawFileSizeGrowth as AuthorDrawCommitFileSizeGrowth
from authortrackwriter.content import AuthorDrawAcceptedPullRequests
from authortrackwriter.content import AuthorDrawFileCountGrowth
from authortrackwriter.content import AuthorDrawFileSizeGrowth as AuthorDrawContentFileSizeGrowth
from authortrackwriter.content import AuthorDrawReleaseGrowth
from authortrackwriter.content import AuthorDrawRepositoryGrowth
from authortrackwriter.content import AuthorDrawRepositoryKeyword
from authortrackwriter.content import AuthorDrawRepositoryLogKeyword
from authortrackwriter.content import AuthorDrawSearchedPaths
from authortrackwriter.creator import AuthorDrawCommitFrequency
from authortrackwriter.creator import AuthorDrawIssuesClosed
from authortrackwriter.creator import AuthorDrawLineGrowth
from authortrackwriter.patrons import AuthorDrawPatrons
from authortrackwriter.patrons import AuthorDrawPatronsWords
from authortrackwriter.survey import AuthorDrawSurvey
from authortrackwriter.survey import AuthorDrawSurveyQuestion
from authortrackwriter.traffic import AuthorDrawClones
from authortrackwriter.traffic import AuthorDrawPaths
from authortrackwriter.traffic import AuthorDrawReferrers
from authortrackwriter.traffic import AuthorDrawViews
from authortrackwriter.worldmap import AuthorDrawWorldmapMovement

from datetime import datetime
import sys
import time

# exit values
EXIT_OK = 0
EXIT_FAIL = 7


def main():
    AuthorScanRepository.AuthorScanRepository(False)
    AuthorWordManager.AuthorWordManager()
    AuthorGraphResultPrinter.AuthorGraphResultPrinter()

    print("Reporting View files")
    AuthorDrawDirectory.run()
    AuthorDrawFile.run()
    AuthorDrawFileLineGrowth.run()
    AuthorDrawCommitFileSizeGrowth.run()
    AuthorDrawAcceptedPullRequests.run()
    AuthorDrawFileCountGrowth.run()
    AuthorDrawContentFileSizeGrowth.run()
    AuthorDrawReleaseGrowth.run()
    AuthorDrawRepositoryGrowth.run()
    AuthorDrawRepositoryKeyword.run()
    AuthorDrawRepositoryLogKeyword.run()
    AuthorDrawSearchedPaths.run()
    AuthorDrawCommitFrequency.run()
    AuthorDrawIssuesClosed.run()
    AuthorDrawLineGrowth.run()
    AuthorDrawPatrons.run()
    AuthorDrawPatronsWords.run()
    AuthorDrawSurveyQuestion.run()
    AuthorDrawSurvey.run()
    AuthorDrawClones.run()
    AuthorDrawPaths.run()
    AuthorDrawReferrers.run()
    AuthorDrawViews.run()
    AuthorDrawWorldmapMovement.run()
    print('Done')


def run():
    main()
    exit_code = EXIT_OK
    return exit_code


if __name__ == '__main__':
    sys.exit(run())
