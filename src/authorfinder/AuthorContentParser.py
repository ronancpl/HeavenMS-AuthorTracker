# Generated from rules/AuthorContentParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("\u00e4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\5\2\62\n\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\6\3<\n\3\r")
        buf.write("\3\16\3=\3\4\7\4A\n\4\f\4\16\4D\13\4\3\5\3\5\5\5H\n\5")
        buf.write("\3\6\3\6\7\6L\n\6\f\6\16\6O\13\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\6\7X\n\7\r\7\16\7Y\3\7\5\7]\n\7\3\7\5\7`\n\7\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\7\13l\n\13\f\13")
        buf.write("\16\13o\13\13\3\f\7\fr\n\f\f\f\16\fu\13\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\5\r~\n\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\6\17\u0087\n\17\r\17\16\17\u0088\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0097")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00a6\n\21\3\22\5\22\u00a9\n\22\3")
        buf.write("\23\3\23\3\23\5\23\u00ae\n\23\3\23\3\23\3\23\5\23\u00b3")
        buf.write("\n\23\3\23\3\23\3\23\5\23\u00b8\n\23\3\23\5\23\u00bb\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\7\24\u00c2\n\24\f\24\16\24")
        buf.write("\u00c5\13\24\5\24\u00c7\n\24\3\25\3\25\5\25\u00cb\n\25")
        buf.write("\3\25\7\25\u00ce\n\25\f\25\16\25\u00d1\13\25\3\25\5\25")
        buf.write("\u00d4\n\25\3\26\6\26\u00d7\n\26\r\26\16\26\u00d8\3\27")
        buf.write("\3\27\3\27\3\30\7\30\u00df\n\30\f\30\16\30\u00e2\13\30")
        buf.write("\3\30\5=\u0088\u00e0\2\31\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\2\t\4\2\26\26\30\31\3\2\31\32\3\2\30")
        buf.write("\31\3\2\5\6\4\2\34\34\36\36\4\2\4\4\32\32\4\3\5\6\33\33")
        buf.write("\2\u00f6\2\61\3\2\2\2\4;\3\2\2\2\6B\3\2\2\2\bG\3\2\2\2")
        buf.write("\nI\3\2\2\2\f_\3\2\2\2\16a\3\2\2\2\20c\3\2\2\2\22f\3\2")
        buf.write("\2\2\24m\3\2\2\2\26s\3\2\2\2\30}\3\2\2\2\32\177\3\2\2")
        buf.write("\2\34\u0086\3\2\2\2\36\u0096\3\2\2\2 \u00a5\3\2\2\2\"")
        buf.write("\u00a8\3\2\2\2$\u00ba\3\2\2\2&\u00bc\3\2\2\2(\u00c8\3")
        buf.write("\2\2\2*\u00d6\3\2\2\2,\u00da\3\2\2\2.\u00e0\3\2\2\2\60")
        buf.write("\62\5\b\5\2\61\60\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2")
        buf.write("\63\64\5\6\4\2\64\65\3\2\2\2\65\66\5\4\3\2\66\67\7\2\2")
        buf.write("\3\67\3\3\2\2\289\5\b\5\29:\5\6\4\2:<\3\2\2\2;8\3\2\2")
        buf.write("\2<=\3\2\2\2=>\3\2\2\2=;\3\2\2\2>\5\3\2\2\2?A\n\2\2\2")
        buf.write("@?\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\7\3\2\2\2DB")
        buf.write("\3\2\2\2EH\5\n\6\2FH\5\32\16\2GE\3\2\2\2GF\3\2\2\2H\t")
        buf.write("\3\2\2\2IM\7\26\2\2JL\5\f\7\2KJ\3\2\2\2LO\3\2\2\2MK\3")
        buf.write("\2\2\2MN\3\2\2\2NP\3\2\2\2OM\3\2\2\2PQ\7\27\2\2Q\13\3")
        buf.write("\2\2\2RS\5\20\t\2ST\7\31\2\2T`\3\2\2\2UX\5\36\20\2VX\5")
        buf.write(" \21\2WU\3\2\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2")
        buf.write("\2Z\\\3\2\2\2[]\7\33\2\2\\[\3\2\2\2\\]\3\2\2\2]`\3\2\2")
        buf.write("\2^`\5\16\b\2_R\3\2\2\2_W\3\2\2\2_^\3\2\2\2`\r\3\2\2\2")
        buf.write("ab\13\2\2\2b\17\3\2\2\2cd\5\22\n\2de\5\26\f\2e\21\3\2")
        buf.write("\2\2fg\7\25\2\2gh\5\24\13\2hi\7\33\2\2i\23\3\2\2\2jl\t")
        buf.write("\3\2\2kj\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2n\25\3\2")
        buf.write("\2\2om\3\2\2\2pr\5\30\r\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2")
        buf.write("\2st\3\2\2\2t\27\3\2\2\2us\3\2\2\2vw\5\"\22\2wx\7\33\2")
        buf.write("\2x~\3\2\2\2y~\5\22\n\2z{\5\"\22\2{|\5\22\n\2|~\3\2\2")
        buf.write("\2}v\3\2\2\2}y\3\2\2\2}z\3\2\2\2~\31\3\2\2\2\177\u0080")
        buf.write("\t\4\2\2\u0080\u0081\5\34\17\2\u0081\u0082\7\33\2\2\u0082")
        buf.write("\33\3\2\2\2\u0083\u0087\5\36\20\2\u0084\u0087\5 \21\2")
        buf.write("\u0085\u0087\13\2\2\2\u0086\u0083\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0088\u0086\3\2\2\2\u0089\35\3\2\2\2\u008a")
        buf.write("\u008b\7\t\2\2\u008b\u0097\5\"\22\2\u008c\u008d\7\n\2")
        buf.write("\2\u008d\u0097\5\"\22\2\u008e\u008f\7\13\2\2\u008f\u0097")
        buf.write("\5\"\22\2\u0090\u0091\7\f\2\2\u0091\u0097\5\"\22\2\u0092")
        buf.write("\u0093\7\r\2\2\u0093\u0097\5\"\22\2\u0094\u0095\7\16\2")
        buf.write("\2\u0095\u0097\5\"\22\2\u0096\u008a\3\2\2\2\u0096\u008c")
        buf.write("\3\2\2\2\u0096\u008e\3\2\2\2\u0096\u0090\3\2\2\2\u0096")
        buf.write("\u0092\3\2\2\2\u0096\u0094\3\2\2\2\u0097\37\3\2\2\2\u0098")
        buf.write("\u0099\7\17\2\2\u0099\u00a6\5\"\22\2\u009a\u009b\7\20")
        buf.write("\2\2\u009b\u00a6\5\"\22\2\u009c\u009d\7\22\2\2\u009d\u00a6")
        buf.write("\5\"\22\2\u009e\u009f\7\23\2\2\u009f\u00a6\5\"\22\2\u00a0")
        buf.write("\u00a1\7\24\2\2\u00a1\u00a6\5\"\22\2\u00a2\u00a3\5\"\22")
        buf.write("\2\u00a3\u00a4\7\21\2\2\u00a4\u00a6\3\2\2\2\u00a5\u0098")
        buf.write("\3\2\2\2\u00a5\u009a\3\2\2\2\u00a5\u009c\3\2\2\2\u00a5")
        buf.write("\u009e\3\2\2\2\u00a5\u00a0\3\2\2\2\u00a5\u00a2\3\2\2\2")
        buf.write("\u00a6!\3\2\2\2\u00a7\u00a9\5$\23\2\u00a8\u00a7\3\2\2")
        buf.write("\2\u00a8\u00a9\3\2\2\2\u00a9#\3\2\2\2\u00aa\u00ab\5&\24")
        buf.write("\2\u00ab\u00ad\t\5\2\2\u00ac\u00ae\5$\23\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00bb\3\2\2\2\u00af")
        buf.write("\u00bb\5&\24\2\u00b0\u00b2\t\5\2\2\u00b1\u00b3\5$\23\2")
        buf.write("\u00b2\u00b1\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00bb\3")
        buf.write("\2\2\2\u00b4\u00b5\5,\27\2\u00b5\u00b7\t\5\2\2\u00b6\u00b8")
        buf.write("\5$\23\2\u00b7\u00b6\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8")
        buf.write("\u00bb\3\2\2\2\u00b9\u00bb\5,\27\2\u00ba\u00aa\3\2\2\2")
        buf.write("\u00ba\u00af\3\2\2\2\u00ba\u00b0\3\2\2\2\u00ba\u00b4\3")
        buf.write("\2\2\2\u00ba\u00b9\3\2\2\2\u00bb%\3\2\2\2\u00bc\u00c6")
        buf.write("\5(\25\2\u00bd\u00be\7\7\2\2\u00be\u00bf\5(\25\2\u00bf")
        buf.write("\u00c3\7\b\2\2\u00c0\u00c2\5*\26\2\u00c1\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3")
        buf.write("\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00bd")
        buf.write("\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\'\3\2\2\2\u00c8\u00ca")
        buf.write("\5*\26\2\u00c9\u00cb\7\3\2\2\u00ca\u00c9\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cf\3\2\2\2\u00cc\u00ce\7\34\2")
        buf.write("\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d2\u00d4\5,\27\2\u00d3\u00d2\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4)\3\2\2\2\u00d5\u00d7\t\6\2")
        buf.write("\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9+\3\2\2\2\u00da\u00db")
        buf.write("\t\7\2\2\u00db\u00dc\5.\30\2\u00dc-\3\2\2\2\u00dd\u00df")
        buf.write("\n\b\2\2\u00de\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1/\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\36\61=BGMWY\\_ms}\u0086\u0088\u0096\u00a5")
        buf.write("\u00a8\u00ad\u00b2\u00b7\u00ba\u00c3\u00c6\u00ca\u00cf")
        buf.write("\u00d3\u00d8\u00e0")
        return buf.getvalue()


