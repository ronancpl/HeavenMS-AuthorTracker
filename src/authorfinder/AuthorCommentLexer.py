# Generated from rules/AuthorCommentLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\17\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\2\2\5\3\3\5\4\7\5\3\2\2\2\16\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\3\t\3\2\2\2\5\13\3\2\2\2\7\r\3\2\2\2\t")
        buf.write("\n\7>\2\2\n\4\3\2\2\2\13\f\7@\2\2\f\6\3\2\2\2\r\16\13")
        buf.write("\2\2\2\16\b\3\2\2\2\3\2\2")
        return buf.getvalue()


class AuthorCommentLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LCMP = 1
    RCMP = 2
    ANY = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "LCMP", "RCMP", "ANY" ]

    ruleNames = [ "LCMP", "RCMP", "ANY" ]

    grammarFileName = "AuthorCommentLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


