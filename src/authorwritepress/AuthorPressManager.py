from datetime import datetime
from datetime import timedelta
import math
import re

from authorscanner import AuthorScanRepository


def getPathSectionInfo(fileName):
    ret = ''
    jn = None

    r = re.match('(.*)_jn([0-9]+).png$', fileName)
    if r is not None:
        ret += r.group(1) + '/'
        jn = int(r.group(2))

    return ret, jn


def fetchTimesectionStamp(timesection_idx, days, months):
    days_interval = scanner.getDayCount(months, days)
    start_time = scanner.repository_start_time
    time_stamp = start_time + timedelta(days=days_interval * timesection_idx)
    return time_stamp


class AuthorPressManager:

    def getPathSectionInfo(self, fileName):
        return getPathSectionInfo(fileName)


    def getTimesectionStamp(self, timesection_idx, days=0, months=0):
        return fetchTimesectionStamp(timesection_idx, days, months)


    def __init__(self):
        global pressManager
        pressManager = self

        global scanner
        scanner = AuthorScanRepository.scanner


global pressManager
pressManager = None