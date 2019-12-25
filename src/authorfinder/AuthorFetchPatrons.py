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

from antlr4 import *
from authorfinder import AuthorDocumentLexer
from authorfinder import AuthorDocumentParserListener
from authorfinder import AuthorDocumentParser
from authorfinder import AuthorCommentLexer
from authorfinder import AuthorCommentParser
from authorfinder import AuthorCommentParserListener
from authorfinder import AuthorContentLexer
from authorfinder import AuthorContentParser
from authorfinder import AuthorContentParserListener
from authorconstants import AuthorPatronableDocumentChecker
from datetime import datetime
import json
import os
import errno
from enum import Enum


patronsLibPath = '../../lib/patrons'


class PatronType(Enum):
    AUTHOR = 'AUTHOR'
    AUTHBY = 'AUTHBY'
    CONTRB = 'CONTRB'


class AuthorDocumentListener(AuthorDocumentParserListener.AuthorDocumentParserListener):

    comments = []
    token_stream = None

    def setTokenStream(self, ts):
        self.token_stream = ts

    def fetchCommentBlocks(self):
        outputComments = self.comments.copy()
        self.comments.clear()

        return outputComments

    def enterCommentBlock(self, ctx):
        self.comments.append(self.token_stream.getText(ctx.getSourceInterval()))

    def enterCommentLine(self, ctx):
        self.comments.append(self.token_stream.getText(ctx.getSourceInterval()))

class AuthorCommentListener(AuthorCommentParserListener.AuthorCommentParserListener):

    text = ''

    def enterScopeSpec(self, ctx):
        self.text += ctx.getText()

    def getScopeText(self):
        return self.text


class AuthorContentListener(AuthorContentParserListener.AuthorContentParserListener):

    def __init__(self):
        self.patronNames = []


    def getPatronAtomicText(self, ctx):
        text = ctx.patronSingleton().getText().strip()    # trim trailing spaces from sides

        patronDevteam = ctx.DEVTEAM()
        if patronDevteam is not None:
            text += u"\u000C"   # form feed to signalize it's a devteam

        return text

    # parse patron names...

    def getPatronText(self, ctx):
        patronAtomics = ctx.patronAtomic()
        if len(patronAtomics) > 1:
            return [self.getPatronAtomicText(patronAtomics[0]), self.getPatronAtomicText(patronAtomics[1])]
        else:
            return [self.getPatronAtomicText(patronAtomics[0])]

    def processPatronName(self, patronNameCtx, patronType):
        if patronNameCtx is not None:
            patronName = self.getPatronText(patronNameCtx)
            if len(patronName[0]) > 0:
                self.patronNames.append([patronName, patronType.name])
                # print(patronType.name + ' : ' + str(patronName))


    def processPatronNames(self, patronNamesCtx, patronType):
        self.processPatronName(patronNamesCtx.patronName(), patronType)
        if patronNamesCtx.patronNames() is not None:
            self.processPatronNames(patronNamesCtx.patronNames(), patronType)

    def processPatronNamesWrap(self, patronNamesWrapCtx, patronType):
        patronNamesCtx = patronNamesWrapCtx.patronNames()
        if patronNamesCtx is not None:
            self.processPatronNames(patronNamesCtx, patronType)


    # parse patron names in reverse...

    def getPatronTextLeft(self, ctx):
        patronAtomics = ctx.patronAtomicLeft()
        if len(patronAtomics) > 1:
            return [self.getPatronAtomicText(patronAtomics[0]), self.getPatronAtomicText(patronAtomics[1])]
        else:
            return [self.getPatronAtomicText(patronAtomics[0])]

    def processPatronNameLeft(self, patronNameCtx, patronType):
        if patronNameCtx is not None:
            patronName = self.getPatronTextLeft(patronNameCtx)
            if len(patronName[0]) > 0:
                self.patronNames.append([patronName, patronType.name])
                # print(patronType.name + ' : ' + str(patronName))

    def processPatronNamesLeft(self, patronNamesCtx, patronType):
        self.processPatronNameLeft(patronNamesCtx.patronNameLeft(), patronType)
        if patronNamesCtx.patronNamesLeft() is not None:
            self.processPatronNamesLeft(patronNamesCtx.patronNamesLeft(), patronType)

    def processPatronNamesWrapLeft(self, patronNamesWrapCtx, patronType):
        patronNamesCtx = patronNamesWrapCtx.patronNamesLeft()
        if patronNamesCtx is not None:
            self.processPatronNamesLeft(patronNamesCtx, patronType)

    def enterEveryRule(self, ctx):
        #print(ctx.getText())
        pass

    def enterCommentBlockSpec(self, ctx):
        #print(ctx.getText())
        pass

    def enterCommentByLine(self, ctx):
        patronWrap = ctx.patronNamesWrap()
        self.processPatronNamesWrap(patronWrap, PatronType.AUTHBY)

    def enterAuthor(self, ctx):
        patronWrap = ctx.patronNamesWrap()
        self.processPatronNamesWrap(patronWrap, PatronType.AUTHOR)

    def enterContributor(self, ctx):
        patronWrap = ctx.patronNamesWrap()
        if patronWrap is not None:
            self.processPatronNamesWrap(patronWrap, PatronType.CONTRB)
        else:
            patronWrap = ctx.patronNamesWrapLeft()
            self.processPatronNamesWrapLeft(patronWrap, PatronType.CONTRB)

    def clearPatronNames(self):
        self.patronNames.clear()

    def getPatronNames(self):
        return self.patronNames.copy()


