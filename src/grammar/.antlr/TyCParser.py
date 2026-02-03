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
        buf.write("\u01e9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3l\n\3\3\4\3\4\3\4\5\4q\n\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6\u0086\n\6\3\7\3\7\5\7\u008a\n\7\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u0090\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u0097\n\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00a0\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00af")
        buf.write("\n\r\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00be\n\20\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u00c4\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00cb\n\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00db\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\5\25\u00e6\n\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00ed\n\26\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u00f4\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00fc")
        buf.write("\n\30\f\30\16\30\u00ff\13\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\7\31\u0107\n\31\f\31\16\31\u010a\13\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0115\n\32\f")
        buf.write("\32\16\32\u0118\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0129")
        buf.write("\n\33\f\33\16\33\u012c\13\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\7\34\u0137\n\34\f\34\16\34\u013a")
        buf.write("\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\7\35\u0148\n\35\f\35\16\35\u014b\13\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0154\n\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u015b\n\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \7 \u0164\n \f \16 \u0167\13 \3!\3!\3!\3!\3!\3!\7")
        buf.write("!\u016f\n!\f!\16!\u0172\13!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\5\"\u017d\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\5#\u018b\n#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\5%\u019f\n%\3&\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\5(\u01b4")
        buf.write("\n(\3)\3)\5)\u01b8\n)\3*\3*\5*\u01bc\n*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\5,\u01ca\n,\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\5-\u01d4\n-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\5\61\u01e4\n\61\3\62\3\62\3\62")
        buf.write("\3\62\2\n.\60\62\64\668>@\63\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`b\2\3\6\2\t\t\f\f\16\16,,\2\u01f4\2d\3\2\2\2\4k\3\2")
        buf.write("\2\2\6p\3\2\2\2\br\3\2\2\2\n\u0085\3\2\2\2\f\u0089\3\2")
        buf.write("\2\2\16\u008f\3\2\2\2\20\u0096\3\2\2\2\22\u0098\3\2\2")
        buf.write("\2\24\u009f\3\2\2\2\26\u00a1\3\2\2\2\30\u00ae\3\2\2\2")
        buf.write("\32\u00b0\3\2\2\2\34\u00b2\3\2\2\2\36\u00bd\3\2\2\2 \u00c3")
        buf.write("\3\2\2\2\"\u00ca\3\2\2\2$\u00da\3\2\2\2&\u00dc\3\2\2\2")
        buf.write("(\u00e5\3\2\2\2*\u00ec\3\2\2\2,\u00f3\3\2\2\2.\u00f5\3")
        buf.write("\2\2\2\60\u0100\3\2\2\2\62\u010b\3\2\2\2\64\u0119\3\2")
        buf.write("\2\2\66\u012d\3\2\2\28\u013b\3\2\2\2:\u0153\3\2\2\2<\u015a")
        buf.write("\3\2\2\2>\u015c\3\2\2\2@\u0168\3\2\2\2B\u017c\3\2\2\2")
        buf.write("D\u018a\3\2\2\2F\u018c\3\2\2\2H\u019e\3\2\2\2J\u01a0\3")
        buf.write("\2\2\2L\u01a6\3\2\2\2N\u01b3\3\2\2\2P\u01b7\3\2\2\2R\u01bb")
        buf.write("\3\2\2\2T\u01bd\3\2\2\2V\u01c9\3\2\2\2X\u01d3\3\2\2\2")
        buf.write("Z\u01d5\3\2\2\2\\\u01d7\3\2\2\2^\u01da\3\2\2\2`\u01e3")
        buf.write("\3\2\2\2b\u01e5\3\2\2\2de\5\4\3\2ef\7\2\2\3f\3\3\2\2\2")
        buf.write("gh\5\6\4\2hi\5\4\3\2il\3\2\2\2jl\3\2\2\2kg\3\2\2\2kj\3")
        buf.write("\2\2\2l\5\3\2\2\2mq\5$\23\2nq\5\n\6\2oq\5\26\f\2pm\3\2")
        buf.write("\2\2pn\3\2\2\2po\3\2\2\2q\7\3\2\2\2rs\t\2\2\2s\t\3\2\2")
        buf.write("\2tu\5\f\7\2uv\7,\2\2vw\7%\2\2wx\5\16\b\2xy\7&\2\2yz\7")
        buf.write("\'\2\2z{\5\24\13\2{|\7(\2\2|\u0086\3\2\2\2}~\7,\2\2~\177")
        buf.write("\7%\2\2\177\u0080\5\16\b\2\u0080\u0081\7&\2\2\u0081\u0082")
        buf.write("\7\'\2\2\u0082\u0083\5\24\13\2\u0083\u0084\7(\2\2\u0084")
        buf.write("\u0086\3\2\2\2\u0085t\3\2\2\2\u0085}\3\2\2\2\u0086\13")
        buf.write("\3\2\2\2\u0087\u008a\5\b\5\2\u0088\u008a\7\21\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\r\3\2\2\2\u008b")
        buf.write("\u008c\5\22\n\2\u008c\u008d\5\20\t\2\u008d\u0090\3\2\2")
        buf.write("\2\u008e\u0090\3\2\2\2\u008f\u008b\3\2\2\2\u008f\u008e")
        buf.write("\3\2\2\2\u0090\17\3\2\2\2\u0091\u0092\7)\2\2\u0092\u0093")
        buf.write("\5\22\n\2\u0093\u0094\5\20\t\2\u0094\u0097\3\2\2\2\u0095")
        buf.write("\u0097\3\2\2\2\u0096\u0091\3\2\2\2\u0096\u0095\3\2\2\2")
        buf.write("\u0097\21\3\2\2\2\u0098\u0099\5\b\5\2\u0099\u009a\7,\2")
        buf.write("\2\u009a\23\3\2\2\2\u009b\u009c\5D#\2\u009c\u009d\5\24")
        buf.write("\13\2\u009d\u00a0\3\2\2\2\u009e\u00a0\3\2\2\2\u009f\u009b")
        buf.write("\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\25\3\2\2\2\u00a1\u00a2")
        buf.write("\7\17\2\2\u00a2\u00a3\7,\2\2\u00a3\u00a4\7\'\2\2\u00a4")
        buf.write("\u00a5\5\30\r\2\u00a5\u00a6\7(\2\2\u00a6\u00a7\7*\2\2")
        buf.write("\u00a7\27\3\2\2\2\u00a8\u00a9\5\32\16\2\u00a9\u00aa\7")
        buf.write(",\2\2\u00aa\u00ab\7*\2\2\u00ab\u00ac\5\30\r\2\u00ac\u00af")
        buf.write("\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00a8\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\31\3\2\2\2\u00b0\u00b1\5\b\5\2\u00b1")
        buf.write("\33\3\2\2\2\u00b2\u00b3\7,\2\2\u00b3\u00b4\5\36\20\2\u00b4")
        buf.write("\u00b5\7*\2\2\u00b5\35\3\2\2\2\u00b6\u00be\7,\2\2\u00b7")
        buf.write("\u00b8\7,\2\2\u00b8\u00b9\7#\2\2\u00b9\u00ba\7\'\2\2\u00ba")
        buf.write("\u00bb\5 \21\2\u00bb\u00bc\7(\2\2\u00bc\u00be\3\2\2\2")
        buf.write("\u00bd\u00b6\3\2\2\2\u00bd\u00b7\3\2\2\2\u00be\37\3\2")
        buf.write("\2\2\u00bf\u00c0\5,\27\2\u00c0\u00c1\5\"\22\2\u00c1\u00c4")
        buf.write("\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00bf\3\2\2\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4!\3\2\2\2\u00c5\u00c6\7)\2\2\u00c6")
        buf.write("\u00c7\5,\27\2\u00c7\u00c8\5\"\22\2\u00c8\u00cb\3\2\2")
        buf.write("\2\u00c9\u00cb\3\2\2\2\u00ca\u00c5\3\2\2\2\u00ca\u00c9")
        buf.write("\3\2\2\2\u00cb#\3\2\2\2\u00cc\u00cd\7\3\2\2\u00cd\u00ce")
        buf.write("\7,\2\2\u00ce\u00cf\7#\2\2\u00cf\u00db\5,\27\2\u00d0\u00d1")
        buf.write("\7\3\2\2\u00d1\u00db\7,\2\2\u00d2\u00d3\5\b\5\2\u00d3")
        buf.write("\u00d4\7,\2\2\u00d4\u00d5\7#\2\2\u00d5\u00d6\5,\27\2\u00d6")
        buf.write("\u00db\3\2\2\2\u00d7\u00d8\5\b\5\2\u00d8\u00d9\7,\2\2")
        buf.write("\u00d9\u00db\3\2\2\2\u00da\u00cc\3\2\2\2\u00da\u00d0\3")
        buf.write("\2\2\2\u00da\u00d2\3\2\2\2\u00da\u00d7\3\2\2\2\u00db%")
        buf.write("\3\2\2\2\u00dc\u00dd\7,\2\2\u00dd\u00de\7%\2\2\u00de\u00df")
        buf.write("\5(\25\2\u00df\u00e0\7&\2\2\u00e0\'\3\2\2\2\u00e1\u00e2")
        buf.write("\5,\27\2\u00e2\u00e3\5*\26\2\u00e3\u00e6\3\2\2\2\u00e4")
        buf.write("\u00e6\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e6)\3\2\2\2\u00e7\u00e8\7)\2\2\u00e8\u00e9\5,\27\2")
        buf.write("\u00e9\u00ea\5*\26\2\u00ea\u00ed\3\2\2\2\u00eb\u00ed\3")
        buf.write("\2\2\2\u00ec\u00e7\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed+")
        buf.write("\3\2\2\2\u00ee\u00ef\5.\30\2\u00ef\u00f0\7#\2\2\u00f0")
        buf.write("\u00f1\5,\27\2\u00f1\u00f4\3\2\2\2\u00f2\u00f4\5.\30\2")
        buf.write("\u00f3\u00ee\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4-\3\2\2")
        buf.write("\2\u00f5\u00f6\b\30\1\2\u00f6\u00f7\5\60\31\2\u00f7\u00fd")
        buf.write("\3\2\2\2\u00f8\u00f9\f\4\2\2\u00f9\u00fa\7\36\2\2\u00fa")
        buf.write("\u00fc\5\60\31\2\u00fb\u00f8\3\2\2\2\u00fc\u00ff\3\2\2")
        buf.write("\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe/\3\2")
        buf.write("\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101\b\31\1\2\u0101\u0102")
        buf.write("\5\62\32\2\u0102\u0108\3\2\2\2\u0103\u0104\f\4\2\2\u0104")
        buf.write("\u0105\7\37\2\2\u0105\u0107\5\62\32\2\u0106\u0103\3\2")
        buf.write("\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\61\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c")
        buf.write("\b\32\1\2\u010c\u010d\5\64\33\2\u010d\u0116\3\2\2\2\u010e")
        buf.write("\u010f\f\5\2\2\u010f\u0110\7\30\2\2\u0110\u0115\5\64\33")
        buf.write("\2\u0111\u0112\f\4\2\2\u0112\u0113\7\31\2\2\u0113\u0115")
        buf.write("\5\64\33\2\u0114\u010e\3\2\2\2\u0114\u0111\3\2\2\2\u0115")
        buf.write("\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\63\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\b\33")
        buf.write("\1\2\u011a\u011b\5\66\34\2\u011b\u012a\3\2\2\2\u011c\u011d")
        buf.write("\f\7\2\2\u011d\u011e\7\32\2\2\u011e\u0129\5\66\34\2\u011f")
        buf.write("\u0120\f\6\2\2\u0120\u0121\7\34\2\2\u0121\u0129\5\66\34")
        buf.write("\2\u0122\u0123\f\5\2\2\u0123\u0124\7\33\2\2\u0124\u0129")
        buf.write("\5\66\34\2\u0125\u0126\f\4\2\2\u0126\u0127\7\35\2\2\u0127")
        buf.write("\u0129\5\66\34\2\u0128\u011c\3\2\2\2\u0128\u011f\3\2\2")
        buf.write("\2\u0128\u0122\3\2\2\2\u0128\u0125\3\2\2\2\u0129\u012c")
        buf.write("\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("\65\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u012e\b\34\1\2\u012e")
        buf.write("\u012f\58\35\2\u012f\u0138\3\2\2\2\u0130\u0131\f\5\2\2")
        buf.write("\u0131\u0132\7\23\2\2\u0132\u0137\58\35\2\u0133\u0134")
        buf.write("\f\4\2\2\u0134\u0135\7\24\2\2\u0135\u0137\58\35\2\u0136")
        buf.write("\u0130\3\2\2\2\u0136\u0133\3\2\2\2\u0137\u013a\3\2\2\2")
        buf.write("\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\67\3\2")
        buf.write("\2\2\u013a\u0138\3\2\2\2\u013b\u013c\b\35\1\2\u013c\u013d")
        buf.write("\5:\36\2\u013d\u0149\3\2\2\2\u013e\u013f\f\6\2\2\u013f")
        buf.write("\u0140\7\25\2\2\u0140\u0148\5:\36\2\u0141\u0142\f\5\2")
        buf.write("\2\u0142\u0143\7\26\2\2\u0143\u0148\5:\36\2\u0144\u0145")
        buf.write("\f\4\2\2\u0145\u0146\7\27\2\2\u0146\u0148\5:\36\2\u0147")
        buf.write("\u013e\3\2\2\2\u0147\u0141\3\2\2\2\u0147\u0144\3\2\2\2")
        buf.write("\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3")
        buf.write("\2\2\2\u014a9\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d")
        buf.write("\7 \2\2\u014d\u0154\5:\36\2\u014e\u014f\7\23\2\2\u014f")
        buf.write("\u0154\5:\36\2\u0150\u0151\7\24\2\2\u0151\u0154\5:\36")
        buf.write("\2\u0152\u0154\5<\37\2\u0153\u014c\3\2\2\2\u0153\u014e")
        buf.write("\3\2\2\2\u0153\u0150\3\2\2\2\u0153\u0152\3\2\2\2\u0154")
        buf.write(";\3\2\2\2\u0155\u0156\7!\2\2\u0156\u015b\5<\37\2\u0157")
        buf.write("\u0158\7\"\2\2\u0158\u015b\5<\37\2\u0159\u015b\5> \2\u015a")
        buf.write("\u0155\3\2\2\2\u015a\u0157\3\2\2\2\u015a\u0159\3\2\2\2")
        buf.write("\u015b=\3\2\2\2\u015c\u015d\b \1\2\u015d\u015e\5@!\2\u015e")
        buf.write("\u0165\3\2\2\2\u015f\u0160\f\5\2\2\u0160\u0164\7!\2\2")
        buf.write("\u0161\u0162\f\4\2\2\u0162\u0164\7\"\2\2\u0163\u015f\3")
        buf.write("\2\2\2\u0163\u0161\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166?\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0168\u0169\b!\1\2\u0169\u016a\5B\"\2\u016a\u0170")
        buf.write("\3\2\2\2\u016b\u016c\f\4\2\2\u016c\u016d\7$\2\2\u016d")
        buf.write("\u016f\5B\"\2\u016e\u016b\3\2\2\2\u016f\u0172\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171A\3\2\2")
        buf.write("\2\u0172\u0170\3\2\2\2\u0173\u017d\7-\2\2\u0174\u017d")
        buf.write("\7.\2\2\u0175\u017d\7/\2\2\u0176\u017d\7,\2\2\u0177\u017d")
        buf.write("\5&\24\2\u0178\u0179\7%\2\2\u0179\u017a\5,\27\2\u017a")
        buf.write("\u017b\7&\2\2\u017b\u017d\3\2\2\2\u017c\u0173\3\2\2\2")
        buf.write("\u017c\u0174\3\2\2\2\u017c\u0175\3\2\2\2\u017c\u0176\3")
        buf.write("\2\2\2\u017c\u0177\3\2\2\2\u017c\u0178\3\2\2\2\u017dC")
        buf.write("\3\2\2\2\u017e\u017f\5$\23\2\u017f\u0180\7*\2\2\u0180")
        buf.write("\u018b\3\2\2\2\u0181\u018b\5F$\2\u0182\u018b\5H%\2\u0183")
        buf.write("\u018b\5J&\2\u0184\u018b\5L\'\2\u0185\u018b\5T+\2\u0186")
        buf.write("\u018b\5\\/\2\u0187\u018b\5^\60\2\u0188\u018b\5`\61\2")
        buf.write("\u0189\u018b\5b\62\2\u018a\u017e\3\2\2\2\u018a\u0181\3")
        buf.write("\2\2\2\u018a\u0182\3\2\2\2\u018a\u0183\3\2\2\2\u018a\u0184")
        buf.write("\3\2\2\2\u018a\u0185\3\2\2\2\u018a\u0186\3\2\2\2\u018a")
        buf.write("\u0187\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u0189\3\2\2\2")
        buf.write("\u018bE\3\2\2\2\u018c\u018d\7\'\2\2\u018d\u018e\5\24\13")
        buf.write("\2\u018e\u018f\7(\2\2\u018fG\3\2\2\2\u0190\u0191\7\13")
        buf.write("\2\2\u0191\u0192\7%\2\2\u0192\u0193\5,\27\2\u0193\u0194")
        buf.write("\7&\2\2\u0194\u0195\5D#\2\u0195\u019f\3\2\2\2\u0196\u0197")
        buf.write("\7\13\2\2\u0197\u0198\7%\2\2\u0198\u0199\5,\27\2\u0199")
        buf.write("\u019a\7&\2\2\u019a\u019b\5D#\2\u019b\u019c\7\b\2\2\u019c")
        buf.write("\u019d\5D#\2\u019d\u019f\3\2\2\2\u019e\u0190\3\2\2\2\u019e")
        buf.write("\u0196\3\2\2\2\u019fI\3\2\2\2\u01a0\u01a1\7\22\2\2\u01a1")
        buf.write("\u01a2\7%\2\2\u01a2\u01a3\5,\27\2\u01a3\u01a4\7&\2\2\u01a4")
        buf.write("\u01a5\5D#\2\u01a5K\3\2\2\2\u01a6\u01a7\7\n\2\2\u01a7")
        buf.write("\u01a8\7%\2\2\u01a8\u01a9\5N(\2\u01a9\u01aa\7*\2\2\u01aa")
        buf.write("\u01ab\5P)\2\u01ab\u01ac\7*\2\2\u01ac\u01ad\5R*\2\u01ad")
        buf.write("\u01ae\7&\2\2\u01ae\u01af\5D#\2\u01afM\3\2\2\2\u01b0\u01b4")
        buf.write("\5$\23\2\u01b1\u01b4\5,\27\2\u01b2\u01b4\3\2\2\2\u01b3")
        buf.write("\u01b0\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2")
        buf.write("\u01b4O\3\2\2\2\u01b5\u01b8\5,\27\2\u01b6\u01b8\3\2\2")
        buf.write("\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8Q\3\2")
        buf.write("\2\2\u01b9\u01bc\5,\27\2\u01ba\u01bc\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bcS\3\2\2\2\u01bd\u01be")
        buf.write("\7\20\2\2\u01be\u01bf\7%\2\2\u01bf\u01c0\5,\27\2\u01c0")
        buf.write("\u01c1\7&\2\2\u01c1\u01c2\7\'\2\2\u01c2\u01c3\5V,\2\u01c3")
        buf.write("\u01c4\7(\2\2\u01c4U\3\2\2\2\u01c5\u01c6\5X-\2\u01c6\u01c7")
        buf.write("\5V,\2\u01c7\u01ca\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c5")
        buf.write("\3\2\2\2\u01c9\u01c8\3\2\2\2\u01caW\3\2\2\2\u01cb\u01cc")
        buf.write("\7\5\2\2\u01cc\u01cd\5Z.\2\u01cd\u01ce\7+\2\2\u01ce\u01cf")
        buf.write("\5\24\13\2\u01cf\u01d4\3\2\2\2\u01d0\u01d1\7\7\2\2\u01d1")
        buf.write("\u01d2\7+\2\2\u01d2\u01d4\5\24\13\2\u01d3\u01cb\3\2\2")
        buf.write("\2\u01d3\u01d0\3\2\2\2\u01d4Y\3\2\2\2\u01d5\u01d6\5,\27")
        buf.write("\2\u01d6[\3\2\2\2\u01d7\u01d8\7\4\2\2\u01d8\u01d9\7*\2")
        buf.write("\2\u01d9]\3\2\2\2\u01da\u01db\7\6\2\2\u01db\u01dc\7*\2")
        buf.write("\2\u01dc_\3\2\2\2\u01dd\u01de\7\r\2\2\u01de\u01df\5,\27")
        buf.write("\2\u01df\u01e0\7*\2\2\u01e0\u01e4\3\2\2\2\u01e1\u01e2")
        buf.write("\7\r\2\2\u01e2\u01e4\7*\2\2\u01e3\u01dd\3\2\2\2\u01e3")
        buf.write("\u01e1\3\2\2\2\u01e4a\3\2\2\2\u01e5\u01e6\5,\27\2\u01e6")
        buf.write("\u01e7\7*\2\2\u01e7c\3\2\2\2)kp\u0085\u0089\u008f\u0096")
        buf.write("\u009f\u00ae\u00bd\u00c3\u00ca\u00da\u00e5\u00ec\u00f3")
        buf.write("\u00fd\u0108\u0114\u0116\u0128\u012a\u0136\u0138\u0147")
        buf.write("\u0149\u0153\u015a\u0163\u0165\u0170\u017c\u018a\u019e")
        buf.write("\u01b3\u01b7\u01bb\u01c9\u01d3\u01e3")
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
    RULE_funccalldecl = 18
    RULE_arglist = 19
    RULE_argtail = 20
    RULE_expr = 21
    RULE_expr1 = 22
    RULE_expr2 = 23
    RULE_expr3 = 24
    RULE_expr4 = 25
    RULE_expr5 = 26
    RULE_expr6 = 27
    RULE_expr7 = 28
    RULE_expr8 = 29
    RULE_expr9 = 30
    RULE_expr10 = 31
    RULE_expr11 = 32
    RULE_stmt = 33
    RULE_blockstmt = 34
    RULE_ifstmt = 35
    RULE_whilestmt = 36
    RULE_forstmt = 37
    RULE_init = 38
    RULE_cond = 39
    RULE_updt = 40
    RULE_switchstmt = 41
    RULE_caselist = 42
    RULE_caseclause = 43
    RULE_caseexpr = 44
    RULE_breakstmt = 45
    RULE_continuestmt = 46
    RULE_returnstmt = 47
    RULE_exprstmt = 48

    ruleNames =  [ "program", "manydecls", "decl", "typ", "funcdecl", "rettyp", 
                   "paramlist", "paramtail", "pardecl", "stmtlist", "structdecl", 
                   "memlist", "memtyp", "structvardecl", "structvar", "exprlist", 
                   "exprtail", "vardecl", "funccalldecl", "arglist", "argtail", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
                   "stmt", "blockstmt", "ifstmt", "whilestmt", "forstmt", 
                   "init", "cond", "updt", "switchstmt", "caselist", "caseclause", 
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
            self.state = 98
            self.manydecls()
            self.state = 99
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
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.AUTO, TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.STRUCT, TyCParser.VOID, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.decl()
                self.state = 102
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

        def vardecl(self):
            return self.getTypedRuleContext(TyCParser.VardeclContext,0)


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
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.funcdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.structdecl()
                pass


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
            self.state = 112
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.rettyp()
                self.state = 115
                self.match(TyCParser.ID)
                self.state = 116
                self.match(TyCParser.LP)
                self.state = 117
                self.paramlist()
                self.state = 118
                self.match(TyCParser.RP)
                self.state = 119
                self.match(TyCParser.LB)
                self.state = 120
                self.stmtlist()
                self.state = 121
                self.match(TyCParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(TyCParser.ID)
                self.state = 124
                self.match(TyCParser.LP)
                self.state = 125
                self.paramlist()
                self.state = 126
                self.match(TyCParser.RP)
                self.state = 127
                self.match(TyCParser.LB)
                self.state = 128
                self.stmtlist()
                self.state = 129
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
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.typ()
                pass
            elif token in [TyCParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
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
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.pardecl()
                self.state = 138
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(TyCParser.CM)
                self.state = 144
                self.pardecl()
                self.state = 145
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
            self.state = 150
            self.typ()
            self.state = 151
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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.AUTO, TyCParser.BREAK, TyCParser.CONTINUE, TyCParser.FLOAT, TyCParser.FOR, TyCParser.IF, TyCParser.INT, TyCParser.RETURN, TyCParser.STRING, TyCParser.SWITCH, TyCParser.WHILE, TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.stmt()
                self.state = 154
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
            self.state = 159
            self.match(TyCParser.STRUCT)
            self.state = 160
            self.match(TyCParser.ID)
            self.state = 161
            self.match(TyCParser.LB)
            self.state = 162
            self.memlist()
            self.state = 163
            self.match(TyCParser.RB)
            self.state = 164
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
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.memtyp()
                self.state = 167
                self.match(TyCParser.ID)
                self.state = 168
                self.match(TyCParser.SM)
                self.state = 169
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
            self.state = 174
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
            self.state = 176
            self.match(TyCParser.ID)
            self.state = 177
            self.structvar()
            self.state = 178
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
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(TyCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(TyCParser.ID)
                self.state = 182
                self.match(TyCParser.ASSIGN)
                self.state = 183
                self.match(TyCParser.LB)
                self.state = 184
                self.exprlist()
                self.state = 185
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
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.expr()
                self.state = 190
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
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(TyCParser.CM)
                self.state = 196
                self.expr()
                self.state = 197
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
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(TyCParser.AUTO)
                self.state = 203
                self.match(TyCParser.ID)
                self.state = 204
                self.match(TyCParser.ASSIGN)
                self.state = 205
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(TyCParser.AUTO)
                self.state = 207
                self.match(TyCParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.typ()
                self.state = 209
                self.match(TyCParser.ID)
                self.state = 210
                self.match(TyCParser.ASSIGN)
                self.state = 211
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.typ()
                self.state = 214
                self.match(TyCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccalldeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def arglist(self):
            return self.getTypedRuleContext(TyCParser.ArglistContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_funccalldecl




    def funccalldecl(self):

        localctx = TyCParser.FunccalldeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funccalldecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(TyCParser.ID)
            self.state = 219
            self.match(TyCParser.LP)
            self.state = 220
            self.arglist()
            self.state = 221
            self.match(TyCParser.RP)
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
        self.enterRule(localctx, 38, self.RULE_arglist)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.expr()
                self.state = 224
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
        self.enterRule(localctx, 40, self.RULE_argtail)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(TyCParser.CM)
                self.state = 230
                self.expr()
                self.state = 231
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
        self.enterRule(localctx, 42, self.RULE_expr)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.expr1(0)
                self.state = 237
                self.match(TyCParser.ASSIGN)
                self.state = 238
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 246
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 247
                    self.match(TyCParser.OR)
                    self.state = 248
                    self.expr2(0) 
                self.state = 253
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 257
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 258
                    self.match(TyCParser.AND)
                    self.state = 259
                    self.expr3(0) 
                self.state = 264
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 274
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 268
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 269
                        self.match(TyCParser.EQUAL)
                        self.state = 270
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 271
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 272
                        self.match(TyCParser.NOTEQUAL)
                        self.state = 273
                        self.expr4(0)
                        pass

             
                self.state = 278
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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 294
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 282
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 283
                        self.match(TyCParser.LESSTHAN)
                        self.state = 284
                        self.expr5(0)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 285
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 286
                        self.match(TyCParser.LESSTHAN_EQUAL)
                        self.state = 287
                        self.expr5(0)
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 288
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 289
                        self.match(TyCParser.GREATERTHAN)
                        self.state = 290
                        self.expr5(0)
                        pass

                    elif la_ == 4:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 291
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 292
                        self.match(TyCParser.GREATERTHAN_EQUAL)
                        self.state = 293
                        self.expr5(0)
                        pass

             
                self.state = 298
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.expr6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 308
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 302
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 303
                        self.match(TyCParser.ADD)
                        self.state = 304
                        self.expr6(0)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 305
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 306
                        self.match(TyCParser.SUB)
                        self.state = 307
                        self.expr6(0)
                        pass

             
                self.state = 312
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 325
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 316
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 317
                        self.match(TyCParser.MUL)
                        self.state = 318
                        self.expr7()
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 319
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 320
                        self.match(TyCParser.DIV)
                        self.state = 321
                        self.expr7()
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 322
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 323
                        self.match(TyCParser.MOD)
                        self.state = 324
                        self.expr7()
                        pass

             
                self.state = 329
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
        self.enterRule(localctx, 56, self.RULE_expr7)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(TyCParser.NOT)
                self.state = 331
                self.expr7()
                pass
            elif token in [TyCParser.ADD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(TyCParser.ADD)
                self.state = 333
                self.expr7()
                pass
            elif token in [TyCParser.SUB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
                self.match(TyCParser.SUB)
                self.state = 335
                self.expr7()
                pass
            elif token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 336
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
        self.enterRule(localctx, 58, self.RULE_expr8)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(TyCParser.INCREMENT)
                self.state = 340
                self.expr8()
                pass
            elif token in [TyCParser.DECREMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(TyCParser.DECREMENT)
                self.state = 342
                self.expr8()
                pass
            elif token in [TyCParser.LP, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.expr10(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 353
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 349
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 350
                        self.match(TyCParser.INCREMENT)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 351
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 352
                        self.match(TyCParser.DECREMENT)
                        pass

             
                self.state = 357
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


        def ACCESS(self):
            return self.getToken(TyCParser.ACCESS, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr10



    def expr10(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr10Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr10, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.expr11()
            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr10Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr10)
                    self.state = 361
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 362
                    self.match(TyCParser.ACCESS)
                    self.state = 363
                    self.expr11() 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def funccalldecl(self):
            return self.getTypedRuleContext(TyCParser.FunccalldeclContext,0)


        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr11




    def expr11(self):

        localctx = TyCParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr11)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(TyCParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(TyCParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.match(TyCParser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
                self.match(TyCParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 373
                self.funccalldecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 374
                self.match(TyCParser.LP)
                self.state = 375
                self.expr()
                self.state = 376
                self.match(TyCParser.RP)
                pass


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
        self.enterRule(localctx, 66, self.RULE_stmt)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
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
                self.blockstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 386
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 387
                self.switchstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 388
                self.breakstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 389
                self.continuestmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 390
                self.returnstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 391
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
        self.enterRule(localctx, 68, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(TyCParser.LB)
            self.state = 395
            self.stmtlist()
            self.state = 396
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
        self.enterRule(localctx, 70, self.RULE_ifstmt)
        try:
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(TyCParser.IF)
                self.state = 399
                self.match(TyCParser.LP)
                self.state = 400
                self.expr()
                self.state = 401
                self.match(TyCParser.RP)
                self.state = 402
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(TyCParser.IF)
                self.state = 405
                self.match(TyCParser.LP)
                self.state = 406
                self.expr()
                self.state = 407
                self.match(TyCParser.RP)
                self.state = 408
                self.stmt()
                self.state = 409
                self.match(TyCParser.ELSE)
                self.state = 410
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
        self.enterRule(localctx, 72, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(TyCParser.WHILE)
            self.state = 415
            self.match(TyCParser.LP)
            self.state = 416
            self.expr()
            self.state = 417
            self.match(TyCParser.RP)
            self.state = 418
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
        self.enterRule(localctx, 74, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(TyCParser.FOR)
            self.state = 421
            self.match(TyCParser.LP)
            self.state = 422
            self.init()
            self.state = 423
            self.match(TyCParser.SM)
            self.state = 424
            self.cond()
            self.state = 425
            self.match(TyCParser.SM)
            self.state = 426
            self.updt()
            self.state = 427
            self.match(TyCParser.RP)
            self.state = 428
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
        self.enterRule(localctx, 76, self.RULE_init)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
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
        self.enterRule(localctx, 78, self.RULE_cond)
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
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
        self.enterRule(localctx, 80, self.RULE_updt)
        try:
            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
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
        self.enterRule(localctx, 82, self.RULE_switchstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(TyCParser.SWITCH)
            self.state = 444
            self.match(TyCParser.LP)
            self.state = 445
            self.expr()
            self.state = 446
            self.match(TyCParser.RP)
            self.state = 447
            self.match(TyCParser.LB)
            self.state = 448
            self.caselist()
            self.state = 449
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
        self.enterRule(localctx, 84, self.RULE_caselist)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CASE, TyCParser.DEFAULT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.caseclause()
                self.state = 452
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
        self.enterRule(localctx, 86, self.RULE_caseclause)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(TyCParser.CASE)
                self.state = 458
                self.caseexpr()
                self.state = 459
                self.match(TyCParser.CL)
                self.state = 460
                self.stmtlist()
                pass
            elif token in [TyCParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.match(TyCParser.DEFAULT)
                self.state = 463
                self.match(TyCParser.CL)
                self.state = 464
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
        self.enterRule(localctx, 88, self.RULE_caseexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
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
        self.enterRule(localctx, 90, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(TyCParser.BREAK)
            self.state = 470
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
        self.enterRule(localctx, 92, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(TyCParser.CONTINUE)
            self.state = 473
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
        self.enterRule(localctx, 94, self.RULE_returnstmt)
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.match(TyCParser.RETURN)
                self.state = 476
                self.expr()
                self.state = 477
                self.match(TyCParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.match(TyCParser.RETURN)
                self.state = 480
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
        self.enterRule(localctx, 96, self.RULE_exprstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.expr()
            self.state = 484
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
        self._predicates[22] = self.expr1_sempred
        self._predicates[23] = self.expr2_sempred
        self._predicates[24] = self.expr3_sempred
        self._predicates[25] = self.expr4_sempred
        self._predicates[26] = self.expr5_sempred
        self._predicates[27] = self.expr6_sempred
        self._predicates[30] = self.expr9_sempred
        self._predicates[31] = self.expr10_sempred
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
                return self.precpred(self._ctx, 2)
         




