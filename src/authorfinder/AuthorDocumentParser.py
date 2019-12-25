# Generated from rules/AuthorDocumentParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write(">\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\5\2\26\n\2\3\2\3\2\3\3\3\3\5")
        buf.write("\3\34\n\3\3\3\3\3\6\3 \n\3\r\3\16\3!\3\4\7\4%\n\4\f\4")
        buf.write("\16\4(\13\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\7\7\63")
        buf.write("\n\7\f\7\16\7\66\13\7\3\b\7\b9\n\b\f\b\16\b<\13\b\3\b")
        buf.write("\5&\64:\2\t\2\4\6\b\n\f\16\2\3\3\2\5\6\2=\2\25\3\2\2\2")
        buf.write("\4\37\3\2\2\2\6&\3\2\2\2\b)\3\2\2\2\n-\3\2\2\2\f\64\3")
        buf.write("\2\2\2\16:\3\2\2\2\20\26\5\4\3\2\21\22\5\6\4\2\22\23\5")
        buf.write("\4\3\2\23\26\3\2\2\2\24\26\5\6\4\2\25\20\3\2\2\2\25\21")
        buf.write("\3\2\2\2\25\24\3\2\2\2\26\27\3\2\2\2\27\30\7\2\2\3\30")
        buf.write("\3\3\2\2\2\31\34\5\b\5\2\32\34\5\n\6\2\33\31\3\2\2\2\33")
        buf.write("\32\3\2\2\2\34\35\3\2\2\2\35\36\5\6\4\2\36 \3\2\2\2\37")
        buf.write("\33\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\5\3\2\2")
        buf.write("\2#%\13\2\2\2$#\3\2\2\2%(\3\2\2\2&\'\3\2\2\2&$\3\2\2\2")
        buf.write("\'\7\3\2\2\2(&\3\2\2\2)*\7\3\2\2*+\5\f\7\2+,\7\4\2\2,")
        buf.write("\t\3\2\2\2-.\t\2\2\2./\5\16\b\2/\60\7\7\2\2\60\13\3\2")
        buf.write("\2\2\61\63\13\2\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64\65")
        buf.write("\3\2\2\2\64\62\3\2\2\2\65\r\3\2\2\2\66\64\3\2\2\2\679")
        buf.write("\13\2\2\28\67\3\2\2\29<\3\2\2\2:;\3\2\2\2:8\3\2\2\2;\17")
        buf.write("\3\2\2\2<:\3\2\2\2\b\25\33!&\64:")
        return buf.getvalue()