def authorReadComment(comment_content):
    try:
        isa = InputStream(comment_content + '\n')
        lexer = AuthorContentLexer.AuthorContentLexer(isa)
        stream = CommonTokenStream(lexer)

        parser = AuthorContentParser.AuthorContentParser(stream)
        tree = parser.main()

        listener = AuthorContentListener()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        ret = listener.getPatronNames()
        listener.clearPatronNames()

        return ret

    except UnicodeDecodeError:
        return []


def authorParseCommentIgnores(comment_content):
    try:
        isa = InputStream(comment_content)
        lexer = AuthorCommentLexer.AuthorCommentLexer(isa)
        stream = CommonTokenStream(lexer)

        parser = AuthorCommentParser.AuthorCommentParser(stream)
        tree = parser.main()

        listener = AuthorCommentListener()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener.getScopeText()

    except UnicodeDecodeError:
        return []


def authorReadSourceFile(filePath):
    try:
        print('\n---------- ' + filePath + ' ----------')
        file = open(filePath, 'r')

        file_data = ""
        for line in file:
            file_data += line

        patrons = authorReadSourceFileContent(file_data)
        for patron_name, patron_type in patrons:
            print(patron_type + ' : ' + str(patron_name))

        return patrons

    except UnicodeDecodeError:
        return []


def isLicenseComment(comment_content, comment_idx):
    return comment_content.find('General Public License') > -1


def authorReadSourceFileContent(fileContent):
    isa = InputStream(fileContent + '\n')
    lexer = AuthorDocumentLexer.AuthorDocumentLexer(isa)
    stream = CommonTokenStream(lexer)

    parser = AuthorDocumentParser.AuthorDocumentParser(stream)
    tree = parser.main()

    listener = AuthorDocumentListener()
    listener.setTokenStream(stream)

    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    patron_names = []

    comments = listener.fetchCommentBlocks()
    comment_idx = 0
    for comment_content in comments:
        if not isLicenseComment(comment_content, comment_idx):
            patron_names.extend(authorReadComment(authorParseCommentIgnores(comment_content)))

        comment_idx += 1

    return patron_names


def authorReadPatronFile(fileName, filePath):
    fileStats = os.stat(filePath)
    if fileStats is not None:
        fileSize = fileStats.st_size  # get file size in bytes

        if AuthorPatronableDocumentChecker.isPatronableRepositoryFile(fileName, fileSize):
            patrons = authorReadSourceFile(filePath)
            if len(patrons) > 0:
                return [filePath, patrons]

    return None


def authorReadDirectoryRecursively(directoryName, directoryPath):
    global directoryIgnores
    if directoryName in directoryIgnores or not AuthorPatronableDocumentChecker.isPatronableRepositoryDirectory(directoryName):
        return []

    dirList = []
    patronFiles = []

    for fileName in os.listdir(directoryPath):
        filePath = directoryPath + '/' + fileName
        if os.path.isdir(filePath):
            dirList.append((fileName, filePath))
        else:
            patronFileData = authorReadPatronFile(fileName, filePath)
            if patronFileData is not None:
                patronFiles.append(patronFileData)

    for dirName, dirItem in dirList:
        patronFiles.extend(authorReadDirectoryRecursively(dirName, dirItem))

    return patronFiles


def setupDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


class AuthorFetchPatrons:

    def authorFetchFileContentPatrons(self, fileContent):
        return authorReadSourceFileContent(fileContent)


    def authorDumpSourcePatrons(self, rootPath, dirIgnores):
        setupDir(patronsLibPath + '/a.txt')

        global directoryIgnores
        directoryIgnores = dirIgnores

        # getting timestamp
        today = datetime.today()
        todayString = "{}-{}-{}".format(today.year, today.month, today.day)

        for itemName in os.listdir(rootPath):
            print('Parsing ' + itemName)
            if itemName in directoryIgnores:
                continue

            filePath = rootPath + '/' + itemName

            if os.path.isdir(filePath):
                patronFiles = authorReadDirectoryRecursively(itemName, filePath)
            else:
                patronFiles = []

                patronItem = authorReadPatronFile(itemName, filePath)
                if patronItem is not None:
                    patronFiles.append(patronItem)

            if len(patronFiles) > 0:
                file = open(patronsLibPath + '/' + itemName + ".txt", 'a')

                # saving new content
                patronContent = {'patrons': patronFiles}
                blob = {'fetchDate': todayString, 'content': patronContent}
                file.write("" + json.dumps(blob) + ",\n")
                file.close()


if __name__ == '__main__':
    dir_ignore = ['handbook']
    AuthorFetchPatrons().authorDumpSourcePatrons('../../../HeavenMS', dir_ignore)
