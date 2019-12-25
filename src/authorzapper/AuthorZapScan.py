from authorscanner import AuthorScanRepository
from authorscanner.source.game import AuthorGameMapMovement
from authorscanner.source.game import AuthorGameTracker
from authorscanner.source.project import AuthorAtomicDirectoryModificationCount
from authorscanner.source.project import AuthorAtomicFileModificationCount
from authorscanner.source.project import AuthorCommitFileLineGrowth
from authorscanner.source.project import AuthorCommitFileSizeGrowth
from authorscanner.source.project import AuthorContentAcceptedPullRequests
from authorscanner.source.project import AuthorContentFileCountGrowth
from authorscanner.source.project import AuthorContentFileSizeGrowth
from authorscanner.source.project import AuthorContentReleaseGrowth
from authorscanner.source.project import AuthorContentRepositoryGrowth
from authorscanner.source.project import AuthorContentRepositoryKeyword
from authorscanner.source.project import AuthorContentRepositoryLogKeyword
from authorscanner.source.project import AuthorContentSearchedPaths
from authorscanner.source.project import AuthorTrafficClones
from authorscanner.source.project import AuthorTrafficPaths
from authorscanner.source.project import AuthorTrafficReferrers
from authorscanner.source.project import AuthorTrafficViews
from authorscanner.source.users import AuthorUsersCreatorCommitFrequency
from authorscanner.source.users import AuthorUsersCreatorIssuesClosed
from authorscanner.source.users import AuthorUsersCreatorLineGrowth
from authorscanner.survey import AuthorSurveyTable

from authorscanner.words import AuthorWordManager

from authortrackprocessor import AuthorTrackRepository
from authortrackscorer import AuthorScoreRepository
from authortrackworder import AuthorWordifyRepository

from datetime import datetime
import sys
import time

# exit values
EXIT_OK = 0
EXIT_FAIL = 7


def main():
    AuthorScanRepository.AuthorScanRepository(True)
    AuthorWordManager.AuthorWordManager()
    tracked_file_movement, overworld_tracked_movement = AuthorGameTracker.run()

    print("Reporting Scan files")
    AuthorGameMapMovement.run(overworld_tracked_movement)
    AuthorAtomicDirectoryModificationCount.run()
    AuthorAtomicFileModificationCount.run()
    AuthorCommitFileLineGrowth.run()
    AuthorCommitFileSizeGrowth.run()
    AuthorContentAcceptedPullRequests.run()
    AuthorContentFileCountGrowth.run()
    AuthorContentFileSizeGrowth.run()
    AuthorContentReleaseGrowth.run()
    AuthorContentRepositoryGrowth.run()
    AuthorContentRepositoryKeyword.run()
    AuthorContentSearchedPaths.run()
    AuthorTrafficClones.run()
    AuthorTrafficPaths.run()
    AuthorTrafficReferrers.run()
    AuthorTrafficViews.run()
    AuthorUsersCreatorCommitFrequency.run()
    AuthorUsersCreatorIssuesClosed.run()
    AuthorUsersCreatorLineGrowth.run()

    AuthorTrackRepository.AuthorTrackRepository()
    AuthorContentRepositoryLogKeyword.run()
    AuthorSurveyTable.run()
    AuthorScoreRepository.run()
    AuthorWordifyRepository.run()

    AuthorScanRepository.scanner.printFileDumpChecks()


def run():
    main()
    exit_code = EXIT_OK
    return exit_code


if __name__ == '__main__':
    sys.exit(run())
