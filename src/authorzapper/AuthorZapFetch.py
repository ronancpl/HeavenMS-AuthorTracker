from authorfetcher import AuthorFetchRepository
from authorfetcher import AuthorFetchRepositoryCommits
from authorfetcher import AuthorFetchRepositoryFileSystem
#from authorfetcher import AuthorFetchRepositoryFileSystemMovement
from authorfetcher import AuthorFetchRepositoryGitTreeMovement
from authorfetcher import AuthorFetchRepositoryPatrons
from authorfetcher import AuthorFetchRepositoryUsers
from authorfetcher import AuthorFetchRepositoryUsersEvents
from authorfetcher import AuthorFetchRepositoryUsersPulls


from datetime import datetime
import sys
import time


# exit values
EXIT_OK = 0
EXIT_FAIL = 7


def runAuthorScript(author_script):
    global reqGet

    if author_script.run() != EXIT_OK:
        if reqGet is not None and 'X-RateLimit-Reset' in reqGet.headers:
            time.sleep(max(20,float(reqGet.headers['X-RateLimit-Reset']) - float(datetime.utcnow().timestamp())))
        else:
            time.sleep(1 * 60 * 60)


def main():
    runAuthorScript(AuthorFetchRepository)
    runAuthorScript(AuthorFetchRepositoryCommits)
    runAuthorScript(AuthorFetchRepositoryFileSystem)
    runAuthorScript(AuthorFetchRepositoryGitTreeMovement)
    runAuthorScript(AuthorFetchRepositoryPatrons)
    runAuthorScript(AuthorFetchRepositoryUsers)

    runAuthorScript(AuthorFetchRepositoryUsersEvents)
    runAuthorScript(AuthorFetchRepositoryUsersPulls)


def run():
    main()
    exit_code = EXIT_OK
    return exit_code


if __name__ == '__main__':
    sys.exit(run())
