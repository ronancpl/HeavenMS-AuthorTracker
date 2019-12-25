package antlr;

// Generated from rules/DescriptionCodeParser.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DescriptionCodeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		TOKEN_AMP=1, TOKEN_APOS=2, TOKEN_QUOT=3, ANY_CHARACTER=4;
	public static final int
		RULE_codeTokenSpec = 0, RULE_ignoreSpec = 1, RULE_mainSpec = 2, RULE_compilationUnit = 3;
	public static final String[] ruleNames = {
		"codeTokenSpec", "ignoreSpec", "mainSpec", "compilationUnit"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'&amp;'", "'&apos;'", "'&quot;'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "TOKEN_AMP", "TOKEN_APOS", "TOKEN_QUOT", "ANY_CHARACTER"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "DescriptionCodeParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DescriptionCodeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class CodeTokenSpecContext extends ParserRuleContext {
		public TerminalNode TOKEN_AMP() { return getToken(DescriptionCodeParser.TOKEN_AMP, 0); }
		public TerminalNode TOKEN_APOS() { return getToken(DescriptionCodeParser.TOKEN_APOS, 0); }
		public TerminalNode TOKEN_QUOT() { return getToken(DescriptionCodeParser.TOKEN_QUOT, 0); }
		public CodeTokenSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_codeTokenSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionCodeParserListener ) ((DescriptionCodeParserListener)listener).enterCodeTokenSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionCodeParserListener ) ((DescriptionCodeParserListener)listener).exitCodeTokenSpec(this);
		}
	}

	public final CodeTokenSpecContext codeTokenSpec() throws RecognitionException {
		CodeTokenSpecContext _localctx = new CodeTokenSpecContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_codeTokenSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TOKEN_AMP) | (1L << TOKEN_APOS) | (1L << TOKEN_QUOT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IgnoreSpecContext extends ParserRuleContext {
		public IgnoreSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ignoreSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionCodeParserListener ) ((DescriptionCodeParserListener)listener).enterIgnoreSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionCodeParserListener ) ((DescriptionCodeParserListener)listener).exitIgnoreSpec(this);
		}
	}

	public final IgnoreSpecContext ignoreSpec() throws RecognitionException {
		IgnoreSpecContext _localctx = new IgnoreSpecContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_ignoreSpec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			matchWildcard();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainSpecContext extends ParserRuleContext {
		public CodeTokenSpecContext codeTokenSpec() {
			return getRuleContext(CodeTokenSpecContext.class,0);
		}
		public IgnoreSpecContext ignoreSpec() {
			return getRuleContext(IgnoreSpecContext.class,0);
		}
		public MainSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mainSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionCodeParserListener ) ((DescriptionCodeParserListener)listener).enterMainSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionCodeParserListener ) ((DescriptionCodeParserListener)listener).exitMainSpec(this);
		}
	}

	public final MainSpecContext mainSpec() throws RecognitionException {
		MainSpecContext _localctx = new MainSpecContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_mainSpec);
		try {
			setState(14);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(12);
				codeTokenSpec();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(13);
				ignoreSpec();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CompilationUnitContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(DescriptionCodeParser.EOF, 0); }
		public List<MainSpecContext> mainSpec() {
			return getRuleContexts(MainSpecContext.class);
		}
		public MainSpecContext mainSpec(int i) {
			return getRuleContext(MainSpecContext.class,i);
		}
		public CompilationUnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compilationUnit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionCodeParserListener ) ((DescriptionCodeParserListener)listener).enterCompilationUnit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionCodeParserListener ) ((DescriptionCodeParserListener)listener).exitCompilationUnit(this);
		}
	}

	public final CompilationUnitContext compilationUnit() throws RecognitionException {
		CompilationUnitContext _localctx = new CompilationUnitContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_compilationUnit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TOKEN_AMP) | (1L << TOKEN_APOS) | (1L << TOKEN_QUOT) | (1L << ANY_CHARACTER))) != 0)) {
				{
				{
				setState(16);
				mainSpec();
				}
				}
				setState(21);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(22);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6\33\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3\4\3\4\5\4\21\n\4\3\5\7\5\24\n\5"+
		"\f\5\16\5\27\13\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2\3\3\2\3\5\2\30\2\n\3\2\2"+
		"\2\4\f\3\2\2\2\6\20\3\2\2\2\b\25\3\2\2\2\n\13\t\2\2\2\13\3\3\2\2\2\f\r"+
		"\13\2\2\2\r\5\3\2\2\2\16\21\5\2\2\2\17\21\5\4\3\2\20\16\3\2\2\2\20\17"+
		"\3\2\2\2\21\7\3\2\2\2\22\24\5\6\4\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23"+
		"\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2\30\31\7\2\2\3\31\t"+
		"\3\2\2\2\4\20\25";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}