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
        buf.write("\u018d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\7,\u011e\n,\f,\16,\u0121\13,\3-\5-\u0124")
        buf.write("\n-\3-\6-\u0127\n-\r-\16-\u0128\3.\5.\u012c\n.\3.\7.\u012f")
        buf.write("\n.\f.\16.\u0132\13.\3.\3.\6.\u0136\n.\r.\16.\u0137\3")
        buf.write(".\3.\5.\u013c\n.\3.\6.\u013f\n.\r.\16.\u0140\5.\u0143")
        buf.write("\n.\3.\5.\u0146\n.\3.\6.\u0149\n.\r.\16.\u014a\3.\3.\5")
        buf.write(".\u014f\n.\3.\6.\u0152\n.\r.\16.\u0153\3.\3.\5.\u0158")
        buf.write("\n.\3.\6.\u015b\n.\r.\16.\u015c\5.\u015f\n.\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\7\60\u0167\n\60\f\60\16\60\u016a\13\60\3")
        buf.write("\60\3\60\3\60\3\61\6\61\u0170\n\61\r\61\16\61\u0171\3")
        buf.write("\61\3\61\3\62\3\62\3\62\7\62\u0179\n\62\f\62\16\62\u017c")
        buf.write("\13\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\7\63\u0185\n")
        buf.write("\63\f\63\16\63\u0188\13\63\3\63\3\63\3\64\3\64\2\2\65")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\2_\60a\61c\62e\63g\64\3\2\f\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\3\2//\3\2\62;\4\2GGgg\t\2$$^^ddhhpptt")
        buf.write("vv\3\2$$\6\2\f\f\17\17$$^^\5\2\13\f\16\17\"\"\13\2\f\f")
        buf.write("\17\17$$^^ddhhppttvv\2\u01a3\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5w\3\2\2\2\7\u0085\3\2")
        buf.write("\2\2\t\u008a\3\2\2\2\13\u0090\3\2\2\2\r\u0095\3\2\2\2")
        buf.write("\17\u009e\3\2\2\2\21\u00a6\3\2\2\2\23\u00ab\3\2\2\2\25")
        buf.write("\u00b1\3\2\2\2\27\u00b5\3\2\2\2\31\u00b8\3\2\2\2\33\u00bc")
        buf.write("\3\2\2\2\35\u00c3\3\2\2\2\37\u00ca\3\2\2\2!\u00d1\3\2")
        buf.write("\2\2#\u00d8\3\2\2\2%\u00dd\3\2\2\2\'\u00e3\3\2\2\2)\u00e5")
        buf.write("\3\2\2\2+\u00e7\3\2\2\2-\u00e9\3\2\2\2/\u00eb\3\2\2\2")
        buf.write("\61\u00ed\3\2\2\2\63\u00f0\3\2\2\2\65\u00f3\3\2\2\2\67")
        buf.write("\u00f5\3\2\2\29\u00f7\3\2\2\2;\u00fa\3\2\2\2=\u00fd\3")
        buf.write("\2\2\2?\u0100\3\2\2\2A\u0103\3\2\2\2C\u0105\3\2\2\2E\u0108")
        buf.write("\3\2\2\2G\u010b\3\2\2\2I\u010d\3\2\2\2K\u010f\3\2\2\2")
        buf.write("M\u0111\3\2\2\2O\u0113\3\2\2\2Q\u0115\3\2\2\2S\u0117\3")
        buf.write("\2\2\2U\u0119\3\2\2\2W\u011b\3\2\2\2Y\u0123\3\2\2\2[\u015e")
        buf.write("\3\2\2\2]\u0160\3\2\2\2_\u0163\3\2\2\2a\u016f\3\2\2\2")
        buf.write("c\u0175\3\2\2\2e\u0181\3\2\2\2g\u018b\3\2\2\2ij\7u\2\2")
        buf.write("jk\7v\2\2kl\7c\2\2lm\7v\2\2mn\7g\2\2no\7o\2\2op\7g\2\2")
        buf.write("pq\7p\2\2qr\7v\2\2rs\7n\2\2st\7k\2\2tu\7u\2\2uv\7v\2\2")
        buf.write("v\4\3\2\2\2wx\7u\2\2xy\7v\2\2yz\7t\2\2z{\7w\2\2{|\7e\2")
        buf.write("\2|}\7v\2\2}~\7x\2\2~\177\7c\2\2\177\u0080\7t\2\2\u0080")
        buf.write("\u0081\7f\2\2\u0081\u0082\7g\2\2\u0082\u0083\7e\2\2\u0083")
        buf.write("\u0084\7n\2\2\u0084\6\3\2\2\2\u0085\u0086\7c\2\2\u0086")
        buf.write("\u0087\7w\2\2\u0087\u0088\7v\2\2\u0088\u0089\7q\2\2\u0089")
        buf.write("\b\3\2\2\2\u008a\u008b\7d\2\2\u008b\u008c\7t\2\2\u008c")
        buf.write("\u008d\7g\2\2\u008d\u008e\7c\2\2\u008e\u008f\7m\2\2\u008f")
        buf.write("\n\3\2\2\2\u0090\u0091\7e\2\2\u0091\u0092\7c\2\2\u0092")
        buf.write("\u0093\7u\2\2\u0093\u0094\7g\2\2\u0094\f\3\2\2\2\u0095")
        buf.write("\u0096\7e\2\2\u0096\u0097\7q\2\2\u0097\u0098\7p\2\2\u0098")
        buf.write("\u0099\7v\2\2\u0099\u009a\7k\2\2\u009a\u009b\7p\2\2\u009b")
        buf.write("\u009c\7w\2\2\u009c\u009d\7g\2\2\u009d\16\3\2\2\2\u009e")
        buf.write("\u009f\7f\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7h\2\2\u00a1")
        buf.write("\u00a2\7c\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4\7n\2\2\u00a4")
        buf.write("\u00a5\7v\2\2\u00a5\20\3\2\2\2\u00a6\u00a7\7g\2\2\u00a7")
        buf.write("\u00a8\7n\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa\7g\2\2\u00aa")
        buf.write("\22\3\2\2\2\u00ab\u00ac\7h\2\2\u00ac\u00ad\7n\2\2\u00ad")
        buf.write("\u00ae\7q\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7v\2\2\u00b0")
        buf.write("\24\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3\7q\2\2\u00b3")
        buf.write("\u00b4\7t\2\2\u00b4\26\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6")
        buf.write("\u00b7\7h\2\2\u00b7\30\3\2\2\2\u00b8\u00b9\7k\2\2\u00b9")
        buf.write("\u00ba\7p\2\2\u00ba\u00bb\7v\2\2\u00bb\32\3\2\2\2\u00bc")
        buf.write("\u00bd\7t\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7v\2\2\u00bf")
        buf.write("\u00c0\7w\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7p\2\2\u00c2")
        buf.write("\34\3\2\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5\7v\2\2\u00c5")
        buf.write("\u00c6\7t\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8")
        buf.write("\u00c9\7i\2\2\u00c9\36\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb")
        buf.write("\u00cc\7v\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7w\2\2\u00ce")
        buf.write("\u00cf\7e\2\2\u00cf\u00d0\7v\2\2\u00d0 \3\2\2\2\u00d1")
        buf.write("\u00d2\7u\2\2\u00d2\u00d3\7y\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7v\2\2\u00d5\u00d6\7e\2\2\u00d6\u00d7\7j\2\2\u00d7")
        buf.write("\"\3\2\2\2\u00d8\u00d9\7x\2\2\u00d9\u00da\7q\2\2\u00da")
        buf.write("\u00db\7k\2\2\u00db\u00dc\7f\2\2\u00dc$\3\2\2\2\u00dd")
        buf.write("\u00de\7y\2\2\u00de\u00df\7j\2\2\u00df\u00e0\7k\2\2\u00e0")
        buf.write("\u00e1\7n\2\2\u00e1\u00e2\7g\2\2\u00e2&\3\2\2\2\u00e3")
        buf.write("\u00e4\7-\2\2\u00e4(\3\2\2\2\u00e5\u00e6\7/\2\2\u00e6")
        buf.write("*\3\2\2\2\u00e7\u00e8\7,\2\2\u00e8,\3\2\2\2\u00e9\u00ea")
        buf.write("\7\61\2\2\u00ea.\3\2\2\2\u00eb\u00ec\7\'\2\2\u00ec\60")
        buf.write("\3\2\2\2\u00ed\u00ee\7?\2\2\u00ee\u00ef\7?\2\2\u00ef\62")
        buf.write("\3\2\2\2\u00f0\u00f1\7#\2\2\u00f1\u00f2\7?\2\2\u00f2\64")
        buf.write("\3\2\2\2\u00f3\u00f4\7>\2\2\u00f4\66\3\2\2\2\u00f5\u00f6")
        buf.write("\7@\2\2\u00f68\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8\u00f9")
        buf.write("\7?\2\2\u00f9:\3\2\2\2\u00fa\u00fb\7@\2\2\u00fb\u00fc")
        buf.write("\7?\2\2\u00fc<\3\2\2\2\u00fd\u00fe\7~\2\2\u00fe\u00ff")
        buf.write("\7~\2\2\u00ff>\3\2\2\2\u0100\u0101\7(\2\2\u0101\u0102")
        buf.write("\7(\2\2\u0102@\3\2\2\2\u0103\u0104\7#\2\2\u0104B\3\2\2")
        buf.write("\2\u0105\u0106\7-\2\2\u0106\u0107\7-\2\2\u0107D\3\2\2")
        buf.write("\2\u0108\u0109\7/\2\2\u0109\u010a\7/\2\2\u010aF\3\2\2")
        buf.write("\2\u010b\u010c\7?\2\2\u010cH\3\2\2\2\u010d\u010e\7\60")
        buf.write("\2\2\u010eJ\3\2\2\2\u010f\u0110\7*\2\2\u0110L\3\2\2\2")
        buf.write("\u0111\u0112\7+\2\2\u0112N\3\2\2\2\u0113\u0114\7}\2\2")
        buf.write("\u0114P\3\2\2\2\u0115\u0116\7\177\2\2\u0116R\3\2\2\2\u0117")
        buf.write("\u0118\7.\2\2\u0118T\3\2\2\2\u0119\u011a\7=\2\2\u011a")
        buf.write("V\3\2\2\2\u011b\u011f\t\2\2\2\u011c\u011e\t\3\2\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120X\3\2\2\2\u0121\u011f\3\2\2")
        buf.write("\2\u0122\u0124\t\4\2\2\u0123\u0122\3\2\2\2\u0123\u0124")
        buf.write("\3\2\2\2\u0124\u0126\3\2\2\2\u0125\u0127\t\5\2\2\u0126")
        buf.write("\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0126\3\2\2\2")
        buf.write("\u0128\u0129\3\2\2\2\u0129Z\3\2\2\2\u012a\u012c\t\4\2")
        buf.write("\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u0130")
        buf.write("\3\2\2\2\u012d\u012f\t\5\2\2\u012e\u012d\3\2\2\2\u012f")
        buf.write("\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131\u0133\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0135\7")
        buf.write("\60\2\2\u0134\u0136\t\5\2\2\u0135\u0134\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u0142\3\2\2\2\u0139\u013b\t\6\2\2\u013a\u013c\t")
        buf.write("\4\2\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013e")
        buf.write("\3\2\2\2\u013d\u013f\t\5\2\2\u013e\u013d\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2")
        buf.write("\u0141\u0143\3\2\2\2\u0142\u0139\3\2\2\2\u0142\u0143\3")
        buf.write("\2\2\2\u0143\u015f\3\2\2\2\u0144\u0146\t\4\2\2\u0145\u0144")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147")
        buf.write("\u0149\t\5\2\2\u0148\u0147\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014c\u015f\7\60\2\2\u014d\u014f\t\4\2\2\u014e")
        buf.write("\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2")
        buf.write("\u0150\u0152\t\5\2\2\u0151\u0150\3\2\2\2\u0152\u0153\3")
        buf.write("\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0157\t\6\2\2\u0156\u0158\t\4\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u015a\3\2\2\2")
        buf.write("\u0159\u015b\t\5\2\2\u015a\u0159\3\2\2\2\u015b\u015c\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f")
        buf.write("\3\2\2\2\u015e\u012b\3\2\2\2\u015e\u0145\3\2\2\2\u015e")
        buf.write("\u014e\3\2\2\2\u015f\\\3\2\2\2\u0160\u0161\7^\2\2\u0161")
        buf.write("\u0162\t\7\2\2\u0162^\3\2\2\2\u0163\u0168\t\b\2\2\u0164")
        buf.write("\u0167\5]/\2\u0165\u0167\n\t\2\2\u0166\u0164\3\2\2\2\u0166")
        buf.write("\u0165\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0168\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u0168\3")
        buf.write("\2\2\2\u016b\u016c\t\b\2\2\u016c\u016d\b\60\2\2\u016d")
        buf.write("`\3\2\2\2\u016e\u0170\t\n\2\2\u016f\u016e\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173\u0174\b\61\3\2\u0174b\3\2\2")
        buf.write("\2\u0175\u017a\7$\2\2\u0176\u0179\5]/\2\u0177\u0179\n")
        buf.write("\t\2\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179\u017c")
        buf.write("\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u017d\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017e\7^\2\2")
        buf.write("\u017e\u017f\n\13\2\2\u017f\u0180\b\62\4\2\u0180d\3\2")
        buf.write("\2\2\u0181\u0186\t\b\2\2\u0182\u0185\5]/\2\u0183\u0185")
        buf.write("\n\t\2\2\u0184\u0182\3\2\2\2\u0184\u0183\3\2\2\2\u0185")
        buf.write("\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0189\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\b")
        buf.write("\63\5\2\u018af\3\2\2\2\u018b\u018c\13\2\2\2\u018ch\3\2")
        buf.write("\2\2\32\2\u011f\u0123\u0128\u012b\u0130\u0137\u013b\u0140")
        buf.write("\u0142\u0145\u014a\u014e\u0153\u0157\u015c\u015e\u0166")
        buf.write("\u0168\u0171\u0178\u017a\u0184\u0186\6\3\60\2\b\2\2\3")
        buf.write("\62\3\3\63\4")
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
            "'statementlist'", "'structvardecl'", "'auto'", "'break'", "'case'", 
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
     


