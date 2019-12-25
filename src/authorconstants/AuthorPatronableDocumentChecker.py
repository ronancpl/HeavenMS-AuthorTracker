# Heuristic binary/text file type detection thanks to Eli Bendersky
# src: https://stackoverflow.com/questions/1446549/how-to-identify-binary-and-text-files-using-python

from authorconstants import AuthorConstantLimit
from authorscanner.words import AuthorWordManager


def istext(s):
    if "\0" in s:
        return False

    if not s:  # Empty files are considered text
        return True

    t = AuthorWordManager.getReadableCharacters(s)

    # If more than 30% non-text characters, then
    # this is considered a binary file
    if len(t) / len(s) > 0.30:
        return False
    return True


def isextensionpatronablefile(fileextension):
    return fileextension not in AuthorConstantLimit.WrapLimit.NONPATRONABLE_FILE_EXTENSIONS.getValue()


def istextfile(filecontent, blocksize=512):
    return istext(filecontent[:min(len(filecontent), blocksize)])


def isPatronableRepositoryFile(file_path, file_size):
    if file_size > AuthorConstantLimit.WrapLimit.PATRON_FILE_MAXSIZE.getValue():
        return False

    file_extension = file_path[file_path.rfind('.') + 1:]
    return isextensionpatronablefile(file_extension)


def isPatronableRepositoryDirectory(dir_name):
    return dir_name not in AuthorConstantLimit.WrapLimit.NONPATRONABLE_DIRECTORIES.getValue()
