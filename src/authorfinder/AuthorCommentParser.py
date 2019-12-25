# Generated from rules/AuthorCommentParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write(")\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16\n")
        buf.write("\2\f\2\16\2\21\13\2\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\6\3\6\7\6\"\n\6\f\6\16\6%\13\6")
        buf.write("\3\6\3\6\3\6\3\17\2\7\2\4\6\b\n\2\2\2\'\2\17\3\2\2\2\4")
        buf.write("\27\3\2\2\2\6\31\3\2\2\2\b\35\3\2\2\2\n#\3\2\2\2\f\16")
        buf.write("\13\2\2\2\r\f\3\2\2\2\16\21\3\2\2\2\17\20\3\2\2\2\17\r")
        buf.write("\3\2\2\2\20\3\3\2\2\2\21\17\3\2\2\2\22\23\7\3\2\2\23\24")
        buf.write("\5\4\3\2\24\25\7\4\2\2\25\30\3\2\2\2\26\30\5\2\2\2\27")
        buf.write("\22\3\2\2\2\27\26\3\2\2\2\30\5\3\2\2\2\31\32\7\3\2\2\32")
        buf.write("\33\5\4\3\2\33\34\7\4\2\2\34\7\3\2\2\2\35\36\13\2\2\2")
        buf.write("\36\t\3\2\2\2\37\"\5\6\4\2 \"\5\b\5\2!\37\3\2\2\2! \3")
        buf.write("\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$&\3\2\2\2%#\3\2")
        buf.write("\2\2&\'\7\2\2\3\'\13\3\2\2\2\6\17\27!#")
        return buf.getvalue()


class AuthorCommentParser ( Parser ):

    grammarFileName = "AuthorCommentParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "LCMP", "RCMP", "ANY" ]

    RULE_anySpec = 0
    RULE_commentSpec = 1
    RULE_mainSpec = 2
    RULE_scopeSpec = 3
    RULE_main = 4

    ruleNames =  [ "anySpec", "commentSpec", "mainSpec", "scopeSpec", "main" ]

    EOF = Token.EOF
    LCMP=1
    RCMP=2
    ANY=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class AnySpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AuthorCommentParser.RULE_anySpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnySpec" ):
                listener.enterAnySpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnySpec" ):
                listener.exitAnySpec(self)




    def anySpec(self):

        localctx = AuthorCommentParser.AnySpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_anySpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 10
                    self.matchWildcard() 
                self.state = 15
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

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

        def LCMP(self):
            return self.getToken(AuthorCommentParser.LCMP, 0)

        def commentSpec(self):
            return self.getTypedRuleContext(AuthorCommentParser.CommentSpecContext,0)


        def RCMP(self):
            return self.getToken(AuthorCommentParser.RCMP, 0)

        def anySpec(self):
            return self.getTypedRuleContext(AuthorCommentParser.AnySpecContext,0)


        def getRuleIndex(self):
            return AuthorCommentParser.RULE_commentSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentSpec" ):
                listener.enterCommentSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentSpec" ):
                listener.exitCommentSpec(self)




    def commentSpec(self):

        localctx = AuthorCommentParser.CommentSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commentSpec)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(AuthorCommentParser.LCMP)
                self.state = 17
                self.commentSpec()
                self.state = 18
                self.match(AuthorCommentParser.RCMP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.anySpec()
                pass


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

        def LCMP(self):
            return self.getToken(AuthorCommentParser.LCMP, 0)

        def commentSpec(self):
            return self.getTypedRuleContext(AuthorCommentParser.CommentSpecContext,0)


        def RCMP(self):
            return self.getToken(AuthorCommentParser.RCMP, 0)

        def getRuleIndex(self):
            return AuthorCommentParser.RULE_mainSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainSpec" ):
                listener.enterMainSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainSpec" ):
                listener.exitMainSpec(self)




    def mainSpec(self):

        localctx = AuthorCommentParser.MainSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mainSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(AuthorCommentParser.LCMP)
            self.state = 24
            self.commentSpec()
            self.state = 25
            self.match(AuthorCommentParser.RCMP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ScopeSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AuthorCommentParser.RULE_scopeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScopeSpec" ):
                listener.enterScopeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScopeSpec" ):
                listener.exitScopeSpec(self)




    def scopeSpec(self):

        localctx = AuthorCommentParser.ScopeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_scopeSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AuthorCommentParser.EOF, 0)

        def mainSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorCommentParser.MainSpecContext)
            else:
                return self.getTypedRuleContext(AuthorCommentParser.MainSpecContext,i)


        def scopeSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AuthorCommentParser.ScopeSpecContext)
            else:
                return self.getTypedRuleContext(AuthorCommentParser.ScopeSpecContext,i)


        def getRuleIndex(self):
            return AuthorCommentParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = AuthorCommentParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AuthorCommentParser.LCMP) | (1 << AuthorCommentParser.RCMP) | (1 << AuthorCommentParser.ANY))) != 0):
                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 29
                    self.mainSpec()
                    pass

                elif la_ == 2:
                    self.state = 30
                    self.scopeSpec()
                    pass


                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(AuthorCommentParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





