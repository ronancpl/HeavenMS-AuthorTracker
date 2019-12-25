from authorscanner import AuthorScanRepository

from authorwritepress import AuthorPressManager
from authorwritepress import AuthorPressResize
from authorwritepress import AuthorPressStamp

from datetime import datetime
import sys
import time

# exit values
EXIT_OK = 0
EXIT_FAIL = 7


def main():
    AuthorScanRepository.AuthorScanRepository(False)
    AuthorPressManager.AuthorPressManager()

    print("Pressing graph files")
    AuthorPressResize.press()
    AuthorPressStamp.press()



def run():
    main()
    exit_code = EXIT_OK
    return exit_code


if __name__ == '__main__':
    sys.exit(run())
