import PIL
from PIL import Image, ImageDraw
import errno
import os
import re

from authorscanner import AuthorScanRepository
from authorwritepress import AuthorPressManager

def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def stampImageFile(filePath, days_interval):
    if os.path.splitext(filePath)[1] != '.png':
        return

    section_info = pressManager.getPathSectionInfo(filePath)
    if section_info[1] is not None:
        timesection_date = pressManager.getTimesectionStamp(section_info[1], days=days_interval)
        timesection_pos = (10, 17.777)

        img = Image.open(scanner.wordpress_path + filePath)
        draw = ImageDraw.Draw(img)

        draw.text(timesection_pos, timesection_date.strftime('%Y-%m-%d'), fill='rgb(0, 0, 0)')
        img.save(scanner.wordpress_path + filePath)


def stampReadDirectoryRecursively(directoryPath, days_interval):
    dirList = []

    for fileName in os.listdir(scanner.wordpress_path + directoryPath):
        filePath = directoryPath + '/' + fileName
        if os.path.isdir(scanner.wordpress_path + filePath):
            dirList.append(filePath)
        else:
            stampImageFile(filePath, days_interval)

    for subdirectoryPath in dirList:
        stampReadDirectoryRecursively(subdirectoryPath, days_interval)


def stampPlotDirectory(directoryPath, months=0, days=0):
    days_interval = scanner.getDayCount(months, days)
    if days_interval > 0:
        if directoryPath == '':
            directoryPath = '.'

        stampReadDirectoryRecursively('/' + directoryPath + '/', days_interval)


def press():
    global scanner
    scanner = AuthorScanRepository.scanner

    global pressManager
    pressManager = AuthorPressManager.pressManager

    print('Timestamping timesectioned graphs')
    stampPlotDirectory('worldmaps', days=20)
    stampPlotDirectory('project/content', months=3)
    stampPlotDirectory('project/traffic', days=40)

if __name__ == '__main__':
    press()
