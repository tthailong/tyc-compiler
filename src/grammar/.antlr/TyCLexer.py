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
        buf.write("\u0184\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("+\3,\6,\u010c\n,\r,\16,\u010d\3-\7-\u0111\n-\f-\16-\u0114")
        buf.write("\13-\3-\3-\6-\u0118\n-\r-\16-\u0119\3-\3-\3-\5-\u011f")
        buf.write("\n-\3-\6-\u0122\n-\r-\16-\u0123\5-\u0126\n-\3-\6-\u0129")
        buf.write("\n-\r-\16-\u012a\3-\3-\6-\u012f\n-\r-\16-\u0130\3-\3-")
        buf.write("\3-\5-\u0136\n-\3-\6-\u0139\n-\r-\16-\u013a\5-\u013d\n")
        buf.write("-\3.\3.\3.\3/\3/\3/\7/\u0145\n/\f/\16/\u0148\13/\3/\3")
        buf.write("/\3/\3\60\6\60\u014e\n\60\r\60\16\60\u014f\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\7\61\u0158\n\61\f\61\16\61\u015b\13")
        buf.write("\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u0163\n\62\f\62")
        buf.write("\16\62\u0166\13\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\7\63\u0170\n\63\f\63\16\63\u0173\13\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\7\64\u017c\n\64\f\64\16\64\u017f")
        buf.write("\13\64\3\64\3\64\3\65\3\65\3\u0164\2\66\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]")
        buf.write("/_\60a\61c\62e\63g\64i\65\3\2\f\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\4\2GGgg\t\2$$^^ddhhppttvv\3\2$$\6\2\f\f\17")
        buf.write("\17$$^^\5\2\13\f\16\17\"\"\4\2\f\f\17\17\13\2\f\f\17\17")
        buf.write("$$^^ddhhppttvv\2\u019a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3\2\2\2\5p\3\2\2\2\7")
        buf.write("v\3\2\2\2\t{\3\2\2\2\13\u0084\3\2\2\2\r\u008c\3\2\2\2")
        buf.write("\17\u0091\3\2\2\2\21\u0097\3\2\2\2\23\u009b\3\2\2\2\25")
        buf.write("\u009e\3\2\2\2\27\u00a2\3\2\2\2\31\u00a9\3\2\2\2\33\u00b0")
        buf.write("\3\2\2\2\35\u00b7\3\2\2\2\37\u00be\3\2\2\2!\u00c3\3\2")
        buf.write("\2\2#\u00c9\3\2\2\2%\u00cb\3\2\2\2\'\u00cd\3\2\2\2)\u00cf")
        buf.write("\3\2\2\2+\u00d1\3\2\2\2-\u00d3\3\2\2\2/\u00d6\3\2\2\2")
        buf.write("\61\u00d9\3\2\2\2\63\u00db\3\2\2\2\65\u00dd\3\2\2\2\67")
        buf.write("\u00e0\3\2\2\29\u00e3\3\2\2\2;\u00e6\3\2\2\2=\u00e9\3")
        buf.write("\2\2\2?\u00eb\3\2\2\2A\u00ee\3\2\2\2C\u00f1\3\2\2\2E\u00f3")
        buf.write("\3\2\2\2G\u00f5\3\2\2\2I\u00f7\3\2\2\2K\u00f9\3\2\2\2")
        buf.write("M\u00fb\3\2\2\2O\u00fd\3\2\2\2Q\u00ff\3\2\2\2S\u0101\3")
        buf.write("\2\2\2U\u0103\3\2\2\2W\u010b\3\2\2\2Y\u013c\3\2\2\2[\u013e")
        buf.write("\3\2\2\2]\u0141\3\2\2\2_\u014d\3\2\2\2a\u0153\3\2\2\2")
        buf.write("c\u015e\3\2\2\2e\u016c\3\2\2\2g\u0178\3\2\2\2i\u0182\3")
        buf.write("\2\2\2kl\7c\2\2lm\7w\2\2mn\7v\2\2no\7q\2\2o\4\3\2\2\2")
        buf.write("pq\7d\2\2qr\7t\2\2rs\7g\2\2st\7c\2\2tu\7m\2\2u\6\3\2\2")
        buf.write("\2vw\7e\2\2wx\7c\2\2xy\7u\2\2yz\7g\2\2z\b\3\2\2\2{|\7")
        buf.write("e\2\2|}\7q\2\2}~\7p\2\2~\177\7v\2\2\177\u0080\7k\2\2\u0080")
        buf.write("\u0081\7p\2\2\u0081\u0082\7w\2\2\u0082\u0083\7g\2\2\u0083")
        buf.write("\n\3\2\2\2\u0084\u0085\7f\2\2\u0085\u0086\7g\2\2\u0086")
        buf.write("\u0087\7h\2\2\u0087\u0088\7c\2\2\u0088\u0089\7w\2\2\u0089")
        buf.write("\u008a\7n\2\2\u008a\u008b\7v\2\2\u008b\f\3\2\2\2\u008c")
        buf.write("\u008d\7g\2\2\u008d\u008e\7n\2\2\u008e\u008f\7u\2\2\u008f")
        buf.write("\u0090\7g\2\2\u0090\16\3\2\2\2\u0091\u0092\7h\2\2\u0092")
        buf.write("\u0093\7n\2\2\u0093\u0094\7q\2\2\u0094\u0095\7c\2\2\u0095")
        buf.write("\u0096\7v\2\2\u0096\20\3\2\2\2\u0097\u0098\7h\2\2\u0098")
        buf.write("\u0099\7q\2\2\u0099\u009a\7t\2\2\u009a\22\3\2\2\2\u009b")
        buf.write("\u009c\7k\2\2\u009c\u009d\7h\2\2\u009d\24\3\2\2\2\u009e")
        buf.write("\u009f\7k\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1")
        buf.write("\26\3\2\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7g\2\2\u00a4")
        buf.write("\u00a5\7v\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7t\2\2\u00a7")
        buf.write("\u00a8\7p\2\2\u00a8\30\3\2\2\2\u00a9\u00aa\7u\2\2\u00aa")
        buf.write("\u00ab\7v\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7k\2\2\u00ad")
        buf.write("\u00ae\7p\2\2\u00ae\u00af\7i\2\2\u00af\32\3\2\2\2\u00b0")
        buf.write("\u00b1\7u\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7t\2\2\u00b3")
        buf.write("\u00b4\7w\2\2\u00b4\u00b5\7e\2\2\u00b5\u00b6\7v\2\2\u00b6")
        buf.write("\34\3\2\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9\7y\2\2\u00b9")
        buf.write("\u00ba\7k\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7e\2\2\u00bc")
        buf.write("\u00bd\7j\2\2\u00bd\36\3\2\2\2\u00be\u00bf\7x\2\2\u00bf")
        buf.write("\u00c0\7q\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7f\2\2\u00c2")
        buf.write(" \3\2\2\2\u00c3\u00c4\7y\2\2\u00c4\u00c5\7j\2\2\u00c5")
        buf.write("\u00c6\7k\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\"\3\2\2\2\u00c9\u00ca\7-\2\2\u00ca$\3\2\2\2\u00cb\u00cc")
        buf.write("\7/\2\2\u00cc&\3\2\2\2\u00cd\u00ce\7,\2\2\u00ce(\3\2\2")
        buf.write("\2\u00cf\u00d0\7\61\2\2\u00d0*\3\2\2\2\u00d1\u00d2\7\'")
        buf.write("\2\2\u00d2,\3\2\2\2\u00d3\u00d4\7?\2\2\u00d4\u00d5\7?")
        buf.write("\2\2\u00d5.\3\2\2\2\u00d6\u00d7\7#\2\2\u00d7\u00d8\7?")
        buf.write("\2\2\u00d8\60\3\2\2\2\u00d9\u00da\7>\2\2\u00da\62\3\2")
        buf.write("\2\2\u00db\u00dc\7@\2\2\u00dc\64\3\2\2\2\u00dd\u00de\7")
        buf.write(">\2\2\u00de\u00df\7?\2\2\u00df\66\3\2\2\2\u00e0\u00e1")
        buf.write("\7@\2\2\u00e1\u00e2\7?\2\2\u00e28\3\2\2\2\u00e3\u00e4")
        buf.write("\7~\2\2\u00e4\u00e5\7~\2\2\u00e5:\3\2\2\2\u00e6\u00e7")
        buf.write("\7(\2\2\u00e7\u00e8\7(\2\2\u00e8<\3\2\2\2\u00e9\u00ea")
        buf.write("\7#\2\2\u00ea>\3\2\2\2\u00eb\u00ec\7-\2\2\u00ec\u00ed")
        buf.write("\7-\2\2\u00ed@\3\2\2\2\u00ee\u00ef\7/\2\2\u00ef\u00f0")
        buf.write("\7/\2\2\u00f0B\3\2\2\2\u00f1\u00f2\7?\2\2\u00f2D\3\2\2")
        buf.write("\2\u00f3\u00f4\7\60\2\2\u00f4F\3\2\2\2\u00f5\u00f6\7*")
        buf.write("\2\2\u00f6H\3\2\2\2\u00f7\u00f8\7+\2\2\u00f8J\3\2\2\2")
        buf.write("\u00f9\u00fa\7}\2\2\u00faL\3\2\2\2\u00fb\u00fc\7\177\2")
        buf.write("\2\u00fcN\3\2\2\2\u00fd\u00fe\7.\2\2\u00feP\3\2\2\2\u00ff")
        buf.write("\u0100\7=\2\2\u0100R\3\2\2\2\u0101\u0102\7<\2\2\u0102")
        buf.write("T\3\2\2\2\u0103\u0107\t\2\2\2\u0104\u0106\t\3\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0108\3\2\2\2\u0108V\3\2\2\2\u0109\u0107\3\2\2")
        buf.write("\2\u010a\u010c\t\4\2\2\u010b\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("X\3\2\2\2\u010f\u0111\t\4\2\2\u0110\u010f\3\2\2\2\u0111")
        buf.write("\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2")
        buf.write("\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0117\7")
        buf.write("\60\2\2\u0116\u0118\t\4\2\2\u0117\u0116\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2")
        buf.write("\u011a\u0125\3\2\2\2\u011b\u011e\t\5\2\2\u011c\u011f\5")
        buf.write("%\23\2\u011d\u011f\5#\22\2\u011e\u011c\3\2\2\2\u011e\u011d")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2\u0120")
        buf.write("\u0122\t\4\2\2\u0121\u0120\3\2\2\2\u0122\u0123\3\2\2\2")
        buf.write("\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\3")
        buf.write("\2\2\2\u0125\u011b\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u013d")
        buf.write("\3\2\2\2\u0127\u0129\t\4\2\2\u0128\u0127\3\2\2\2\u0129")
        buf.write("\u012a\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c\u013d\7\60\2\2\u012d\u012f")
        buf.write("\t\4\2\2\u012e\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u0135\t\5\2\2\u0133\u0136\5%\23\2\u0134\u0136\5")
        buf.write("#\22\2\u0135\u0133\3\2\2\2\u0135\u0134\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0139\t\4\2\2\u0138")
        buf.write("\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0138\3\2\2\2")
        buf.write("\u013a\u013b\3\2\2\2\u013b\u013d\3\2\2\2\u013c\u0112\3")
        buf.write("\2\2\2\u013c\u0128\3\2\2\2\u013c\u012e\3\2\2\2\u013dZ")
        buf.write("\3\2\2\2\u013e\u013f\7^\2\2\u013f\u0140\t\6\2\2\u0140")
        buf.write("\\\3\2\2\2\u0141\u0146\t\7\2\2\u0142\u0145\5[.\2\u0143")
        buf.write("\u0145\n\b\2\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2\2")
        buf.write("\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3")
        buf.write("\2\2\2\u0147\u0149\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a")
        buf.write("\t\7\2\2\u014a\u014b\b/\2\2\u014b^\3\2\2\2\u014c\u014e")
        buf.write("\t\t\2\2\u014d\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\u0152\b\60\3\2\u0152`\3\2\2\2\u0153\u0154\7\61")
        buf.write("\2\2\u0154\u0155\7\61\2\2\u0155\u0159\3\2\2\2\u0156\u0158")
        buf.write("\n\n\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015c\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015c\u015d\b\61\3\2\u015db\3\2\2")
        buf.write("\2\u015e\u015f\7\61\2\2\u015f\u0160\7,\2\2\u0160\u0164")
        buf.write("\3\2\2\2\u0161\u0163\13\2\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0165\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0165\u0167\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168\7")
        buf.write(",\2\2\u0168\u0169\7\61\2\2\u0169\u016a\3\2\2\2\u016a\u016b")
        buf.write("\b\62\3\2\u016bd\3\2\2\2\u016c\u0171\7$\2\2\u016d\u0170")
        buf.write("\5[.\2\u016e\u0170\n\b\2\2\u016f\u016d\3\2\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0174\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0174\u0175\7^\2\2\u0175\u0176\n\13\2\2\u0176\u0177\b")
        buf.write("\63\4\2\u0177f\3\2\2\2\u0178\u017d\t\7\2\2\u0179\u017c")
        buf.write("\5[.\2\u017a\u017c\n\b\2\2\u017b\u0179\3\2\2\2\u017b\u017a")
        buf.write("\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u0180\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u0180\u0181\b\64\5\2\u0181h\3\2\2\2\u0182\u0183\13\2")
        buf.write("\2\2\u0183j\3\2\2\2\30\2\u0107\u010d\u0112\u0119\u011e")
        buf.write("\u0123\u0125\u012a\u0130\u0135\u013a\u013c\u0144\u0146")
        buf.write("\u014f\u0159\u0164\u016f\u0171\u017b\u017d\6\3/\2\b\2")
        buf.write("\2\3\63\3\3\64\4")
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
     


