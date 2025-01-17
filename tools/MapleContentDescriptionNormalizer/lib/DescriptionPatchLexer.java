// Generated from rules/DescriptionPatchLexer.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DescriptionPatchLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"KEYWORD_SUCCESS", "KEYWORD_LEVEL", "KEYWORD_JOB", "KEYWORD_CONDITION", 
		"KEYWORD_CLASS", "KEYWORD_WHEN", "KEYWORD_GIVES", "KEYWORD_IMPROVES", 
		"KEYWORD_INCREASES", "KEYWORD_RECOVER", "KEYWORD_RESTORES", "KEYWORD_FULLY", 
		"KEYWORD_CAN", "KEYWORD_SPEED", "KEYWORD_MESO", "KEYWORD_ACCURACY", "KEYWORD_AVOIDABILITY", 
		"KEYWORD_EVASION", "KEYWORD_PROTECTION", "KEYWORD_DOUBLE", "KEYWORD_ITEM", 
		"KEYWORD_JUMP", "KEYWORD_ATTACK", "KEYWORD_DEFENSE", "KEYWORD_WEAPON", 
		"KEYWORD_MAGIC", "KEYWORD_DEF", "KEYWORD_IF", "KEYWORD_THE", "NUMBER", 
		"CODE_C", "CODE", "SIGN", "MARK", "WS", "TARGET_BACKSLASH", "TARGET_R", 
		"TARGET_N", "TARGET_C", "TARGET_PLUS", "TARGET_MINUS", "ANY_CHARACTER"
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


	public DescriptionPatchLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "DescriptionPatchLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,\u013c\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3"+
		"\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20"+
		"\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27"+
		"\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36"+
		"\3\36\3\37\6\37\u0120\n\37\r\37\16\37\u0121\3 \3 \3 \3!\3!\3\"\3\"\3#"+
		"\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\2\2,\3\3\5\4\7\5"+
		"\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G"+
		"%I&K\'M(O)Q*S+U,\3\2\6\3\2\62;\5\2##\60\60AA\3\2<=\5\2\13\13\16\17\"\""+
		"\2\u013c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2"+
		"\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27"+
		"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2"+
		"\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2"+
		"\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2"+
		"\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2"+
		"\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S"+
		"\3\2\2\2\2U\3\2\2\2\3W\3\2\2\2\5_\3\2\2\2\7e\3\2\2\2\ti\3\2\2\2\13s\3"+
		"\2\2\2\ry\3\2\2\2\17~\3\2\2\2\21\u0084\3\2\2\2\23\u008d\3\2\2\2\25\u0097"+
		"\3\2\2\2\27\u009f\3\2\2\2\31\u00a8\3\2\2\2\33\u00ae\3\2\2\2\35\u00b2\3"+
		"\2\2\2\37\u00b8\3\2\2\2!\u00bd\3\2\2\2#\u00c6\3\2\2\2%\u00d3\3\2\2\2\'"+
		"\u00db\3\2\2\2)\u00e6\3\2\2\2+\u00ed\3\2\2\2-\u00f2\3\2\2\2/\u00f7\3\2"+
		"\2\2\61\u00fe\3\2\2\2\63\u0106\3\2\2\2\65\u010d\3\2\2\2\67\u0113\3\2\2"+
		"\29\u0117\3\2\2\2;\u011a\3\2\2\2=\u011f\3\2\2\2?\u0123\3\2\2\2A\u0126"+
		"\3\2\2\2C\u0128\3\2\2\2E\u012a\3\2\2\2G\u012c\3\2\2\2I\u012e\3\2\2\2K"+
		"\u0130\3\2\2\2M\u0132\3\2\2\2O\u0134\3\2\2\2Q\u0136\3\2\2\2S\u0138\3\2"+
		"\2\2U\u013a\3\2\2\2WX\7U\2\2XY\7w\2\2YZ\7e\2\2Z[\7e\2\2[\\\7g\2\2\\]\7"+
		"u\2\2]^\7u\2\2^\4\3\2\2\2_`\7N\2\2`a\7g\2\2ab\7x\2\2bc\7g\2\2cd\7n\2\2"+
		"d\6\3\2\2\2ef\7L\2\2fg\7q\2\2gh\7d\2\2h\b\3\2\2\2ij\7E\2\2jk\7q\2\2kl"+
		"\7p\2\2lm\7f\2\2mn\7k\2\2no\7v\2\2op\7k\2\2pq\7q\2\2qr\7p\2\2r\n\3\2\2"+
		"\2st\7E\2\2tu\7n\2\2uv\7c\2\2vw\7u\2\2wx\7u\2\2x\f\3\2\2\2yz\7Y\2\2z{"+
		"\7j\2\2{|\7g\2\2|}\7p\2\2}\16\3\2\2\2~\177\7I\2\2\177\u0080\7k\2\2\u0080"+
		"\u0081\7x\2\2\u0081\u0082\7g\2\2\u0082\u0083\7u\2\2\u0083\20\3\2\2\2\u0084"+
		"\u0085\7K\2\2\u0085\u0086\7o\2\2\u0086\u0087\7r\2\2\u0087\u0088\7t\2\2"+
		"\u0088\u0089\7q\2\2\u0089\u008a\7x\2\2\u008a\u008b\7g\2\2\u008b\u008c"+
		"\7u\2\2\u008c\22\3\2\2\2\u008d\u008e\7K\2\2\u008e\u008f\7p\2\2\u008f\u0090"+
		"\7e\2\2\u0090\u0091\7t\2\2\u0091\u0092\7g\2\2\u0092\u0093\7c\2\2\u0093"+
		"\u0094\7u\2\2\u0094\u0095\7g\2\2\u0095\u0096\7u\2\2\u0096\24\3\2\2\2\u0097"+
		"\u0098\7T\2\2\u0098\u0099\7g\2\2\u0099\u009a\7e\2\2\u009a\u009b\7q\2\2"+
		"\u009b\u009c\7x\2\2\u009c\u009d\7g\2\2\u009d\u009e\7t\2\2\u009e\26\3\2"+
		"\2\2\u009f\u00a0\7T\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7u\2\2\u00a2\u00a3"+
		"\7v\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7g\2\2\u00a6"+
		"\u00a7\7u\2\2\u00a7\30\3\2\2\2\u00a8\u00a9\7H\2\2\u00a9\u00aa\7w\2\2\u00aa"+
		"\u00ab\7n\2\2\u00ab\u00ac\7n\2\2\u00ac\u00ad\7{\2\2\u00ad\32\3\2\2\2\u00ae"+
		"\u00af\7E\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7p\2\2\u00b1\34\3\2\2\2\u00b2"+
		"\u00b3\7U\2\2\u00b3\u00b4\7r\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7g\2\2"+
		"\u00b6\u00b7\7f\2\2\u00b7\36\3\2\2\2\u00b8\u00b9\7O\2\2\u00b9\u00ba\7"+
		"g\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7q\2\2\u00bc \3\2\2\2\u00bd\u00be"+
		"\7C\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1\7w\2\2\u00c1"+
		"\u00c2\7t\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7{\2\2"+
		"\u00c5\"\3\2\2\2\u00c6\u00c7\7C\2\2\u00c7\u00c8\7x\2\2\u00c8\u00c9\7q"+
		"\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7f\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd"+
		"\7d\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7k\2\2\u00d0"+
		"\u00d1\7v\2\2\u00d1\u00d2\7{\2\2\u00d2$\3\2\2\2\u00d3\u00d4\7G\2\2\u00d4"+
		"\u00d5\7x\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d8\7k\2\2"+
		"\u00d8\u00d9\7q\2\2\u00d9\u00da\7p\2\2\u00da&\3\2\2\2\u00db\u00dc\7R\2"+
		"\2\u00dc\u00dd\7t\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7v\2\2\u00df\u00e0"+
		"\7g\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7k\2\2\u00e3"+
		"\u00e4\7q\2\2\u00e4\u00e5\7p\2\2\u00e5(\3\2\2\2\u00e6\u00e7\7F\2\2\u00e7"+
		"\u00e8\7q\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7d\2\2\u00ea\u00eb\7n\2\2"+
		"\u00eb\u00ec\7g\2\2\u00ec*\3\2\2\2\u00ed\u00ee\7K\2\2\u00ee\u00ef\7v\2"+
		"\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7o\2\2\u00f1,\3\2\2\2\u00f2\u00f3\7"+
		"L\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7o\2\2\u00f5\u00f6\7r\2\2\u00f6."+
		"\3\2\2\2\u00f7\u00f8\7C\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7v\2\2\u00fa"+
		"\u00fb\7c\2\2\u00fb\u00fc\7e\2\2\u00fc\u00fd\7m\2\2\u00fd\60\3\2\2\2\u00fe"+
		"\u00ff\7F\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7h\2\2\u0101\u0102\7g\2\2"+
		"\u0102\u0103\7p\2\2\u0103\u0104\7u\2\2\u0104\u0105\7g\2\2\u0105\62\3\2"+
		"\2\2\u0106\u0107\7Y\2\2\u0107\u0108\7g\2\2\u0108\u0109\7c\2\2\u0109\u010a"+
		"\7r\2\2\u010a\u010b\7q\2\2\u010b\u010c\7p\2\2\u010c\64\3\2\2\2\u010d\u010e"+
		"\7O\2\2\u010e\u010f\7c\2\2\u010f\u0110\7i\2\2\u0110\u0111\7k\2\2\u0111"+
		"\u0112\7e\2\2\u0112\66\3\2\2\2\u0113\u0114\7F\2\2\u0114\u0115\7g\2\2\u0115"+
		"\u0116\7h\2\2\u01168\3\2\2\2\u0117\u0118\7K\2\2\u0118\u0119\7h\2\2\u0119"+
		":\3\2\2\2\u011a\u011b\7V\2\2\u011b\u011c\7j\2\2\u011c\u011d\7g\2\2\u011d"+
		"<\3\2\2\2\u011e\u0120\t\2\2\2\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2\2"+
		"\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122>\3\2\2\2\u0123\u0124\7"+
		"%\2\2\u0124\u0125\7e\2\2\u0125@\3\2\2\2\u0126\u0127\7%\2\2\u0127B\3\2"+
		"\2\2\u0128\u0129\t\3\2\2\u0129D\3\2\2\2\u012a\u012b\t\4\2\2\u012bF\3\2"+
		"\2\2\u012c\u012d\t\5\2\2\u012dH\3\2\2\2\u012e\u012f\7^\2\2\u012fJ\3\2"+
		"\2\2\u0130\u0131\7t\2\2\u0131L\3\2\2\2\u0132\u0133\7p\2\2\u0133N\3\2\2"+
		"\2\u0134\u0135\7e\2\2\u0135P\3\2\2\2\u0136\u0137\7-\2\2\u0137R\3\2\2\2"+
		"\u0138\u0139\7/\2\2\u0139T\3\2\2\2\u013a\u013b\13\2\2\2\u013bV\3\2\2\2"+
		"\4\2\u0121\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}