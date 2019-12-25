# Generated from rules/AuthorDocumentLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("!\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2")
        buf.write("\2\2 \2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\22\3\2\2\2\7")
        buf.write("\25\3\2\2\2\t\30\3\2\2\2\13\33\3\2\2\2\r\35\3\2\2\2\17")
        buf.write("\20\7\61\2\2\20\21\7,\2\2\21\4\3\2\2\2\22\23\7,\2\2\23")
        buf.write("\24\7\61\2\2\24\6\3\2\2\2\25\26\7\61\2\2\26\27\7\61\2")
        buf.write("\2\27\b\3\2\2\2\30\31\7/\2\2\31\32\7/\2\2\32\n\3\2\2\2")
        buf.write("\33\34\7\f\2\2\34\f\3\2\2\2\35\36\13\2\2\2\36\37\3\2\2")
        buf.write("\2\37 \b\7\2\2 \16\3\2\2\2\3\2\3\2O\2")
        return buf.getvalue()


class AuthorDocumentLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_OPEN = 1
    COMMENT_CLOSE = 2
    COMMENT_LINE1 = 3
    COMMENT_LINE2 = 4
    LINE_FEED = 5
    CHARACTERS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'/*'", "'*/'", "'//'", "'--'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_OPEN", "COMMENT_CLOSE", "COMMENT_LINE1", "COMMENT_LINE2", 
            "LINE_FEED", "CHARACTERS" ]

    ruleNames = [ "COMMENT_OPEN", "COMMENT_CLOSE", "COMMENT_LINE1", "COMMENT_LINE2", 
                  "LINE_FEED", "CHARACTERS" ]

    grammarFileName = "AuthorDocumentLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


