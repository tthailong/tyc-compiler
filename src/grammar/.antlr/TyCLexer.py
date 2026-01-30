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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0184\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\7,\u0115\n,\f,\16")
        buf.write(",\u0118\13,\3-\5-\u011b\n-\3-\6-\u011e\n-\r-\16-\u011f")
        buf.write("\3.\5.\u0123\n.\3.\7.\u0126\n.\f.\16.\u0129\13.\3.\3.")
        buf.write("\6.\u012d\n.\r.\16.\u012e\3.\3.\5.\u0133\n.\3.\6.\u0136")
        buf.write("\n.\r.\16.\u0137\5.\u013a\n.\3.\5.\u013d\n.\3.\6.\u0140")
        buf.write("\n.\r.\16.\u0141\3.\3.\5.\u0146\n.\3.\6.\u0149\n.\r.\16")
        buf.write(".\u014a\3.\3.\5.\u014f\n.\3.\6.\u0152\n.\r.\16.\u0153")
        buf.write("\5.\u0156\n.\3/\3/\3/\3\60\3\60\3\60\7\60\u015e\n\60\f")
        buf.write("\60\16\60\u0161\13\60\3\60\3\60\3\60\3\61\6\61\u0167\n")
        buf.write("\61\r\61\16\61\u0168\3\61\3\61\3\62\3\62\3\62\7\62\u0170")
        buf.write("\n\62\f\62\16\62\u0173\13\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\7\63\u017c\n\63\f\63\16\63\u017f\13\63\3\63")
        buf.write("\3\63\3\64\3\64\2\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\60a\61c\62e\63")
        buf.write("g\64\3\2\f\5\2C\\aac|\6\2\62;C\\aac|\3\2//\3\2\62;\4\2")
        buf.write("GGgg\t\2$$^^ddhhppttvv\3\2$$\6\2\f\f\17\17$$^^\5\2\13")
        buf.write("\f\16\17\"\"\13\2\f\f\17\17$$^^ddhhppttvv\2\u019a\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\3i\3")
        buf.write("\2\2\2\5w\3\2\2\2\7|\3\2\2\2\t\u0081\3\2\2\2\13\u0087")
        buf.write("\3\2\2\2\r\u008c\3\2\2\2\17\u0095\3\2\2\2\21\u009d\3\2")
        buf.write("\2\2\23\u00a2\3\2\2\2\25\u00a8\3\2\2\2\27\u00ac\3\2\2")
        buf.write("\2\31\u00af\3\2\2\2\33\u00b3\3\2\2\2\35\u00ba\3\2\2\2")
        buf.write("\37\u00c1\3\2\2\2!\u00c8\3\2\2\2#\u00cf\3\2\2\2%\u00d4")
        buf.write("\3\2\2\2\'\u00da\3\2\2\2)\u00dc\3\2\2\2+\u00de\3\2\2\2")
        buf.write("-\u00e0\3\2\2\2/\u00e2\3\2\2\2\61\u00e4\3\2\2\2\63\u00e7")
        buf.write("\3\2\2\2\65\u00ea\3\2\2\2\67\u00ec\3\2\2\29\u00ee\3\2")
        buf.write("\2\2;\u00f1\3\2\2\2=\u00f4\3\2\2\2?\u00f7\3\2\2\2A\u00fa")
        buf.write("\3\2\2\2C\u00fc\3\2\2\2E\u00ff\3\2\2\2G\u0102\3\2\2\2")
        buf.write("I\u0104\3\2\2\2K\u0106\3\2\2\2M\u0108\3\2\2\2O\u010a\3")
        buf.write("\2\2\2Q\u010c\3\2\2\2S\u010e\3\2\2\2U\u0110\3\2\2\2W\u0112")
        buf.write("\3\2\2\2Y\u011a\3\2\2\2[\u0155\3\2\2\2]\u0157\3\2\2\2")
        buf.write("_\u015a\3\2\2\2a\u0166\3\2\2\2c\u016c\3\2\2\2e\u0178\3")
        buf.write("\2\2\2g\u0182\3\2\2\2ij\7u\2\2jk\7v\2\2kl\7c\2\2lm\7v")
        buf.write("\2\2mn\7g\2\2no\7o\2\2op\7g\2\2pq\7p\2\2qr\7v\2\2rs\7")
        buf.write("n\2\2st\7k\2\2tu\7u\2\2uv\7v\2\2v\4\3\2\2\2wx\7g\2\2x")
        buf.write("y\7z\2\2yz\7r\2\2z{\7t\2\2{\6\3\2\2\2|}\7c\2\2}~\7w\2")
        buf.write("\2~\177\7v\2\2\177\u0080\7q\2\2\u0080\b\3\2\2\2\u0081")
        buf.write("\u0082\7d\2\2\u0082\u0083\7t\2\2\u0083\u0084\7g\2\2\u0084")
        buf.write("\u0085\7c\2\2\u0085\u0086\7m\2\2\u0086\n\3\2\2\2\u0087")
        buf.write("\u0088\7e\2\2\u0088\u0089\7c\2\2\u0089\u008a\7u\2\2\u008a")
        buf.write("\u008b\7g\2\2\u008b\f\3\2\2\2\u008c\u008d\7e\2\2\u008d")
        buf.write("\u008e\7q\2\2\u008e\u008f\7p\2\2\u008f\u0090\7v\2\2\u0090")
        buf.write("\u0091\7k\2\2\u0091\u0092\7p\2\2\u0092\u0093\7w\2\2\u0093")
        buf.write("\u0094\7g\2\2\u0094\16\3\2\2\2\u0095\u0096\7f\2\2\u0096")
        buf.write("\u0097\7g\2\2\u0097\u0098\7h\2\2\u0098\u0099\7c\2\2\u0099")
        buf.write("\u009a\7w\2\2\u009a\u009b\7n\2\2\u009b\u009c\7v\2\2\u009c")
        buf.write("\20\3\2\2\2\u009d\u009e\7g\2\2\u009e\u009f\7n\2\2\u009f")
        buf.write("\u00a0\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\22\3\2\2\2\u00a2")
        buf.write("\u00a3\7h\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7q\2\2\u00a5")
        buf.write("\u00a6\7c\2\2\u00a6\u00a7\7v\2\2\u00a7\24\3\2\2\2\u00a8")
        buf.write("\u00a9\7h\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7t\2\2\u00ab")
        buf.write("\26\3\2\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7h\2\2\u00ae")
        buf.write("\30\3\2\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1")
        buf.write("\u00b2\7v\2\2\u00b2\32\3\2\2\2\u00b3\u00b4\7t\2\2\u00b4")
        buf.write("\u00b5\7g\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7w\2\2\u00b7")
        buf.write("\u00b8\7t\2\2\u00b8\u00b9\7p\2\2\u00b9\34\3\2\2\2\u00ba")
        buf.write("\u00bb\7u\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd")
        buf.write("\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7i\2\2\u00c0")
        buf.write("\36\3\2\2\2\u00c1\u00c2\7u\2\2\u00c2\u00c3\7v\2\2\u00c3")
        buf.write("\u00c4\7t\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7e\2\2\u00c6")
        buf.write("\u00c7\7v\2\2\u00c7 \3\2\2\2\u00c8\u00c9\7u\2\2\u00c9")
        buf.write("\u00ca\7y\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\u00cd\7e\2\2\u00cd\u00ce\7j\2\2\u00ce\"\3\2\2\2\u00cf")
        buf.write("\u00d0\7x\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7k\2\2\u00d2")
        buf.write("\u00d3\7f\2\2\u00d3$\3\2\2\2\u00d4\u00d5\7y\2\2\u00d5")
        buf.write("\u00d6\7j\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7n\2\2\u00d8")
        buf.write("\u00d9\7g\2\2\u00d9&\3\2\2\2\u00da\u00db\7-\2\2\u00db")
        buf.write("(\3\2\2\2\u00dc\u00dd\7/\2\2\u00dd*\3\2\2\2\u00de\u00df")
        buf.write("\7,\2\2\u00df,\3\2\2\2\u00e0\u00e1\7\61\2\2\u00e1.\3\2")
        buf.write("\2\2\u00e2\u00e3\7\'\2\2\u00e3\60\3\2\2\2\u00e4\u00e5")
        buf.write("\7?\2\2\u00e5\u00e6\7?\2\2\u00e6\62\3\2\2\2\u00e7\u00e8")
        buf.write("\7#\2\2\u00e8\u00e9\7?\2\2\u00e9\64\3\2\2\2\u00ea\u00eb")
        buf.write("\7>\2\2\u00eb\66\3\2\2\2\u00ec\u00ed\7@\2\2\u00ed8\3\2")
        buf.write("\2\2\u00ee\u00ef\7>\2\2\u00ef\u00f0\7?\2\2\u00f0:\3\2")
        buf.write("\2\2\u00f1\u00f2\7@\2\2\u00f2\u00f3\7?\2\2\u00f3<\3\2")
        buf.write("\2\2\u00f4\u00f5\7~\2\2\u00f5\u00f6\7~\2\2\u00f6>\3\2")
        buf.write("\2\2\u00f7\u00f8\7(\2\2\u00f8\u00f9\7(\2\2\u00f9@\3\2")
        buf.write("\2\2\u00fa\u00fb\7#\2\2\u00fbB\3\2\2\2\u00fc\u00fd\7-")
        buf.write("\2\2\u00fd\u00fe\7-\2\2\u00feD\3\2\2\2\u00ff\u0100\7/")
        buf.write("\2\2\u0100\u0101\7/\2\2\u0101F\3\2\2\2\u0102\u0103\7?")
        buf.write("\2\2\u0103H\3\2\2\2\u0104\u0105\7\60\2\2\u0105J\3\2\2")
        buf.write("\2\u0106\u0107\7*\2\2\u0107L\3\2\2\2\u0108\u0109\7+\2")
        buf.write("\2\u0109N\3\2\2\2\u010a\u010b\7}\2\2\u010bP\3\2\2\2\u010c")
        buf.write("\u010d\7\177\2\2\u010dR\3\2\2\2\u010e\u010f\7.\2\2\u010f")
        buf.write("T\3\2\2\2\u0110\u0111\7=\2\2\u0111V\3\2\2\2\u0112\u0116")
        buf.write("\t\2\2\2\u0113\u0115\t\3\2\2\u0114\u0113\3\2\2\2\u0115")
        buf.write("\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117X\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011b\t\4\2")
        buf.write("\2\u011a\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d")
        buf.write("\3\2\2\2\u011c\u011e\t\5\2\2\u011d\u011c\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120Z\3\2\2\2\u0121\u0123\t\4\2\2\u0122\u0121\3\2\2")
        buf.write("\2\u0122\u0123\3\2\2\2\u0123\u0127\3\2\2\2\u0124\u0126")
        buf.write("\t\5\2\2\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a\3\2\2\2")
        buf.write("\u0129\u0127\3\2\2\2\u012a\u012c\7\60\2\2\u012b\u012d")
        buf.write("\t\5\2\2\u012c\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0139\3\2\2\2")
        buf.write("\u0130\u0132\t\6\2\2\u0131\u0133\t\4\2\2\u0132\u0131\3")
        buf.write("\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0136")
        buf.write("\t\5\2\2\u0135\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2")
        buf.write("\u0139\u0130\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0156\3")
        buf.write("\2\2\2\u013b\u013d\t\4\2\2\u013c\u013b\3\2\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u0140\t\5\2\2\u013f")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0156\7")
        buf.write("\60\2\2\u0144\u0146\t\4\2\2\u0145\u0144\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0149\t\5\2\2")
        buf.write("\u0148\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e")
        buf.write("\t\6\2\2\u014d\u014f\t\4\2\2\u014e\u014d\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u0152\t\5\2\2")
        buf.write("\u0151\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0151\3")
        buf.write("\2\2\2\u0153\u0154\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u0122")
        buf.write("\3\2\2\2\u0155\u013c\3\2\2\2\u0155\u0145\3\2\2\2\u0156")
        buf.write("\\\3\2\2\2\u0157\u0158\7^\2\2\u0158\u0159\t\7\2\2\u0159")
        buf.write("^\3\2\2\2\u015a\u015f\t\b\2\2\u015b\u015e\5]/\2\u015c")
        buf.write("\u015e\n\t\2\2\u015d\u015b\3\2\2\2\u015d\u015c\3\2\2\2")
        buf.write("\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3")
        buf.write("\2\2\2\u0160\u0162\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0163")
        buf.write("\t\b\2\2\u0163\u0164\b\60\2\2\u0164`\3\2\2\2\u0165\u0167")
        buf.write("\t\n\2\2\u0166\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016a\u016b\b\61\3\2\u016bb\3\2\2\2\u016c\u0171\7$\2")
        buf.write("\2\u016d\u0170\5]/\2\u016e\u0170\n\t\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u016f\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0174\u0175\7^\2\2\u0175\u0176\n\13\2\2")
        buf.write("\u0176\u0177\b\62\4\2\u0177d\3\2\2\2\u0178\u017d\t\b\2")
        buf.write("\2\u0179\u017c\5]/\2\u017a\u017c\n\t\2\2\u017b\u0179\3")
        buf.write("\2\2\2\u017b\u017a\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u0180\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0181\b\63\5\2\u0181f\3\2\2\2\u0182")
        buf.write("\u0183\13\2\2\2\u0183h\3\2\2\2\32\2\u0116\u011a\u011f")
        buf.write("\u0122\u0127\u012e\u0132\u0137\u0139\u013c\u0141\u0145")
        buf.write("\u014a\u014e\u0153\u0155\u015d\u015f\u0168\u016f\u0171")
        buf.write("\u017b\u017d\6\3\60\2\b\2\2\3\62\3\3\63\4")
        return buf.getvalue()


class TyCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    AUTO = 3
    BREAK = 4
    CASE = 5
    CONTINUE = 6
    DEFAULT = 7
    ELSE = 8
    FLOAT = 9
    FOR = 10
    IF = 11
    INT = 12
    RETURN = 13
    STRING = 14
    STRUCT = 15
    SWITCH = 16
    VOID = 17
    WHILE = 18
    ADD = 19
    SUB = 20
    MUL = 21
    DIV = 22
    MOD = 23
    EQUAL = 24
    NOTEQUAL = 25
    LESSTHAN = 26
    GREATERTHAN = 27
    LESSTHAN_EQUAL = 28
    GREATERTHAN_EQUAL = 29
    OR = 30
    AND = 31
    NOT = 32
    INCREMENT = 33
    DECREMENT = 34
    ASSIGN = 35
    ACCESS = 36
    LP = 37
    RP = 38
    LB = 39
    RB = 40
    CM = 41
    SM = 42
    ID = 43
    INTLIT = 44
    FLOATLIT = 45
    STRINGLIT = 46
    WS = 47
    ILLEGAL_ESCAPE = 48
    UNCLOSE_STRING = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'statementlist'", "'expr'", "'auto'", "'break'", "'case'", 
            "'continue'", "'default'", "'else'", "'float'", "'for'", "'if'", 
            "'int'", "'return'", "'string'", "'struct'", "'switch'", "'void'", 
            "'while'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
            "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'++'", 
            "'--'", "'='", "'.'", "'('", "')'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", 
            "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", "SWITCH", 
            "VOID", "WHILE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
            "NOTEQUAL", "LESSTHAN", "GREATERTHAN", "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", 
            "OR", "AND", "NOT", "INCREMENT", "DECREMENT", "ASSIGN", "ACCESS", 
            "LP", "RP", "LB", "RB", "CM", "SM", "ID", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", 
                  "ELSE", "FLOAT", "FOR", "IF", "INT", "RETURN", "STRING", 
                  "STRUCT", "SWITCH", "VOID", "WHILE", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "EQUAL", "NOTEQUAL", "LESSTHAN", "GREATERTHAN", 
                  "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", "OR", "AND", "NOT", 
                  "INCREMENT", "DECREMENT", "ASSIGN", "ACCESS", "LP", "RP", 
                  "LB", "RB", "CM", "SM", "ID", "INTLIT", "FLOATLIT", "ESCAPE", 
                  "STRINGLIT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
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
            actions[46] = self.STRINGLIT_action 
            actions[48] = self.ILLEGAL_ESCAPE_action 
            actions[49] = self.UNCLOSE_STRING_action 
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
     


