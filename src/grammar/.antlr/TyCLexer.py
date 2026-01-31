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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u018e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\2\3\2\7\2p\n\2\f\2\16\2s\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3{\n\3\f\3\16\3~\13\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\6\4\u0086\n\4\r\4\16\4\u0087\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$")
        buf.write("\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,")
        buf.write("\3,\3-\3-\3.\3.\7.\u0126\n.\f.\16.\u0129\13.\3/\5/\u012c")
        buf.write("\n/\3/\6/\u012f\n/\r/\16/\u0130\3\60\5\60\u0134\n\60\3")
        buf.write("\60\7\60\u0137\n\60\f\60\16\60\u013a\13\60\3\60\3\60\6")
        buf.write("\60\u013e\n\60\r\60\16\60\u013f\3\60\3\60\5\60\u0144\n")
        buf.write("\60\3\60\6\60\u0147\n\60\r\60\16\60\u0148\5\60\u014b\n")
        buf.write("\60\3\60\5\60\u014e\n\60\3\60\6\60\u0151\n\60\r\60\16")
        buf.write("\60\u0152\3\60\3\60\5\60\u0157\n\60\3\60\6\60\u015a\n")
        buf.write("\60\r\60\16\60\u015b\3\60\3\60\5\60\u0160\n\60\3\60\6")
        buf.write("\60\u0163\n\60\r\60\16\60\u0164\5\60\u0167\n\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\7\62\u016f\n\62\f\62\16\62\u0172")
        buf.write("\13\62\3\62\3\62\3\62\3\63\3\63\3\63\7\63\u017a\n\63\f")
        buf.write("\63\16\63\u017d\13\63\3\63\3\63\3\63\3\63\3\64\3\64\3")
        buf.write("\64\7\64\u0186\n\64\f\64\16\64\u0189\13\64\3\64\3\64\3")
        buf.write("\65\3\65\3|\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\2c\62e\63g\64i")
        buf.write("\65\3\2\r\4\2\f\f\17\17\5\2\13\f\16\17\"\"\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\3\2//\3\2\62;\4\2GGgg\t\2$$^^ddhhpptt")
        buf.write("vv\3\2$$\6\2\f\f\17\17$$^^\13\2\f\f\17\17$$^^ddhhpptt")
        buf.write("vv\2\u01a6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g")
        buf.write("\3\2\2\2\2i\3\2\2\2\3k\3\2\2\2\5v\3\2\2\2\7\u0085\3\2")
        buf.write("\2\2\t\u008b\3\2\2\2\13\u0090\3\2\2\2\r\u0096\3\2\2\2")
        buf.write("\17\u009b\3\2\2\2\21\u00a4\3\2\2\2\23\u00ac\3\2\2\2\25")
        buf.write("\u00b1\3\2\2\2\27\u00b7\3\2\2\2\31\u00bb\3\2\2\2\33\u00be")
        buf.write("\3\2\2\2\35\u00c2\3\2\2\2\37\u00c9\3\2\2\2!\u00d0\3\2")
        buf.write("\2\2#\u00d7\3\2\2\2%\u00de\3\2\2\2\'\u00e3\3\2\2\2)\u00e9")
        buf.write("\3\2\2\2+\u00eb\3\2\2\2-\u00ed\3\2\2\2/\u00ef\3\2\2\2")
        buf.write("\61\u00f1\3\2\2\2\63\u00f3\3\2\2\2\65\u00f6\3\2\2\2\67")
        buf.write("\u00f9\3\2\2\29\u00fb\3\2\2\2;\u00fd\3\2\2\2=\u0100\3")
        buf.write("\2\2\2?\u0103\3\2\2\2A\u0106\3\2\2\2C\u0109\3\2\2\2E\u010b")
        buf.write("\3\2\2\2G\u010e\3\2\2\2I\u0111\3\2\2\2K\u0113\3\2\2\2")
        buf.write("M\u0115\3\2\2\2O\u0117\3\2\2\2Q\u0119\3\2\2\2S\u011b\3")
        buf.write("\2\2\2U\u011d\3\2\2\2W\u011f\3\2\2\2Y\u0121\3\2\2\2[\u0123")
        buf.write("\3\2\2\2]\u012b\3\2\2\2_\u0166\3\2\2\2a\u0168\3\2\2\2")
        buf.write("c\u016b\3\2\2\2e\u0176\3\2\2\2g\u0182\3\2\2\2i\u018c\3")
        buf.write("\2\2\2kl\7\61\2\2lm\7\61\2\2mq\3\2\2\2np\n\2\2\2on\3\2")
        buf.write("\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2sq\3\2\2\2")
        buf.write("tu\b\2\2\2u\4\3\2\2\2vw\7\61\2\2wx\7,\2\2x|\3\2\2\2y{")
        buf.write("\13\2\2\2zy\3\2\2\2{~\3\2\2\2|}\3\2\2\2|z\3\2\2\2}\177")
        buf.write("\3\2\2\2~|\3\2\2\2\177\u0080\7,\2\2\u0080\u0081\7\61\2")
        buf.write("\2\u0081\u0082\3\2\2\2\u0082\u0083\b\3\2\2\u0083\6\3\2")
        buf.write("\2\2\u0084\u0086\t\3\2\2\u0085\u0084\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0089\u008a\b\4\2\2\u008a\b\3\2\2\2\u008b")
        buf.write("\u008c\7c\2\2\u008c\u008d\7w\2\2\u008d\u008e\7v\2\2\u008e")
        buf.write("\u008f\7q\2\2\u008f\n\3\2\2\2\u0090\u0091\7d\2\2\u0091")
        buf.write("\u0092\7t\2\2\u0092\u0093\7g\2\2\u0093\u0094\7c\2\2\u0094")
        buf.write("\u0095\7m\2\2\u0095\f\3\2\2\2\u0096\u0097\7e\2\2\u0097")
        buf.write("\u0098\7c\2\2\u0098\u0099\7u\2\2\u0099\u009a\7g\2\2\u009a")
        buf.write("\16\3\2\2\2\u009b\u009c\7e\2\2\u009c\u009d\7q\2\2\u009d")
        buf.write("\u009e\7p\2\2\u009e\u009f\7v\2\2\u009f\u00a0\7k\2\2\u00a0")
        buf.write("\u00a1\7p\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7g\2\2\u00a3")
        buf.write("\20\3\2\2\2\u00a4\u00a5\7f\2\2\u00a5\u00a6\7g\2\2\u00a6")
        buf.write("\u00a7\7h\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7w\2\2\u00a9")
        buf.write("\u00aa\7n\2\2\u00aa\u00ab\7v\2\2\u00ab\22\3\2\2\2\u00ac")
        buf.write("\u00ad\7g\2\2\u00ad\u00ae\7n\2\2\u00ae\u00af\7u\2\2\u00af")
        buf.write("\u00b0\7g\2\2\u00b0\24\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2")
        buf.write("\u00b3\7n\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7c\2\2\u00b5")
        buf.write("\u00b6\7v\2\2\u00b6\26\3\2\2\2\u00b7\u00b8\7h\2\2\u00b8")
        buf.write("\u00b9\7q\2\2\u00b9\u00ba\7t\2\2\u00ba\30\3\2\2\2\u00bb")
        buf.write("\u00bc\7k\2\2\u00bc\u00bd\7h\2\2\u00bd\32\3\2\2\2\u00be")
        buf.write("\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7v\2\2\u00c1")
        buf.write("\34\3\2\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4\7g\2\2\u00c4")
        buf.write("\u00c5\7v\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7\7t\2\2\u00c7")
        buf.write("\u00c8\7p\2\2\u00c8\36\3\2\2\2\u00c9\u00ca\7u\2\2\u00ca")
        buf.write("\u00cb\7v\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7k\2\2\u00cd")
        buf.write("\u00ce\7p\2\2\u00ce\u00cf\7i\2\2\u00cf \3\2\2\2\u00d0")
        buf.write("\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7t\2\2\u00d3")
        buf.write("\u00d4\7w\2\2\u00d4\u00d5\7e\2\2\u00d5\u00d6\7v\2\2\u00d6")
        buf.write("\"\3\2\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9\7y\2\2\u00d9")
        buf.write("\u00da\7k\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7e\2\2\u00dc")
        buf.write("\u00dd\7j\2\2\u00dd$\3\2\2\2\u00de\u00df\7x\2\2\u00df")
        buf.write("\u00e0\7q\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7f\2\2\u00e2")
        buf.write("&\3\2\2\2\u00e3\u00e4\7y\2\2\u00e4\u00e5\7j\2\2\u00e5")
        buf.write("\u00e6\7k\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("(\3\2\2\2\u00e9\u00ea\7-\2\2\u00ea*\3\2\2\2\u00eb\u00ec")
        buf.write("\7/\2\2\u00ec,\3\2\2\2\u00ed\u00ee\7,\2\2\u00ee.\3\2\2")
        buf.write("\2\u00ef\u00f0\7\61\2\2\u00f0\60\3\2\2\2\u00f1\u00f2\7")
        buf.write("\'\2\2\u00f2\62\3\2\2\2\u00f3\u00f4\7?\2\2\u00f4\u00f5")
        buf.write("\7?\2\2\u00f5\64\3\2\2\2\u00f6\u00f7\7#\2\2\u00f7\u00f8")
        buf.write("\7?\2\2\u00f8\66\3\2\2\2\u00f9\u00fa\7>\2\2\u00fa8\3\2")
        buf.write("\2\2\u00fb\u00fc\7@\2\2\u00fc:\3\2\2\2\u00fd\u00fe\7>")
        buf.write("\2\2\u00fe\u00ff\7?\2\2\u00ff<\3\2\2\2\u0100\u0101\7@")
        buf.write("\2\2\u0101\u0102\7?\2\2\u0102>\3\2\2\2\u0103\u0104\7~")
        buf.write("\2\2\u0104\u0105\7~\2\2\u0105@\3\2\2\2\u0106\u0107\7(")
        buf.write("\2\2\u0107\u0108\7(\2\2\u0108B\3\2\2\2\u0109\u010a\7#")
        buf.write("\2\2\u010aD\3\2\2\2\u010b\u010c\7-\2\2\u010c\u010d\7-")
        buf.write("\2\2\u010dF\3\2\2\2\u010e\u010f\7/\2\2\u010f\u0110\7/")
        buf.write("\2\2\u0110H\3\2\2\2\u0111\u0112\7?\2\2\u0112J\3\2\2\2")
        buf.write("\u0113\u0114\7\60\2\2\u0114L\3\2\2\2\u0115\u0116\7*\2")
        buf.write("\2\u0116N\3\2\2\2\u0117\u0118\7+\2\2\u0118P\3\2\2\2\u0119")
        buf.write("\u011a\7}\2\2\u011aR\3\2\2\2\u011b\u011c\7\177\2\2\u011c")
        buf.write("T\3\2\2\2\u011d\u011e\7.\2\2\u011eV\3\2\2\2\u011f\u0120")
        buf.write("\7=\2\2\u0120X\3\2\2\2\u0121\u0122\7<\2\2\u0122Z\3\2\2")
        buf.write("\2\u0123\u0127\t\4\2\2\u0124\u0126\t\5\2\2\u0125\u0124")
        buf.write("\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128\\\3\2\2\2\u0129\u0127\3\2\2\2\u012a")
        buf.write("\u012c\t\6\2\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012c\u012e\3\2\2\2\u012d\u012f\t\7\2\2\u012e\u012d\3")
        buf.write("\2\2\2\u012f\u0130\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131^\3\2\2\2\u0132\u0134\t\6\2\2\u0133\u0132")
        buf.write("\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0138\3\2\2\2\u0135")
        buf.write("\u0137\t\7\2\2\u0136\u0135\3\2\2\2\u0137\u013a\3\2\2\2")
        buf.write("\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3")
        buf.write("\2\2\2\u013a\u0138\3\2\2\2\u013b\u013d\7\60\2\2\u013c")
        buf.write("\u013e\t\7\2\2\u013d\u013c\3\2\2\2\u013e\u013f\3\2\2\2")
        buf.write("\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u014a\3")
        buf.write("\2\2\2\u0141\u0143\t\b\2\2\u0142\u0144\t\6\2\2\u0143\u0142")
        buf.write("\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145")
        buf.write("\u0147\t\7\2\2\u0146\u0145\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014b\3")
        buf.write("\2\2\2\u014a\u0141\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u0167")
        buf.write("\3\2\2\2\u014c\u014e\t\6\2\2\u014d\u014c\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u0151\t\7\2\2")
        buf.write("\u0150\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0150\3")
        buf.write("\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0167")
        buf.write("\7\60\2\2\u0155\u0157\t\6\2\2\u0156\u0155\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u015a\t\7\2\2")
        buf.write("\u0159\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0159\3")
        buf.write("\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f")
        buf.write("\t\b\2\2\u015e\u0160\t\6\2\2\u015f\u015e\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u0163\t\7\2\2")
        buf.write("\u0162\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0133")
        buf.write("\3\2\2\2\u0166\u014d\3\2\2\2\u0166\u0156\3\2\2\2\u0167")
        buf.write("`\3\2\2\2\u0168\u0169\7^\2\2\u0169\u016a\t\t\2\2\u016a")
        buf.write("b\3\2\2\2\u016b\u0170\t\n\2\2\u016c\u016f\5a\61\2\u016d")
        buf.write("\u016f\n\13\2\2\u016e\u016c\3\2\2\2\u016e\u016d\3\2\2")
        buf.write("\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171")
        buf.write("\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2\2\u0173")
        buf.write("\u0174\t\n\2\2\u0174\u0175\b\62\3\2\u0175d\3\2\2\2\u0176")
        buf.write("\u017b\7$\2\2\u0177\u017a\5a\61\2\u0178\u017a\n\13\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a\u017d\3")
        buf.write("\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e")
        buf.write("\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\7^\2\2\u017f")
        buf.write("\u0180\n\f\2\2\u0180\u0181\b\63\4\2\u0181f\3\2\2\2\u0182")
        buf.write("\u0187\t\n\2\2\u0183\u0186\5a\61\2\u0184\u0186\n\13\2")
        buf.write("\2\u0185\u0183\3\2\2\2\u0185\u0184\3\2\2\2\u0186\u0189")
        buf.write("\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("\u018a\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b\b\64\5")
        buf.write("\2\u018bh\3\2\2\2\u018c\u018d\13\2\2\2\u018dj\3\2\2\2")
        buf.write("\34\2q|\u0087\u0127\u012b\u0130\u0133\u0138\u013f\u0143")
        buf.write("\u0148\u014a\u014d\u0152\u0156\u015b\u015f\u0164\u0166")
        buf.write("\u016e\u0170\u0179\u017b\u0185\u0187\6\b\2\2\3\62\2\3")
        buf.write("\63\3\3\64\4")
        return buf.getvalue()


class TyCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_COMMENT = 1
    BLOCK_COMMENT = 2
    WS = 3
    AUTO = 4
    BREAK = 5
    CASE = 6
    CONTINUE = 7
    DEFAULT = 8
    ELSE = 9
    FLOAT = 10
    FOR = 11
    IF = 12
    INT = 13
    RETURN = 14
    STRING = 15
    STRUCT = 16
    SWITCH = 17
    VOID = 18
    WHILE = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    MOD = 24
    EQUAL = 25
    NOTEQUAL = 26
    LESSTHAN = 27
    GREATERTHAN = 28
    LESSTHAN_EQUAL = 29
    GREATERTHAN_EQUAL = 30
    OR = 31
    AND = 32
    NOT = 33
    INCREMENT = 34
    DECREMENT = 35
    ASSIGN = 36
    ACCESS = 37
    LP = 38
    RP = 39
    LB = 40
    RB = 41
    CM = 42
    SM = 43
    CL = 44
    ID = 45
    INTLIT = 46
    FLOATLIT = 47
    STRINGLIT = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50
    ERROR_CHAR = 51

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
            "LINE_COMMENT", "BLOCK_COMMENT", "WS", "AUTO", "BREAK", "CASE", 
            "CONTINUE", "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", 
            "RETURN", "STRING", "STRUCT", "SWITCH", "VOID", "WHILE", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", "LESSTHAN", 
            "GREATERTHAN", "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", "OR", 
            "AND", "NOT", "INCREMENT", "DECREMENT", "ASSIGN", "ACCESS", 
            "LP", "RP", "LB", "RB", "CM", "SM", "CL", "ID", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "LINE_COMMENT", "BLOCK_COMMENT", "WS", "AUTO", "BREAK", 
                  "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", "FOR", 
                  "IF", "INT", "RETURN", "STRING", "STRUCT", "SWITCH", "VOID", 
                  "WHILE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", 
                  "LESSTHAN", "GREATERTHAN", "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", 
                  "OR", "AND", "NOT", "INCREMENT", "DECREMENT", "ASSIGN", 
                  "ACCESS", "LP", "RP", "LB", "RB", "CM", "SM", "CL", "ID", 
                  "INTLIT", "FLOATLIT", "ESCAPE", "STRINGLIT", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            actions[48] = self.STRINGLIT_action 
            actions[49] = self.ILLEGAL_ESCAPE_action 
            actions[50] = self.UNCLOSE_STRING_action 
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
     