class AuthorDocumentParser ( Parser ):

    grammarFileName = "AuthorDocumentParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/*'", "'*/'", "'//'", "'--'", "'\n'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_OPEN", "COMMENT_CLOSE", "COMMENT_LINE1", 
                      "COMMENT_LINE2", "LINE_FEED", "CHARACTERS" ]

    RULE_main = 0
    RULE_mainSpec = 1
    RULE_codeSpec = 2
    RULE_commentBlock = 3
    RULE_commentLine = 4
    RULE_commentBlockSpec = 5
    RULE_commentInlineSpec = 6

    ruleNames =  [ "main", "mainSpec", "codeSpec", "commentBlock", "commentLine", 
                   "commentBlockSpec", "commentInlineSpec" ]

    EOF = Token.EOF
    COMMENT_OPEN=1
    COMMENT_CLOSE=2
    COMMENT_LINE1=3
    COMMENT_LINE2=4
    LINE_FEED=5
    CHARACTERS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AuthorDocumentParser.EOF, 0)

        def mainSpec(self):
            return self.getTypedRuleContext(AuthorDocumentParser.MainSpecContext,0)


        def codeSpec(self):
            return self.getTypedRuleContext(AuthorDocumentParser.CodeSpecContext,0)


        def getRuleIndex(self):
            return AuthorDocumentParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = AuthorDocumentParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 14
                self.mainSpec()
                pass

            elif la_ == 2:
                self.state = 15
                self.codeSpec()
                self.state = 16
                self.mainSpec()
                pass

            elif la_ == 3:
                self.state = 18
                self.codeSpec()
                pass


            self.state = 21
            self.match(AuthorDocumentParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def codeSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorDocumentParser.CodeSpecContext)
            else:
                return self.getTypedRuleContext(AuthorDocumentParser.CodeSpecContext,i)


        def commentBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorDocumentParser.CommentBlockContext)
            else:
                return self.getTypedRuleContext(AuthorDocumentParser.CommentBlockContext,i)


        def commentLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorDocumentParser.CommentLineContext)
            else:
                return self.getTypedRuleContext(AuthorDocumentParser.CommentLineContext,i)


        def getRuleIndex(self):
            return AuthorDocumentParser.RULE_mainSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainSpec" ):
                listener.enterMainSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainSpec" ):
                listener.exitMainSpec(self)




    def mainSpec(self):

        localctx = AuthorDocumentParser.MainSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [AuthorDocumentParser.COMMENT_OPEN]:
                    self.state = 23
                    self.commentBlock()
                    pass
                elif token in [AuthorDocumentParser.COMMENT_LINE1, AuthorDocumentParser.COMMENT_LINE2]:
                    self.state = 24
                    self.commentLine()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 27
                self.codeSpec()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AuthorDocumentParser.COMMENT_OPEN) | (1 << AuthorDocumentParser.COMMENT_LINE1) | (1 << AuthorDocumentParser.COMMENT_LINE2))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CodeSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AuthorDocumentParser.RULE_codeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeSpec" ):
                listener.enterCodeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeSpec" ):
                listener.exitCodeSpec(self)




    def codeSpec(self):

        localctx = AuthorDocumentParser.CodeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_codeSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 33
                    self.matchWildcard() 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT_OPEN(self):
            return self.getToken(AuthorDocumentParser.COMMENT_OPEN, 0)

        def commentBlockSpec(self):
            return self.getTypedRuleContext(AuthorDocumentParser.CommentBlockSpecContext,0)


        def COMMENT_CLOSE(self):
            return self.getToken(AuthorDocumentParser.COMMENT_CLOSE, 0)

        def getRuleIndex(self):
            return AuthorDocumentParser.RULE_commentBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentBlock" ):
                listener.enterCommentBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentBlock" ):
                listener.exitCommentBlock(self)




    def commentBlock(self):

        localctx = AuthorDocumentParser.CommentBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_commentBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(AuthorDocumentParser.COMMENT_OPEN)
            self.state = 40
            self.commentBlockSpec()
            self.state = 41
            self.match(AuthorDocumentParser.COMMENT_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentLineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commentInlineSpec(self):
            return self.getTypedRuleContext(AuthorDocumentParser.CommentInlineSpecContext,0)


        def LINE_FEED(self):
            return self.getToken(AuthorDocumentParser.LINE_FEED, 0)

        def COMMENT_LINE1(self):
            return self.getToken(AuthorDocumentParser.COMMENT_LINE1, 0)

        def COMMENT_LINE2(self):
            return self.getToken(AuthorDocumentParser.COMMENT_LINE2, 0)

        def getRuleIndex(self):
            return AuthorDocumentParser.RULE_commentLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentLine" ):
                listener.enterCommentLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentLine" ):
                listener.exitCommentLine(self)




    def commentLine(self):

        localctx = AuthorDocumentParser.CommentLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_commentLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==AuthorDocumentParser.COMMENT_LINE1 or _la==AuthorDocumentParser.COMMENT_LINE2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 44
            self.commentInlineSpec()
            self.state = 45
            self.match(AuthorDocumentParser.LINE_FEED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentBlockSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AuthorDocumentParser.RULE_commentBlockSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentBlockSpec" ):
                listener.enterCommentBlockSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentBlockSpec" ):
                listener.exitCommentBlockSpec(self)




    def commentBlockSpec(self):

        localctx = AuthorDocumentParser.CommentBlockSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_commentBlockSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 47
                    self.matchWildcard() 
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentInlineSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AuthorDocumentParser.RULE_commentInlineSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentInlineSpec" ):
                listener.enterCommentInlineSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentInlineSpec" ):
                listener.exitCommentInlineSpec(self)




    def commentInlineSpec(self):

        localctx = AuthorDocumentParser.CommentInlineSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_commentInlineSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 53
                    self.matchWildcard() 
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





