from authorwrapper.atomic import AuthorWrapDirectory
from authorwrapper.atomic import AuthorWrapFile
from authorwrapper.commit import AuthorWrapFileLineGrowth
from authorwrapper.commit import AuthorWrapFileSizeGrowth
from authorwrapper.content import AuthorWrapAcceptedPullRequests
from authorwrapper.content import AuthorWrapFileCount
from authorwrapper.content import AuthorWrapFileSize
from authorwrapper.content import AuthorWrapReleaseGrowth
from authorwrapper.content import AuthorWrapRepositoryGrowth
from authorwrapper.content import AuthorWrapRepositoryKeywords
from authorwrapper.content import AuthorWrapRepositoryLogKeywords
from authorwrapper.creator import AuthorWrapIssueCommitFrequency
from authorwrapper.creator import AuthorWrapLineGrowth
from authorwrapper.patrons import AuthorWrapPatrons
from authorwrapper.patrons import AuthorWrapPatronsWords
from authorwrapper.survey import AuthorWrapSurvey
from authorwrapper.traffic import AuthorWrapCloneViews
from authorwrapper.traffic import AuthorWrapPaths
from authorwrapper.traffic import AuthorWrapReferrers

from authorscanner import AuthorScanRepository
from authorscanner.words import AuthorWordManager
from authortrackwriter import AuthorGraphResultPrinter

from datetime import datetime
import sys
import time

# exit values
EXIT_OK = 0
EXIT_FAIL = 7


def main():
    AuthorScanRepository.AuthorScanRepository(False)
    AuthorGraphResultPrinter.AuthorGraphResultPrinter()
    AuthorWordManager.AuthorWordManager()

    print("Reporting Wrap files")
    AuthorWrapDirectory.plot()
    AuthorWrapFile.plot()
    AuthorWrapFileLineGrowth.plot()
    AuthorWrapFileSizeGrowth.plot()
    AuthorWrapAcceptedPullRequests.plot()
    AuthorWrapFileCount.plot()
    AuthorWrapFileSize.plot()
    AuthorWrapReleaseGrowth.plot()
    AuthorWrapRepositoryGrowth.plot()
    AuthorWrapRepositoryKeywords.plot()
    AuthorWrapRepositoryLogKeywords.plot()
    AuthorWrapIssueCommitFrequency.plot()
    AuthorWrapLineGrowth.plot()
    AuthorWrapPatrons.plot()
    AuthorWrapPatronsWords.plot()
    AuthorWrapSurvey.plot()
    AuthorWrapCloneViews.plot()
    AuthorWrapPaths.plot()
    AuthorWrapReferrers.plot()


def run():
    main()
    exit_code = EXIT_OK
    return exit_code


if __name__ == '__main__':
    sys.exit(run())