class AuthorContentParser ( Parser ):

    grammarFileName = "AuthorContentParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'dev team'", "' for '", "'&'", "','", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "''s idea'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'/*'", "'*/'", "'//'", "'--'", 
                     "'-'", "'\n'", "' '" ]

    symbolicNames = [ "<INVALID>", "DEVTEAM", "FOR", "AMPERSAND", "COMMA", 
                      "LPAR", "RPAR", "CT_AUTHOR1", "CT_AUTHOR2", "CT_AUTHOR3", 
                      "CT_AUTHOR4", "CT_AUTHOR5", "CT_AUTHOR6", "CT_THANKSTO", 
                      "CT_THANKS", "CT_IDEA", "CT_CREDIT1", "CT_CREDIT2", 
                      "CT_CLEANUP", "CM_BY", "COMMENT_OPEN", "COMMENT_CLOSE", 
                      "COMMENT_LINE1", "COMMENT_LINE2", "COMMENT_HYPN", 
                      "LINE_FEED", "WS", "IGNORE_SPACE", "IDENTIFIER" ]

    RULE_main = 0
    RULE_mainSpec = 1
    RULE_codeSpec = 2
    RULE_commentSpec = 3
    RULE_commentBlock = 4
    RULE_commentBlockSpec = 5
    RULE_out = 6
    RULE_commentByBlockSpec = 7
    RULE_commentByHeader = 8
    RULE_commentByHeaderSkip = 9
    RULE_commentByBody = 10
    RULE_commentByLine = 11
    RULE_commentLine = 12
    RULE_commentInlineSpec = 13
    RULE_author = 14
    RULE_contributor = 15
    RULE_patronNamesWrap = 16
    RULE_patronNames = 17
    RULE_patronName = 18
    RULE_patronAtomic = 19
    RULE_patronSingleton = 20
    RULE_patronAtomicSkip = 21
    RULE_patronCommentInternal = 22

    ruleNames =  [ "main", "mainSpec", "codeSpec", "commentSpec", "commentBlock", 
                   "commentBlockSpec", "out", "commentByBlockSpec", "commentByHeader", 
                   "commentByHeaderSkip", "commentByBody", "commentByLine", 
                   "commentLine", "commentInlineSpec", "author", "contributor", 
                   "patronNamesWrap", "patronNames", "patronName", "patronAtomic", 
                   "patronSingleton", "patronAtomicSkip", "patronCommentInternal" ]

    EOF = Token.EOF
    DEVTEAM=1
    FOR=2
    AMPERSAND=3
    COMMA=4
    LPAR=5
    RPAR=6
    CT_AUTHOR1=7
    CT_AUTHOR2=8
    CT_AUTHOR3=9
    CT_AUTHOR4=10
    CT_AUTHOR5=11
    CT_AUTHOR6=12
    CT_THANKSTO=13
    CT_THANKS=14
    CT_IDEA=15
    CT_CREDIT1=16
    CT_CREDIT2=17
    CT_CLEANUP=18
    CM_BY=19
    COMMENT_OPEN=20
    COMMENT_CLOSE=21
    COMMENT_LINE1=22
    COMMENT_LINE2=23
    COMMENT_HYPN=24
    LINE_FEED=25
    WS=26
    IGNORE_SPACE=27
    IDENTIFIER=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainSpec(self):
            return self.getTypedRuleContext(AuthorContentParser.MainSpecContext,0)


        def EOF(self):
            return self.getToken(AuthorContentParser.EOF, 0)

        def codeSpec(self):
            return self.getTypedRuleContext(AuthorContentParser.CodeSpecContext,0)


        def commentSpec(self):
            return self.getTypedRuleContext(AuthorContentParser.CommentSpecContext,0)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = AuthorContentParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 46
                self.commentSpec()


            self.state = 49
            self.codeSpec()
            self.state = 51
            self.mainSpec()
            self.state = 52
            self.match(AuthorContentParser.EOF)
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

        def commentSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.CommentSpecContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.CommentSpecContext,i)


        def codeSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.CodeSpecContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.CodeSpecContext,i)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_mainSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainSpec" ):
                listener.enterMainSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainSpec" ):
                listener.exitMainSpec(self)




    def mainSpec(self):

        localctx = AuthorContentParser.MainSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 54
                    self.commentSpec()
                    self.state = 55
                    self.codeSpec()

                else:
                    raise NoViableAltException(self)
                self.state = 59 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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

        def COMMENT_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.COMMENT_OPEN)
            else:
                return self.getToken(AuthorContentParser.COMMENT_OPEN, i)

        def COMMENT_LINE1(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.COMMENT_LINE1)
            else:
                return self.getToken(AuthorContentParser.COMMENT_LINE1, i)

        def COMMENT_LINE2(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.COMMENT_LINE2)
            else:
                return self.getToken(AuthorContentParser.COMMENT_LINE2, i)

        def getRuleIndex(self):
            return AuthorContentParser.RULE_codeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeSpec" ):
                listener.enterCodeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeSpec" ):
                listener.exitCodeSpec(self)




    def codeSpec(self):

        localctx = AuthorContentParser.CodeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_codeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AuthorContentParser.DEVTEAM) | (1 << AuthorContentParser.FOR) | (1 << AuthorContentParser.AMPERSAND) | (1 << AuthorContentParser.COMMA) | (1 << AuthorContentParser.LPAR) | (1 << AuthorContentParser.RPAR) | (1 << AuthorContentParser.CT_AUTHOR1) | (1 << AuthorContentParser.CT_AUTHOR2) | (1 << AuthorContentParser.CT_AUTHOR3) | (1 << AuthorContentParser.CT_AUTHOR4) | (1 << AuthorContentParser.CT_AUTHOR5) | (1 << AuthorContentParser.CT_AUTHOR6) | (1 << AuthorContentParser.CT_THANKSTO) | (1 << AuthorContentParser.CT_THANKS) | (1 << AuthorContentParser.CT_IDEA) | (1 << AuthorContentParser.CT_CREDIT1) | (1 << AuthorContentParser.CT_CREDIT2) | (1 << AuthorContentParser.CT_CLEANUP) | (1 << AuthorContentParser.CM_BY) | (1 << AuthorContentParser.COMMENT_CLOSE) | (1 << AuthorContentParser.COMMENT_HYPN) | (1 << AuthorContentParser.LINE_FEED) | (1 << AuthorContentParser.WS) | (1 << AuthorContentParser.IGNORE_SPACE) | (1 << AuthorContentParser.IDENTIFIER))) != 0):
                self.state = 61
                _la = self._input.LA(1)
                if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AuthorContentParser.COMMENT_OPEN) | (1 << AuthorContentParser.COMMENT_LINE1) | (1 << AuthorContentParser.COMMENT_LINE2))) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commentBlock(self):
            return self.getTypedRuleContext(AuthorContentParser.CommentBlockContext,0)


        def commentLine(self):
            return self.getTypedRuleContext(AuthorContentParser.CommentLineContext,0)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentSpec" ):
                listener.enterCommentSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentSpec" ):
                listener.exitCommentSpec(self)




    def commentSpec(self):

        localctx = AuthorContentParser.CommentSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_commentSpec)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AuthorContentParser.COMMENT_OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.commentBlock()
                pass
            elif token in [AuthorContentParser.COMMENT_LINE1, AuthorContentParser.COMMENT_LINE2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.commentLine()
                pass
            else:
                raise NoViableAltException(self)

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
            return self.getToken(AuthorContentParser.COMMENT_OPEN, 0)

        def COMMENT_CLOSE(self):
            return self.getToken(AuthorContentParser.COMMENT_CLOSE, 0)

        def commentBlockSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.CommentBlockSpecContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.CommentBlockSpecContext,i)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentBlock" ):
                listener.enterCommentBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentBlock" ):
                listener.exitCommentBlock(self)




    def commentBlock(self):

        localctx = AuthorContentParser.CommentBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_commentBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(AuthorContentParser.COMMENT_OPEN)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 72
                    self.commentBlockSpec() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 78
            self.match(AuthorContentParser.COMMENT_CLOSE)
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

        def commentByBlockSpec(self):
            return self.getTypedRuleContext(AuthorContentParser.CommentByBlockSpecContext,0)


        def COMMENT_LINE2(self):
            return self.getToken(AuthorContentParser.COMMENT_LINE2, 0)

        def author(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.AuthorContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.AuthorContext,i)


        def contributor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.ContributorContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.ContributorContext,i)


        def LINE_FEED(self):
            return self.getToken(AuthorContentParser.LINE_FEED, 0)

        def out(self):
            return self.getTypedRuleContext(AuthorContentParser.OutContext,0)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentBlockSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentBlockSpec" ):
                listener.enterCommentBlockSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentBlockSpec" ):
                listener.exitCommentBlockSpec(self)




    def commentBlockSpec(self):

        localctx = AuthorContentParser.CommentBlockSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_commentBlockSpec)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.commentByBlockSpec()
                self.state = 81
                self.match(AuthorContentParser.COMMENT_LINE2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 85
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [AuthorContentParser.CT_AUTHOR1, AuthorContentParser.CT_AUTHOR2, AuthorContentParser.CT_AUTHOR3, AuthorContentParser.CT_AUTHOR4, AuthorContentParser.CT_AUTHOR5, AuthorContentParser.CT_AUTHOR6]:
                            self.state = 83
                            self.author()
                            pass
                        elif token in [AuthorContentParser.FOR, AuthorContentParser.AMPERSAND, AuthorContentParser.COMMA, AuthorContentParser.CT_THANKSTO, AuthorContentParser.CT_THANKS, AuthorContentParser.CT_IDEA, AuthorContentParser.CT_CREDIT1, AuthorContentParser.CT_CREDIT2, AuthorContentParser.CT_CLEANUP, AuthorContentParser.COMMENT_HYPN, AuthorContentParser.WS, AuthorContentParser.IDENTIFIER]:
                            self.state = 84
                            self.contributor()
                            pass
                        else:
                            raise NoViableAltException(self)


                    else:
                        raise NoViableAltException(self)
                    self.state = 87 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 90
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 89
                    self.match(AuthorContentParser.LINE_FEED)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.out()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OutContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AuthorContentParser.RULE_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOut" ):
                listener.enterOut(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOut" ):
                listener.exitOut(self)




    def out(self):

        localctx = AuthorContentParser.OutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_out)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentByBlockSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commentByHeader(self):
            return self.getTypedRuleContext(AuthorContentParser.CommentByHeaderContext,0)


        def commentByBody(self):
            return self.getTypedRuleContext(AuthorContentParser.CommentByBodyContext,0)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentByBlockSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentByBlockSpec" ):
                listener.enterCommentByBlockSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentByBlockSpec" ):
                listener.exitCommentByBlockSpec(self)




    def commentByBlockSpec(self):

        localctx = AuthorContentParser.CommentByBlockSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_commentByBlockSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.commentByHeader()
            self.state = 98
            self.commentByBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentByHeaderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM_BY(self):
            return self.getToken(AuthorContentParser.CM_BY, 0)

        def commentByHeaderSkip(self):
            return self.getTypedRuleContext(AuthorContentParser.CommentByHeaderSkipContext,0)


        def LINE_FEED(self):
            return self.getToken(AuthorContentParser.LINE_FEED, 0)

        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentByHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentByHeader" ):
                listener.enterCommentByHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentByHeader" ):
                listener.exitCommentByHeader(self)




    def commentByHeader(self):

        localctx = AuthorContentParser.CommentByHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_commentByHeader)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(AuthorContentParser.CM_BY)
            self.state = 101
            self.commentByHeaderSkip()
            self.state = 102
            self.match(AuthorContentParser.LINE_FEED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentByHeaderSkipContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT_LINE2(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.COMMENT_LINE2)
            else:
                return self.getToken(AuthorContentParser.COMMENT_LINE2, i)

        def COMMENT_HYPN(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.COMMENT_HYPN)
            else:
                return self.getToken(AuthorContentParser.COMMENT_HYPN, i)

        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentByHeaderSkip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentByHeaderSkip" ):
                listener.enterCommentByHeaderSkip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentByHeaderSkip" ):
                listener.exitCommentByHeaderSkip(self)




    def commentByHeaderSkip(self):

        localctx = AuthorContentParser.CommentByHeaderSkipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_commentByHeaderSkip)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AuthorContentParser.COMMENT_LINE2 or _la==AuthorContentParser.COMMENT_HYPN:
                self.state = 104
                _la = self._input.LA(1)
                if not(_la==AuthorContentParser.COMMENT_LINE2 or _la==AuthorContentParser.COMMENT_HYPN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentByBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commentByLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.CommentByLineContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.CommentByLineContext,i)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentByBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentByBody" ):
                listener.enterCommentByBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentByBody" ):
                listener.exitCommentByBody(self)




    def commentByBody(self):

        localctx = AuthorContentParser.CommentByBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_commentByBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AuthorContentParser.FOR) | (1 << AuthorContentParser.AMPERSAND) | (1 << AuthorContentParser.COMMA) | (1 << AuthorContentParser.CM_BY) | (1 << AuthorContentParser.COMMENT_HYPN) | (1 << AuthorContentParser.LINE_FEED) | (1 << AuthorContentParser.WS) | (1 << AuthorContentParser.IDENTIFIER))) != 0):
                self.state = 110
                self.commentByLine()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentByLineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def patronNamesWrap(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronNamesWrapContext,0)


        def LINE_FEED(self):
            return self.getToken(AuthorContentParser.LINE_FEED, 0)

        def commentByHeader(self):
            return self.getTypedRuleContext(AuthorContentParser.CommentByHeaderContext,0)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentByLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentByLine" ):
                listener.enterCommentByLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentByLine" ):
                listener.exitCommentByLine(self)




    def commentByLine(self):

        localctx = AuthorContentParser.CommentByLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_commentByLine)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.patronNamesWrap()
                self.state = 117
                self.match(AuthorContentParser.LINE_FEED)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.commentByHeader()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.patronNamesWrap()
                self.state = 121
                self.commentByHeader()
                pass


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
            return self.getTypedRuleContext(AuthorContentParser.CommentInlineSpecContext,0)


        def LINE_FEED(self):
            return self.getToken(AuthorContentParser.LINE_FEED, 0)

        def COMMENT_LINE1(self):
            return self.getToken(AuthorContentParser.COMMENT_LINE1, 0)

        def COMMENT_LINE2(self):
            return self.getToken(AuthorContentParser.COMMENT_LINE2, 0)

        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentLine" ):
                listener.enterCommentLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentLine" ):
                listener.exitCommentLine(self)




    def commentLine(self):

        localctx = AuthorContentParser.CommentLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_commentLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not(_la==AuthorContentParser.COMMENT_LINE1 or _la==AuthorContentParser.COMMENT_LINE2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 126
            self.commentInlineSpec()
            self.state = 127
            self.match(AuthorContentParser.LINE_FEED)
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

        def author(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.AuthorContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.AuthorContext,i)


        def contributor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.ContributorContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.ContributorContext,i)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_commentInlineSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentInlineSpec" ):
                listener.enterCommentInlineSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentInlineSpec" ):
                listener.exitCommentInlineSpec(self)




    def commentInlineSpec(self):

        localctx = AuthorContentParser.CommentInlineSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_commentInlineSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 132
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        self.state = 129
                        self.author()
                        pass

                    elif la_ == 2:
                        self.state = 130
                        self.contributor()
                        pass

                    elif la_ == 3:
                        self.state = 131
                        self.matchWildcard()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 134 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AuthorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CT_AUTHOR1(self):
            return self.getToken(AuthorContentParser.CT_AUTHOR1, 0)

        def patronNamesWrap(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronNamesWrapContext,0)


        def CT_AUTHOR2(self):
            return self.getToken(AuthorContentParser.CT_AUTHOR2, 0)

        def CT_AUTHOR3(self):
            return self.getToken(AuthorContentParser.CT_AUTHOR3, 0)

        def CT_AUTHOR4(self):
            return self.getToken(AuthorContentParser.CT_AUTHOR4, 0)

        def CT_AUTHOR5(self):
            return self.getToken(AuthorContentParser.CT_AUTHOR5, 0)

        def CT_AUTHOR6(self):
            return self.getToken(AuthorContentParser.CT_AUTHOR6, 0)

        def getRuleIndex(self):
            return AuthorContentParser.RULE_author

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAuthor" ):
                listener.enterAuthor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAuthor" ):
                listener.exitAuthor(self)




    def author(self):

        localctx = AuthorContentParser.AuthorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_author)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AuthorContentParser.CT_AUTHOR1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(AuthorContentParser.CT_AUTHOR1)
                self.state = 137
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.CT_AUTHOR2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(AuthorContentParser.CT_AUTHOR2)
                self.state = 139
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.CT_AUTHOR3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(AuthorContentParser.CT_AUTHOR3)
                self.state = 141
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.CT_AUTHOR4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.match(AuthorContentParser.CT_AUTHOR4)
                self.state = 143
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.CT_AUTHOR5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.match(AuthorContentParser.CT_AUTHOR5)
                self.state = 145
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.CT_AUTHOR6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.match(AuthorContentParser.CT_AUTHOR6)
                self.state = 147
                self.patronNamesWrap()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContributorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CT_THANKSTO(self):
            return self.getToken(AuthorContentParser.CT_THANKSTO, 0)

        def patronNamesWrap(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronNamesWrapContext,0)


        def CT_THANKS(self):
            return self.getToken(AuthorContentParser.CT_THANKS, 0)

        def CT_CREDIT1(self):
            return self.getToken(AuthorContentParser.CT_CREDIT1, 0)

        def CT_CREDIT2(self):
            return self.getToken(AuthorContentParser.CT_CREDIT2, 0)

        def CT_CLEANUP(self):
            return self.getToken(AuthorContentParser.CT_CLEANUP, 0)

        def CT_IDEA(self):
            return self.getToken(AuthorContentParser.CT_IDEA, 0)

        def getRuleIndex(self):
            return AuthorContentParser.RULE_contributor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContributor" ):
                listener.enterContributor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContributor" ):
                listener.exitContributor(self)




    def contributor(self):

        localctx = AuthorContentParser.ContributorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_contributor)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AuthorContentParser.CT_THANKSTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(AuthorContentParser.CT_THANKSTO)
                self.state = 151
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.CT_THANKS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(AuthorContentParser.CT_THANKS)
                self.state = 153
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.CT_CREDIT1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.match(AuthorContentParser.CT_CREDIT1)
                self.state = 155
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.CT_CREDIT2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.match(AuthorContentParser.CT_CREDIT2)
                self.state = 157
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.CT_CLEANUP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(AuthorContentParser.CT_CLEANUP)
                self.state = 159
                self.patronNamesWrap()
                pass
            elif token in [AuthorContentParser.FOR, AuthorContentParser.AMPERSAND, AuthorContentParser.COMMA, AuthorContentParser.CT_IDEA, AuthorContentParser.COMMENT_HYPN, AuthorContentParser.WS, AuthorContentParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 160
                self.patronNamesWrap()
                self.state = 161
                self.match(AuthorContentParser.CT_IDEA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatronNamesWrapContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def patronNames(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronNamesContext,0)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_patronNamesWrap

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatronNamesWrap" ):
                listener.enterPatronNamesWrap(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatronNamesWrap" ):
                listener.exitPatronNamesWrap(self)




    def patronNamesWrap(self):

        localctx = AuthorContentParser.PatronNamesWrapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_patronNamesWrap)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 165
                self.patronNames()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatronNamesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def patronName(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronNameContext,0)


        def AMPERSAND(self):
            return self.getToken(AuthorContentParser.AMPERSAND, 0)

        def COMMA(self):
            return self.getToken(AuthorContentParser.COMMA, 0)

        def patronNames(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronNamesContext,0)


        def patronAtomicSkip(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronAtomicSkipContext,0)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_patronNames

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatronNames" ):
                listener.enterPatronNames(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatronNames" ):
                listener.exitPatronNames(self)




    def patronNames(self):

        localctx = AuthorContentParser.PatronNamesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_patronNames)
        self._la = 0 # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.patronName()
                self.state = 169
                _la = self._input.LA(1)
                if not(_la==AuthorContentParser.AMPERSAND or _la==AuthorContentParser.COMMA):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 171
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 170
                    self.patronNames()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.patronName()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                _la = self._input.LA(1)
                if not(_la==AuthorContentParser.AMPERSAND or _la==AuthorContentParser.COMMA):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 175
                    self.patronNames()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.patronAtomicSkip()
                self.state = 179
                _la = self._input.LA(1)
                if not(_la==AuthorContentParser.AMPERSAND or _la==AuthorContentParser.COMMA):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 181
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 180
                    self.patronNames()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 183
                self.patronAtomicSkip()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatronNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def patronAtomic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.PatronAtomicContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.PatronAtomicContext,i)


        def LPAR(self):
            return self.getToken(AuthorContentParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(AuthorContentParser.RPAR, 0)

        def patronSingleton(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorContentParser.PatronSingletonContext)
            else:
                return self.getTypedRuleContext(AuthorContentParser.PatronSingletonContext,i)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_patronName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatronName" ):
                listener.enterPatronName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatronName" ):
                listener.exitPatronName(self)




    def patronName(self):

        localctx = AuthorContentParser.PatronNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_patronName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.patronAtomic()
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 187
                self.match(AuthorContentParser.LPAR)
                self.state = 188
                self.patronAtomic()
                self.state = 189
                self.match(AuthorContentParser.RPAR)
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 190
                        self.patronSingleton() 
                    self.state = 195
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatronAtomicContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def patronSingleton(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronSingletonContext,0)


        def DEVTEAM(self):
            return self.getToken(AuthorContentParser.DEVTEAM, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.WS)
            else:
                return self.getToken(AuthorContentParser.WS, i)

        def patronAtomicSkip(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronAtomicSkipContext,0)


        def getRuleIndex(self):
            return AuthorContentParser.RULE_patronAtomic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatronAtomic" ):
                listener.enterPatronAtomic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatronAtomic" ):
                listener.exitPatronAtomic(self)




    def patronAtomic(self):

        localctx = AuthorContentParser.PatronAtomicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_patronAtomic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.patronSingleton()
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 199
                self.match(AuthorContentParser.DEVTEAM)


            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 202
                    self.match(AuthorContentParser.WS) 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 208
                self.patronAtomicSkip()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatronSingletonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.IDENTIFIER)
            else:
                return self.getToken(AuthorContentParser.IDENTIFIER, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.WS)
            else:
                return self.getToken(AuthorContentParser.WS, i)

        def getRuleIndex(self):
            return AuthorContentParser.RULE_patronSingleton

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatronSingleton" ):
                listener.enterPatronSingleton(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatronSingleton" ):
                listener.exitPatronSingleton(self)




    def patronSingleton(self):

        localctx = AuthorContentParser.PatronSingletonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_patronSingleton)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 211
                    _la = self._input.LA(1)
                    if not(_la==AuthorContentParser.WS or _la==AuthorContentParser.IDENTIFIER):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 214 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatronAtomicSkipContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def patronCommentInternal(self):
            return self.getTypedRuleContext(AuthorContentParser.PatronCommentInternalContext,0)


        def COMMENT_HYPN(self):
            return self.getToken(AuthorContentParser.COMMENT_HYPN, 0)

        def FOR(self):
            return self.getToken(AuthorContentParser.FOR, 0)

        def getRuleIndex(self):
            return AuthorContentParser.RULE_patronAtomicSkip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatronAtomicSkip" ):
                listener.enterPatronAtomicSkip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatronAtomicSkip" ):
                listener.exitPatronAtomicSkip(self)




    def patronAtomicSkip(self):

        localctx = AuthorContentParser.PatronAtomicSkipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_patronAtomicSkip)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            _la = self._input.LA(1)
            if not(_la==AuthorContentParser.FOR or _la==AuthorContentParser.COMMENT_HYPN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 217
            self.patronCommentInternal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatronCommentInternalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_FEED(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.LINE_FEED)
            else:
                return self.getToken(AuthorContentParser.LINE_FEED, i)

        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.EOF)
            else:
                return self.getToken(AuthorContentParser.EOF, i)

        def AMPERSAND(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.AMPERSAND)
            else:
                return self.getToken(AuthorContentParser.AMPERSAND, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AuthorContentParser.COMMA)
            else:
                return self.getToken(AuthorContentParser.COMMA, i)

        def getRuleIndex(self):
            return AuthorContentParser.RULE_patronCommentInternal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatronCommentInternal" ):
                listener.enterPatronCommentInternal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatronCommentInternal" ):
                listener.exitPatronCommentInternal(self)




    def patronCommentInternal(self):

        localctx = AuthorContentParser.PatronCommentInternalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_patronCommentInternal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 219
                    _la = self._input.LA(1)
                    if _la <= 0 or ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (AuthorContentParser.EOF - -1)) | (1 << (AuthorContentParser.AMPERSAND - -1)) | (1 << (AuthorContentParser.COMMA - -1)) | (1 << (AuthorContentParser.LINE_FEED - -1)))) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





