'''
    This file is part of the HeavenMS MapleStory Server
    Copyleft (L) 2016 - 2018 RonanLana

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation version 3 as published by
    the Free Software Foundation. You may not use, modify or distribute
    this program under any other version of the GNU Affero General Public
    License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys

from datetime import datetime
import json


class AuthorScanJsonReader:
    duplicateTargets = ['id', 'sha']


    def parseDate(self, date_str):
        format_str = '%Y-%m-%d'  # The format
        return datetime.strptime(date_str, format_str)


    def getDateFilestamp(self, timestamp):
        # returns string with only timestamp digits
        return ''.join(c for c in timestamp if c.isdigit())


    def hasDuplicateContent(self, jsonEntry, jsonFetchedEntries):
        for target in self.duplicateTargets:
            if target in jsonEntry and (target, jsonEntry[target]) in jsonFetchedEntries:
                return target

        return None


    def mergeContentsInternal(self, jsonCt):
        jsonRet = []
        for jsonItem in jsonCt:
            if isinstance(jsonItem, list):
                jsonItemMerge = self.mergeContentsInternal(jsonItem)
                for jsonIt in jsonItemMerge:
                    jsonRet.append(jsonIt)
            else:
                jsonRet.append(jsonItem)

        return jsonRet


    def mergeContents(self, jsonCt):
        if isinstance(jsonCt, list):
            return self.mergeContentsInternal(jsonCt)
        else:
            return jsonCt


    def fetchDuplicateEntries(self, jsonSt):
        jsonEntries = {}
        jsonDuplicated = {}

        jsonRes = []
        for jsonItem in jsonSt:
            jsonCt = jsonItem['content']

            if not isinstance(jsonCt, list):
                jsonCt = [jsonCt]
            else:
                jsonCt = self.mergeContents(jsonCt)

            for jsonIt in jsonCt:
                duplicate = self.hasDuplicateContent(jsonIt, jsonEntries)
                if duplicate is not None:
                    jsonDuplicated[jsonIt[duplicate], duplicate] = (jsonIt, jsonItem['fetchDate'])
                else:
                    for key, value in jsonIt.items():
                        if key in self.duplicateTargets:
                            jsonEntries[key, value] = 1   # risk taking unrelated data to be matched by using key-value mapping

            jsonItem['content'] = jsonCt
            jsonRes.append(jsonItem)

        return (jsonRes, jsonDuplicated)


    def fetchEntries(self, jsonSt):
        jsonRes = []
        for jsonItem in jsonSt:
            jsonCt = jsonItem['content']

            if not isinstance(jsonCt, list):
                jsonCt = [jsonCt]
            else:
                jsonCt = self.mergeContents(jsonCt)

            jsonItem['content'] = jsonCt
            jsonRes.append(jsonItem)

        return jsonRes


    def isDuplicateContent(self, jsonDate, jsonElem, jsonRepeat):
        for key, value in jsonElem.items():
            if key in self.duplicateTargets and (value, key) in jsonRepeat:
                (repCont, repDate) = jsonRepeat[(value, key)]

                if repDate is not jsonDate:
                    return True

        return False


    def removeDuplicateEntries(self, jsonSt, jsonRepeat):
        jsonRes = []

        for jsonItem in jsonSt:
            jsonCt = jsonItem['content']
            jsonDate = jsonItem['fetchDate']

            jsonResElem = {}
            jsonResElemCont = []
            jsonResElem['fetchDate'] = jsonDate

            for jsonElem in jsonCt:
                if not self.isDuplicateContent(jsonDate, jsonElem, jsonRepeat):
                    jsonResElemCont.append(jsonElem)

            jsonResElem['content'] = jsonResElemCont
            jsonRes.append(jsonResElem)

        return jsonRes


    def readFileRaw(self, filename):    # temporary
        file = open(filename, 'r')
        st = file.read()
        st = st[:-2]
        st = '[' + st + ']'

        jsonRaw = json.loads(st)
        if not jsonRaw:
            return jsonRaw

        return self.mergeContents(jsonRaw)


    def readFile(self, filename, removeDuplicates):
        file = open(filename, 'r')
        st = file.read()
        st = st[:-2]
        st = '[' + st + ']'

        jsonRaw = json.loads(st)
        if not jsonRaw:
            return jsonRaw

        jsonSt = []     # effective JSON content

        lastDate = datetime(2000,1,1)   # remove chronologically tantamount entries
        temp = {}
        thisDate = None
        for jsonItem in jsonRaw:
            thisDate = self.parseDate(jsonItem['fetchDate'])

            if (thisDate - lastDate).days >= 5 and 'documentation_url' not in temp:
                jsonData = {'fetchDate': lastDate, 'content': temp}
                jsonSt.append(jsonData)
                lastDate = thisDate

            temp = jsonItem['content']

        if 'documentation_url' not in temp:
            jsonSt.append({'fetchDate': thisDate, 'content': temp})

        # remove "empty temp" as head content
        jsonSt.pop(0)

        if removeDuplicates:    # objectively parses internal JSON entries checking for duplicated data
            (jsonSt, jsonRepeat) = self.fetchDuplicateEntries(jsonSt)
            return self.removeDuplicateEntries(jsonSt, jsonRepeat)

        else:
            return self.fetchEntries(jsonSt)
