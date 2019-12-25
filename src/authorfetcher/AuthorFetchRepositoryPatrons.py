from authorfinder import AuthorFetchPatrons


import sys
import traceback

# exit values
EXIT_OK = 0
EXIT_FAIL = 7


def main():
    dir_ignore = ['handbook']
    AuthorFetchPatrons.AuthorFetchPatrons().authorDumpSourcePatrons('../../../HeavenMS', dir_ignore)


def run():
    main()
    exit_code = EXIT_OK

    return exit_code


if __name__ == '__main__':
    sys.exit(run())