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
        buf.write("\u01ed\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3l\n\3\3\4\3\4\5\4p\n\4\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u0085\n\6\3\7\3\7\5\7\u0089\n\7\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u008f\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u0096\n\t\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\5\13\u009f\n\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ae\n\r")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00bd\n\20\3\21\3\21\3\21\3\21\5\21\u00c3")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00ca\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00da\n\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u00e5\n\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u00ec\n\26\3\27\3\27\3\27\3\27\3\27\5\27\u00f3")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00fb\n\30\f")
        buf.write("\30\16\30\u00fe\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u0106\n\31\f\31\16\31\u0109\13\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\7\32\u0114\n\32\f\32\16\32")
        buf.write("\u0117\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0128\n\33\f\33")
        buf.write("\16\33\u012b\13\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\7\34\u0136\n\34\f\34\16\34\u0139\13\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\7\35\u0147\n\35\f\35\16\35\u014a\13\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u0153\n\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\5\37\u015a\n\37\3 \3 \3 \3 \3 \3 \3 \7 \u0163")
        buf.write("\n \f \16 \u0166\13 \3!\3!\3!\3!\3!\3!\7!\u016e\n!\f!")
        buf.write("\16!\u0171\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0180\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\5#\u018f\n#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01a3\n%\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\5(")
        buf.write("\u01b8\n(\3)\3)\5)\u01bc\n)\3*\3*\5*\u01c0\n*\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3,\3,\3,\3,\5,\u01ce\n,\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\5-\u01d8\n-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\5\61\u01e8\n\61\3\62\3\62")
        buf.write("\3\62\3\62\2\n.\60\62\64\668>@\63\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`b\2\3\6\2\t\t\f\f\16\16,,\2\u01f9\2d\3\2\2\2\4")
        buf.write("k\3\2\2\2\6o\3\2\2\2\bq\3\2\2\2\n\u0084\3\2\2\2\f\u0088")
        buf.write("\3\2\2\2\16\u008e\3\2\2\2\20\u0095\3\2\2\2\22\u0097\3")
        buf.write("\2\2\2\24\u009e\3\2\2\2\26\u00a0\3\2\2\2\30\u00ad\3\2")
        buf.write("\2\2\32\u00af\3\2\2\2\34\u00b1\3\2\2\2\36\u00bc\3\2\2")
        buf.write("\2 \u00c2\3\2\2\2\"\u00c9\3\2\2\2$\u00d9\3\2\2\2&\u00db")
        buf.write("\3\2\2\2(\u00e4\3\2\2\2*\u00eb\3\2\2\2,\u00f2\3\2\2\2")
        buf.write(".\u00f4\3\2\2\2\60\u00ff\3\2\2\2\62\u010a\3\2\2\2\64\u0118")
        buf.write("\3\2\2\2\66\u012c\3\2\2\28\u013a\3\2\2\2:\u0152\3\2\2")
        buf.write("\2<\u0159\3\2\2\2>\u015b\3\2\2\2@\u0167\3\2\2\2B\u017f")
        buf.write("\3\2\2\2D\u018e\3\2\2\2F\u0190\3\2\2\2H\u01a2\3\2\2\2")
        buf.write("J\u01a4\3\2\2\2L\u01aa\3\2\2\2N\u01b7\3\2\2\2P\u01bb\3")
        buf.write("\2\2\2R\u01bf\3\2\2\2T\u01c1\3\2\2\2V\u01cd\3\2\2\2X\u01d7")
        buf.write("\3\2\2\2Z\u01d9\3\2\2\2\\\u01db\3\2\2\2^\u01de\3\2\2\2")
        buf.write("`\u01e7\3\2\2\2b\u01e9\3\2\2\2de\5\4\3\2ef\7\2\2\3f\3")
        buf.write("\3\2\2\2gh\5\6\4\2hi\5\4\3\2il\3\2\2\2jl\3\2\2\2kg\3\2")
        buf.write("\2\2kj\3\2\2\2l\5\3\2\2\2mp\5\n\6\2np\5\26\f\2om\3\2\2")
        buf.write("\2on\3\2\2\2p\7\3\2\2\2qr\t\2\2\2r\t\3\2\2\2st\5\f\7\2")
        buf.write("tu\7,\2\2uv\7%\2\2vw\5\16\b\2wx\7&\2\2xy\7\'\2\2yz\5\24")
        buf.write("\13\2z{\7(\2\2{\u0085\3\2\2\2|}\7,\2\2}~\7%\2\2~\177\5")
        buf.write("\16\b\2\177\u0080\7&\2\2\u0080\u0081\7\'\2\2\u0081\u0082")
        buf.write("\5\24\13\2\u0082\u0083\7(\2\2\u0083\u0085\3\2\2\2\u0084")
        buf.write("s\3\2\2\2\u0084|\3\2\2\2\u0085\13\3\2\2\2\u0086\u0089")
        buf.write("\5\b\5\2\u0087\u0089\7\21\2\2\u0088\u0086\3\2\2\2\u0088")
        buf.write("\u0087\3\2\2\2\u0089\r\3\2\2\2\u008a\u008b\5\22\n\2\u008b")
        buf.write("\u008c\5\20\t\2\u008c\u008f\3\2\2\2\u008d\u008f\3\2\2")
        buf.write("\2\u008e\u008a\3\2\2\2\u008e\u008d\3\2\2\2\u008f\17\3")
        buf.write("\2\2\2\u0090\u0091\7)\2\2\u0091\u0092\5\22\n\2\u0092\u0093")
        buf.write("\5\20\t\2\u0093\u0096\3\2\2\2\u0094\u0096\3\2\2\2\u0095")
        buf.write("\u0090\3\2\2\2\u0095\u0094\3\2\2\2\u0096\21\3\2\2\2\u0097")
        buf.write("\u0098\5\b\5\2\u0098\u0099\7,\2\2\u0099\23\3\2\2\2\u009a")
        buf.write("\u009b\5D#\2\u009b\u009c\5\24\13\2\u009c\u009f\3\2\2\2")
        buf.write("\u009d\u009f\3\2\2\2\u009e\u009a\3\2\2\2\u009e\u009d\3")
        buf.write("\2\2\2\u009f\25\3\2\2\2\u00a0\u00a1\7\17\2\2\u00a1\u00a2")
        buf.write("\7,\2\2\u00a2\u00a3\7\'\2\2\u00a3\u00a4\5\30\r\2\u00a4")
        buf.write("\u00a5\7(\2\2\u00a5\u00a6\7*\2\2\u00a6\27\3\2\2\2\u00a7")
        buf.write("\u00a8\5\32\16\2\u00a8\u00a9\7,\2\2\u00a9\u00aa\7*\2\2")
        buf.write("\u00aa\u00ab\5\30\r\2\u00ab\u00ae\3\2\2\2\u00ac\u00ae")
        buf.write("\3\2\2\2\u00ad\u00a7\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\31\3\2\2\2\u00af\u00b0\5\b\5\2\u00b0\33\3\2\2\2\u00b1")
        buf.write("\u00b2\7,\2\2\u00b2\u00b3\5\36\20\2\u00b3\u00b4\7*\2\2")
        buf.write("\u00b4\35\3\2\2\2\u00b5\u00bd\7,\2\2\u00b6\u00b7\7,\2")
        buf.write("\2\u00b7\u00b8\7#\2\2\u00b8\u00b9\7\'\2\2\u00b9\u00ba")
        buf.write("\5 \21\2\u00ba\u00bb\7(\2\2\u00bb\u00bd\3\2\2\2\u00bc")
        buf.write("\u00b5\3\2\2\2\u00bc\u00b6\3\2\2\2\u00bd\37\3\2\2\2\u00be")
        buf.write("\u00bf\5,\27\2\u00bf\u00c0\5\"\22\2\u00c0\u00c3\3\2\2")
        buf.write("\2\u00c1\u00c3\3\2\2\2\u00c2\u00be\3\2\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3!\3\2\2\2\u00c4\u00c5\7)\2\2\u00c5\u00c6")
        buf.write("\5,\27\2\u00c6\u00c7\5\"\22\2\u00c7\u00ca\3\2\2\2\u00c8")
        buf.write("\u00ca\3\2\2\2\u00c9\u00c4\3\2\2\2\u00c9\u00c8\3\2\2\2")
        buf.write("\u00ca#\3\2\2\2\u00cb\u00cc\7\3\2\2\u00cc\u00cd\7,\2\2")
        buf.write("\u00cd\u00ce\7#\2\2\u00ce\u00da\5,\27\2\u00cf\u00d0\7")
        buf.write("\3\2\2\u00d0\u00da\7,\2\2\u00d1\u00d2\5\b\5\2\u00d2\u00d3")
        buf.write("\7,\2\2\u00d3\u00d4\7#\2\2\u00d4\u00d5\5,\27\2\u00d5\u00da")
        buf.write("\3\2\2\2\u00d6\u00d7\5\b\5\2\u00d7\u00d8\7,\2\2\u00d8")
        buf.write("\u00da\3\2\2\2\u00d9\u00cb\3\2\2\2\u00d9\u00cf\3\2\2\2")
        buf.write("\u00d9\u00d1\3\2\2\2\u00d9\u00d6\3\2\2\2\u00da%\3\2\2")
        buf.write("\2\u00db\u00dc\7,\2\2\u00dc\u00dd\7%\2\2\u00dd\u00de\5")
        buf.write("(\25\2\u00de\u00df\7&\2\2\u00df\'\3\2\2\2\u00e0\u00e1")
        buf.write("\5,\27\2\u00e1\u00e2\5*\26\2\u00e2\u00e5\3\2\2\2\u00e3")
        buf.write("\u00e5\3\2\2\2\u00e4\u00e0\3\2\2\2\u00e4\u00e3\3\2\2\2")
        buf.write("\u00e5)\3\2\2\2\u00e6\u00e7\7)\2\2\u00e7\u00e8\5,\27\2")
        buf.write("\u00e8\u00e9\5*\26\2\u00e9\u00ec\3\2\2\2\u00ea\u00ec\3")
        buf.write("\2\2\2\u00eb\u00e6\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec+")
        buf.write("\3\2\2\2\u00ed\u00ee\5.\30\2\u00ee\u00ef\7#\2\2\u00ef")
        buf.write("\u00f0\5,\27\2\u00f0\u00f3\3\2\2\2\u00f1\u00f3\5.\30\2")
        buf.write("\u00f2\u00ed\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3-\3\2\2")
        buf.write("\2\u00f4\u00f5\b\30\1\2\u00f5\u00f6\5\60\31\2\u00f6\u00fc")
        buf.write("\3\2\2\2\u00f7\u00f8\f\4\2\2\u00f8\u00f9\7\36\2\2\u00f9")
        buf.write("\u00fb\5\60\31\2\u00fa\u00f7\3\2\2\2\u00fb\u00fe\3\2\2")
        buf.write("\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd/\3\2")
        buf.write("\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\b\31\1\2\u0100\u0101")
        buf.write("\5\62\32\2\u0101\u0107\3\2\2\2\u0102\u0103\f\4\2\2\u0103")
        buf.write("\u0104\7\37\2\2\u0104\u0106\5\62\32\2\u0105\u0102\3\2")
        buf.write("\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\61\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b")
        buf.write("\b\32\1\2\u010b\u010c\5\64\33\2\u010c\u0115\3\2\2\2\u010d")
        buf.write("\u010e\f\5\2\2\u010e\u010f\7\30\2\2\u010f\u0114\5\64\33")
        buf.write("\2\u0110\u0111\f\4\2\2\u0111\u0112\7\31\2\2\u0112\u0114")
        buf.write("\5\64\33\2\u0113\u010d\3\2\2\2\u0113\u0110\3\2\2\2\u0114")
        buf.write("\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\63\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\b\33")
        buf.write("\1\2\u0119\u011a\5\66\34\2\u011a\u0129\3\2\2\2\u011b\u011c")
        buf.write("\f\7\2\2\u011c\u011d\7\32\2\2\u011d\u0128\5\66\34\2\u011e")
        buf.write("\u011f\f\6\2\2\u011f\u0120\7\34\2\2\u0120\u0128\5\66\34")
        buf.write("\2\u0121\u0122\f\5\2\2\u0122\u0123\7\33\2\2\u0123\u0128")
        buf.write("\5\66\34\2\u0124\u0125\f\4\2\2\u0125\u0126\7\35\2\2\u0126")
        buf.write("\u0128\5\66\34\2\u0127\u011b\3\2\2\2\u0127\u011e\3\2\2")
        buf.write("\2\u0127\u0121\3\2\2\2\u0127\u0124\3\2\2\2\u0128\u012b")
        buf.write("\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a")
        buf.write("\65\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d\b\34\1\2\u012d")
        buf.write("\u012e\58\35\2\u012e\u0137\3\2\2\2\u012f\u0130\f\5\2\2")
        buf.write("\u0130\u0131\7\23\2\2\u0131\u0136\58\35\2\u0132\u0133")
        buf.write("\f\4\2\2\u0133\u0134\7\24\2\2\u0134\u0136\58\35\2\u0135")
        buf.write("\u012f\3\2\2\2\u0135\u0132\3\2\2\2\u0136\u0139\3\2\2\2")
        buf.write("\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\67\3\2")
        buf.write("\2\2\u0139\u0137\3\2\2\2\u013a\u013b\b\35\1\2\u013b\u013c")
        buf.write("\5:\36\2\u013c\u0148\3\2\2\2\u013d\u013e\f\6\2\2\u013e")
        buf.write("\u013f\7\25\2\2\u013f\u0147\5:\36\2\u0140\u0141\f\5\2")
        buf.write("\2\u0141\u0142\7\26\2\2\u0142\u0147\5:\36\2\u0143\u0144")
        buf.write("\f\4\2\2\u0144\u0145\7\27\2\2\u0145\u0147\5:\36\2\u0146")
        buf.write("\u013d\3\2\2\2\u0146\u0140\3\2\2\2\u0146\u0143\3\2\2\2")
        buf.write("\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3")
        buf.write("\2\2\2\u01499\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c")
        buf.write("\7 \2\2\u014c\u0153\5:\36\2\u014d\u014e\7\23\2\2\u014e")
        buf.write("\u0153\5:\36\2\u014f\u0150\7\24\2\2\u0150\u0153\5:\36")
        buf.write("\2\u0151\u0153\5<\37\2\u0152\u014b\3\2\2\2\u0152\u014d")
        buf.write("\3\2\2\2\u0152\u014f\3\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write(";\3\2\2\2\u0154\u0155\7!\2\2\u0155\u015a\5<\37\2\u0156")
        buf.write("\u0157\7\"\2\2\u0157\u015a\5<\37\2\u0158\u015a\5> \2\u0159")
        buf.write("\u0154\3\2\2\2\u0159\u0156\3\2\2\2\u0159\u0158\3\2\2\2")
        buf.write("\u015a=\3\2\2\2\u015b\u015c\b \1\2\u015c\u015d\5@!\2\u015d")
        buf.write("\u0164\3\2\2\2\u015e\u015f\f\5\2\2\u015f\u0163\7!\2\2")
        buf.write("\u0160\u0161\f\4\2\2\u0161\u0163\7\"\2\2\u0162\u015e\3")
        buf.write("\2\2\2\u0162\u0160\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165?\3\2\2\2\u0166\u0164")
        buf.write("\3\2\2\2\u0167\u0168\b!\1\2\u0168\u0169\5B\"\2\u0169\u016f")
        buf.write("\3\2\2\2\u016a\u016b\f\4\2\2\u016b\u016c\7$\2\2\u016c")
        buf.write("\u016e\5B\"\2\u016d\u016a\3\2\2\2\u016e\u0171\3\2\2\2")
        buf.write("\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170A\3\2\2")
        buf.write("\2\u0171\u016f\3\2\2\2\u0172\u0180\7-\2\2\u0173\u0180")
        buf.write("\7.\2\2\u0174\u0180\7/\2\2\u0175\u0180\7,\2\2\u0176\u0180")
        buf.write("\5&\24\2\u0177\u0178\7%\2\2\u0178\u0179\5,\27\2\u0179")
        buf.write("\u017a\7&\2\2\u017a\u0180\3\2\2\2\u017b\u017c\7\'\2\2")
        buf.write("\u017c\u017d\5 \21\2\u017d\u017e\7(\2\2\u017e\u0180\3")
        buf.write("\2\2\2\u017f\u0172\3\2\2\2\u017f\u0173\3\2\2\2\u017f\u0174")
        buf.write("\3\2\2\2\u017f\u0175\3\2\2\2\u017f\u0176\3\2\2\2\u017f")
        buf.write("\u0177\3\2\2\2\u017f\u017b\3\2\2\2\u0180C\3\2\2\2\u0181")
        buf.write("\u0182\5$\23\2\u0182\u0183\7*\2\2\u0183\u018f\3\2\2\2")
        buf.write("\u0184\u018f\5\34\17\2\u0185\u018f\5F$\2\u0186\u018f\5")
        buf.write("H%\2\u0187\u018f\5J&\2\u0188\u018f\5L\'\2\u0189\u018f")
        buf.write("\5T+\2\u018a\u018f\5\\/\2\u018b\u018f\5^\60\2\u018c\u018f")
        buf.write("\5`\61\2\u018d\u018f\5b\62\2\u018e\u0181\3\2\2\2\u018e")
        buf.write("\u0184\3\2\2\2\u018e\u0185\3\2\2\2\u018e\u0186\3\2\2\2")
        buf.write("\u018e\u0187\3\2\2\2\u018e\u0188\3\2\2\2\u018e\u0189\3")
        buf.write("\2\2\2\u018e\u018a\3\2\2\2\u018e\u018b\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018e\u018d\3\2\2\2\u018fE\3\2\2\2\u0190\u0191")
        buf.write("\7\'\2\2\u0191\u0192\5\24\13\2\u0192\u0193\7(\2\2\u0193")
        buf.write("G\3\2\2\2\u0194\u0195\7\13\2\2\u0195\u0196\7%\2\2\u0196")
        buf.write("\u0197\5,\27\2\u0197\u0198\7&\2\2\u0198\u0199\5D#\2\u0199")
        buf.write("\u01a3\3\2\2\2\u019a\u019b\7\13\2\2\u019b\u019c\7%\2\2")
        buf.write("\u019c\u019d\5,\27\2\u019d\u019e\7&\2\2\u019e\u019f\5")
        buf.write("D#\2\u019f\u01a0\7\b\2\2\u01a0\u01a1\5D#\2\u01a1\u01a3")
        buf.write("\3\2\2\2\u01a2\u0194\3\2\2\2\u01a2\u019a\3\2\2\2\u01a3")
        buf.write("I\3\2\2\2\u01a4\u01a5\7\22\2\2\u01a5\u01a6\7%\2\2\u01a6")
        buf.write("\u01a7\5,\27\2\u01a7\u01a8\7&\2\2\u01a8\u01a9\5D#\2\u01a9")
        buf.write("K\3\2\2\2\u01aa\u01ab\7\n\2\2\u01ab\u01ac\7%\2\2\u01ac")
        buf.write("\u01ad\5N(\2\u01ad\u01ae\7*\2\2\u01ae\u01af\5P)\2\u01af")
        buf.write("\u01b0\7*\2\2\u01b0\u01b1\5R*\2\u01b1\u01b2\7&\2\2\u01b2")
        buf.write("\u01b3\5D#\2\u01b3M\3\2\2\2\u01b4\u01b8\5$\23\2\u01b5")
        buf.write("\u01b8\5,\27\2\u01b6\u01b8\3\2\2\2\u01b7\u01b4\3\2\2\2")
        buf.write("\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8O\3\2\2")
        buf.write("\2\u01b9\u01bc\5,\27\2\u01ba\u01bc\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bcQ\3\2\2\2\u01bd\u01c0")
        buf.write("\5,\27\2\u01be\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0S\3\2\2\2\u01c1\u01c2\7\20\2\2\u01c2")
        buf.write("\u01c3\7%\2\2\u01c3\u01c4\5,\27\2\u01c4\u01c5\7&\2\2\u01c5")
        buf.write("\u01c6\7\'\2\2\u01c6\u01c7\5V,\2\u01c7\u01c8\7(\2\2\u01c8")
        buf.write("U\3\2\2\2\u01c9\u01ca\5X-\2\u01ca\u01cb\5V,\2\u01cb\u01ce")
        buf.write("\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01c9\3\2\2\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01ceW\3\2\2\2\u01cf\u01d0\7\5\2\2\u01d0")
        buf.write("\u01d1\5Z.\2\u01d1\u01d2\7+\2\2\u01d2\u01d3\5\24\13\2")
        buf.write("\u01d3\u01d8\3\2\2\2\u01d4\u01d5\7\7\2\2\u01d5\u01d6\7")
        buf.write("+\2\2\u01d6\u01d8\5\24\13\2\u01d7\u01cf\3\2\2\2\u01d7")
        buf.write("\u01d4\3\2\2\2\u01d8Y\3\2\2\2\u01d9\u01da\5,\27\2\u01da")
        buf.write("[\3\2\2\2\u01db\u01dc\7\4\2\2\u01dc\u01dd\7*\2\2\u01dd")
        buf.write("]\3\2\2\2\u01de\u01df\7\6\2\2\u01df\u01e0\7*\2\2\u01e0")
        buf.write("_\3\2\2\2\u01e1\u01e2\7\r\2\2\u01e2\u01e3\5,\27\2\u01e3")
        buf.write("\u01e4\7*\2\2\u01e4\u01e8\3\2\2\2\u01e5\u01e6\7\r\2\2")
        buf.write("\u01e6\u01e8\7*\2\2\u01e7\u01e1\3\2\2\2\u01e7\u01e5\3")
        buf.write("\2\2\2\u01e8a\3\2\2\2\u01e9\u01ea\5,\27\2\u01ea\u01eb")
        buf.write("\7*\2\2\u01ebc\3\2\2\2)ko\u0084\u0088\u008e\u0095\u009e")
        buf.write("\u00ad\u00bc\u00c2\u00c9\u00d9\u00e4\u00eb\u00f2\u00fc")
        buf.write("\u0107\u0113\u0115\u0127\u0129\u0135\u0137\u0146\u0148")
        buf.write("\u0152\u0159\u0162\u0164\u016f\u017f\u018e\u01a2\u01b7")
        buf.write("\u01bb\u01bf\u01cd\u01d7\u01e7")
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
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.STRUCT, TyCParser.VOID, TyCParser.ID]:
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
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.VOID, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.funcdecl()
                pass
            elif token in [TyCParser.STRUCT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
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
            self.state = 111
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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.rettyp()
                self.state = 114
                self.match(TyCParser.ID)
                self.state = 115
                self.match(TyCParser.LP)
                self.state = 116
                self.paramlist()
                self.state = 117
                self.match(TyCParser.RP)
                self.state = 118
                self.match(TyCParser.LB)
                self.state = 119
                self.stmtlist()
                self.state = 120
                self.match(TyCParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(TyCParser.ID)
                self.state = 123
                self.match(TyCParser.LP)
                self.state = 124
                self.paramlist()
                self.state = 125
                self.match(TyCParser.RP)
                self.state = 126
                self.match(TyCParser.LB)
                self.state = 127
                self.stmtlist()
                self.state = 128
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
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.typ()
                pass
            elif token in [TyCParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
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
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.pardecl()
                self.state = 137
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
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(TyCParser.CM)
                self.state = 143
                self.pardecl()
                self.state = 144
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
            self.state = 149
            self.typ()
            self.state = 150
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
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.AUTO, TyCParser.BREAK, TyCParser.CONTINUE, TyCParser.FLOAT, TyCParser.FOR, TyCParser.IF, TyCParser.INT, TyCParser.RETURN, TyCParser.STRING, TyCParser.SWITCH, TyCParser.WHILE, TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.stmt()
                self.state = 153
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
            self.state = 158
            self.match(TyCParser.STRUCT)
            self.state = 159
            self.match(TyCParser.ID)
            self.state = 160
            self.match(TyCParser.LB)
            self.state = 161
            self.memlist()
            self.state = 162
            self.match(TyCParser.RB)
            self.state = 163
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
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.memtyp()
                self.state = 166
                self.match(TyCParser.ID)
                self.state = 167
                self.match(TyCParser.SM)
                self.state = 168
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
            self.state = 173
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
            self.state = 175
            self.match(TyCParser.ID)
            self.state = 176
            self.structvar()
            self.state = 177
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(TyCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(TyCParser.ID)
                self.state = 181
                self.match(TyCParser.ASSIGN)
                self.state = 182
                self.match(TyCParser.LB)
                self.state = 183
                self.exprlist()
                self.state = 184
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
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.expr()
                self.state = 189
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
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(TyCParser.CM)
                self.state = 195
                self.expr()
                self.state = 196
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
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(TyCParser.AUTO)
                self.state = 202
                self.match(TyCParser.ID)
                self.state = 203
                self.match(TyCParser.ASSIGN)
                self.state = 204
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(TyCParser.AUTO)
                self.state = 206
                self.match(TyCParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.typ()
                self.state = 208
                self.match(TyCParser.ID)
                self.state = 209
                self.match(TyCParser.ASSIGN)
                self.state = 210
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.typ()
                self.state = 213
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
            self.state = 217
            self.match(TyCParser.ID)
            self.state = 218
            self.match(TyCParser.LP)
            self.state = 219
            self.arglist()
            self.state = 220
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
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
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
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(TyCParser.CM)
                self.state = 229
                self.expr()
                self.state = 230
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
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.expr1(0)
                self.state = 236
                self.match(TyCParser.ASSIGN)
                self.state = 237
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
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
            self.state = 243
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 245
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 246
                    self.match(TyCParser.OR)
                    self.state = 247
                    self.expr2(0) 
                self.state = 252
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
            self.state = 254
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    self.match(TyCParser.AND)
                    self.state = 258
                    self.expr3(0) 
                self.state = 263
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
            self.state = 265
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 273
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 267
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 268
                        self.match(TyCParser.EQUAL)
                        self.state = 269
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 270
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 271
                        self.match(TyCParser.NOTEQUAL)
                        self.state = 272
                        self.expr4(0)
                        pass

             
                self.state = 277
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
            self.state = 279
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 293
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 281
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 282
                        self.match(TyCParser.LESSTHAN)
                        self.state = 283
                        self.expr5(0)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 284
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 285
                        self.match(TyCParser.LESSTHAN_EQUAL)
                        self.state = 286
                        self.expr5(0)
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 287
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 288
                        self.match(TyCParser.GREATERTHAN)
                        self.state = 289
                        self.expr5(0)
                        pass

                    elif la_ == 4:
                        localctx = TyCParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 290
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 291
                        self.match(TyCParser.GREATERTHAN_EQUAL)
                        self.state = 292
                        self.expr5(0)
                        pass

             
                self.state = 297
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
            self.state = 299
            self.expr6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 307
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 301
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 302
                        self.match(TyCParser.ADD)
                        self.state = 303
                        self.expr6(0)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 304
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 305
                        self.match(TyCParser.SUB)
                        self.state = 306
                        self.expr6(0)
                        pass

             
                self.state = 311
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
            self.state = 313
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 324
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 315
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 316
                        self.match(TyCParser.MUL)
                        self.state = 317
                        self.expr7()
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 318
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 319
                        self.match(TyCParser.DIV)
                        self.state = 320
                        self.expr7()
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 321
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 322
                        self.match(TyCParser.MOD)
                        self.state = 323
                        self.expr7()
                        pass

             
                self.state = 328
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
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(TyCParser.NOT)
                self.state = 330
                self.expr7()
                pass
            elif token in [TyCParser.ADD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(TyCParser.ADD)
                self.state = 332
                self.expr7()
                pass
            elif token in [TyCParser.SUB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 333
                self.match(TyCParser.SUB)
                self.state = 334
                self.expr7()
                pass
            elif token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 335
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
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(TyCParser.INCREMENT)
                self.state = 339
                self.expr8()
                pass
            elif token in [TyCParser.DECREMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.match(TyCParser.DECREMENT)
                self.state = 341
                self.expr8()
                pass
            elif token in [TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 342
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
            self.state = 346
            self.expr10(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 352
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 348
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 349
                        self.match(TyCParser.INCREMENT)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 350
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 351
                        self.match(TyCParser.DECREMENT)
                        pass

             
                self.state = 356
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
            self.state = 358
            self.expr11()
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr10Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr10)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    self.match(TyCParser.ACCESS)
                    self.state = 362
                    self.expr11() 
                self.state = 367
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
        self.enterRule(localctx, 64, self.RULE_expr11)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.match(TyCParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(TyCParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370
                self.match(TyCParser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 371
                self.match(TyCParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 372
                self.funccalldecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 373
                self.match(TyCParser.LP)
                self.state = 374
                self.expr()
                self.state = 375
                self.match(TyCParser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 377
                self.match(TyCParser.LB)
                self.state = 378
                self.exprlist()
                self.state = 379
                self.match(TyCParser.RB)
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
        self.enterRule(localctx, 66, self.RULE_stmt)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.vardecl()
                self.state = 384
                self.match(TyCParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.structvardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 387
                self.blockstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 388
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 389
                self.whilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 390
                self.forstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 391
                self.switchstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 392
                self.breakstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 393
                self.continuestmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 394
                self.returnstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 395
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
            self.state = 398
            self.match(TyCParser.LB)
            self.state = 399
            self.stmtlist()
            self.state = 400
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
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(TyCParser.IF)
                self.state = 403
                self.match(TyCParser.LP)
                self.state = 404
                self.expr()
                self.state = 405
                self.match(TyCParser.RP)
                self.state = 406
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(TyCParser.IF)
                self.state = 409
                self.match(TyCParser.LP)
                self.state = 410
                self.expr()
                self.state = 411
                self.match(TyCParser.RP)
                self.state = 412
                self.stmt()
                self.state = 413
                self.match(TyCParser.ELSE)
                self.state = 414
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
            self.state = 418
            self.match(TyCParser.WHILE)
            self.state = 419
            self.match(TyCParser.LP)
            self.state = 420
            self.expr()
            self.state = 421
            self.match(TyCParser.RP)
            self.state = 422
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
            self.state = 424
            self.match(TyCParser.FOR)
            self.state = 425
            self.match(TyCParser.LP)
            self.state = 426
            self.init()
            self.state = 427
            self.match(TyCParser.SM)
            self.state = 428
            self.cond()
            self.state = 429
            self.match(TyCParser.SM)
            self.state = 430
            self.updt()
            self.state = 431
            self.match(TyCParser.RP)
            self.state = 432
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
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
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
            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
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
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADD, TyCParser.SUB, TyCParser.NOT, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LP, TyCParser.LB, TyCParser.ID, TyCParser.INTLIT, TyCParser.FLOATLIT, TyCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
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
            self.state = 447
            self.match(TyCParser.SWITCH)
            self.state = 448
            self.match(TyCParser.LP)
            self.state = 449
            self.expr()
            self.state = 450
            self.match(TyCParser.RP)
            self.state = 451
            self.match(TyCParser.LB)
            self.state = 452
            self.caselist()
            self.state = 453
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
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CASE, TyCParser.DEFAULT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.caseclause()
                self.state = 456
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
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.match(TyCParser.CASE)
                self.state = 462
                self.caseexpr()
                self.state = 463
                self.match(TyCParser.CL)
                self.state = 464
                self.stmtlist()
                pass
            elif token in [TyCParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.match(TyCParser.DEFAULT)
                self.state = 467
                self.match(TyCParser.CL)
                self.state = 468
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
            self.state = 471
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
            self.state = 473
            self.match(TyCParser.BREAK)
            self.state = 474
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
            self.state = 476
            self.match(TyCParser.CONTINUE)
            self.state = 477
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
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.match(TyCParser.RETURN)
                self.state = 480
                self.expr()
                self.state = 481
                self.match(TyCParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.match(TyCParser.RETURN)
                self.state = 484
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
            self.state = 487
            self.expr()
            self.state = 488
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
         




