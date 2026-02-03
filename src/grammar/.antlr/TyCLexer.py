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
        buf.write("\u0190\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3+\3+\7+\u0106\n+\f+\16+\u0109\13")
        buf.write("+\3,\5,\u010c\n,\3,\6,\u010f\n,\r,\16,\u0110\3-\5-\u0114")
        buf.write("\n-\3-\7-\u0117\n-\f-\16-\u011a\13-\3-\3-\6-\u011e\n-")
        buf.write("\r-\16-\u011f\3-\3-\3-\5-\u0125\n-\3-\6-\u0128\n-\r-\16")
        buf.write("-\u0129\5-\u012c\n-\3-\5-\u012f\n-\3-\6-\u0132\n-\r-\16")
        buf.write("-\u0133\3-\3-\5-\u0138\n-\3-\6-\u013b\n-\r-\16-\u013c")
        buf.write("\3-\3-\3-\5-\u0142\n-\3-\6-\u0145\n-\r-\16-\u0146\5-\u0149")
        buf.write("\n-\3.\3.\3.\3/\3/\3/\7/\u0151\n/\f/\16/\u0154\13/\3/")
        buf.write("\3/\3/\3\60\6\60\u015a\n\60\r\60\16\60\u015b\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u0164\n\61\f\61\16\61\u0167")
        buf.write("\13\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u016f\n\62\f")
        buf.write("\62\16\62\u0172\13\62\3\62\3\62\3\62\3\62\3\62\3\63\3")
        buf.write("\63\3\63\7\63\u017c\n\63\f\63\16\63\u017f\13\63\3\63\3")
        buf.write("\63\3\63\3\63\3\64\3\64\3\64\7\64\u0188\n\64\f\64\16\64")
        buf.write("\u018b\13\64\3\64\3\64\3\65\3\65\3\u0170\2\66\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[\2]/_\60a\61c\62e\63g\64i\65\3\2\r\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2//\3\2\62;\4\2GGgg\t\2$$^^ddhhppttvv\3\2$")
        buf.write("$\6\2\f\f\17\17$$^^\5\2\13\f\16\17\"\"\4\2\f\f\17\17\13")
        buf.write("\2\f\f\17\17$$^^ddhhppttvv\2\u01aa\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3\2\2\2\5")
        buf.write("p\3\2\2\2\7v\3\2\2\2\t{\3\2\2\2\13\u0084\3\2\2\2\r\u008c")
        buf.write("\3\2\2\2\17\u0091\3\2\2\2\21\u0097\3\2\2\2\23\u009b\3")
        buf.write("\2\2\2\25\u009e\3\2\2\2\27\u00a2\3\2\2\2\31\u00a9\3\2")
        buf.write("\2\2\33\u00b0\3\2\2\2\35\u00b7\3\2\2\2\37\u00be\3\2\2")
        buf.write("\2!\u00c3\3\2\2\2#\u00c9\3\2\2\2%\u00cb\3\2\2\2\'\u00cd")
        buf.write("\3\2\2\2)\u00cf\3\2\2\2+\u00d1\3\2\2\2-\u00d3\3\2\2\2")
        buf.write("/\u00d6\3\2\2\2\61\u00d9\3\2\2\2\63\u00db\3\2\2\2\65\u00dd")
        buf.write("\3\2\2\2\67\u00e0\3\2\2\29\u00e3\3\2\2\2;\u00e6\3\2\2")
        buf.write("\2=\u00e9\3\2\2\2?\u00eb\3\2\2\2A\u00ee\3\2\2\2C\u00f1")
        buf.write("\3\2\2\2E\u00f3\3\2\2\2G\u00f5\3\2\2\2I\u00f7\3\2\2\2")
        buf.write("K\u00f9\3\2\2\2M\u00fb\3\2\2\2O\u00fd\3\2\2\2Q\u00ff\3")
        buf.write("\2\2\2S\u0101\3\2\2\2U\u0103\3\2\2\2W\u010b\3\2\2\2Y\u0148")
        buf.write("\3\2\2\2[\u014a\3\2\2\2]\u014d\3\2\2\2_\u0159\3\2\2\2")
        buf.write("a\u015f\3\2\2\2c\u016a\3\2\2\2e\u0178\3\2\2\2g\u0184\3")
        buf.write("\2\2\2i\u018e\3\2\2\2kl\7c\2\2lm\7w\2\2mn\7v\2\2no\7q")
        buf.write("\2\2o\4\3\2\2\2pq\7d\2\2qr\7t\2\2rs\7g\2\2st\7c\2\2tu")
        buf.write("\7m\2\2u\6\3\2\2\2vw\7e\2\2wx\7c\2\2xy\7u\2\2yz\7g\2\2")
        buf.write("z\b\3\2\2\2{|\7e\2\2|}\7q\2\2}~\7p\2\2~\177\7v\2\2\177")
        buf.write("\u0080\7k\2\2\u0080\u0081\7p\2\2\u0081\u0082\7w\2\2\u0082")
        buf.write("\u0083\7g\2\2\u0083\n\3\2\2\2\u0084\u0085\7f\2\2\u0085")
        buf.write("\u0086\7g\2\2\u0086\u0087\7h\2\2\u0087\u0088\7c\2\2\u0088")
        buf.write("\u0089\7w\2\2\u0089\u008a\7n\2\2\u008a\u008b\7v\2\2\u008b")
        buf.write("\f\3\2\2\2\u008c\u008d\7g\2\2\u008d\u008e\7n\2\2\u008e")
        buf.write("\u008f\7u\2\2\u008f\u0090\7g\2\2\u0090\16\3\2\2\2\u0091")
        buf.write("\u0092\7h\2\2\u0092\u0093\7n\2\2\u0093\u0094\7q\2\2\u0094")
        buf.write("\u0095\7c\2\2\u0095\u0096\7v\2\2\u0096\20\3\2\2\2\u0097")
        buf.write("\u0098\7h\2\2\u0098\u0099\7q\2\2\u0099\u009a\7t\2\2\u009a")
        buf.write("\22\3\2\2\2\u009b\u009c\7k\2\2\u009c\u009d\7h\2\2\u009d")
        buf.write("\24\3\2\2\2\u009e\u009f\7k\2\2\u009f\u00a0\7p\2\2\u00a0")
        buf.write("\u00a1\7v\2\2\u00a1\26\3\2\2\2\u00a2\u00a3\7t\2\2\u00a3")
        buf.write("\u00a4\7g\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7w\2\2\u00a6")
        buf.write("\u00a7\7t\2\2\u00a7\u00a8\7p\2\2\u00a8\30\3\2\2\2\u00a9")
        buf.write("\u00aa\7u\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7t\2\2\u00ac")
        buf.write("\u00ad\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7i\2\2\u00af")
        buf.write("\32\3\2\2\2\u00b0\u00b1\7u\2\2\u00b1\u00b2\7v\2\2\u00b2")
        buf.write("\u00b3\7t\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7e\2\2\u00b5")
        buf.write("\u00b6\7v\2\2\u00b6\34\3\2\2\2\u00b7\u00b8\7u\2\2\u00b8")
        buf.write("\u00b9\7y\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7v\2\2\u00bb")
        buf.write("\u00bc\7e\2\2\u00bc\u00bd\7j\2\2\u00bd\36\3\2\2\2\u00be")
        buf.write("\u00bf\7x\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7k\2\2\u00c1")
        buf.write("\u00c2\7f\2\2\u00c2 \3\2\2\2\u00c3\u00c4\7y\2\2\u00c4")
        buf.write("\u00c5\7j\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7n\2\2\u00c7")
        buf.write("\u00c8\7g\2\2\u00c8\"\3\2\2\2\u00c9\u00ca\7-\2\2\u00ca")
        buf.write("$\3\2\2\2\u00cb\u00cc\7/\2\2\u00cc&\3\2\2\2\u00cd\u00ce")
        buf.write("\7,\2\2\u00ce(\3\2\2\2\u00cf\u00d0\7\61\2\2\u00d0*\3\2")
        buf.write("\2\2\u00d1\u00d2\7\'\2\2\u00d2,\3\2\2\2\u00d3\u00d4\7")
        buf.write("?\2\2\u00d4\u00d5\7?\2\2\u00d5.\3\2\2\2\u00d6\u00d7\7")
        buf.write("#\2\2\u00d7\u00d8\7?\2\2\u00d8\60\3\2\2\2\u00d9\u00da")
        buf.write("\7>\2\2\u00da\62\3\2\2\2\u00db\u00dc\7@\2\2\u00dc\64\3")
        buf.write("\2\2\2\u00dd\u00de\7>\2\2\u00de\u00df\7?\2\2\u00df\66")
        buf.write("\3\2\2\2\u00e0\u00e1\7@\2\2\u00e1\u00e2\7?\2\2\u00e28")
        buf.write("\3\2\2\2\u00e3\u00e4\7~\2\2\u00e4\u00e5\7~\2\2\u00e5:")
        buf.write("\3\2\2\2\u00e6\u00e7\7(\2\2\u00e7\u00e8\7(\2\2\u00e8<")
        buf.write("\3\2\2\2\u00e9\u00ea\7#\2\2\u00ea>\3\2\2\2\u00eb\u00ec")
        buf.write("\7-\2\2\u00ec\u00ed\7-\2\2\u00ed@\3\2\2\2\u00ee\u00ef")
        buf.write("\7/\2\2\u00ef\u00f0\7/\2\2\u00f0B\3\2\2\2\u00f1\u00f2")
        buf.write("\7?\2\2\u00f2D\3\2\2\2\u00f3\u00f4\7\60\2\2\u00f4F\3\2")
        buf.write("\2\2\u00f5\u00f6\7*\2\2\u00f6H\3\2\2\2\u00f7\u00f8\7+")
        buf.write("\2\2\u00f8J\3\2\2\2\u00f9\u00fa\7}\2\2\u00faL\3\2\2\2")
        buf.write("\u00fb\u00fc\7\177\2\2\u00fcN\3\2\2\2\u00fd\u00fe\7.\2")
        buf.write("\2\u00feP\3\2\2\2\u00ff\u0100\7=\2\2\u0100R\3\2\2\2\u0101")
        buf.write("\u0102\7<\2\2\u0102T\3\2\2\2\u0103\u0107\t\2\2\2\u0104")
        buf.write("\u0106\t\3\2\2\u0105\u0104\3\2\2\2\u0106\u0109\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108V\3\2\2")
        buf.write("\2\u0109\u0107\3\2\2\2\u010a\u010c\t\4\2\2\u010b\u010a")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010e\3\2\2\2\u010d")
        buf.write("\u010f\t\5\2\2\u010e\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111X\3\2\2")
        buf.write("\2\u0112\u0114\t\4\2\2\u0113\u0112\3\2\2\2\u0113\u0114")
        buf.write("\3\2\2\2\u0114\u0118\3\2\2\2\u0115\u0117\t\5\2\2\u0116")
        buf.write("\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119\u011b\3\2\2\2\u011a\u0118\3")
        buf.write("\2\2\2\u011b\u011d\7\60\2\2\u011c\u011e\t\5\2\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120\u012b\3\2\2\2\u0121\u0124\t")
        buf.write("\6\2\2\u0122\u0125\5%\23\2\u0123\u0125\5#\22\2\u0124\u0122")
        buf.write("\3\2\2\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0127\3\2\2\2\u0126\u0128\t\5\2\2\u0127\u0126\3\2\2\2")
        buf.write("\u0128\u0129\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\u012c\3\2\2\2\u012b\u0121\3\2\2\2\u012b\u012c")
        buf.write("\3\2\2\2\u012c\u0149\3\2\2\2\u012d\u012f\t\4\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0131\3\2\2\2")
        buf.write("\u0130\u0132\t\5\2\2\u0131\u0130\3\2\2\2\u0132\u0133\3")
        buf.write("\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135")
        buf.write("\3\2\2\2\u0135\u0149\7\60\2\2\u0136\u0138\t\4\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2")
        buf.write("\u0139\u013b\t\5\2\2\u013a\u0139\3\2\2\2\u013b\u013c\3")
        buf.write("\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e")
        buf.write("\3\2\2\2\u013e\u0141\t\6\2\2\u013f\u0142\5%\23\2\u0140")
        buf.write("\u0142\5#\22\2\u0141\u013f\3\2\2\2\u0141\u0140\3\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143\u0145\t")
        buf.write("\5\2\2\u0144\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\3\2\2\2\u0148")
        buf.write("\u0113\3\2\2\2\u0148\u012e\3\2\2\2\u0148\u0137\3\2\2\2")
        buf.write("\u0149Z\3\2\2\2\u014a\u014b\7^\2\2\u014b\u014c\t\7\2\2")
        buf.write("\u014c\\\3\2\2\2\u014d\u0152\t\b\2\2\u014e\u0151\5[.\2")
        buf.write("\u014f\u0151\n\t\2\2\u0150\u014e\3\2\2\2\u0150\u014f\3")
        buf.write("\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153\u0155\3\2\2\2\u0154\u0152\3\2\2\2\u0155")
        buf.write("\u0156\t\b\2\2\u0156\u0157\b/\2\2\u0157^\3\2\2\2\u0158")
        buf.write("\u015a\t\n\2\2\u0159\u0158\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\3")
        buf.write("\2\2\2\u015d\u015e\b\60\3\2\u015e`\3\2\2\2\u015f\u0160")
        buf.write("\7\61\2\2\u0160\u0161\7\61\2\2\u0161\u0165\3\2\2\2\u0162")
        buf.write("\u0164\n\13\2\2\u0163\u0162\3\2\2\2\u0164\u0167\3\2\2")
        buf.write("\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0168")
        buf.write("\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\b\61\3\2\u0169")
        buf.write("b\3\2\2\2\u016a\u016b\7\61\2\2\u016b\u016c\7,\2\2\u016c")
        buf.write("\u0170\3\2\2\2\u016d\u016f\13\2\2\2\u016e\u016d\3\2\2")
        buf.write("\2\u016f\u0172\3\2\2\2\u0170\u0171\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2\2\u0173")
        buf.write("\u0174\7,\2\2\u0174\u0175\7\61\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\b\62\3\2\u0177d\3\2\2\2\u0178\u017d\7$\2")
        buf.write("\2\u0179\u017c\5[.\2\u017a\u017c\n\t\2\2\u017b\u0179\3")
        buf.write("\2\2\2\u017b\u017a\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u0180\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0181\7^\2\2\u0181\u0182\n\f\2\2")
        buf.write("\u0182\u0183\b\63\4\2\u0183f\3\2\2\2\u0184\u0189\t\b\2")
        buf.write("\2\u0185\u0188\5[.\2\u0186\u0188\n\t\2\2\u0187\u0185\3")
        buf.write("\2\2\2\u0187\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018c\u018d\b\64\5\2\u018dh\3\2\2\2\u018e")
        buf.write("\u018f\13\2\2\2\u018fj\3\2\2\2\34\2\u0107\u010b\u0110")
        buf.write("\u0113\u0118\u011f\u0124\u0129\u012b\u012e\u0133\u0137")
        buf.write("\u013c\u0141\u0146\u0148\u0150\u0152\u015b\u0165\u0170")
        buf.write("\u017b\u017d\u0187\u0189\6\3/\2\b\2\2\3\63\3\3\64\4")
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
    LINE_COMMENT = 47
    BLOCK_COMMENT = 48
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
            "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", 
            "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", "SWITCH", 
            "VOID", "WHILE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
            "NOTEQUAL", "LESSTHAN", "GREATERTHAN", "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", 
            "OR", "AND", "NOT", "INCREMENT", "DECREMENT", "ASSIGN", "ACCESS", 
            "LP", "RP", "LB", "RB", "CM", "SM", "CL", "ID", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", 
                  "FLOAT", "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", 
                  "SWITCH", "VOID", "WHILE", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "EQUAL", "NOTEQUAL", "LESSTHAN", "GREATERTHAN", 
                  "LESSTHAN_EQUAL", "GREATERTHAN_EQUAL", "OR", "AND", "NOT", 
                  "INCREMENT", "DECREMENT", "ASSIGN", "ACCESS", "LP", "RP", 
                  "LB", "RB", "CM", "SM", "CL", "ID", "INTLIT", "FLOATLIT", 
                  "ESCAPE", "STRINGLIT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

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
     


