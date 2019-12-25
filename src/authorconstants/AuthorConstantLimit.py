from enum import Enum


def nameset(namelist):
    ret = set()
    for name in namelist:
        ret.add(name)

    return ret


class WrapLimit(Enum):
    UNDEFINED = -1
    PATRON_FILE_MAXSIZE = 578000
    PATRON_COMMIT_FILES_MAXSIZE = 5500
    REPOSITORY_ISSUES_PULLS_COUNT = 541

    PATRON_DISTINGUISHED_CHAT_COUNT = 28000

    COMMIT_DIFF_SIZE_LIMIT = 50000

    FILE_EMPTY_DIFFS_MAXRATE = 0.0777

    FILE_DUMP_DIFF_MINSIZE = 200
    CODE_DUMP_DIFF_MINSIZE = 7777
    TXT_DUMP_DIFF_MINSIZE = 100
    XML_DUMP_DIFF_MINSIZE = 420

    FILE_DUMP_DIRECTORY_MINDEPTH = 2

    FILE_DUMP_DIRECTORY_DIFF_MINSIZE = 20
    CODE_DUMP_DIRECTORY_DIFF_MINSIZE = 50
    TXT_DUMP_DIRECTORY_DIFF_MINSIZE = 20
    XML_DUMP_DIRECTORY_DIFF_MINSIZE = 15

    WARN_COMMIT_FILE_DUMPS_COUNT = 5

    LOG_TRANSLATE = False

    NONPATRONABLE_FILE_EXTENSIONS = nameset(['xml', 'jar', 'class', 'sample'])
    NONPATRONABLE_DIRECTORIES = nameset(['logs', 'build', 'dist', 'nbproject', '.git', 'wz', 'dev', 'cores'])

    def getValue(self):
        return self.value
