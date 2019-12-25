package antlr;

// Generated from rules/DescriptionPatchParser.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DescriptionPatchParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		KEYWORD_SUCCESS=1, KEYWORD_LEVEL=2, KEYWORD_JOB=3, KEYWORD_CONDITION=4, 
		KEYWORD_CLASS=5, KEYWORD_WHEN=6, KEYWORD_GIVES=7, KEYWORD_IMPROVES=8, 
		KEYWORD_INCREASES=9, KEYWORD_RECOVER=10, KEYWORD_RESTORES=11, KEYWORD_FULLY=12, 
		KEYWORD_CAN=13, KEYWORD_SPEED=14, KEYWORD_MESO=15, KEYWORD_ACCURACY=16, 
		KEYWORD_AVOIDABILITY=17, KEYWORD_EVASION=18, KEYWORD_PROTECTION=19, KEYWORD_DOUBLE=20, 
		KEYWORD_ITEM=21, KEYWORD_JUMP=22, KEYWORD_ATTACK=23, KEYWORD_DEFENSE=24, 
		KEYWORD_WEAPON=25, KEYWORD_MAGIC=26, KEYWORD_DEF=27, KEYWORD_IF=28, KEYWORD_THE=29, 
		NUMBER=30, CODE_C=31, CODE=32, SIGN=33, MARK=34, WS=35, TARGET_BACKSLASH=36, 
		TARGET_R=37, TARGET_N=38, TARGET_C=39, TARGET_PLUS=40, TARGET_MINUS=41, 
		ANY_CHARACTER=42;
	public static final int
		RULE_dotSpec = 0, RULE_anyKeywordSpec = 1, RULE_textSpec = 2, RULE_expectedCarriageReturnSpec = 3, 
		RULE_expectedLineForwardSpec = 4, RULE_expectedLineBreakSpec = 5, RULE_whitespaceBeforeKeywordSpec = 6, 
		RULE_whitespaceOrLineBreakSpec = 7, RULE_codeSpec = 8, RULE_lineBreakMaybeCodeSpec = 9, 
		RULE_potentialConflictSpec = 10, RULE_signMaybeWhitespaceSpec = 11, RULE_signConflictSpec = 12, 
		RULE_whitespaceSpec = 13, RULE_spacedDotSpec = 14, RULE_moreConflictSpec = 15, 
		RULE_ignoreSpec = 16, RULE_mainSpec = 17, RULE_compilationUnit = 18;
	public static final String[] ruleNames = {
		"dotSpec", "anyKeywordSpec", "textSpec", "expectedCarriageReturnSpec", 
		"expectedLineForwardSpec", "expectedLineBreakSpec", "whitespaceBeforeKeywordSpec", 
		"whitespaceOrLineBreakSpec", "codeSpec", "lineBreakMaybeCodeSpec", "potentialConflictSpec", 
		"signMaybeWhitespaceSpec", "signConflictSpec", "whitespaceSpec", "spacedDotSpec", 
		"moreConflictSpec", "ignoreSpec", "mainSpec", "compilationUnit"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'Success'", "'Level'", "'Job'", "'Condition'", "'Class'", "'When'", 
		"'Gives'", "'Improves'", "'Increases'", "'Recover'", "'Restores'", "'Fully'", 
		"'Can'", "'Speed'", "'Meso'", "'Accuracy'", "'Avoidability'", "'Evasion'", 
		"'Protection'", "'Double'", "'Item'", "'Jump'", "'Attack'", "'Defense'", 
		"'Weapon'", "'Magic'", "'Def'", "'If'", "'The'", null, "'#c'", "'#'", 
		null, null, null, "'\\'", "'r'", "'n'", "'c'", "'+'", "'-'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "KEYWORD_SUCCESS", "KEYWORD_LEVEL", "KEYWORD_JOB", "KEYWORD_CONDITION", 
		"KEYWORD_CLASS", "KEYWORD_WHEN", "KEYWORD_GIVES", "KEYWORD_IMPROVES", 
		"KEYWORD_INCREASES", "KEYWORD_RECOVER", "KEYWORD_RESTORES", "KEYWORD_FULLY", 
		"KEYWORD_CAN", "KEYWORD_SPEED", "KEYWORD_MESO", "KEYWORD_ACCURACY", "KEYWORD_AVOIDABILITY", 
		"KEYWORD_EVASION", "KEYWORD_PROTECTION", "KEYWORD_DOUBLE", "KEYWORD_ITEM", 
		"KEYWORD_JUMP", "KEYWORD_ATTACK", "KEYWORD_DEFENSE", "KEYWORD_WEAPON", 
		"KEYWORD_MAGIC", "KEYWORD_DEF", "KEYWORD_IF", "KEYWORD_THE", "NUMBER", 
		"CODE_C", "CODE", "SIGN", "MARK", "WS", "TARGET_BACKSLASH", "TARGET_R", 
		"TARGET_N", "TARGET_C", "TARGET_PLUS", "TARGET_MINUS", "ANY_CHARACTER"
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
	public String getGrammarFileName() { return "DescriptionPatchParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DescriptionPatchParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class DotSpecContext extends ParserRuleContext {
		public TerminalNode SIGN() { return getToken(DescriptionPatchParser.SIGN, 0); }
		public TerminalNode MARK() { return getToken(DescriptionPatchParser.MARK, 0); }
		public DotSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dotSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterDotSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitDotSpec(this);
		}
	}

	public final DotSpecContext dotSpec() throws RecognitionException {
		DotSpecContext _localctx = new DotSpecContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_dotSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			_la = _input.LA(1);
			if ( !(_la==SIGN || _la==MARK) ) {
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

	public static class AnyKeywordSpecContext extends ParserRuleContext {
		public TerminalNode KEYWORD_SUCCESS() { return getToken(DescriptionPatchParser.KEYWORD_SUCCESS, 0); }
		public TerminalNode KEYWORD_LEVEL() { return getToken(DescriptionPatchParser.KEYWORD_LEVEL, 0); }
		public TerminalNode KEYWORD_JOB() { return getToken(DescriptionPatchParser.KEYWORD_JOB, 0); }
		public TerminalNode KEYWORD_CONDITION() { return getToken(DescriptionPatchParser.KEYWORD_CONDITION, 0); }
		public TerminalNode KEYWORD_CLASS() { return getToken(DescriptionPatchParser.KEYWORD_CLASS, 0); }
		public TerminalNode KEYWORD_WHEN() { return getToken(DescriptionPatchParser.KEYWORD_WHEN, 0); }
		public TerminalNode KEYWORD_GIVES() { return getToken(DescriptionPatchParser.KEYWORD_GIVES, 0); }
		public TerminalNode KEYWORD_IMPROVES() { return getToken(DescriptionPatchParser.KEYWORD_IMPROVES, 0); }
		public TerminalNode KEYWORD_INCREASES() { return getToken(DescriptionPatchParser.KEYWORD_INCREASES, 0); }
		public TerminalNode KEYWORD_RECOVER() { return getToken(DescriptionPatchParser.KEYWORD_RECOVER, 0); }
		public TerminalNode KEYWORD_RESTORES() { return getToken(DescriptionPatchParser.KEYWORD_RESTORES, 0); }
		public TerminalNode KEYWORD_FULLY() { return getToken(DescriptionPatchParser.KEYWORD_FULLY, 0); }
		public TerminalNode KEYWORD_CAN() { return getToken(DescriptionPatchParser.KEYWORD_CAN, 0); }
		public TerminalNode KEYWORD_SPEED() { return getToken(DescriptionPatchParser.KEYWORD_SPEED, 0); }
		public TerminalNode KEYWORD_MESO() { return getToken(DescriptionPatchParser.KEYWORD_MESO, 0); }
		public TerminalNode KEYWORD_ACCURACY() { return getToken(DescriptionPatchParser.KEYWORD_ACCURACY, 0); }
		public TerminalNode KEYWORD_AVOIDABILITY() { return getToken(DescriptionPatchParser.KEYWORD_AVOIDABILITY, 0); }
		public TerminalNode KEYWORD_EVASION() { return getToken(DescriptionPatchParser.KEYWORD_EVASION, 0); }
		public TerminalNode KEYWORD_PROTECTION() { return getToken(DescriptionPatchParser.KEYWORD_PROTECTION, 0); }
		public TerminalNode KEYWORD_DOUBLE() { return getToken(DescriptionPatchParser.KEYWORD_DOUBLE, 0); }
		public TerminalNode KEYWORD_ITEM() { return getToken(DescriptionPatchParser.KEYWORD_ITEM, 0); }
		public TerminalNode KEYWORD_JUMP() { return getToken(DescriptionPatchParser.KEYWORD_JUMP, 0); }
		public TerminalNode KEYWORD_ATTACK() { return getToken(DescriptionPatchParser.KEYWORD_ATTACK, 0); }
		public TerminalNode KEYWORD_DEFENSE() { return getToken(DescriptionPatchParser.KEYWORD_DEFENSE, 0); }
		public TerminalNode KEYWORD_WEAPON() { return getToken(DescriptionPatchParser.KEYWORD_WEAPON, 0); }
		public TerminalNode KEYWORD_MAGIC() { return getToken(DescriptionPatchParser.KEYWORD_MAGIC, 0); }
		public TerminalNode KEYWORD_DEF() { return getToken(DescriptionPatchParser.KEYWORD_DEF, 0); }
		public TerminalNode KEYWORD_IF() { return getToken(DescriptionPatchParser.KEYWORD_IF, 0); }
		public TerminalNode KEYWORD_THE() { return getToken(DescriptionPatchParser.KEYWORD_THE, 0); }
		public TerminalNode NUMBER() { return getToken(DescriptionPatchParser.NUMBER, 0); }
		public TerminalNode CODE_C() { return getToken(DescriptionPatchParser.CODE_C, 0); }
		public AnyKeywordSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_anyKeywordSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterAnyKeywordSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitAnyKeywordSpec(this);
		}
	}

	public final AnyKeywordSpecContext anyKeywordSpec() throws RecognitionException {
		AnyKeywordSpecContext _localctx = new AnyKeywordSpecContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_anyKeywordSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KEYWORD_SUCCESS) | (1L << KEYWORD_LEVEL) | (1L << KEYWORD_JOB) | (1L << KEYWORD_CONDITION) | (1L << KEYWORD_CLASS) | (1L << KEYWORD_WHEN) | (1L << KEYWORD_GIVES) | (1L << KEYWORD_IMPROVES) | (1L << KEYWORD_INCREASES) | (1L << KEYWORD_RECOVER) | (1L << KEYWORD_RESTORES) | (1L << KEYWORD_FULLY) | (1L << KEYWORD_CAN) | (1L << KEYWORD_SPEED) | (1L << KEYWORD_MESO) | (1L << KEYWORD_ACCURACY) | (1L << KEYWORD_AVOIDABILITY) | (1L << KEYWORD_EVASION) | (1L << KEYWORD_PROTECTION) | (1L << KEYWORD_DOUBLE) | (1L << KEYWORD_ITEM) | (1L << KEYWORD_JUMP) | (1L << KEYWORD_ATTACK) | (1L << KEYWORD_DEFENSE) | (1L << KEYWORD_WEAPON) | (1L << KEYWORD_MAGIC) | (1L << KEYWORD_DEF) | (1L << KEYWORD_IF) | (1L << KEYWORD_THE) | (1L << NUMBER) | (1L << CODE_C))) != 0)) ) {
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

	public static class TextSpecContext extends ParserRuleContext {
		public AnyKeywordSpecContext anyKeywordSpec() {
			return getRuleContext(AnyKeywordSpecContext.class,0);
		}
		public TerminalNode ANY_CHARACTER() { return getToken(DescriptionPatchParser.ANY_CHARACTER, 0); }
		public TerminalNode TARGET_R() { return getToken(DescriptionPatchParser.TARGET_R, 0); }
		public TerminalNode TARGET_N() { return getToken(DescriptionPatchParser.TARGET_N, 0); }
		public TerminalNode TARGET_C() { return getToken(DescriptionPatchParser.TARGET_C, 0); }
		public TextSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_textSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterTextSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitTextSpec(this);
		}
	}

	public final TextSpecContext textSpec() throws RecognitionException {
		TextSpecContext _localctx = new TextSpecContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_textSpec);
		try {
			setState(47);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEYWORD_SUCCESS:
			case KEYWORD_LEVEL:
			case KEYWORD_JOB:
			case KEYWORD_CONDITION:
			case KEYWORD_CLASS:
			case KEYWORD_WHEN:
			case KEYWORD_GIVES:
			case KEYWORD_IMPROVES:
			case KEYWORD_INCREASES:
			case KEYWORD_RECOVER:
			case KEYWORD_RESTORES:
			case KEYWORD_FULLY:
			case KEYWORD_CAN:
			case KEYWORD_SPEED:
			case KEYWORD_MESO:
			case KEYWORD_ACCURACY:
			case KEYWORD_AVOIDABILITY:
			case KEYWORD_EVASION:
			case KEYWORD_PROTECTION:
			case KEYWORD_DOUBLE:
			case KEYWORD_ITEM:
			case KEYWORD_JUMP:
			case KEYWORD_ATTACK:
			case KEYWORD_DEFENSE:
			case KEYWORD_WEAPON:
			case KEYWORD_MAGIC:
			case KEYWORD_DEF:
			case KEYWORD_IF:
			case KEYWORD_THE:
			case NUMBER:
			case CODE_C:
				enterOuterAlt(_localctx, 1);
				{
				setState(42);
				anyKeywordSpec();
				}
				break;
			case ANY_CHARACTER:
				enterOuterAlt(_localctx, 2);
				{
				setState(43);
				match(ANY_CHARACTER);
				}
				break;
			case TARGET_R:
				enterOuterAlt(_localctx, 3);
				{
				setState(44);
				match(TARGET_R);
				}
				break;
			case TARGET_N:
				enterOuterAlt(_localctx, 4);
				{
				setState(45);
				match(TARGET_N);
				}
				break;
			case TARGET_C:
				enterOuterAlt(_localctx, 5);
				{
				setState(46);
				match(TARGET_C);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class ExpectedCarriageReturnSpecContext extends ParserRuleContext {
		public TerminalNode TARGET_R() { return getToken(DescriptionPatchParser.TARGET_R, 0); }
		public TerminalNode TARGET_BACKSLASH() { return getToken(DescriptionPatchParser.TARGET_BACKSLASH, 0); }
		public ExpectedCarriageReturnSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expectedCarriageReturnSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterExpectedCarriageReturnSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitExpectedCarriageReturnSpec(this);
		}
	}

	public final ExpectedCarriageReturnSpecContext expectedCarriageReturnSpec() throws RecognitionException {
		ExpectedCarriageReturnSpecContext _localctx = new ExpectedCarriageReturnSpecContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_expectedCarriageReturnSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(50);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TARGET_BACKSLASH) {
				{
				setState(49);
				match(TARGET_BACKSLASH);
				}
			}

			setState(52);
			match(TARGET_R);
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

	public static class ExpectedLineForwardSpecContext extends ParserRuleContext {
		public TerminalNode TARGET_N() { return getToken(DescriptionPatchParser.TARGET_N, 0); }
		public TerminalNode TARGET_BACKSLASH() { return getToken(DescriptionPatchParser.TARGET_BACKSLASH, 0); }
		public ExpectedLineForwardSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expectedLineForwardSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterExpectedLineForwardSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitExpectedLineForwardSpec(this);
		}
	}

	public final ExpectedLineForwardSpecContext expectedLineForwardSpec() throws RecognitionException {
		ExpectedLineForwardSpecContext _localctx = new ExpectedLineForwardSpecContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_expectedLineForwardSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TARGET_BACKSLASH) {
				{
				setState(54);
				match(TARGET_BACKSLASH);
				}
			}

			setState(57);
			match(TARGET_N);
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

	public static class ExpectedLineBreakSpecContext extends ParserRuleContext {
		public ExpectedLineForwardSpecContext expectedLineForwardSpec() {
			return getRuleContext(ExpectedLineForwardSpecContext.class,0);
		}
		public ExpectedCarriageReturnSpecContext expectedCarriageReturnSpec() {
			return getRuleContext(ExpectedCarriageReturnSpecContext.class,0);
		}
		public ExpectedLineBreakSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expectedLineBreakSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterExpectedLineBreakSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitExpectedLineBreakSpec(this);
		}
	}

	public final ExpectedLineBreakSpecContext expectedLineBreakSpec() throws RecognitionException {
		ExpectedLineBreakSpecContext _localctx = new ExpectedLineBreakSpecContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_expectedLineBreakSpec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(59);
				expectedCarriageReturnSpec();
				}
				break;
			}
			setState(62);
			expectedLineForwardSpec();
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

	public static class WhitespaceBeforeKeywordSpecContext extends ParserRuleContext {
		public List<TerminalNode> WS() { return getTokens(DescriptionPatchParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(DescriptionPatchParser.WS, i);
		}
		public WhitespaceBeforeKeywordSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whitespaceBeforeKeywordSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterWhitespaceBeforeKeywordSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitWhitespaceBeforeKeywordSpec(this);
		}
	}

	public final WhitespaceBeforeKeywordSpecContext whitespaceBeforeKeywordSpec() throws RecognitionException {
		WhitespaceBeforeKeywordSpecContext _localctx = new WhitespaceBeforeKeywordSpecContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_whitespaceBeforeKeywordSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(64);
				match(WS);
				}
				}
				setState(67); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WS );
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

	public static class WhitespaceOrLineBreakSpecContext extends ParserRuleContext {
		public ExpectedLineBreakSpecContext expectedLineBreakSpec() {
			return getRuleContext(ExpectedLineBreakSpecContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(DescriptionPatchParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(DescriptionPatchParser.WS, i);
		}
		public WhitespaceOrLineBreakSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whitespaceOrLineBreakSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterWhitespaceOrLineBreakSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitWhitespaceOrLineBreakSpec(this);
		}
	}

	public final WhitespaceOrLineBreakSpecContext whitespaceOrLineBreakSpec() throws RecognitionException {
		WhitespaceOrLineBreakSpecContext _localctx = new WhitespaceOrLineBreakSpecContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_whitespaceOrLineBreakSpec);
		try {
			int _alt;
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TARGET_BACKSLASH:
			case TARGET_R:
			case TARGET_N:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				expectedLineBreakSpec();
				}
				break;
			case WS:
				enterOuterAlt(_localctx, 2);
				{
				setState(71); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(70);
						match(WS);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(73); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class CodeSpecContext extends ParserRuleContext {
		public TerminalNode CODE_C() { return getToken(DescriptionPatchParser.CODE_C, 0); }
		public TerminalNode TARGET_C() { return getToken(DescriptionPatchParser.TARGET_C, 0); }
		public TerminalNode CODE() { return getToken(DescriptionPatchParser.CODE, 0); }
		public CodeSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_codeSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterCodeSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitCodeSpec(this);
		}
	}

	public final CodeSpecContext codeSpec() throws RecognitionException {
		CodeSpecContext _localctx = new CodeSpecContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_codeSpec);
		int _la;
		try {
			setState(83);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(CODE_C);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==CODE) {
					{
					setState(78);
					match(CODE);
					}
				}

				setState(81);
				match(TARGET_C);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(82);
				match(CODE);
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

	public static class LineBreakMaybeCodeSpecContext extends ParserRuleContext {
		public ExpectedLineBreakSpecContext expectedLineBreakSpec() {
			return getRuleContext(ExpectedLineBreakSpecContext.class,0);
		}
		public CodeSpecContext codeSpec() {
			return getRuleContext(CodeSpecContext.class,0);
		}
		public LineBreakMaybeCodeSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineBreakMaybeCodeSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterLineBreakMaybeCodeSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitLineBreakMaybeCodeSpec(this);
		}
	}

	public final LineBreakMaybeCodeSpecContext lineBreakMaybeCodeSpec() throws RecognitionException {
		LineBreakMaybeCodeSpecContext _localctx = new LineBreakMaybeCodeSpecContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_lineBreakMaybeCodeSpec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			expectedLineBreakSpec();
			setState(87);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(86);
				codeSpec();
				}
				break;
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

	public static class PotentialConflictSpecContext extends ParserRuleContext {
		public TextSpecContext textSpec() {
			return getRuleContext(TextSpecContext.class,0);
		}
		public LineBreakMaybeCodeSpecContext lineBreakMaybeCodeSpec() {
			return getRuleContext(LineBreakMaybeCodeSpecContext.class,0);
		}
		public AnyKeywordSpecContext anyKeywordSpec() {
			return getRuleContext(AnyKeywordSpecContext.class,0);
		}
		public List<DotSpecContext> dotSpec() {
			return getRuleContexts(DotSpecContext.class);
		}
		public DotSpecContext dotSpec(int i) {
			return getRuleContext(DotSpecContext.class,i);
		}
		public List<WhitespaceOrLineBreakSpecContext> whitespaceOrLineBreakSpec() {
			return getRuleContexts(WhitespaceOrLineBreakSpecContext.class);
		}
		public WhitespaceOrLineBreakSpecContext whitespaceOrLineBreakSpec(int i) {
			return getRuleContext(WhitespaceOrLineBreakSpecContext.class,i);
		}
		public WhitespaceBeforeKeywordSpecContext whitespaceBeforeKeywordSpec() {
			return getRuleContext(WhitespaceBeforeKeywordSpecContext.class,0);
		}
		public PotentialConflictSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_potentialConflictSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterPotentialConflictSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitPotentialConflictSpec(this);
		}
	}

	public final PotentialConflictSpecContext potentialConflictSpec() throws RecognitionException {
		PotentialConflictSpecContext _localctx = new PotentialConflictSpecContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_potentialConflictSpec);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			textSpec();
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SIGN || _la==MARK) {
				{
				{
				setState(90);
				dotSpec();
				}
				}
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(99);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(96);
					whitespaceOrLineBreakSpec();
					}
					} 
				}
				setState(101);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			setState(102);
			lineBreakMaybeCodeSpec();
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(103);
				whitespaceBeforeKeywordSpec();
				}
			}

			setState(106);
			anyKeywordSpec();
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

	public static class SignMaybeWhitespaceSpecContext extends ParserRuleContext {
		public List<TerminalNode> SIGN() { return getTokens(DescriptionPatchParser.SIGN); }
		public TerminalNode SIGN(int i) {
			return getToken(DescriptionPatchParser.SIGN, i);
		}
		public List<TerminalNode> WS() { return getTokens(DescriptionPatchParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(DescriptionPatchParser.WS, i);
		}
		public SignMaybeWhitespaceSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signMaybeWhitespaceSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterSignMaybeWhitespaceSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitSignMaybeWhitespaceSpec(this);
		}
	}

	public final SignMaybeWhitespaceSpecContext signMaybeWhitespaceSpec() throws RecognitionException {
		SignMaybeWhitespaceSpecContext _localctx = new SignMaybeWhitespaceSpecContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_signMaybeWhitespaceSpec);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(SIGN);
			setState(112);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(109);
					_la = _input.LA(1);
					if ( !(_la==SIGN || _la==WS) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					} 
				}
				setState(114);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
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

	public static class SignConflictSpecContext extends ParserRuleContext {
		public TextSpecContext textSpec() {
			return getRuleContext(TextSpecContext.class,0);
		}
		public SignMaybeWhitespaceSpecContext signMaybeWhitespaceSpec() {
			return getRuleContext(SignMaybeWhitespaceSpecContext.class,0);
		}
		public AnyKeywordSpecContext anyKeywordSpec() {
			return getRuleContext(AnyKeywordSpecContext.class,0);
		}
		public List<WhitespaceOrLineBreakSpecContext> whitespaceOrLineBreakSpec() {
			return getRuleContexts(WhitespaceOrLineBreakSpecContext.class);
		}
		public WhitespaceOrLineBreakSpecContext whitespaceOrLineBreakSpec(int i) {
			return getRuleContext(WhitespaceOrLineBreakSpecContext.class,i);
		}
		public SignConflictSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signConflictSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterSignConflictSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitSignConflictSpec(this);
		}
	}

	public final SignConflictSpecContext signConflictSpec() throws RecognitionException {
		SignConflictSpecContext _localctx = new SignConflictSpecContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_signConflictSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			textSpec();
			setState(116);
			signMaybeWhitespaceSpec();
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << WS) | (1L << TARGET_BACKSLASH) | (1L << TARGET_R) | (1L << TARGET_N))) != 0)) {
				{
				{
				setState(117);
				whitespaceOrLineBreakSpec();
				}
				}
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(123);
			anyKeywordSpec();
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

	public static class WhitespaceSpecContext extends ParserRuleContext {
		public List<TerminalNode> WS() { return getTokens(DescriptionPatchParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(DescriptionPatchParser.WS, i);
		}
		public WhitespaceSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whitespaceSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterWhitespaceSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitWhitespaceSpec(this);
		}
	}

	public final WhitespaceSpecContext whitespaceSpec() throws RecognitionException {
		WhitespaceSpecContext _localctx = new WhitespaceSpecContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_whitespaceSpec);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(126); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(125);
					match(WS);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(128); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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

	public static class SpacedDotSpecContext extends ParserRuleContext {
		public WhitespaceSpecContext whitespaceSpec() {
			return getRuleContext(WhitespaceSpecContext.class,0);
		}
		public DotSpecContext dotSpec() {
			return getRuleContext(DotSpecContext.class,0);
		}
		public SpacedDotSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_spacedDotSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterSpacedDotSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitSpacedDotSpec(this);
		}
	}

	public final SpacedDotSpecContext spacedDotSpec() throws RecognitionException {
		SpacedDotSpecContext _localctx = new SpacedDotSpecContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_spacedDotSpec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			whitespaceSpec();
			setState(131);
			dotSpec();
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

	public static class MoreConflictSpecContext extends ParserRuleContext {
		public TerminalNode WS() { return getToken(DescriptionPatchParser.WS, 0); }
		public List<WhitespaceSpecContext> whitespaceSpec() {
			return getRuleContexts(WhitespaceSpecContext.class);
		}
		public WhitespaceSpecContext whitespaceSpec(int i) {
			return getRuleContext(WhitespaceSpecContext.class,i);
		}
		public TerminalNode NUMBER() { return getToken(DescriptionPatchParser.NUMBER, 0); }
		public TerminalNode TARGET_MINUS() { return getToken(DescriptionPatchParser.TARGET_MINUS, 0); }
		public TerminalNode TARGET_PLUS() { return getToken(DescriptionPatchParser.TARGET_PLUS, 0); }
		public List<DotSpecContext> dotSpec() {
			return getRuleContexts(DotSpecContext.class);
		}
		public DotSpecContext dotSpec(int i) {
			return getRuleContext(DotSpecContext.class,i);
		}
		public SpacedDotSpecContext spacedDotSpec() {
			return getRuleContext(SpacedDotSpecContext.class,0);
		}
		public MoreConflictSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_moreConflictSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterMoreConflictSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitMoreConflictSpec(this);
		}
	}

	public final MoreConflictSpecContext moreConflictSpec() throws RecognitionException {
		MoreConflictSpecContext _localctx = new MoreConflictSpecContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_moreConflictSpec);
		int _la;
		try {
			int _alt;
			setState(163);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				match(WS);
				setState(134);
				whitespaceSpec();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(136);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SIGN || _la==MARK) {
					{
					setState(135);
					dotSpec();
					}
				}

				setState(138);
				_la = _input.LA(1);
				if ( !(_la==TARGET_PLUS || _la==TARGET_MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(139);
				whitespaceSpec();
				setState(140);
				match(NUMBER);
				setState(142);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
				case 1:
					{
					setState(141);
					spacedDotSpec();
					}
					break;
				}
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(144);
				dotSpec();
				setState(145);
				_la = _input.LA(1);
				if ( !(_la==TARGET_PLUS || _la==TARGET_MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(147);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(146);
					whitespaceSpec();
					}
				}

				setState(149);
				match(NUMBER);
				setState(151);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
				case 1:
					{
					setState(150);
					spacedDotSpec();
					}
					break;
				}
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(153);
				dotSpec();
				setState(158);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						setState(156);
						_errHandler.sync(this);
						switch (_input.LA(1)) {
						case WS:
							{
							setState(154);
							whitespaceSpec();
							}
							break;
						case SIGN:
						case MARK:
							{
							setState(155);
							dotSpec();
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						} 
					}
					setState(160);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
				}
				setState(161);
				dotSpec();
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

	public static class IgnoreSpecContext extends ParserRuleContext {
		public IgnoreSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ignoreSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterIgnoreSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitIgnoreSpec(this);
		}
	}

	public final IgnoreSpecContext ignoreSpec() throws RecognitionException {
		IgnoreSpecContext _localctx = new IgnoreSpecContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_ignoreSpec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
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
		public PotentialConflictSpecContext potentialConflictSpec() {
			return getRuleContext(PotentialConflictSpecContext.class,0);
		}
		public SignConflictSpecContext signConflictSpec() {
			return getRuleContext(SignConflictSpecContext.class,0);
		}
		public MoreConflictSpecContext moreConflictSpec() {
			return getRuleContext(MoreConflictSpecContext.class,0);
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
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterMainSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitMainSpec(this);
		}
	}

	public final MainSpecContext mainSpec() throws RecognitionException {
		MainSpecContext _localctx = new MainSpecContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_mainSpec);
		try {
			setState(171);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				potentialConflictSpec();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(168);
				signConflictSpec();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(169);
				moreConflictSpec();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(170);
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
		public TerminalNode EOF() { return getToken(DescriptionPatchParser.EOF, 0); }
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
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).enterCompilationUnit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DescriptionPatchParserListener ) ((DescriptionPatchParserListener)listener).exitCompilationUnit(this);
		}
	}

	public final CompilationUnitContext compilationUnit() throws RecognitionException {
		CompilationUnitContext _localctx = new CompilationUnitContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_compilationUnit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KEYWORD_SUCCESS) | (1L << KEYWORD_LEVEL) | (1L << KEYWORD_JOB) | (1L << KEYWORD_CONDITION) | (1L << KEYWORD_CLASS) | (1L << KEYWORD_WHEN) | (1L << KEYWORD_GIVES) | (1L << KEYWORD_IMPROVES) | (1L << KEYWORD_INCREASES) | (1L << KEYWORD_RECOVER) | (1L << KEYWORD_RESTORES) | (1L << KEYWORD_FULLY) | (1L << KEYWORD_CAN) | (1L << KEYWORD_SPEED) | (1L << KEYWORD_MESO) | (1L << KEYWORD_ACCURACY) | (1L << KEYWORD_AVOIDABILITY) | (1L << KEYWORD_EVASION) | (1L << KEYWORD_PROTECTION) | (1L << KEYWORD_DOUBLE) | (1L << KEYWORD_ITEM) | (1L << KEYWORD_JUMP) | (1L << KEYWORD_ATTACK) | (1L << KEYWORD_DEFENSE) | (1L << KEYWORD_WEAPON) | (1L << KEYWORD_MAGIC) | (1L << KEYWORD_DEF) | (1L << KEYWORD_IF) | (1L << KEYWORD_THE) | (1L << NUMBER) | (1L << CODE_C) | (1L << CODE) | (1L << SIGN) | (1L << MARK) | (1L << WS) | (1L << TARGET_BACKSLASH) | (1L << TARGET_R) | (1L << TARGET_N) | (1L << TARGET_C) | (1L << TARGET_PLUS) | (1L << TARGET_MINUS) | (1L << ANY_CHARACTER))) != 0)) {
				{
				{
				setState(173);
				mainSpec();
				}
				}
				setState(178);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(179);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u00b8\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\62\n\4\3"+
		"\5\5\5\65\n\5\3\5\3\5\3\6\5\6:\n\6\3\6\3\6\3\7\5\7?\n\7\3\7\3\7\3\b\6"+
		"\bD\n\b\r\b\16\bE\3\t\3\t\6\tJ\n\t\r\t\16\tK\5\tN\n\t\3\n\3\n\5\nR\n\n"+
		"\3\n\3\n\5\nV\n\n\3\13\3\13\5\13Z\n\13\3\f\3\f\7\f^\n\f\f\f\16\fa\13\f"+
		"\3\f\7\fd\n\f\f\f\16\fg\13\f\3\f\3\f\5\fk\n\f\3\f\3\f\3\r\3\r\7\rq\n\r"+
		"\f\r\16\rt\13\r\3\16\3\16\3\16\7\16y\n\16\f\16\16\16|\13\16\3\16\3\16"+
		"\3\17\6\17\u0081\n\17\r\17\16\17\u0082\3\20\3\20\3\20\3\21\3\21\3\21\5"+
		"\21\u008b\n\21\3\21\3\21\3\21\3\21\5\21\u0091\n\21\3\21\3\21\3\21\5\21"+
		"\u0096\n\21\3\21\3\21\5\21\u009a\n\21\3\21\3\21\3\21\7\21\u009f\n\21\f"+
		"\21\16\21\u00a2\13\21\3\21\3\21\5\21\u00a6\n\21\3\22\3\22\3\23\3\23\3"+
		"\23\3\23\5\23\u00ae\n\23\3\24\7\24\u00b1\n\24\f\24\16\24\u00b4\13\24\3"+
		"\24\3\24\3\24\2\2\25\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&\2\6\3"+
		"\2#$\3\2\3!\4\2##%%\3\2*+\2\u00c5\2(\3\2\2\2\4*\3\2\2\2\6\61\3\2\2\2\b"+
		"\64\3\2\2\2\n9\3\2\2\2\f>\3\2\2\2\16C\3\2\2\2\20M\3\2\2\2\22U\3\2\2\2"+
		"\24W\3\2\2\2\26[\3\2\2\2\30n\3\2\2\2\32u\3\2\2\2\34\u0080\3\2\2\2\36\u0084"+
		"\3\2\2\2 \u00a5\3\2\2\2\"\u00a7\3\2\2\2$\u00ad\3\2\2\2&\u00b2\3\2\2\2"+
		"()\t\2\2\2)\3\3\2\2\2*+\t\3\2\2+\5\3\2\2\2,\62\5\4\3\2-\62\7,\2\2.\62"+
		"\7\'\2\2/\62\7(\2\2\60\62\7)\2\2\61,\3\2\2\2\61-\3\2\2\2\61.\3\2\2\2\61"+
		"/\3\2\2\2\61\60\3\2\2\2\62\7\3\2\2\2\63\65\7&\2\2\64\63\3\2\2\2\64\65"+
		"\3\2\2\2\65\66\3\2\2\2\66\67\7\'\2\2\67\t\3\2\2\28:\7&\2\298\3\2\2\29"+
		":\3\2\2\2:;\3\2\2\2;<\7(\2\2<\13\3\2\2\2=?\5\b\5\2>=\3\2\2\2>?\3\2\2\2"+
		"?@\3\2\2\2@A\5\n\6\2A\r\3\2\2\2BD\7%\2\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2"+
		"EF\3\2\2\2F\17\3\2\2\2GN\5\f\7\2HJ\7%\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2"+
		"\2KL\3\2\2\2LN\3\2\2\2MG\3\2\2\2MI\3\2\2\2N\21\3\2\2\2OV\7!\2\2PR\7\""+
		"\2\2QP\3\2\2\2QR\3\2\2\2RS\3\2\2\2SV\7)\2\2TV\7\"\2\2UO\3\2\2\2UQ\3\2"+
		"\2\2UT\3\2\2\2V\23\3\2\2\2WY\5\f\7\2XZ\5\22\n\2YX\3\2\2\2YZ\3\2\2\2Z\25"+
		"\3\2\2\2[_\5\6\4\2\\^\5\2\2\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2"+
		"`e\3\2\2\2a_\3\2\2\2bd\5\20\t\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2"+
		"\2fh\3\2\2\2ge\3\2\2\2hj\5\24\13\2ik\5\16\b\2ji\3\2\2\2jk\3\2\2\2kl\3"+
		"\2\2\2lm\5\4\3\2m\27\3\2\2\2nr\7#\2\2oq\t\4\2\2po\3\2\2\2qt\3\2\2\2rp"+
		"\3\2\2\2rs\3\2\2\2s\31\3\2\2\2tr\3\2\2\2uv\5\6\4\2vz\5\30\r\2wy\5\20\t"+
		"\2xw\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{}\3\2\2\2|z\3\2\2\2}~\5\4\3"+
		"\2~\33\3\2\2\2\177\u0081\7%\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2"+
		"\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\35\3\2\2\2\u0084\u0085"+
		"\5\34\17\2\u0085\u0086\5\2\2\2\u0086\37\3\2\2\2\u0087\u0088\7%\2\2\u0088"+
		"\u00a6\5\34\17\2\u0089\u008b\5\2\2\2\u008a\u0089\3\2\2\2\u008a\u008b\3"+
		"\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\t\5\2\2\u008d\u008e\5\34\17\2\u008e"+
		"\u0090\7 \2\2\u008f\u0091\5\36\20\2\u0090\u008f\3\2\2\2\u0090\u0091\3"+
		"\2\2\2\u0091\u00a6\3\2\2\2\u0092\u0093\5\2\2\2\u0093\u0095\t\5\2\2\u0094"+
		"\u0096\5\34\17\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\3"+
		"\2\2\2\u0097\u0099\7 \2\2\u0098\u009a\5\36\20\2\u0099\u0098\3\2\2\2\u0099"+
		"\u009a\3\2\2\2\u009a\u00a6\3\2\2\2\u009b\u00a0\5\2\2\2\u009c\u009f\5\34"+
		"\17\2\u009d\u009f\5\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f"+
		"\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3\2"+
		"\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\5\2\2\2\u00a4\u00a6\3\2\2\2\u00a5"+
		"\u0087\3\2\2\2\u00a5\u008a\3\2\2\2\u00a5\u0092\3\2\2\2\u00a5\u009b\3\2"+
		"\2\2\u00a6!\3\2\2\2\u00a7\u00a8\13\2\2\2\u00a8#\3\2\2\2\u00a9\u00ae\5"+
		"\26\f\2\u00aa\u00ae\5\32\16\2\u00ab\u00ae\5 \21\2\u00ac\u00ae\5\"\22\2"+
		"\u00ad\u00a9\3\2\2\2\u00ad\u00aa\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac"+
		"\3\2\2\2\u00ae%\3\2\2\2\u00af\u00b1\5$\23\2\u00b0\u00af\3\2\2\2\u00b1"+
		"\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b5\3\2"+
		"\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b6\7\2\2\3\u00b6\'\3\2\2\2\33\61\64"+
		"9>EKMQUY_ejrz\u0082\u008a\u0090\u0095\u0099\u009e\u00a0\u00a5\u00ad\u00b2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}