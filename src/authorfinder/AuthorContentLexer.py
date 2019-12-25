# Generated from rules/AuthorContentLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u01b6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\bu\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\5\t\u009d\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\n\u00c5\n\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00e1\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00f9")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0113")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u0129\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\5\17\u0139\n\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0159\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u0173\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u018b\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0197\n\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\6\34\u01ac\n")
        buf.write("\34\r\34\16\34\u01ad\3\34\3\34\3\35\6\35\u01b3\n\35\r")
        buf.write("\35\16\35\u01b4\3\u01b4\2\36\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36\3\2\3\4\2\13\13\16\17\2\u01ce\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\3;\3\2\2\2\5D\3\2\2\2\7J\3\2\2\2\tL\3\2\2\2\13N\3\2\2")
        buf.write("\2\rP\3\2\2\2\17t\3\2\2\2\21\u009c\3\2\2\2\23\u00c4\3")
        buf.write("\2\2\2\25\u00e0\3\2\2\2\27\u00f8\3\2\2\2\31\u0112\3\2")
        buf.write("\2\2\33\u0128\3\2\2\2\35\u0138\3\2\2\2\37\u013a\3\2\2")
        buf.write("\2!\u0158\3\2\2\2#\u0172\3\2\2\2%\u018a\3\2\2\2\'\u0196")
        buf.write("\3\2\2\2)\u0198\3\2\2\2+\u019b\3\2\2\2-\u019e\3\2\2\2")
        buf.write("/\u01a1\3\2\2\2\61\u01a4\3\2\2\2\63\u01a6\3\2\2\2\65\u01a8")
        buf.write("\3\2\2\2\67\u01ab\3\2\2\29\u01b2\3\2\2\2;<\7f\2\2<=\7")
        buf.write("g\2\2=>\7x\2\2>?\7\"\2\2?@\7v\2\2@A\7g\2\2AB\7c\2\2BC")
        buf.write("\7o\2\2C\4\3\2\2\2DE\7\"\2\2EF\7h\2\2FG\7q\2\2GH\7t\2")
        buf.write("\2HI\7\"\2\2I\6\3\2\2\2JK\7(\2\2K\b\3\2\2\2LM\7.\2\2M")
        buf.write("\n\3\2\2\2NO\7*\2\2O\f\3\2\2\2PQ\7+\2\2Q\16\3\2\2\2RS")
        buf.write("\7B\2\2ST\7c\2\2TU\7w\2\2UV\7v\2\2VW\7j\2\2WX\7q\2\2X")
        buf.write("Y\7t\2\2YZ\7<\2\2Zu\7\"\2\2[\\\7B\2\2\\]\7C\2\2]^\7w\2")
        buf.write("\2^_\7v\2\2_`\7j\2\2`a\7q\2\2ab\7t\2\2bc\7<\2\2cu\7\"")
        buf.write("\2\2de\7c\2\2ef\7w\2\2fg\7v\2\2gh\7j\2\2hi\7q\2\2ij\7")
        buf.write("t\2\2jk\7<\2\2ku\7\"\2\2lm\7C\2\2mn\7w\2\2no\7v\2\2op")
        buf.write("\7j\2\2pq\7q\2\2qr\7t\2\2rs\7<\2\2su\7\"\2\2tR\3\2\2\2")
        buf.write("t[\3\2\2\2td\3\2\2\2tl\3\2\2\2u\20\3\2\2\2vw\7B\2\2wx")
        buf.write("\7c\2\2xy\7w\2\2yz\7v\2\2z{\7j\2\2{|\7q\2\2|}\7t\2\2}")
        buf.write("~\7\"\2\2~\177\7<\2\2\177\u009d\7\"\2\2\u0080\u0081\7")
        buf.write("B\2\2\u0081\u0082\7C\2\2\u0082\u0083\7w\2\2\u0083\u0084")
        buf.write("\7v\2\2\u0084\u0085\7j\2\2\u0085\u0086\7q\2\2\u0086\u0087")
        buf.write("\7t\2\2\u0087\u0088\7\"\2\2\u0088\u0089\7<\2\2\u0089\u009d")
        buf.write("\7\"\2\2\u008a\u008b\7c\2\2\u008b\u008c\7w\2\2\u008c\u008d")
        buf.write("\7v\2\2\u008d\u008e\7j\2\2\u008e\u008f\7q\2\2\u008f\u0090")
        buf.write("\7t\2\2\u0090\u0091\7\"\2\2\u0091\u0092\7<\2\2\u0092\u009d")
        buf.write("\7\"\2\2\u0093\u0094\7C\2\2\u0094\u0095\7w\2\2\u0095\u0096")
        buf.write("\7v\2\2\u0096\u0097\7j\2\2\u0097\u0098\7q\2\2\u0098\u0099")
        buf.write("\7t\2\2\u0099\u009a\7\"\2\2\u009a\u009b\7<\2\2\u009b\u009d")
        buf.write("\7\"\2\2\u009cv\3\2\2\2\u009c\u0080\3\2\2\2\u009c\u008a")
        buf.write("\3\2\2\2\u009c\u0093\3\2\2\2\u009d\22\3\2\2\2\u009e\u009f")
        buf.write("\7B\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2")
        buf.write("\7v\2\2\u00a2\u00a3\7j\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\u00a6\7\"\2\2\u00a6\u00a7\7/\2\2\u00a7\u00c5")
        buf.write("\7\"\2\2\u00a8\u00a9\7B\2\2\u00a9\u00aa\7C\2\2\u00aa\u00ab")
        buf.write("\7w\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad\7j\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\u00af\7t\2\2\u00af\u00b0\7\"\2\2\u00b0\u00b1")
        buf.write("\7/\2\2\u00b1\u00c5\7\"\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4")
        buf.write("\7w\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7j\2\2\u00b6\u00b7")
        buf.write("\7q\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7\"\2\2\u00b9\u00ba")
        buf.write("\7/\2\2\u00ba\u00c5\7\"\2\2\u00bb\u00bc\7C\2\2\u00bc\u00bd")
        buf.write("\7w\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7j\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7\"\2\2\u00c2\u00c3")
        buf.write("\7/\2\2\u00c3\u00c5\7\"\2\2\u00c4\u009e\3\2\2\2\u00c4")
        buf.write("\u00a8\3\2\2\2\u00c4\u00b2\3\2\2\2\u00c4\u00bb\3\2\2\2")
        buf.write("\u00c5\24\3\2\2\2\u00c6\u00c7\7B\2\2\u00c7\u00c8\7c\2")
        buf.write("\2\u00c8\u00c9\7w\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\7")
        buf.write("j\2\2\u00cb\u00cc\7q\2\2\u00cc\u00e1\7t\2\2\u00cd\u00ce")
        buf.write("\7B\2\2\u00ce\u00cf\7C\2\2\u00cf\u00d0\7w\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\u00d2\7j\2\2\u00d2\u00d3\7q\2\2\u00d3\u00e1")
        buf.write("\7t\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7")
        buf.write("\7v\2\2\u00d7\u00d8\7j\2\2\u00d8\u00d9\7q\2\2\u00d9\u00e1")
        buf.write("\7t\2\2\u00da\u00db\7C\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\u00de\7j\2\2\u00de\u00df\7q\2\2\u00df\u00e1")
        buf.write("\7t\2\2\u00e0\u00c6\3\2\2\2\u00e0\u00cd\3\2\2\2\u00e0")
        buf.write("\u00d4\3\2\2\2\u00e0\u00da\3\2\2\2\u00e1\26\3\2\2\2\u00e2")
        buf.write("\u00e3\7x\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7t\2\2\u00e5")
        buf.write("\u00e6\7u\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7q\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\u00ea\7\"\2\2\u00ea\u00eb\7d\2\2\u00eb")
        buf.write("\u00ec\7{\2\2\u00ec\u00f9\7\"\2\2\u00ed\u00ee\7X\2\2\u00ee")
        buf.write("\u00ef\7g\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7u\2\2\u00f1")
        buf.write("\u00f2\7k\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7p\2\2\u00f4")
        buf.write("\u00f5\7\"\2\2\u00f5\u00f6\7d\2\2\u00f6\u00f7\7{\2\2\u00f7")
        buf.write("\u00f9\7\"\2\2\u00f8\u00e2\3\2\2\2\u00f8\u00ed\3\2\2\2")
        buf.write("\u00f9\30\3\2\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7r\2")
        buf.write("\2\u00fc\u00fd\7\"\2\2\u00fd\u00fe\7d\2\2\u00fe\u0113")
        buf.write("\7{\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7z\2\2\u0101\u0102")
        buf.write("\7\"\2\2\u0102\u0103\7d\2\2\u0103\u0113\7{\2\2\u0104\u0105")
        buf.write("\7r\2\2\u0105\u0106\7v\2\2\u0106\u0107\7\"\2\2\u0107\u0108")
        buf.write("\7d\2\2\u0108\u0113\7{\2\2\u0109\u010a\7g\2\2\u010a\u010b")
        buf.write("\7f\2\2\u010b\u010c\7\"\2\2\u010c\u010d\7d\2\2\u010d\u0113")
        buf.write("\7{\2\2\u010e\u010f\7+\2\2\u010f\u0110\7\"\2\2\u0110\u0111")
        buf.write("\7d\2\2\u0111\u0113\7{\2\2\u0112\u00fa\3\2\2\2\u0112\u00ff")
        buf.write("\3\2\2\2\u0112\u0104\3\2\2\2\u0112\u0109\3\2\2\2\u0112")
        buf.write("\u010e\3\2\2\2\u0113\32\3\2\2\2\u0114\u0115\7v\2\2\u0115")
        buf.write("\u0116\7j\2\2\u0116\u0117\7c\2\2\u0117\u0118\7p\2\2\u0118")
        buf.write("\u0119\7m\2\2\u0119\u011a\7u\2\2\u011a\u011b\7\"\2\2\u011b")
        buf.write("\u011c\7v\2\2\u011c\u011d\7q\2\2\u011d\u0129\7\"\2\2\u011e")
        buf.write("\u011f\7V\2\2\u011f\u0120\7j\2\2\u0120\u0121\7c\2\2\u0121")
        buf.write("\u0122\7p\2\2\u0122\u0123\7m\2\2\u0123\u0124\7u\2\2\u0124")
        buf.write("\u0125\7\"\2\2\u0125\u0126\7v\2\2\u0126\u0127\7q\2\2\u0127")
        buf.write("\u0129\7\"\2\2\u0128\u0114\3\2\2\2\u0128\u011e\3\2\2\2")
        buf.write("\u0129\34\3\2\2\2\u012a\u012b\7v\2\2\u012b\u012c\7j\2")
        buf.write("\2\u012c\u012d\7c\2\2\u012d\u012e\7p\2\2\u012e\u012f\7")
        buf.write("m\2\2\u012f\u0130\7u\2\2\u0130\u0139\7\"\2\2\u0131\u0132")
        buf.write("\7V\2\2\u0132\u0133\7j\2\2\u0133\u0134\7c\2\2\u0134\u0135")
        buf.write("\7p\2\2\u0135\u0136\7m\2\2\u0136\u0137\7u\2\2\u0137\u0139")
        buf.write("\7\"\2\2\u0138\u012a\3\2\2\2\u0138\u0131\3\2\2\2\u0139")
        buf.write("\36\3\2\2\2\u013a\u013b\7)\2\2\u013b\u013c\7u\2\2\u013c")
        buf.write("\u013d\7\"\2\2\u013d\u013e\7k\2\2\u013e\u013f\7f\2\2\u013f")
        buf.write("\u0140\7g\2\2\u0140\u0141\7c\2\2\u0141 \3\2\2\2\u0142")
        buf.write("\u0143\7e\2\2\u0143\u0144\7t\2\2\u0144\u0145\7g\2\2\u0145")
        buf.write("\u0146\7f\2\2\u0146\u0147\7k\2\2\u0147\u0148\7v\2\2\u0148")
        buf.write("\u0149\7u\2\2\u0149\u014a\7\"\2\2\u014a\u014b\7v\2\2\u014b")
        buf.write("\u014c\7q\2\2\u014c\u0159\7\"\2\2\u014d\u014e\7E\2\2\u014e")
        buf.write("\u014f\7t\2\2\u014f\u0150\7g\2\2\u0150\u0151\7f\2\2\u0151")
        buf.write("\u0152\7k\2\2\u0152\u0153\7v\2\2\u0153\u0154\7u\2\2\u0154")
        buf.write("\u0155\7\"\2\2\u0155\u0156\7v\2\2\u0156\u0157\7q\2\2\u0157")
        buf.write("\u0159\7\"\2\2\u0158\u0142\3\2\2\2\u0158\u014d\3\2\2\2")
        buf.write("\u0159\"\3\2\2\2\u015a\u015b\7e\2\2\u015b\u015c\7t\2\2")
        buf.write("\u015c\u015d\7g\2\2\u015d\u015e\7f\2\2\u015e\u015f\7k")
        buf.write("\2\2\u015f\u0160\7v\2\2\u0160\u0161\7u\2\2\u0161\u0162")
        buf.write("\7\"\2\2\u0162\u0163\7v\2\2\u0163\u0164\7q\2\2\u0164\u0165")
        buf.write("\7<\2\2\u0165\u0173\7\"\2\2\u0166\u0167\7E\2\2\u0167\u0168")
        buf.write("\7t\2\2\u0168\u0169\7g\2\2\u0169\u016a\7f\2\2\u016a\u016b")
        buf.write("\7k\2\2\u016b\u016c\7v\2\2\u016c\u016d\7u\2\2\u016d\u016e")
        buf.write("\7\"\2\2\u016e\u016f\7v\2\2\u016f\u0170\7q\2\2\u0170\u0171")
        buf.write("\7<\2\2\u0171\u0173\7\"\2\2\u0172\u015a\3\2\2\2\u0172")
        buf.write("\u0166\3\2\2\2\u0173$\3\2\2\2\u0174\u0175\7e\2\2\u0175")
        buf.write("\u0176\7n\2\2\u0176\u0177\7g\2\2\u0177\u0178\7c\2\2\u0178")
        buf.write("\u0179\7p\2\2\u0179\u017a\7w\2\2\u017a\u017b\7r\2\2\u017b")
        buf.write("\u017c\7\"\2\2\u017c\u017d\7d\2\2\u017d\u017e\7{\2\2\u017e")
        buf.write("\u018b\7\"\2\2\u017f\u0180\7E\2\2\u0180\u0181\7n\2\2\u0181")
        buf.write("\u0182\7g\2\2\u0182\u0183\7c\2\2\u0183\u0184\7p\2\2\u0184")
        buf.write("\u0185\7w\2\2\u0185\u0186\7r\2\2\u0186\u0187\7\"\2\2\u0187")
        buf.write("\u0188\7d\2\2\u0188\u0189\7{\2\2\u0189\u018b\7\"\2\2\u018a")
        buf.write("\u0174\3\2\2\2\u018a\u017f\3\2\2\2\u018b&\3\2\2\2\u018c")
        buf.write("\u018d\7d\2\2\u018d\u018e\7{\2\2\u018e\u018f\7\"\2\2\u018f")
        buf.write("\u0190\7/\2\2\u0190\u0197\7/\2\2\u0191\u0192\7D\2\2\u0192")
        buf.write("\u0193\7{\2\2\u0193\u0194\7\"\2\2\u0194\u0195\7/\2\2\u0195")
        buf.write("\u0197\7/\2\2\u0196\u018c\3\2\2\2\u0196\u0191\3\2\2\2")
        buf.write("\u0197(\3\2\2\2\u0198\u0199\7\61\2\2\u0199\u019a\7,\2")
        buf.write("\2\u019a*\3\2\2\2\u019b\u019c\7,\2\2\u019c\u019d\7\61")
        buf.write("\2\2\u019d,\3\2\2\2\u019e\u019f\7\61\2\2\u019f\u01a0\7")
        buf.write("\61\2\2\u01a0.\3\2\2\2\u01a1\u01a2\7/\2\2\u01a2\u01a3")
        buf.write("\7/\2\2\u01a3\60\3\2\2\2\u01a4\u01a5\7/\2\2\u01a5\62\3")
        buf.write("\2\2\2\u01a6\u01a7\7\f\2\2\u01a7\64\3\2\2\2\u01a8\u01a9")
        buf.write("\7\"\2\2\u01a9\66\3\2\2\2\u01aa\u01ac\t\2\2\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad")
        buf.write("\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\b\34\2")
        buf.write("\2\u01b08\3\2\2\2\u01b1\u01b3\13\2\2\2\u01b2\u01b1\3\2")
        buf.write("\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b5:\3\2\2\2\21\2t\u009c\u00c4\u00e0\u00f8")
        buf.write("\u0112\u0128\u0138\u0158\u0172\u018a\u0196\u01ad\u01b4")
        buf.write("\3\2\3\2")
        return buf.getvalue()


class AuthorContentLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEVTEAM = 1
    FOR = 2
    AMPERSAND = 3
    COMMA = 4
    LPAR = 5
    RPAR = 6
    CT_AUTHOR1 = 7
    CT_AUTHOR2 = 8
    CT_AUTHOR3 = 9
    CT_AUTHOR4 = 10
    CT_AUTHOR5 = 11
    CT_AUTHOR6 = 12
    CT_THANKSTO = 13
    CT_THANKS = 14
    CT_IDEA = 15
    CT_CREDIT1 = 16
    CT_CREDIT2 = 17
    CT_CLEANUP = 18
    CM_BY = 19
    COMMENT_OPEN = 20
    COMMENT_CLOSE = 21
    COMMENT_LINE1 = 22
    COMMENT_LINE2 = 23
    COMMENT_HYPN = 24
    LINE_FEED = 25
    WS = 26
    IGNORE_SPACE = 27
    IDENTIFIER = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'dev team'", "' for '", "'&'", "','", "'('", "')'", "''s idea'", 
            "'/*'", "'*/'", "'//'", "'--'", "'-'", "'\n'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "DEVTEAM", "FOR", "AMPERSAND", "COMMA", "LPAR", "RPAR", "CT_AUTHOR1", 
            "CT_AUTHOR2", "CT_AUTHOR3", "CT_AUTHOR4", "CT_AUTHOR5", "CT_AUTHOR6", 
            "CT_THANKSTO", "CT_THANKS", "CT_IDEA", "CT_CREDIT1", "CT_CREDIT2", 
            "CT_CLEANUP", "CM_BY", "COMMENT_OPEN", "COMMENT_CLOSE", "COMMENT_LINE1", 
            "COMMENT_LINE2", "COMMENT_HYPN", "LINE_FEED", "WS", "IGNORE_SPACE", 
            "IDENTIFIER" ]

    ruleNames = [ "DEVTEAM", "FOR", "AMPERSAND", "COMMA", "LPAR", "RPAR", 
                  "CT_AUTHOR1", "CT_AUTHOR2", "CT_AUTHOR3", "CT_AUTHOR4", 
                  "CT_AUTHOR5", "CT_AUTHOR6", "CT_THANKSTO", "CT_THANKS", 
                  "CT_IDEA", "CT_CREDIT1", "CT_CREDIT2", "CT_CLEANUP", "CM_BY", 
                  "COMMENT_OPEN", "COMMENT_CLOSE", "COMMENT_LINE1", "COMMENT_LINE2", 
                  "COMMENT_HYPN", "LINE_FEED", "WS", "IGNORE_SPACE", "IDENTIFIER" ]

    grammarFileName = "AuthorContentLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


