import PIL
from PIL import Image
import errno
import os

from authorscanner import AuthorScanRepository
from authorwritepress import AuthorPressManager

basewidth = 700     # relative width of pressable graphs


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def resizeImageFile(filePath):
    if os.path.splitext(filePath)[1] != '.png':
        return

    img = Image.open(scanner.plot_path + filePath)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

    fIdx = filePath.rfind('/')
    folderPath = filePath[:fIdx]
    fileName = filePath[fIdx:]

    section_info = pressManager.getPathSectionInfo(fileName)
    resizedImgPath = scanner.wordpress_path + folderPath + section_info[0] + fileName
    setupDir(resizedImgPath)

    img.save(resizedImgPath)


def resizeReadDirectoryRecursively(directoryPath):
    dirList = []

    for fileName in os.listdir(scanner.plot_path + directoryPath):
        filePath = directoryPath + '/' + fileName
        if os.path.isdir(scanner.plot_path + filePath):
            dirList.append(filePath)
        else:
            resizeImageFile(filePath)

    for subdirectoryPath in dirList:
        resizeReadDirectoryRecursively(subdirectoryPath)


def press():
    global scanner
    scanner = AuthorScanRepository.scanner

    global pressManager
    pressManager = AuthorPressManager.pressManager

    print('Resizing wrapped graphs')
    resizeReadDirectoryRecursively('')


if __name__ == '__main__':
    press()
