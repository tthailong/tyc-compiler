# Generated from d:\Long\Theory\Principles of Programming Languages\BTL\tyc-compiler\src\grammar\TyC.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0171\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\7+\u0102\n+\f+\16+\u0105\13+\3,\5,\u0108\n,\3,\6")
        buf.write(",\u010b\n,\r,\16,\u010c\3-\5-\u0110\n-\3-\7-\u0113\n-")
        buf.write("\f-\16-\u0116\13-\3-\3-\6-\u011a\n-\r-\16-\u011b\3-\3")
        buf.write("-\5-\u0120\n-\3-\6-\u0123\n-\r-\16-\u0124\5-\u0127\n-")
        buf.write("\3-\5-\u012a\n-\3-\6-\u012d\n-\r-\16-\u012e\3-\3-\5-\u0133")
        buf.write("\n-\3-\6-\u0136\n-\r-\16-\u0137\3-\3-\5-\u013c\n-\3-\6")
        buf.write("-\u013f\n-\r-\16-\u0140\5-\u0143\n-\3.\3.\3.\3/\3/\3/")
        buf.write("\7/\u014b\n/\f/\16/\u014e\13/\3/\3/\3/\3\60\6\60\u0154")
        buf.write("\n\60\r\60\16\60\u0155\3\60\3\60\3\61\3\61\3\61\7\61\u015d")
        buf.write("\n\61\f\61\16\61\u0160\13\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\7\62\u0169\n\62\f\62\16\62\u016c\13\62\3\62")
        buf.write("\3\62\3\63\3\63\2\2\64\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]/_\60a\61c\62e\63")
        buf.write("\3\2\f\5\2C\\aac|\6\2\62;C\\aac|\3\2//\3\2\62;\4\2GGg")
        buf.write("g\t\2$$^^ddhhppttvv\3\2$$\6\2\f\f\17\17$$^^\5\2\13\f\16")
        buf.write("\17\"\"\13\2\f\f\17\17$$^^ddhhppttvv\2\u0187\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\3g\3\2\2\2\5l\3\2\2\2\7r")
        buf.write("\3\2\2\2\tw\3\2\2\2\13\u0080\3\2\2\2\r\u0088\3\2\2\2\17")
        buf.write("\u008d\3\2\2\2\21\u0093\3\2\2\2\23\u0097\3\2\2\2\25\u009a")
        buf.write("\3\2\2\2\27\u009e\3\2\2\2\31\u00a5\3\2\2\2\33\u00ac\3")
        buf.write("\2\2\2\35\u00b3\3\2\2\2\37\u00ba\3\2\2\2!\u00bf\3\2\2")
        buf.write("\2#\u00c5\3\2\2\2%\u00c7\3\2\2\2\'\u00c9\3\2\2\2)\u00cb")
        buf.write("\3\2\2\2+\u00cd\3\2\2\2-\u00cf\3\2\2\2/\u00d2\3\2\2\2")
        buf.write("\61\u00d5\3\2\2\2\63\u00d7\3\2\2\2\65\u00d9\3\2\2\2\67")
        buf.write("\u00dc\3\2\2\29\u00df\3\2\2\2;\u00e2\3\2\2\2=\u00e5\3")
        buf.write("\2\2\2?\u00e7\3\2\2\2A\u00ea\3\2\2\2C\u00ed\3\2\2\2E\u00ef")
        buf.write("\3\2\2\2G\u00f1\3\2\2\2I\u00f3\3\2\2\2K\u00f5\3\2\2\2")
        buf.write("M\u00f7\3\2\2\2O\u00f9\3\2\2\2Q\u00fb\3\2\2\2S\u00fd\3")
        buf.write("\2\2\2U\u00ff\3\2\2\2W\u0107\3\2\2\2Y\u0142\3\2\2\2[\u0144")
        buf.write("\3\2\2\2]\u0147\3\2\2\2_\u0153\3\2\2\2a\u0159\3\2\2\2")
        buf.write("c\u0165\3\2\2\2e\u016f\3\2\2\2gh\7c\2\2hi\7w\2\2ij\7v")
        buf.write("\2\2jk\7q\2\2k\4\3\2\2\2lm\7d\2\2mn\7t\2\2no\7g\2\2op")
        buf.write("\7c\2\2pq\7m\2\2q\6\3\2\2\2rs\7e\2\2st\7c\2\2tu\7u\2\2")
        buf.write("uv\7g\2\2v\b\3\2\2\2wx\7e\2\2xy\7q\2\2yz\7p\2\2z{\7v\2")
        buf.write("\2{|\7k\2\2|}\7p\2\2}~\7w\2\2~\177\7g\2\2\177\n\3\2\2")
        buf.write("\2\u0080\u0081\7f\2\2\u0081\u0082\7g\2\2\u0082\u0083\7")
        buf.write("h\2\2\u0083\u0084\7c\2\2\u0084\u0085\7w\2\2\u0085\u0086")
        buf.write("\7n\2\2\u0086\u0087\7v\2\2\u0087\f\3\2\2\2\u0088\u0089")
        buf.write("\7g\2\2\u0089\u008a\7n\2\2\u008a\u008b\7u\2\2\u008b\u008c")
        buf.write("\7g\2\2\u008c\16\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f")
        buf.write("\7n\2\2\u008f\u0090\7q\2\2\u0090\u0091\7c\2\2\u0091\u0092")
        buf.write("\7v\2\2\u0092\20\3\2\2\2\u0093\u0094\7h\2\2\u0094\u0095")
        buf.write("\7q\2\2\u0095\u0096\7t\2\2\u0096\22\3\2\2\2\u0097\u0098")
        buf.write("\7k\2\2\u0098\u0099\7h\2\2\u0099\24\3\2\2\2\u009a\u009b")
        buf.write("\7k\2\2\u009b\u009c\7p\2\2\u009c\u009d\7v\2\2\u009d\26")
        buf.write("\3\2\2\2\u009e\u009f\7t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4")
        buf.write("\7p\2\2\u00a4\30\3\2\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7")
        buf.write("\7v\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\u00ab\7i\2\2\u00ab\32\3\2\2\2\u00ac\u00ad")
        buf.write("\7u\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7t\2\2\u00af\u00b0")
        buf.write("\7w\2\2\u00b0\u00b1\7e\2\2\u00b1\u00b2\7v\2\2\u00b2\34")
        buf.write("\3\2\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5\7y\2\2\u00b5\u00b6")
        buf.write("\7k\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7e\2\2\u00b8\u00b9")
        buf.write("\7j\2\2\u00b9\36\3\2\2\2\u00ba\u00bb\7x\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7f\2\2\u00be \3")
        buf.write("\2\2\2\u00bf\u00c0\7y\2\2\u00c0\u00c1\7j\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7g\2\2\u00c4\"")
        buf.write("\3\2\2\2\u00c5\u00c6\7-\2\2\u00c6$\3\2\2\2\u00c7\u00c8")
        buf.write("\7/\2\2\u00c8&\3\2\2\2\u00c9\u00ca\7,\2\2\u00ca(\3\2\2")
        buf.write("\2\u00cb\u00cc\7\61\2\2\u00cc*\3\2\2\2\u00cd\u00ce\7\'")
        buf.write("\2\2\u00ce,\3\2\2\2\u00cf\u00d0\7?\2\2\u00d0\u00d1\7?")
        buf.write("\2\2\u00d1.\3\2\2\2\u00d2\u00d3\7#\2\2\u00d3\u00d4\7?")
        buf.write("\2\2\u00d4\60\3\2\2\2\u00d5\u00d6\7>\2\2\u00d6\62\3\2")
        buf.write("\2\2\u00d7\u00d8\7@\2\2\u00d8\64\3\2\2\2\u00d9\u00da\7")
        buf.write(">\2\2\u00da\u00db\7?\2\2\u00db\66\3\2\2\2\u00dc\u00dd")
        buf.write("\7@\2\2\u00dd\u00de\7?\2\2\u00de8\3\2\2\2\u00df\u00e0")
        buf.write("\7~\2\2\u00e0\u00e1\7~\2\2\u00e1:\3\2\2\2\u00e2\u00e3")
        buf.write("\7(\2\2\u00e3\u00e4\7(\2\2\u00e4<\3\2\2\2\u00e5\u00e6")
        buf.write("\7#\2\2\u00e6>\3\2\2\2\u00e7\u00e8\7-\2\2\u00e8\u00e9")
        buf.write("\7-\2\2\u00e9@\3\2\2\2\u00ea\u00eb\7/\2\2\u00eb\u00ec")
        buf.write("\7/\2\2\u00ecB\3\2\2\2\u00ed\u00ee\7?\2\2\u00eeD\3\2\2")
        buf.write("\2\u00ef\u00f0\7\60\2\2\u00f0F\3\2\2\2\u00f1\u00f2\7*")
        buf.write("\2\2\u00f2H\3\2\2\2\u00f3\u00f4\7+\2\2\u00f4J\3\2\2\2")
        buf.write("\u00f5\u00f6\7}\2\2\u00f6L\3\2\2\2\u00f7\u00f8\7\177\2")
        buf.write("\2\u00f8N\3\2\2\2\u00f9\u00fa\7.\2\2\u00faP\3\2\2\2\u00fb")
        buf.write("\u00fc\7=\2\2\u00fcR\3\2\2\2\u00fd\u00fe\7<\2\2\u00fe")
        buf.write("T\3\2\2\2\u00ff\u0103\t\2\2\2\u0100\u0102\t\3\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0103\u0104\3\2\2\2\u0104V\3\2\2\2\u0105\u0103\3\2\2")
        buf.write("\2\u0106\u0108\t\4\2\2\u0107\u0106\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u010b\t\5\2\2\u010a")
        buf.write("\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010d\3\2\2\2\u010dX\3\2\2\2\u010e\u0110\t\4\2")
        buf.write("\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0114")
        buf.write("\3\2\2\2\u0111\u0113\t\5\2\2\u0112\u0111\3\2\2\2\u0113")
        buf.write("\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0115\u0117\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0119\7")
        buf.write("\60\2\2\u0118\u011a\t\5\2\2\u0119\u0118\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u0126\3\2\2\2\u011d\u011f\t\6\2\2\u011e\u0120\t")
        buf.write("\4\2\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122")
        buf.write("\3\2\2\2\u0121\u0123\t\5\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("\u0124\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0127\3\2\2\2\u0126\u011d\3\2\2\2\u0126\u0127\3")
        buf.write("\2\2\2\u0127\u0143\3\2\2\2\u0128\u012a\t\4\2\2\u0129\u0128")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012c\3\2\2\2\u012b")
        buf.write("\u012d\t\5\2\2\u012c\u012b\3\2\2\2\u012d\u012e\3\2\2\2")
        buf.write("\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\3")
        buf.write("\2\2\2\u0130\u0143\7\60\2\2\u0131\u0133\t\4\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\3\2\2\2")
        buf.write("\u0134\u0136\t\5\2\2\u0135\u0134\3\2\2\2\u0136\u0137\3")
        buf.write("\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u013b\t\6\2\2\u013a\u013c\t\4\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013e\3\2\2\2")
        buf.write("\u013d\u013f\t\5\2\2\u013e\u013d\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0143")
        buf.write("\3\2\2\2\u0142\u010f\3\2\2\2\u0142\u0129\3\2\2\2\u0142")
        buf.write("\u0132\3\2\2\2\u0143Z\3\2\2\2\u0144\u0145\7^\2\2\u0145")
        buf.write("\u0146\t\7\2\2\u0146\\\3\2\2\2\u0147\u014c\t\b\2\2\u0148")
        buf.write("\u014b\5[.\2\u0149\u014b\n\t\2\2\u014a\u0148\3\2\2\2\u014a")
        buf.write("\u0149\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2")
        buf.write("\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3")
        buf.write("\2\2\2\u014f\u0150\t\b\2\2\u0150\u0151\b/\2\2\u0151^\3")
        buf.write("\2\2\2\u0152\u0154\t\n\2\2\u0153\u0152\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\u0158\b\60\3\2\u0158`\3\2\2\2\u0159")
        buf.write("\u015e\7$\2\2\u015a\u015d\5[.\2\u015b\u015d\n\t\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015d\u0160\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\3")
        buf.write("\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\7^\2\2\u0162\u0163")
        buf.write("\n\13\2\2\u0163\u0164\b\61\4\2\u0164b\3\2\2\2\u0165\u016a")
        buf.write("\t\b\2\2\u0166\u0169\5[.\2\u0167\u0169\n\t\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016d\3\2\2\2")
        buf.write("\u016c\u016a\3\2\2\2\u016d\u016e\b\62\5\2\u016ed\3\2\2")
        buf.write("\2\u016f\u0170\13\2\2\2\u0170f\3\2\2\2\32\2\u0103\u0107")
        buf.write("\u010c\u010f\u0114\u011b\u011f\u0124\u0126\u0129\u012e")
        buf.write("\u0132\u0137\u013b\u0140\u0142\u014a\u014c\u0155\u015c")
        buf.write("\u015e\u0168\u016a\6\3/\2\b\2\2\3\61\3\3\62\4")
        return buf.getvalue()


class TyCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    CASE = 3
    CONTINUE = 4
    DEFAULT = 5
    ELSE = 6
    FLOAT = 7
    FOR = 8
    IF = 9
    INT = 10
    RETURN = 11
    STRING = 12
    STRUCT = 13
    SWITCH = 14
    VOID = 15
    WHILE = 16
    ADD = 17
    SUB = 18
    MUL = 19
    DIV = 20
    MOD = 21
    EQUAL = 22
    NOTEQUAL = 23
    LESSTHAN = 24
    GREATERTHAN = 25
    LESSTHAN_EQUAL = 26
    GREATERTHAN_EQUAL = 27
    OR = 28
    AND = 29
    NOT = 30
    INCREMENT = 31
    DECREMENT = 32
    ASSIGN = 33
    ACCESS = 34
    LP = 35
    RP = 36
    LB = 37
    RB = 38
    CM = 39
    SM = 40
    CL = 41
    ID = 42
    INTLIT = 43
    FLOATLIT = 44
    STRINGLIT = 45
    WS = 46
    ILLEGAL_ESCAPE = 47
    UNCLOSE_STRING = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'case'", "'continue'", "'default'", "'else'", 
            "'float'", "'for'", "'if'", "'int'", "'return'", "'string'", 
            "'struct'", "'switch'", "'void'", "'while'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'||'", "'&&'", "'!'", "'++'", "'--'", "'='", "'.'", "'('", 
            "')'", "'{'", "'}'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", 
            "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", "SWITCH", 
            "VOID", "WHILE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
            "NOTEQUAL", "LESSTHAN", "GREATERTHAN", "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", 
            "OR", "AND", "NOT", "INCREMENT", "DECREMENT", "ASSIGN", "ACCESS", 
            "LP", "RP", "LB", "RB", "CM", "SM", "CL", "ID", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", 
                  "FLOAT", "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", 
                  "SWITCH", "VOID", "WHILE", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "EQUAL", "NOTEQUAL", "LESSTHAN", "GREATERTHAN", 
                  "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", "OR", "AND", "NOT", 
                  "INCREMENT", "DECREMENT", "ASSIGN", "ACCESS", "LP", "RP", 
                  "LB", "RB", "CM", "SM", "CL", "ID", "INTLIT", "FLOATLIT", 
                  "ESCAPE", "STRINGLIT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ERROR_CHAR" ]

    grammarFileName = "TyC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[45] = self.STRINGLIT_action 
            actions[47] = self.ILLEGAL_ESCAPE_action 
            actions[48] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]
     


