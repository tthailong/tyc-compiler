# Generated from d:\Long\Theory\Principles of Programming Languages\BTL\tyc-compiler\src\grammar\TyC.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01ea\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3j\n\3\3\4\3\4\5\4n\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0083")
        buf.write("\n\6\3\7\3\7\5\7\u0087\n\7\3\b\3\b\3\b\3\b\5\b\u008d\n")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\5\t\u0094\n\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u009d\n\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ac\n\r\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00bb\n\20\3\21\3\21\3\21\3\21\5\21\u00c1\n\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u00c8\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u00d8\n\23\3\24\3\24\3\24\3\24\5\24\u00de\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\5\25\u00e5\n\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00ec\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\7\27\u00f4\n\27\f\27\16\27\u00f7\13\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\7\30\u00ff\n\30\f\30\16\30\u0102\13")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31")
        buf.write("\u010d\n\31\f\31\16\31\u0110\13\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\7\32\u0121\n\32\f\32\16\32\u0124\13\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u012f\n\33\f\33\16")
        buf.write("\33\u0132\13\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\7\34\u0140\n\34\f\34\16\34\u0143")
        buf.write("\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u014c\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\5\36\u0153\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\7\37\u015c\n\37\f\37\16\37\u015f")
        buf.write("\13\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \7 \u016c\n \f")
        buf.write(" \16 \u016f\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5")
        buf.write("!\u017d\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u018c\n\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\5$\u01a0\n$\3%\3%\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\5\'\u01b5\n\'")
        buf.write("\3(\3(\5(\u01b9\n(\3)\3)\5)\u01bd\n)\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\5+\u01cb\n+\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\5,\u01d5\n,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u01e5\n\60\3\61\3\61\3\61\3\61\2\n")
        buf.write(",.\60\62\64\66<>\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\3\6\2")
        buf.write("\t\t\f\f\16\16,,\2\u01f7\2b\3\2\2\2\4i\3\2\2\2\6m\3\2")
        buf.write("\2\2\bo\3\2\2\2\n\u0082\3\2\2\2\f\u0086\3\2\2\2\16\u008c")
        buf.write("\3\2\2\2\20\u0093\3\2\2\2\22\u0095\3\2\2\2\24\u009c\3")
        buf.write("\2\2\2\26\u009e\3\2\2\2\30\u00ab\3\2\2\2\32\u00ad\3\2")
        buf.write("\2\2\34\u00af\3\2\2\2\36\u00ba\3\2\2\2 \u00c0\3\2\2\2")
        buf.write("\"\u00c7\3\2\2\2$\u00d7\3\2\2\2&\u00dd\3\2\2\2(\u00e4")
        buf.write("\3\2\2\2*\u00eb\3\2\2\2,\u00ed\3\2\2\2.\u00f8\3\2\2\2")
        buf.write("\60\u0103\3\2\2\2\62\u0111\3\2\2\2\64\u0125\3\2\2\2\66")
        buf.write("\u0133\3\2\2\28\u014b\3\2\2\2:\u0152\3\2\2\2<\u0154\3")
        buf.write("\2\2\2>\u0160\3\2\2\2@\u017c\3\2\2\2B\u018b\3\2\2\2D\u018d")
        buf.write("\3\2\2\2F\u019f\3\2\2\2H\u01a1\3\2\2\2J\u01a7\3\2\2\2")
        buf.write("L\u01b4\3\2\2\2N\u01b8\3\2\2\2P\u01bc\3\2\2\2R\u01be\3")
        buf.write("\2\2\2T\u01ca\3\2\2\2V\u01d4\3\2\2\2X\u01d6\3\2\2\2Z\u01d8")
        buf.write("\3\2\2\2\\\u01db\3\2\2\2^\u01e4\3\2\2\2`\u01e6\3\2\2\2")
        buf.write("bc\5\4\3\2cd\7\2\2\3d\3\3\2\2\2ef\5\6\4\2fg\5\4\3\2gj")
        buf.write("\3\2\2\2hj\3\2\2\2ie\3\2\2\2ih\3\2\2\2j\5\3\2\2\2kn\5")
        buf.write("\n\6\2ln\5\26\f\2mk\3\2\2\2ml\3\2\2\2n\7\3\2\2\2op\t\2")
        buf.write("\2\2p\t\3\2\2\2qr\5\f\7\2rs\7,\2\2st\7%\2\2tu\5\16\b\2")
        buf.write("uv\7&\2\2vw\7\'\2\2wx\5\24\13\2xy\7(\2\2y\u0083\3\2\2")
        buf.write("\2z{\7,\2\2{|\7%\2\2|}\5\16\b\2}~\7&\2\2~\177\7\'\2\2")
        buf.write("\177\u0080\5\24\13\2\u0080\u0081\7(\2\2\u0081\u0083\3")
        buf.write("\2\2\2\u0082q\3\2\2\2\u0082z\3\2\2\2\u0083\13\3\2\2\2")
        buf.write("\u0084\u0087\5\b\5\2\u0085\u0087\7\21\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0085\3\2\2\2\u0087\r\3\2\2\2\u0088\u0089")
        buf.write("\5\22\n\2\u0089\u008a\5\20\t\2\u008a\u008d\3\2\2\2\u008b")
        buf.write("\u008d\3\2\2\2\u008c\u0088\3\2\2\2\u008c\u008b\3\2\2\2")
        buf.write("\u008d\17\3\2\2\2\u008e\u008f\7)\2\2\u008f\u0090\5\22")
        buf.write("\n\2\u0090\u0091\5\20\t\2\u0091\u0094\3\2\2\2\u0092\u0094")
        buf.write("\3\2\2\2\u0093\u008e\3\2\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\21\3\2\2\2\u0095\u0096\5\b\5\2\u0096\u0097\7,\2\2\u0097")
        buf.write("\23\3\2\2\2\u0098\u0099\5B\"\2\u0099\u009a\5\24\13\2\u009a")
        buf.write("\u009d\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u0098\3\2\2\2")
        buf.write("\u009c\u009b\3\2\2\2\u009d\25\3\2\2\2\u009e\u009f\7\17")
        buf.write("\2\2\u009f\u00a0\7,\2\2\u00a0\u00a1\7\'\2\2\u00a1\u00a2")
        buf.write("\5\30\r\2\u00a2\u00a3\7(\2\2\u00a3\u00a4\7*\2\2\u00a4")
        buf.write("\27\3\2\2\2\u00a5\u00a6\5\32\16\2\u00a6\u00a7\7,\2\2\u00a7")
        buf.write("\u00a8\7*\2\2\u00a8\u00a9\5\30\r\2\u00a9\u00ac\3\2\2\2")
        buf.write("\u00aa\u00ac\3\2\2\2\u00ab\u00a5\3\2\2\2\u00ab\u00aa\3")
        buf.write("\2\2\2\u00ac\31\3\2\2\2\u00ad\u00ae\5\b\5\2\u00ae\33\3")
        buf.write("\2\2\2\u00af\u00b0\7,\2\2\u00b0\u00b1\5\36\20\2\u00b1")
        buf.write("\u00b2\7*\2\2\u00b2\35\3\2\2\2\u00b3\u00bb\7,\2\2\u00b4")
        buf.write("\u00b5\7,\2\2\u00b5\u00b6\7#\2\2\u00b6\u00b7\7\'\2\2\u00b7")
        buf.write("\u00b8\5 \21\2\u00b8\u00b9\7(\2\2\u00b9\u00bb\3\2\2\2")
        buf.write("\u00ba\u00b3\3\2\2\2\u00ba\u00b4\3\2\2\2\u00bb\37\3\2")
        buf.write("\2\2\u00bc\u00bd\5*\26\2\u00bd\u00be\5\"\22\2\u00be\u00c1")
        buf.write("\3\2\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c1!\3\2\2\2\u00c2\u00c3\7)\2\2\u00c3")
        buf.write("\u00c4\5*\26\2\u00c4\u00c5\5\"\22\2\u00c5\u00c8\3\2\2")
        buf.write("\2\u00c6\u00c8\3\2\2\2\u00c7\u00c2\3\2\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8#\3\2\2\2\u00c9\u00ca\7\3\2\2\u00ca\u00cb")
        buf.write("\7,\2\2\u00cb\u00cc\7#\2\2\u00cc\u00d8\5*\26\2\u00cd\u00ce")
        buf.write("\7\3\2\2\u00ce\u00d8\7,\2\2\u00cf\u00d0\5\b\5\2\u00d0")
        buf.write("\u00d1\7,\2\2\u00d1\u00d2\7#\2\2\u00d2\u00d3\5*\26\2\u00d3")
        buf.write("\u00d8\3\2\2\2\u00d4\u00d5\5\b\5\2\u00d5\u00d6\7,\2\2")
        buf.write("\u00d6\u00d8\3\2\2\2\u00d7\u00c9\3\2\2\2\u00d7\u00cd\3")
        buf.write("\2\2\2\u00d7\u00cf\3\2\2\2\u00d7\u00d4\3\2\2\2\u00d8%")
        buf.write("\3\2\2\2\u00d9\u00da\5*\26\2\u00da\u00db\5(\25\2\u00db")
        buf.write("\u00de\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00d9\3\2\2\2")
        buf.write("\u00dd\u00dc\3\2\2\2\u00de\'\3\2\2\2\u00df\u00e0\7)\2")
        buf.write("\2\u00e0\u00e1\5*\26\2\u00e1\u00e2\5(\25\2\u00e2\u00e5")
        buf.write("\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00df\3\2\2\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e5)\3\2\2\2\u00e6\u00e7\5,\27\2\u00e7")
        buf.write("\u00e8\7#\2\2\u00e8\u00e9\5*\26\2\u00e9\u00ec\3\2\2\2")
        buf.write("\u00ea\u00ec\5,\27\2\u00eb\u00e6\3\2\2\2\u00eb\u00ea\3")
        buf.write("\2\2\2\u00ec+\3\2\2\2\u00ed\u00ee\b\27\1\2\u00ee\u00ef")
        buf.write("\5.\30\2\u00ef\u00f5\3\2\2\2\u00f0\u00f1\f\4\2\2\u00f1")
        buf.write("\u00f2\7\36\2\2\u00f2\u00f4\5.\30\2\u00f3\u00f0\3\2\2")
        buf.write("\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6")
        buf.write("\3\2\2\2\u00f6-\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9")
        buf.write("\b\30\1\2\u00f9\u00fa\5\60\31\2\u00fa\u0100\3\2\2\2\u00fb")
        buf.write("\u00fc\f\4\2\2\u00fc\u00fd\7\37\2\2\u00fd\u00ff\5\60\31")
        buf.write("\2\u00fe\u00fb\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101/\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0103\u0104\b\31\1\2\u0104\u0105\5\62\32\2\u0105")
        buf.write("\u010e\3\2\2\2\u0106\u0107\f\5\2\2\u0107\u0108\7\30\2")
        buf.write("\2\u0108\u010d\5\62\32\2\u0109\u010a\f\4\2\2\u010a\u010b")
        buf.write("\7\31\2\2\u010b\u010d\5\62\32\2\u010c\u0106\3\2\2\2\u010c")
        buf.write("\u0109\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2")
        buf.write("\u010e\u010f\3\2\2\2\u010f\61\3\2\2\2\u0110\u010e\3\2")
        buf.write("\2\2\u0111\u0112\b\32\1\2\u0112\u0113\5\64\33\2\u0113")
        buf.write("\u0122\3\2\2\2\u0114\u0115\f\7\2\2\u0115\u0116\7\32\2")
        buf.write("\2\u0116\u0121\5\64\33\2\u0117\u0118\f\6\2\2\u0118\u0119")
        buf.write("\7\34\2\2\u0119\u0121\5\64\33\2\u011a\u011b\f\5\2\2\u011b")
        buf.write("\u011c\7\33\2\2\u011c\u0121\5\64\33\2\u011d\u011e\f\4")
        buf.write("\2\2\u011e\u011f\7\35\2\2\u011f\u0121\5\64\33\2\u0120")
        buf.write("\u0114\3\2\2\2\u0120\u0117\3\2\2\2\u0120\u011a\3\2\2\2")
        buf.write("\u0120\u011d\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3")
        buf.write("\2\2\2\u0122\u0123\3\2\2\2\u0123\63\3\2\2\2\u0124\u0122")
        buf.write("\3\2\2\2\u0125\u0126\b\33\1\2\u0126\u0127\5\66\34\2\u0127")
        buf.write("\u0130\3\2\2\2\u0128\u0129\f\5\2\2\u0129\u012a\7\23\2")
        buf.write("\2\u012a\u012f\5\66\34\2\u012b\u012c\f\4\2\2\u012c\u012d")
        buf.write("\7\24\2\2\u012d\u012f\5\66\34\2\u012e\u0128\3\2\2\2\u012e")
        buf.write("\u012b\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131\65\3\2\2\2\u0132\u0130\3\2")
        buf.write("\2\2\u0133\u0134\b\34\1\2\u0134\u0135\58\35\2\u0135\u0141")
        buf.write("\3\2\2\2\u0136\u0137\f\6\2\2\u0137\u0138\7\25\2\2\u0138")
        buf.write("\u0140\58\35\2\u0139\u013a\f\5\2\2\u013a\u013b\7\26\2")
        buf.write("\2\u013b\u0140\58\35\2\u013c\u013d\f\4\2\2\u013d\u013e")
        buf.write("\7\27\2\2\u013e\u0140\58\35\2\u013f\u0136\3\2\2\2\u013f")
        buf.write("\u0139\3\2\2\2\u013f\u013c\3\2\2\2\u0140\u0143\3\2\2\2")
        buf.write("\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\67\3\2")
        buf.write("\2\2\u0143\u0141\3\2\2\2\u0144\u0145\7 \2\2\u0145\u014c")
        buf.write("\58\35\2\u0146\u0147\7\23\2\2\u0147\u014c\58\35\2\u0148")
        buf.write("\u0149\7\24\2\2\u0149\u014c\58\35\2\u014a\u014c\5:\36")
        buf.write("\2\u014b\u0144\3\2\2\2\u014b\u0146\3\2\2\2\u014b\u0148")
        buf.write("\3\2\2\2\u014b\u014a\3\2\2\2\u014c9\3\2\2\2\u014d\u014e")
        buf.write("\7!\2\2\u014e\u0153\5:\36\2\u014f\u0150\7\"\2\2\u0150")
        buf.write("\u0153\5:\36\2\u0151\u0153\5<\37\2\u0152\u014d\3\2\2\2")
        buf.write("\u0152\u014f\3\2\2\2\u0152\u0151\3\2\2\2\u0153;\3\2\2")
        buf.write("\2\u0154\u0155\b\37\1\2\u0155\u0156\5> \2\u0156\u015d")
        buf.write("\3\2\2\2\u0157\u0158\f\5\2\2\u0158\u015c\7!\2\2\u0159")
        buf.write("\u015a\f\4\2\2\u015a\u015c\7\"\2\2\u015b\u0157\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3")
        buf.write("\2\2\2\u015d\u015e\3\2\2\2\u015e=\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u0160\u0161\b \1\2\u0161\u0162\5@!\2\u0162\u016d")
        buf.write("\3\2\2\2\u0163\u0164\f\5\2\2\u0164\u0165\7%\2\2\u0165")
        buf.write("\u0166\5&\24\2\u0166\u0167\7&\2\2\u0167\u016c\3\2\2\2")
        buf.write("\u0168\u0169\f\4\2\2\u0169\u016a\7$\2\2\u016a\u016c\7")
        buf.write(",\2\2\u016b\u0163\3\2\2\2\u016b\u0168\3\2\2\2\u016c\u016f")
        buf.write("\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("?\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u017d\7-\2\2\u0171")
        buf.write("\u017d\7.\2\2\u0172\u017d\7/\2\2\u0173\u017d\7,\2\2\u0174")
        buf.write("\u0175\7%\2\2\u0175\u0176\5*\26\2\u0176\u0177\7&\2\2\u0177")
        buf.write("\u017d\3\2\2\2\u0178\u0179\7\'\2\2\u0179\u017a\5 \21\2")
        buf.write("\u017a\u017b\7(\2\2\u017b\u017d\3\2\2\2\u017c\u0170\3")
        buf.write("\2\2\2\u017c\u0171\3\2\2\2\u017c\u0172\3\2\2\2\u017c\u0173")
        buf.write("\3\2\2\2\u017c\u0174\3\2\2\2\u017c\u0178\3\2\2\2\u017d")
        buf.write("A\3\2\2\2\u017e\u017f\5$\23\2\u017f\u0180\7*\2\2\u0180")
        buf.write("\u018c\3\2\2\2\u0181\u018c\5\34\17\2\u0182\u018c\5D#\2")
        buf.write("\u0183\u018c\5F$\2\u0184\u018c\5H%\2\u0185\u018c\5J&\2")
        buf.write("\u0186\u018c\5R*\2\u0187\u018c\5Z.\2\u0188\u018c\5\\/")
        buf.write("\2\u0189\u018c\5^\60\2\u018a\u018c\5`\61\2\u018b\u017e")
        buf.write("\3\2\2\2\u018b\u0181\3\2\2\2\u018b\u0182\3\2\2\2\u018b")
        buf.write("\u0183\3\2\2\2\u018b\u0184\3\2\2\2\u018b\u0185\3\2\2\2")
        buf.write("\u018b\u0186\3\2\2\2\u018b\u0187\3\2\2\2\u018b\u0188\3")
        buf.write("\2\2\2\u018b\u0189\3\2\2\2\u018b\u018a\3\2\2\2\u018cC")
        buf.write("\3\2\2\2\u018d\u018e\7\'\2\2\u018e\u018f\5\24\13\2\u018f")
        buf.write("\u0190\7(\2\2\u0190E\3\2\2\2\u0191\u0192\7\13\2\2\u0192")
        buf.write("\u0193\7%\2\2\u0193\u0194\5*\26\2\u0194\u0195\7&\2\2\u0195")
        buf.write("\u0196\5B\"\2\u0196\u01a0\3\2\2\2\u0197\u0198\7\13\2\2")
        buf.write("\u0198\u0199\7%\2\2\u0199\u019a\5*\26\2\u019a\u019b\7")
        buf.write("&\2\2\u019b\u019c\5B\"\2\u019c\u019d\7\b\2\2\u019d\u019e")
        buf.write("\5B\"\2\u019e\u01a0\3\2\2\2\u019f\u0191\3\2\2\2\u019f")
        buf.write("\u0197\3\2\2\2\u01a0G\3\2\2\2\u01a1\u01a2\7\22\2\2\u01a2")
        buf.write("\u01a3\7%\2\2\u01a3\u01a4\5*\26\2\u01a4\u01a5\7&\2\2\u01a5")
        buf.write("\u01a6\5B\"\2\u01a6I\3\2\2\2\u01a7\u01a8\7\n\2\2\u01a8")
        buf.write("\u01a9\7%\2\2\u01a9\u01aa\5L\'\2\u01aa\u01ab\7*\2\2\u01ab")
        buf.write("\u01ac\5N(\2\u01ac\u01ad\7*\2\2\u01ad\u01ae\5P)\2\u01ae")
        buf.write("\u01af\7&\2\2\u01af\u01b0\5B\"\2\u01b0K\3\2\2\2\u01b1")
        buf.write("\u01b5\5$\23\2\u01b2\u01b5\5*\26\2\u01b3\u01b5\3\2\2\2")
        buf.write("\u01b4\u01b1\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3")
        buf.write("\2\2\2\u01b5M\3\2\2\2\u01b6\u01b9\5*\26\2\u01b7\u01b9")
        buf.write("\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9")
        buf.write("O\3\2\2\2\u01ba\u01bd\5*\26\2\u01bb\u01bd\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bdQ\3\2\2\2\u01be")
        buf.write("\u01bf\7\20\2\2\u01bf\u01c0\7%\2\2\u01c0\u01c1\5*\26\2")
        buf.write("\u01c1\u01c2\7&\2\2\u01c2\u01c3\7\'\2\2\u01c3\u01c4\5")
        buf.write("T+\2\u01c4\u01c5\7(\2\2\u01c5S\3\2\2\2\u01c6\u01c7\5V")
        buf.write(",\2\u01c7\u01c8\5T+\2\u01c8\u01cb\3\2\2\2\u01c9\u01cb")
        buf.write("\3\2\2\2\u01ca\u01c6\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cb")
        buf.write("U\3\2\2\2\u01cc\u01cd\7\5\2\2\u01cd\u01ce\5X-\2\u01ce")
        buf.write("\u01cf\7+\2\2\u01cf\u01d0\5\24\13\2\u01d0\u01d5\3\2\2")
        buf.write("\2\u01d1\u01d2\7\7\2\2\u01d2\u01d3\7+\2\2\u01d3\u01d5")
        buf.write("\5\24\13\2\u01d4\u01cc\3\2\2\2\u01d4\u01d1\3\2\2\2\u01d5")
        buf.write("W\3\2\2\2\u01d6\u01d7\5*\26\2\u01d7Y\3\2\2\2\u01d8\u01d9")
        buf.write("\7\4\2\2\u01d9\u01da\7*\2\2\u01da[\3\2\2\2\u01db\u01dc")
        buf.write("\7\6\2\2\u01dc\u01dd\7*\2\2\u01dd]\3\2\2\2\u01de\u01df")
        buf.write("\7\r\2\2\u01df\u01e0\5*\26\2\u01e0\u01e1\7*\2\2\u01e1")
        buf.write("\u01e5\3\2\2\2\u01e2\u01e3\7\r\2\2\u01e3\u01e5\7*\2\2")
        buf.write("\u01e4\u01de\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5_\3\2\2")
        buf.write("\2\u01e6\u01e7\5*\26\2\u01e7\u01e8\7*\2\2\u01e8a\3\2\2")
        buf.write("\2*im\u0082\u0086\u008c\u0093\u009c\u00ab\u00ba\u00c0")
        buf.write("\u00c7\u00d7\u00dd\u00e4\u00eb\u00f5\u0100\u010c\u010e")
        buf.write("\u0120\u0122\u012e\u0130\u013f\u0141\u014b\u0152\u015b")
        buf.write("\u015d\u016b\u016d\u017c\u018b\u019f\u01b4\u01b8\u01bc")
        buf.write("\u01ca\u01d4\u01e4")
        return buf.getvalue()


class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'case'", "'continue'", 
                     "'default'", "'else'", "'float'", "'for'", "'if'", 
                     "'int'", "'return'", "'string'", "'struct'", "'switch'", 
                     "'void'", "'while'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'||'", 
                     "'&&'", "'!'", "'++'", "'--'", "'='", "'.'", "'('", 
                     "')'", "'{'", "'}'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "CASE", "CONTINUE", 
                      "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", "RETURN", 
                      "STRING", "STRUCT", "SWITCH", "VOID", "WHILE", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", "LESSTHAN", 
                      "GREATERTHAN", "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", 
                      "OR", "AND", "NOT", "INCREMENT", "DECREMENT", "ASSIGN", 
                      "ACCESS", "LP", "RP", "LB", "RB", "CM", "SM", "CL", 
                      "ID", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_manydecls = 1
    RULE_decl = 2
    RULE_typ = 3
    RULE_funcdecl = 4
    RULE_rettyp = 5
    RULE_paramlist = 6
    RULE_paramtail = 7
    RULE_pardecl = 8
    RULE_stmtlist = 9
    RULE_structdecl = 10
    RULE_memlist = 11
    RULE_memtyp = 12
    RULE_structvardecl = 13
    RULE_structvar = 14
    RULE_exprlist = 15
    RULE_exprtail = 16
    RULE_vardecl = 17
    RULE_arglist = 18
    RULE_argtail = 19
    RULE_expr = 20
    RULE_expr1 = 21
    RULE_expr2 = 22
    RULE_expr3 = 23
    RULE_expr4 = 24
    RULE_expr5 = 25
    RULE_expr6 = 26
    RULE_expr7 = 27
    RULE_expr8 = 28
    RULE_expr9 = 29
    RULE_expr10 = 30
    RULE_expr11 = 31
    RULE_stmt = 32
    RULE_blockstmt = 33
    RULE_ifstmt = 34
    RULE_whilestmt = 35
    RULE_forstmt = 36
    RULE_init = 37
    RULE_cond = 38
    RULE_updt = 39
    RULE_switchstmt = 40
    RULE_caselist = 41
    RULE_caseclause = 42
    RULE_caseexpr = 43
    RULE_breakstmt = 44
    RULE_continuestmt = 45
    RULE_returnstmt = 46
    RULE_exprstmt = 47

    ruleNames =  [ "program", "manydecls", "decl", "typ", "funcdecl", "rettyp", 
                   "paramlist", "paramtail", "pardecl", "stmtlist", "structdecl", 
                   "memlist", "memtyp", "structvardecl", "structvar", "exprlist", 
                   "exprtail", "vardecl", "arglist", "argtail", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "expr10", "expr11", "stmt", 
                   "blockstmt", "ifstmt", "whilestmt", "forstmt", "init", 
                   "cond", "updt", "switchstmt", "caselist", "caseclause", 
                   "caseexpr", "breakstmt", "continuestmt", "returnstmt", 
                   "exprstmt" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    CASE=3
    CONTINUE=4
    DEFAULT=5
    ELSE=6
    FLOAT=7
    FOR=8
    IF=9
    INT=10
    RETURN=11
    STRING=12
    STRUCT=13
    SWITCH=14
    VOID=15
    WHILE=16
    ADD=17
    SUB=18
    MUL=19
    DIV=20
    MOD=21
    EQUAL=22
    NOTEQUAL=23
    LESSTHAN=24
    GREATERTHAN=25
    LESSTHAN_EQUAL=26
    GREATERTHAN_EQUAL=27
    OR=28
    AND=29
    NOT=30
    INCREMENT=31
    DECREMENT=32
    ASSIGN=33
    ACCESS=34
    LP=35
    RP=36
    LB=37
    RB=38
    CM=39
    SM=40
    CL=41
    ID=42
    INTLIT=43
    FLOATLIT=44
    STRINGLIT=45
    WS=46
    LINE_COMMENT=47
    BLOCK_COMMENT=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def manydecls(self):
            return self.getTypedRuleContext(TyCParser.ManydeclsContext,0)


        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.manydecls()
            self.state = 97
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManydeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(TyCParser.DeclContext,0)


        def manydecls(self):
            return self.getTypedRuleContext(TyCParser.ManydeclsContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_manydecls




    def manydecls(self):

        localctx = TyCParser.ManydeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manydecls)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.STRUCT, TyCParser.VOID, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.decl()
                self.state = 100
                self.manydecls()
                pass
            elif token in [TyCParser.EOF]:
                self.enterOuterAlt(localctx, 2)

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


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(TyCParser.FuncdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(TyCParser.StructdeclContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_decl




    def decl(self):

        localctx = TyCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.VOID, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.funcdecl()
                pass
            elif token in [TyCParser.STRUCT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.structdecl()
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


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_typ




    def typ(self):

        localctx = TyCParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.FLOAT) | (1 << TyCParser.INT) | (1 << TyCParser.STRING) | (1 << TyCParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rettyp(self):
            return self.getTypedRuleContext(TyCParser.RettypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(TyCParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_funcdecl




    def funcdecl(self):

        localctx = TyCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.rettyp()
                self.state = 112
                self.match(TyCParser.ID)
                self.state = 113
                self.match(TyCParser.LP)
                self.state = 114
                self.paramlist()
                self.state = 115
                self.match(TyCParser.RP)
                self.state = 116
                self.match(TyCParser.LB)
                self.state = 117
                self.stmtlist()
                self.state = 118
                self.match(TyCParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(TyCParser.ID)
                self.state = 121
                self.match(TyCParser.LP)
                self.state = 122
                self.paramlist()
                self.state = 123
                self.match(TyCParser.RP)
                self.state = 124
                self.match(TyCParser.LB)
                self.state = 125
                self.stmtlist()
                self.state = 126
                self.match(TyCParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RettypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_rettyp




    def rettyp(self):

        localctx = TyCParser.RettypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rettyp)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.typ()
                pass
            elif token in [TyCParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(TyCParser.VOID)
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


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pardecl(self):
            return self.getTypedRuleContext(TyCParser.PardeclContext,0)


        def paramtail(self):
            return self.getTypedRuleContext(TyCParser.ParamtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_paramlist




    def paramlist(self):

        localctx = TyCParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramlist)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.pardecl()
                self.state = 135
                self.paramtail()
                pass
            elif token in [TyCParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class ParamtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(TyCParser.CM, 0)

        def pardecl(self):
            return self.getTypedRuleContext(TyCParser.PardeclContext,0)


        def paramtail(self):
            return self.getTypedRuleContext(TyCParser.ParamtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_paramtail




    def paramtail(self):

        localctx = TyCParser.ParamtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramtail)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(TyCParser.CM)
                self.state = 141
                self.pardecl()
                self.state = 142
                self.paramtail()
                pass
            elif token in [TyCParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class PardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_pardecl




    def pardecl(self):

        localctx = TyCParser.PardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.typ()
            self.state = 148
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmtlist




    def stmtlist(self):

        localctx = TyCParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmtlist)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.AUTO, TyCParser.BREAK, TyCParser.CONTINUE, TyCParser.FLOAT, TyCParser.FOR, TyCParser.IF, TyCParser.INT, TyCParser.RETURN, TyCParser.STRING, TyCParser.SWITCH, TyCParser.WHILE, TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.stmt()
                self.state = 151
                self.stmtlist()
                pass
            elif token in [TyCParser.CASE, TyCParser.DEFAULT, TyCParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def memlist(self):
            return self.getTypedRuleContext(TyCParser.MemlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structdecl




    def structdecl(self):

        localctx = TyCParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(TyCParser.STRUCT)
            self.state = 157
            self.match(TyCParser.ID)
            self.state = 158
            self.match(TyCParser.LB)
            self.state = 159
            self.memlist()
            self.state = 160
            self.match(TyCParser.RB)
            self.state = 161
            self.match(TyCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memtyp(self):
            return self.getTypedRuleContext(TyCParser.MemtypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def memlist(self):
            return self.getTypedRuleContext(TyCParser.MemlistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_memlist




    def memlist(self):

        localctx = TyCParser.MemlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_memlist)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.memtyp()
                self.state = 164
                self.match(TyCParser.ID)
                self.state = 165
                self.match(TyCParser.SM)
                self.state = 166
                self.memlist()
                pass
            elif token in [TyCParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class MemtypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_memtyp




    def memtyp(self):

        localctx = TyCParser.MemtypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_memtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def structvar(self):
            return self.getTypedRuleContext(TyCParser.StructvarContext,0)


        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structvardecl




    def structvardecl(self):

        localctx = TyCParser.StructvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_structvardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(TyCParser.ID)
            self.state = 174
            self.structvar()
            self.state = 175
            self.match(TyCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(TyCParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structvar




    def structvar(self):

        localctx = TyCParser.StructvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structvar)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(TyCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(TyCParser.ID)
                self.state = 179
                self.match(TyCParser.ASSIGN)
                self.state = 180
                self.match(TyCParser.LB)
                self.state = 181
                self.exprlist()
                self.state = 182
                self.match(TyCParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def exprtail(self):
            return self.getTypedRuleContext(TyCParser.ExprtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_exprlist




    def exprlist(self):

        localctx = TyCParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exprlist)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.expr()
                self.state = 187
                self.exprtail()
                pass
            elif token in [TyCParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ExprtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(TyCParser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def exprtail(self):
            return self.getTypedRuleContext(TyCParser.ExprtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_exprtail




    def exprtail(self):

        localctx = TyCParser.ExprtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exprtail)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(TyCParser.CM)
                self.state = 193
                self.expr()
                self.state = 194
                self.exprtail()
                pass
            elif token in [TyCParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_vardecl




    def vardecl(self):

        localctx = TyCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_vardecl)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(TyCParser.AUTO)
                self.state = 200
                self.match(TyCParser.ID)
                self.state = 201
                self.match(TyCParser.ASSIGN)
                self.state = 202
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(TyCParser.AUTO)
                self.state = 204
                self.match(TyCParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.typ()
                self.state = 206
                self.match(TyCParser.ID)
                self.state = 207
                self.match(TyCParser.ASSIGN)
                self.state = 208
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.typ()
                self.state = 211
                self.match(TyCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def argtail(self):
            return self.getTypedRuleContext(TyCParser.ArgtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_arglist




    def arglist(self):

        localctx = TyCParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arglist)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.expr()
                self.state = 216
                self.argtail()
                pass
            elif token in [TyCParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(TyCParser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def argtail(self):
            return self.getTypedRuleContext(TyCParser.ArgtailContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_argtail




    def argtail(self):

        localctx = TyCParser.ArgtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_argtail)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(TyCParser.CM)
                self.state = 222
                self.expr()
                self.state = 223
                self.argtail()
                pass
            elif token in [TyCParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(TyCParser.Expr1Context,0)


        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expr




    def expr(self):

        localctx = TyCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.expr1(0)
                self.state = 229
                self.match(TyCParser.ASSIGN)
                self.state = 230
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(TyCParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(TyCParser.Expr1Context,0)


        def OR(self):
            return self.getToken(TyCParser.OR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 238
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 239
                    self.match(TyCParser.OR)
                    self.state = 240
                    self.expr2(0) 
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(TyCParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(TyCParser.Expr2Context,0)


        def AND(self):
            return self.getToken(TyCParser.AND, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 249
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 250
                    self.match(TyCParser.AND)
                    self.state = 251
                    self.expr3(0) 
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(TyCParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(TyCParser.Expr3Context,0)


        def EQUAL(self):
            return self.getToken(TyCParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(TyCParser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 266
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 260
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 261
                        self.match(TyCParser.EQUAL)
                        self.state = 262
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 263
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 264
                        self.match(TyCParser.NOTEQUAL)
                        self.state = 265
                        self.expr4(0)
                        pass

             
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(TyCParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(TyCParser.Expr4Context,0)


        def LESSTHAN(self):
            return self.getToken(TyCParser.LESSTHAN, 0)

        def LESSTHAN_EQUAL(self):
            return self.getToken(TyCParser.LESSTHAN_EQUAL, 0)

        def GREATERTHAN(self):
            return self.getToken(TyCParser.GREATERTHAN, 0)

        def GREATERTHAN_EQUAL(self):
            return self.getToken(TyCParser.GREATERTHAN_EQUAL, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 286
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 274
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 275
                        self.match(TyCParser.LESSTHAN)
                        self.state = 276
                        self.expr5(0)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 277
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 278
                        self.match(TyCParser.LESSTHAN_EQUAL)
                        self.state = 279
                        self.expr5(0)
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 280
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 281
                        self.match(TyCParser.GREATERTHAN)
                        self.state = 282
                        self.expr5(0)
                        pass

                    elif la_ == 4:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 283
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 284
                        self.match(TyCParser.GREATERTHAN_EQUAL)
                        self.state = 285
                        self.expr5(0)
                        pass

             
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(TyCParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(TyCParser.Expr5Context,0)


        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)

        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr5



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.expr6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 300
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 294
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 295
                        self.match(TyCParser.ADD)
                        self.state = 296
                        self.expr6(0)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 297
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 298
                        self.match(TyCParser.SUB)
                        self.state = 299
                        self.expr6(0)
                        pass

             
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(TyCParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(TyCParser.Expr6Context,0)


        def MUL(self):
            return self.getToken(TyCParser.MUL, 0)

        def DIV(self):
            return self.getToken(TyCParser.DIV, 0)

        def MOD(self):
            return self.getToken(TyCParser.MOD, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr6



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 317
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 308
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 309
                        self.match(TyCParser.MUL)
                        self.state = 310
                        self.expr7()
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 311
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 312
                        self.match(TyCParser.DIV)
                        self.state = 313
                        self.expr7()
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 314
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 315
                        self.match(TyCParser.MOD)
                        self.state = 316
                        self.expr7()
                        pass

             
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(TyCParser.NOT, 0)

        def expr7(self):
            return self.getTypedRuleContext(TyCParser.Expr7Context,0)


        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)

        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)

        def expr8(self):
            return self.getTypedRuleContext(TyCParser.Expr8Context,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expr7




    def expr7(self):

        localctx = TyCParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr7)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(TyCParser.NOT)
                self.state = 323
                self.expr7()
                pass
            elif token in [TyCParser.ADD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(TyCParser.ADD)
                self.state = 325
                self.expr7()
                pass
            elif token in [TyCParser.SUB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.match(TyCParser.SUB)
                self.state = 327
                self.expr7()
                pass
            elif token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.expr8()
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


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def expr8(self):
            return self.getTypedRuleContext(TyCParser.Expr8Context,0)


        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def expr9(self):
            return self.getTypedRuleContext(TyCParser.Expr9Context,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expr8




    def expr8(self):

        localctx = TyCParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr8)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(TyCParser.INCREMENT)
                self.state = 332
                self.expr8()
                pass
            elif token in [TyCParser.DECREMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(TyCParser.DECREMENT)
                self.state = 334
                self.expr8()
                pass
            elif token in [TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.expr9(0)
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


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(TyCParser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(TyCParser.Expr9Context,0)


        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr9



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.expr10(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 345
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 341
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 342
                        self.match(TyCParser.INCREMENT)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 343
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 344
                        self.match(TyCParser.DECREMENT)
                        pass

             
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr11(self):
            return self.getTypedRuleContext(TyCParser.Expr11Context,0)


        def expr10(self):
            return self.getTypedRuleContext(TyCParser.Expr10Context,0)


        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def arglist(self):
            return self.getTypedRuleContext(TyCParser.ArglistContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def ACCESS(self):
            return self.getToken(TyCParser.ACCESS, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr10



    def expr10(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr10Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr10, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.expr11()
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 361
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr10Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr10)
                        self.state = 353
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 354
                        self.match(TyCParser.LP)
                        self.state = 355
                        self.arglist()
                        self.state = 356
                        self.match(TyCParser.RP)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr10Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr10)
                        self.state = 358
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 359
                        self.match(TyCParser.ACCESS)
                        self.state = 360
                        self.match(TyCParser.ID)
                        pass

             
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(TyCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(TyCParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(TyCParser.STRINGLIT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(TyCParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr11




    def expr11(self):

        localctx = TyCParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr11)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(TyCParser.INTLIT)
                pass
            elif token in [TyCParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(TyCParser.FLOATLIT)
                pass
            elif token in [TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self.match(TyCParser.STRINGLIT)
                pass
            elif token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 369
                self.match(TyCParser.ID)
                pass
            elif token in [TyCParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 370
                self.match(TyCParser.LP)
                self.state = 371
                self.expr()
                self.state = 372
                self.match(TyCParser.RP)
                pass
            elif token in [TyCParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 374
                self.match(TyCParser.LB)
                self.state = 375
                self.exprlist()
                self.state = 376
                self.match(TyCParser.RB)
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(TyCParser.VardeclContext,0)


        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def structvardecl(self):
            return self.getTypedRuleContext(TyCParser.StructvardeclContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(TyCParser.BlockstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(TyCParser.IfstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(TyCParser.WhilestmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(TyCParser.ForstmtContext,0)


        def switchstmt(self):
            return self.getTypedRuleContext(TyCParser.SwitchstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(TyCParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(TyCParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(TyCParser.ReturnstmtContext,0)


        def exprstmt(self):
            return self.getTypedRuleContext(TyCParser.ExprstmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmt




    def stmt(self):

        localctx = TyCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stmt)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.vardecl()
                self.state = 381
                self.match(TyCParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.structvardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.blockstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 386
                self.whilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 387
                self.forstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 388
                self.switchstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 389
                self.breakstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 390
                self.continuestmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 391
                self.returnstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 392
                self.exprstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_blockstmt




    def blockstmt(self):

        localctx = TyCParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(TyCParser.LB)
            self.state = 396
            self.stmtlist()
            self.state = 397
            self.match(TyCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TyCParser.IF, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_ifstmt




    def ifstmt(self):

        localctx = TyCParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_ifstmt)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(TyCParser.IF)
                self.state = 400
                self.match(TyCParser.LP)
                self.state = 401
                self.expr()
                self.state = 402
                self.match(TyCParser.RP)
                self.state = 403
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(TyCParser.IF)
                self.state = 406
                self.match(TyCParser.LP)
                self.state = 407
                self.expr()
                self.state = 408
                self.match(TyCParser.RP)
                self.state = 409
                self.stmt()
                self.state = 410
                self.match(TyCParser.ELSE)
                self.state = 411
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_whilestmt




    def whilestmt(self):

        localctx = TyCParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(TyCParser.WHILE)
            self.state = 416
            self.match(TyCParser.LP)
            self.state = 417
            self.expr()
            self.state = 418
            self.match(TyCParser.RP)
            self.state = 419
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def init(self):
            return self.getTypedRuleContext(TyCParser.InitContext,0)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SM)
            else:
                return self.getToken(TyCParser.SM, i)

        def cond(self):
            return self.getTypedRuleContext(TyCParser.CondContext,0)


        def updt(self):
            return self.getTypedRuleContext(TyCParser.UpdtContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forstmt




    def forstmt(self):

        localctx = TyCParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(TyCParser.FOR)
            self.state = 422
            self.match(TyCParser.LP)
            self.state = 423
            self.init()
            self.state = 424
            self.match(TyCParser.SM)
            self.state = 425
            self.cond()
            self.state = 426
            self.match(TyCParser.SM)
            self.state = 427
            self.updt()
            self.state = 428
            self.match(TyCParser.RP)
            self.state = 429
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(TyCParser.VardeclContext,0)


        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_init




    def init(self):

        localctx = TyCParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_init)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_cond




    def cond(self):

        localctx = TyCParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_cond)
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.expr()
                pass
            elif token in [TyCParser.SM]:
                self.enterOuterAlt(localctx, 2)

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


    class UpdtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_updt




    def updt(self):

        localctx = TyCParser.UpdtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_updt)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.expr()
                pass
            elif token in [TyCParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class SwitchstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def caselist(self):
            return self.getTypedRuleContext(TyCParser.CaselistContext,0)


        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_switchstmt




    def switchstmt(self):

        localctx = TyCParser.SwitchstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_switchstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(TyCParser.SWITCH)
            self.state = 445
            self.match(TyCParser.LP)
            self.state = 446
            self.expr()
            self.state = 447
            self.match(TyCParser.RP)
            self.state = 448
            self.match(TyCParser.LB)
            self.state = 449
            self.caselist()
            self.state = 450
            self.match(TyCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaselistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseclause(self):
            return self.getTypedRuleContext(TyCParser.CaseclauseContext,0)


        def caselist(self):
            return self.getTypedRuleContext(TyCParser.CaselistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_caselist




    def caselist(self):

        localctx = TyCParser.CaselistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_caselist)
        try:
            self.state = 456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CASE, TyCParser.DEFAULT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.caseclause()
                self.state = 453
                self.caselist()
                pass
            elif token in [TyCParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class CaseclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def caseexpr(self):
            return self.getTypedRuleContext(TyCParser.CaseexprContext,0)


        def CL(self):
            return self.getToken(TyCParser.CL, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(TyCParser.StmtlistContext,0)


        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_caseclause




    def caseclause(self):

        localctx = TyCParser.CaseclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_caseclause)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.match(TyCParser.CASE)
                self.state = 459
                self.caseexpr()
                self.state = 460
                self.match(TyCParser.CL)
                self.state = 461
                self.stmtlist()
                pass
            elif token in [TyCParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.match(TyCParser.DEFAULT)
                self.state = 464
                self.match(TyCParser.CL)
                self.state = 465
                self.stmtlist()
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


    class CaseexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_caseexpr




    def caseexpr(self):

        localctx = TyCParser.CaseexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_caseexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)

        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_breakstmt




    def breakstmt(self):

        localctx = TyCParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(TyCParser.BREAK)
            self.state = 471
            self.match(TyCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_continuestmt




    def continuestmt(self):

        localctx = TyCParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(TyCParser.CONTINUE)
            self.state = 474
            self.match(TyCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_returnstmt




    def returnstmt(self):

        localctx = TyCParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_returnstmt)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                self.match(TyCParser.RETURN)
                self.state = 477
                self.expr()
                self.state = 478
                self.match(TyCParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.match(TyCParser.RETURN)
                self.state = 481
                self.match(TyCParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SM(self):
            return self.getToken(TyCParser.SM, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exprstmt




    def exprstmt(self):

        localctx = TyCParser.ExprstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_exprstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.expr()
            self.state = 485
            self.match(TyCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expr1_sempred
        self._predicates[22] = self.expr2_sempred
        self._predicates[23] = self.expr3_sempred
        self._predicates[24] = self.expr4_sempred
        self._predicates[25] = self.expr5_sempred
        self._predicates[26] = self.expr6_sempred
        self._predicates[29] = self.expr9_sempred
        self._predicates[30] = self.expr10_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 2)
         

    def expr10_sempred(self, localctx:Expr10Context, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 2)
         




