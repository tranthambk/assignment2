# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0192\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\6\2o\n\2\r\2\16\2p\3\3\3")
        buf.write("\3\3\4\6\4v\n\4\r\4\16\4w\3\4\3\4\7\4|\n\4\f\4\16\4\177")
        buf.write("\13\4\3\4\5\4\u0082\n\4\3\4\7\4\u0085\n\4\f\4\16\4\u0088")
        buf.write("\13\4\3\4\3\4\6\4\u008c\n\4\r\4\16\4\u008d\3\4\5\4\u0091")
        buf.write("\n\4\3\4\6\4\u0094\n\4\r\4\16\4\u0095\3\4\5\4\u0099\n")
        buf.write("\4\5\4\u009b\n\4\3\5\3\5\5\5\u009f\n\5\3\5\6\5\u00a2\n")
        buf.write("\5\r\5\16\5\u00a3\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00af\n\6\3\7\3\7\3\7\3\7\7\7\u00b5\n\7\f\7\16\7")
        buf.write("\u00b8\13\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\7\23\u00f9\n\23\f\23\16")
        buf.write("\23\u00fc\13\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\7\24\u0107\n\24\f\24\16\24\u010a\13\24\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\6")
        buf.write("-\u0145\n-\r-\16-\u0146\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/")
        buf.write("\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\5\63\u016b\n\63\3\63\3\63\3\63\7\63\u0170\n")
        buf.write("\63\f\63\16\63\u0173\13\63\3\64\3\64\3\64\3\64\7\64\u0179")
        buf.write("\n\64\f\64\16\64\u017c\13\64\3\64\3\64\3\64\5\64\u0181")
        buf.write("\n\64\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u0189\n\65\f")
        buf.write("\65\16\65\u018c\13\65\3\65\3\65\3\66\3\66\3\66\3\u00fa")
        buf.write("\2\67\3\3\5\2\7\4\t\2\13\5\r\6\17\2\21\7\23\b\25\t\27")
        buf.write("\n\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25")
        buf.write("/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C E!G")
        buf.write("\"I#K$M%O&Q\'S(U)W\2Y*[+],_-a.c/e\60g\61i\62k\63\3\2\n")
        buf.write("\3\2\62;\4\2C\\c|\4\2GGgg\t\2$$^^ddhhppttvv\6\2\n\f\16")
        buf.write("\17$$^^\4\2\f\f\17\17\5\2\13\f\16\17\"\"\6\2\n\13\16\16")
        buf.write("$$^^\2\u01a9\2\3\3\2\2\2\2\7\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\3n\3\2")
        buf.write("\2\2\5r\3\2\2\2\7\u009a\3\2\2\2\t\u009c\3\2\2\2\13\u00ae")
        buf.write("\3\2\2\2\r\u00b0\3\2\2\2\17\u00bc\3\2\2\2\21\u00be\3\2")
        buf.write("\2\2\23\u00c1\3\2\2\2\25\u00c6\3\2\2\2\27\u00cf\3\2\2")
        buf.write("\2\31\u00d3\3\2\2\2\33\u00d9\3\2\2\2\35\u00dc\3\2\2\2")
        buf.write("\37\u00e2\3\2\2\2!\u00e9\3\2\2\2#\u00ee\3\2\2\2%\u00f4")
        buf.write("\3\2\2\2\'\u0102\3\2\2\2)\u010d\3\2\2\2+\u010f\3\2\2\2")
        buf.write("-\u0111\3\2\2\2/\u0113\3\2\2\2\61\u0115\3\2\2\2\63\u0117")
        buf.write("\3\2\2\2\65\u0119\3\2\2\2\67\u011b\3\2\2\29\u011d\3\2")
        buf.write("\2\2;\u011f\3\2\2\2=\u0121\3\2\2\2?\u0123\3\2\2\2A\u0125")
        buf.write("\3\2\2\2C\u0127\3\2\2\2E\u012a\3\2\2\2G\u012d\3\2\2\2")
        buf.write("I\u012f\3\2\2\2K\u0132\3\2\2\2M\u0134\3\2\2\2O\u0136\3")
        buf.write("\2\2\2Q\u0139\3\2\2\2S\u013c\3\2\2\2U\u013e\3\2\2\2W\u0141")
        buf.write("\3\2\2\2Y\u0144\3\2\2\2[\u014a\3\2\2\2]\u014e\3\2\2\2")
        buf.write("_\u0153\3\2\2\2a\u015b\3\2\2\2c\u0161\3\2\2\2e\u016a\3")
        buf.write("\2\2\2g\u0174\3\2\2\2i\u0184\3\2\2\2k\u018f\3\2\2\2mo")
        buf.write("\t\2\2\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\4\3")
        buf.write("\2\2\2rs\t\3\2\2s\6\3\2\2\2tv\5\17\b\2ut\3\2\2\2vw\3\2")
        buf.write("\2\2wu\3\2\2\2wx\3\2\2\2xy\3\2\2\2y}\7\60\2\2z|\5\17\b")
        buf.write("\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0081\3")
        buf.write("\2\2\2\177}\3\2\2\2\u0080\u0082\5\t\5\2\u0081\u0080\3")
        buf.write("\2\2\2\u0081\u0082\3\2\2\2\u0082\u009b\3\2\2\2\u0083\u0085")
        buf.write("\5\17\b\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0089\u008b\7\60\2\2\u008a\u008c")
        buf.write("\5\17\b\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0090\3\2\2\2")
        buf.write("\u008f\u0091\5\t\5\2\u0090\u008f\3\2\2\2\u0090\u0091\3")
        buf.write("\2\2\2\u0091\u009b\3\2\2\2\u0092\u0094\5\17\b\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0099\5")
        buf.write("\t\5\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009b")
        buf.write("\3\2\2\2\u009au\3\2\2\2\u009a\u0086\3\2\2\2\u009a\u0093")
        buf.write("\3\2\2\2\u009b\b\3\2\2\2\u009c\u009e\t\4\2\2\u009d\u009f")
        buf.write("\7/\2\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00a1\3\2\2\2\u00a0\u00a2\5\17\b\2\u00a1\u00a0\3\2\2")
        buf.write("\2\u00a2\u00a3\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\n\3\2\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\u00a8\7w\2\2\u00a8\u00af\7g\2\2\u00a9\u00aa")
        buf.write("\7h\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7n\2\2\u00ac\u00ad")
        buf.write("\7u\2\2\u00ad\u00af\7g\2\2\u00ae\u00a5\3\2\2\2\u00ae\u00a9")
        buf.write("\3\2\2\2\u00af\f\3\2\2\2\u00b0\u00b6\7$\2\2\u00b1\u00b2")
        buf.write("\7^\2\2\u00b2\u00b5\t\5\2\2\u00b3\u00b5\n\6\2\2\u00b4")
        buf.write("\u00b1\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3")
        buf.write("\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00ba\7$\2\2\u00ba\u00bb")
        buf.write("\b\7\2\2\u00bb\16\3\2\2\2\u00bc\u00bd\t\2\2\2\u00bd\20")
        buf.write("\3\2\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7h\2\2\u00c0\22")
        buf.write("\3\2\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4")
        buf.write("\7u\2\2\u00c4\u00c5\7g\2\2\u00c5\24\3\2\2\2\u00c6\u00c7")
        buf.write("\7e\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7w\2\2\u00cd\u00ce\7g\2\2\u00ce\26\3\2\2\2\u00cf\u00d0")
        buf.write("\7h\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7t\2\2\u00d2\30")
        buf.write("\3\2\2\2\u00d3\u00d4\7y\2\2\u00d4\u00d5\7j\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7g\2\2\u00d8\32")
        buf.write("\3\2\2\2\u00d9\u00da\7f\2\2\u00da\u00db\7q\2\2\u00db\34")
        buf.write("\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de\7t\2\2\u00de\u00df")
        buf.write("\7g\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7m\2\2\u00e1\36")
        buf.write("\3\2\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8 \3\2\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7g\2\2\u00ed\"")
        buf.write("\3\2\2\2\u00ee\u00ef\7h\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7g\2\2\u00f3$\3")
        buf.write("\2\2\2\u00f4\u00f5\7\61\2\2\u00f5\u00f6\7,\2\2\u00f6\u00fa")
        buf.write("\3\2\2\2\u00f7\u00f9\13\2\2\2\u00f8\u00f7\3\2\2\2\u00f9")
        buf.write("\u00fc\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2")
        buf.write("\u00fb\u00fd\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\7")
        buf.write(",\2\2\u00fe\u00ff\7\61\2\2\u00ff\u0100\3\2\2\2\u0100\u0101")
        buf.write("\b\23\3\2\u0101&\3\2\2\2\u0102\u0103\7\61\2\2\u0103\u0104")
        buf.write("\7\61\2\2\u0104\u0108\3\2\2\2\u0105\u0107\n\7\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0108\3")
        buf.write("\2\2\2\u010b\u010c\b\24\3\2\u010c(\3\2\2\2\u010d\u010e")
        buf.write("\7*\2\2\u010e*\3\2\2\2\u010f\u0110\7+\2\2\u0110,\3\2\2")
        buf.write("\2\u0111\u0112\7}\2\2\u0112.\3\2\2\2\u0113\u0114\7\177")
        buf.write("\2\2\u0114\60\3\2\2\2\u0115\u0116\7]\2\2\u0116\62\3\2")
        buf.write("\2\2\u0117\u0118\7_\2\2\u0118\64\3\2\2\2\u0119\u011a\7")
        buf.write(".\2\2\u011a\66\3\2\2\2\u011b\u011c\7=\2\2\u011c8\3\2\2")
        buf.write("\2\u011d\u011e\7-\2\2\u011e:\3\2\2\2\u011f\u0120\7/\2")
        buf.write("\2\u0120<\3\2\2\2\u0121\u0122\7\61\2\2\u0122>\3\2\2\2")
        buf.write("\u0123\u0124\7,\2\2\u0124@\3\2\2\2\u0125\u0126\7#\2\2")
        buf.write("\u0126B\3\2\2\2\u0127\u0128\7#\2\2\u0128\u0129\7?\2\2")
        buf.write("\u0129D\3\2\2\2\u012a\u012b\7~\2\2\u012b\u012c\7~\2\2")
        buf.write("\u012cF\3\2\2\2\u012d\u012e\7>\2\2\u012eH\3\2\2\2\u012f")
        buf.write("\u0130\7>\2\2\u0130\u0131\7?\2\2\u0131J\3\2\2\2\u0132")
        buf.write("\u0133\7?\2\2\u0133L\3\2\2\2\u0134\u0135\7\'\2\2\u0135")
        buf.write("N\3\2\2\2\u0136\u0137\7(\2\2\u0137\u0138\7(\2\2\u0138")
        buf.write("P\3\2\2\2\u0139\u013a\7?\2\2\u013a\u013b\7?\2\2\u013b")
        buf.write("R\3\2\2\2\u013c\u013d\7@\2\2\u013dT\3\2\2\2\u013e\u013f")
        buf.write("\7@\2\2\u013f\u0140\7?\2\2\u0140V\3\2\2\2\u0141\u0142")
        buf.write("\7a\2\2\u0142X\3\2\2\2\u0143\u0145\t\b\2\2\u0144\u0143")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\b-\3\2")
        buf.write("\u0149Z\3\2\2\2\u014a\u014b\7k\2\2\u014b\u014c\7p\2\2")
        buf.write("\u014c\u014d\7v\2\2\u014d\\\3\2\2\2\u014e\u014f\7x\2\2")
        buf.write("\u014f\u0150\7q\2\2\u0150\u0151\7k\2\2\u0151\u0152\7f")
        buf.write("\2\2\u0152^\3\2\2\2\u0153\u0154\7d\2\2\u0154\u0155\7q")
        buf.write("\2\2\u0155\u0156\7q\2\2\u0156\u0157\7n\2\2\u0157\u0158")
        buf.write("\7g\2\2\u0158\u0159\7c\2\2\u0159\u015a\7p\2\2\u015a`\3")
        buf.write("\2\2\2\u015b\u015c\7h\2\2\u015c\u015d\7n\2\2\u015d\u015e")
        buf.write("\7q\2\2\u015e\u015f\7c\2\2\u015f\u0160\7v\2\2\u0160b\3")
        buf.write("\2\2\2\u0161\u0162\7u\2\2\u0162\u0163\7v\2\2\u0163\u0164")
        buf.write("\7t\2\2\u0164\u0165\7k\2\2\u0165\u0166\7p\2\2\u0166\u0167")
        buf.write("\7i\2\2\u0167d\3\2\2\2\u0168\u016b\5\5\3\2\u0169\u016b")
        buf.write("\5W,\2\u016a\u0168\3\2\2\2\u016a\u0169\3\2\2\2\u016b\u0171")
        buf.write("\3\2\2\2\u016c\u0170\5\5\3\2\u016d\u0170\5W,\2\u016e\u0170")
        buf.write("\5\17\b\2\u016f\u016c\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2")
        buf.write("\u0171\u0172\3\2\2\2\u0172f\3\2\2\2\u0173\u0171\3\2\2")
        buf.write("\2\u0174\u017a\7$\2\2\u0175\u0176\7^\2\2\u0176\u0179\t")
        buf.write("\5\2\2\u0177\u0179\n\6\2\2\u0178\u0175\3\2\2\2\u0178\u0177")
        buf.write("\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u0180\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017d\u017e\7^\2\2\u017e\u0181\n\5\2\2\u017f\u0181\t")
        buf.write("\t\2\2\u0180\u017d\3\2\2\2\u0180\u017f\3\2\2\2\u0181\u0182")
        buf.write("\3\2\2\2\u0182\u0183\b\64\4\2\u0183h\3\2\2\2\u0184\u018a")
        buf.write("\7$\2\2\u0185\u0186\7^\2\2\u0186\u0189\t\5\2\2\u0187\u0189")
        buf.write("\n\6\2\2\u0188\u0185\3\2\2\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u018d\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018e\b")
        buf.write("\65\5\2\u018ej\3\2\2\2\u018f\u0190\13\2\2\2\u0190\u0191")
        buf.write("\b\66\6\2\u0191l\3\2\2\2\35\2pw}\u0081\u0086\u008d\u0090")
        buf.write("\u0095\u0098\u009a\u009e\u00a3\u00ae\u00b4\u00b6\u00fa")
        buf.write("\u0108\u0146\u016a\u016f\u0171\u0178\u017a\u0180\u0188")
        buf.write("\u018a\7\3\7\2\b\2\2\3\64\3\3\65\4\3\66\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    Realit = 2
    Booleanlit = 3
    Stringlit = 4
    IF = 5
    ELSE = 6
    CONTINUE = 7
    FOR = 8
    WHILE = 9
    DO = 10
    BREAK = 11
    RETURN = 12
    TRUE = 13
    FALSE = 14
    BLOCK_COMMENT = 15
    LINE_COMMENT = 16
    LB = 17
    RB = 18
    LP = 19
    RP = 20
    LQB = 21
    RQB = 22
    CM = 23
    SEMI = 24
    ADD = 25
    SUB = 26
    DIV = 27
    MUL = 28
    NOT = 29
    NOTEQUAL = 30
    OR = 31
    LESS = 32
    LESSEQUAL = 33
    ASSIGN = 34
    MODUL = 35
    AND = 36
    EQUAL = 37
    GREATER = 38
    GREATEREQUAL = 39
    WS = 40
    INTTYPE = 41
    VOIDTYPE = 42
    BOOLEANTYPE = 43
    FLOATTYPE = 44
    STRINGTYPE = 45
    ID = 46
    ILLEGAL_ESCAPE = 47
    UNCLOSE_STRING = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'continue'", "'for'", "'while'", "'do'", 
            "'break'", "'return'", "'true'", "'false'", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "','", "';'", "'+'", "'-'", "'/'", "'*'", 
            "'!'", "'!='", "'||'", "'<'", "'<='", "'='", "'%'", "'&&'", 
            "'=='", "'>'", "'>='", "'int'", "'void'", "'boolean'", "'float'", 
            "'string'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "Realit", "Booleanlit", "Stringlit", "IF", "ELSE", 
            "CONTINUE", "FOR", "WHILE", "DO", "BREAK", "RETURN", "TRUE", 
            "FALSE", "BLOCK_COMMENT", "LINE_COMMENT", "LB", "RB", "LP", 
            "RP", "LQB", "RQB", "CM", "SEMI", "ADD", "SUB", "DIV", "MUL", 
            "NOT", "NOTEQUAL", "OR", "LESS", "LESSEQUAL", "ASSIGN", "MODUL", 
            "AND", "EQUAL", "GREATER", "GREATEREQUAL", "WS", "INTTYPE", 
            "VOIDTYPE", "BOOLEANTYPE", "FLOATTYPE", "STRINGTYPE", "ID", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "INTLIT", "Letter", "Realit", "Exponent", "Booleanlit", 
                  "Stringlit", "Digit", "IF", "ELSE", "CONTINUE", "FOR", 
                  "WHILE", "DO", "BREAK", "RETURN", "TRUE", "FALSE", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "LB", "RB", "LP", "RP", "LQB", "RQB", 
                  "CM", "SEMI", "ADD", "SUB", "DIV", "MUL", "NOT", "NOTEQUAL", 
                  "OR", "LESS", "LESSEQUAL", "ASSIGN", "MODUL", "AND", "EQUAL", 
                  "GREATER", "GREATEREQUAL", "UNDERSCORE", "WS", "INTTYPE", 
                  "VOIDTYPE", "BOOLEANTYPE", "FLOATTYPE", "STRINGTYPE", 
                  "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.Stringlit_action 
            actions[50] = self.ILLEGAL_ESCAPE_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[52] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def Stringlit_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


