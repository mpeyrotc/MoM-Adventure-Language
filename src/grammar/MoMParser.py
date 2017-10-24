# Generated from src/grammar/MoM.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u01ea\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\6\2l\n\2\r\2\16\2m\3\2\3\2\3\3\3\3\3\3\7")
        buf.write("\3u\n\3\f\3\16\3x\13\3\3\4\3\4\5\4|\n\4\3\4\3\4\5\4\u0080")
        buf.write("\n\4\3\4\3\4\3\4\5\4\u0085\n\4\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u0090\n\6\3\6\3\6\7\6\u0094\n\6\f\6\16")
        buf.write("\6\u0097\13\6\3\6\3\6\7\6\u009b\n\6\f\6\16\6\u009e\13")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\7\n\u00b0\n\n\f\n\16\n\u00b3\13\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\7\n\u00ba\n\n\f\n\16\n\u00bd\13\n\3\n\3\n")
        buf.write("\5\n\u00c1\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00cd\n\13\3\f\3\f\3\f\3\f\5\f\u00d3\n\f")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\16\5\16\u00dc\n\16\3\16\3")
        buf.write("\16\3\16\7\16\u00e1\n\16\f\16\16\16\u00e4\13\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\7\17\u00ed\n\17\f\17\16\17")
        buf.write("\u00f0\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u0107\n\24\3\24\3\24\3\24\7\24\u010c\n")
        buf.write("\24\f\24\16\24\u010f\13\24\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u0118\n\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0127\n\32\3")
        buf.write("\32\3\32\3\32\7\32\u012c\n\32\f\32\16\32\u012f\13\32\3")
        buf.write("\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u013c\n\35\3\35\5\35\u013f\n\35\3\36\3\36\5\36\u0143")
        buf.write("\n\36\3\36\3\36\3\36\3\36\5\36\u0149\n\36\3\36\3\36\7")
        buf.write("\36\u014d\n\36\f\36\16\36\u0150\13\36\3\37\3\37\5\37\u0154")
        buf.write("\n\37\3\37\3\37\3\37\5\37\u0159\n\37\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3!\3!\5!\u0163\n!\3!\3!\3!\7!\u0168\n!\f!\16!\u016b")
        buf.write("\13!\3!\3!\3!\3!\5!\u0171\n!\3!\3!\3!\3!\3\"\3\"\3#\3")
        buf.write("#\3#\3#\5#\u017d\n#\3#\3#\3#\3#\3$\3$\3$\3$\5$\u0187\n")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\7%\u0190\n%\f%\16%\u0193\13%\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\3&\5&\u019d\n&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u01a4\n\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3+\3+\3+\5+")
        buf.write("\u01b2\n+\3+\3+\3+\7+\u01b7\n+\f+\16+\u01ba\13+\3,\3,")
        buf.write("\5,\u01be\n,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\7\61\u01d0\n\61\f\61\16\61\u01d3")
        buf.write("\13\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3")
        buf.write("\63\5\63\u01df\n\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\2\2\65\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2")
        buf.write("\b\4\2\33\33\65\65\4\2\r\16\22\22\3\2\24\30\5\2\37!%%")
        buf.write(",,\5\2\36\36\"$\64\64\4\2\33\33\64\64\2\u01eb\2k\3\2\2")
        buf.write("\2\4q\3\2\2\2\6{\3\2\2\2\b\u0086\3\2\2\2\n\u0089\3\2\2")
        buf.write("\2\f\u00a2\3\2\2\2\16\u00a4\3\2\2\2\20\u00a6\3\2\2\2\22")
        buf.write("\u00a8\3\2\2\2\24\u00cc\3\2\2\2\26\u00ce\3\2\2\2\30\u00d6")
        buf.write("\3\2\2\2\32\u00d8\3\2\2\2\34\u00e9\3\2\2\2\36\u00f3\3")
        buf.write("\2\2\2 \u00fa\3\2\2\2\"\u00fc\3\2\2\2$\u00fe\3\2\2\2&")
        buf.write("\u0100\3\2\2\2(\u0110\3\2\2\2*\u0112\3\2\2\2,\u0119\3")
        buf.write("\2\2\2.\u011b\3\2\2\2\60\u011d\3\2\2\2\62\u011f\3\2\2")
        buf.write("\2\64\u0130\3\2\2\2\66\u0132\3\2\2\28\u013e\3\2\2\2:\u0142")
        buf.write("\3\2\2\2<\u0153\3\2\2\2>\u015c\3\2\2\2@\u015e\3\2\2\2")
        buf.write("B\u0176\3\2\2\2D\u0178\3\2\2\2F\u0182\3\2\2\2H\u018b\3")
        buf.write("\2\2\2J\u0197\3\2\2\2L\u01a3\3\2\2\2N\u01a5\3\2\2\2P\u01a7")
        buf.write("\3\2\2\2R\u01a9\3\2\2\2T\u01ab\3\2\2\2V\u01bd\3\2\2\2")
        buf.write("X\u01bf\3\2\2\2Z\u01c1\3\2\2\2\\\u01c3\3\2\2\2^\u01c5")
        buf.write("\3\2\2\2`\u01c7\3\2\2\2b\u01d7\3\2\2\2d\u01de\3\2\2\2")
        buf.write("f\u01e5\3\2\2\2hl\5\n\6\2il\5\36\20\2jl\5H%\2kh\3\2\2")
        buf.write("\2ki\3\2\2\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2n")
        buf.write("o\3\2\2\2op\7\2\2\3p\3\3\2\2\2qv\5&\24\2rs\7\4\2\2su\5")
        buf.write("&\24\2tr\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\5\3\2")
        buf.write("\2\2xv\3\2\2\2yz\t\2\2\2z|\7\21\2\2{y\3\2\2\2{|\3\2\2")
        buf.write("\2|\177\3\2\2\2}\u0080\7\65\2\2~\u0080\5d\63\2\177}\3")
        buf.write("\2\2\2\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0084\7")
        buf.write("\17\2\2\u0082\u0085\5\26\f\2\u0083\u0085\5&\24\2\u0084")
        buf.write("\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\7\3\2\2\2\u0086")
        buf.write("\u0087\5L\'\2\u0087\u0088\7\n\2\2\u0088\t\3\2\2\2\u0089")
        buf.write("\u008a\7&\2\2\u008a\u008b\7\64\2\2\u008b\u008c\7/\2\2")
        buf.write("\u008c\u008f\5Z.\2\u008d\u008e\7.\2\2\u008e\u0090\7\64")
        buf.write("\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0095\7\6\2\2\u0092\u0094\5D#\2\u0093\u0092")
        buf.write("\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095")
        buf.write("\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0098\u009c\5\32\16\2\u0099\u009b\5@!\2\u009a\u0099\3")
        buf.write("\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009f")
        buf.write("\u00a0\7\7\2\2\u00a0\u00a1\7\n\2\2\u00a1\13\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\r\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\17\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\21\3\2\2\2\u00a8")
        buf.write("\u00a9\7\34\2\2\u00a9\u00aa\7\3\2\2\u00aa\u00ab\5&\24")
        buf.write("\2\u00ab\u00ac\7\5\2\2\u00ac\u00ad\5\f\7\2\u00ad\u00b1")
        buf.write("\7\6\2\2\u00ae\u00b0\5\b\5\2\u00af\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\u00b4\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00c0\7")
        buf.write("\7\2\2\u00b5\u00b6\7\35\2\2\u00b6\u00b7\5\20\t\2\u00b7")
        buf.write("\u00bb\7\6\2\2\u00b8\u00ba\5\b\5\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3")
        buf.write("\2\2\2\u00bc\u00be\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf")
        buf.write("\7\7\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00b5\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\5\16\b")
        buf.write("\2\u00c3\23\3\2\2\2\u00c4\u00cd\7\66\2\2\u00c5\u00cd\7")
        buf.write("\67\2\2\u00c6\u00cd\79\2\2\u00c7\u00cd\7\65\2\2\u00c8")
        buf.write("\u00cd\5d\63\2\u00c9\u00cd\7\61\2\2\u00ca\u00cd\7\62\2")
        buf.write("\2\u00cb\u00cd\5<\37\2\u00cc\u00c4\3\2\2\2\u00cc\u00c5")
        buf.write("\3\2\2\2\u00cc\u00c6\3\2\2\2\u00cc\u00c7\3\2\2\2\u00cc")
        buf.write("\u00c8\3\2\2\2\u00cc\u00c9\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cb\3\2\2\2\u00cd\25\3\2\2\2\u00ce\u00cf\7\'")
        buf.write("\2\2\u00cf\u00d0\7\64\2\2\u00d0\u00d2\7\3\2\2\u00d1\u00d3")
        buf.write("\5\4\3\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d5\7\5\2\2\u00d5\27\3\2\2\2\u00d6")
        buf.write("\u00d7\3\2\2\2\u00d7\31\3\2\2\2\u00d8\u00d9\7\64\2\2\u00d9")
        buf.write("\u00db\7\3\2\2\u00da\u00dc\5:\36\2\u00db\u00da\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\7")
        buf.write("\5\2\2\u00de\u00e2\7\6\2\2\u00df\u00e1\5\b\5\2\u00e0\u00df")
        buf.write("\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e5\u00e6\7\7\2\2\u00e6\u00e7\5\30\r\2\u00e7\u00e8")
        buf.write("\7\n\2\2\u00e8\33\3\2\2\2\u00e9\u00ee\7\63\2\2\u00ea\u00eb")
        buf.write("\7\4\2\2\u00eb\u00ed\7\63\2\2\u00ec\u00ea\3\2\2\2\u00ed")
        buf.write("\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2")
        buf.write("\u00ef\u00f1\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\7")
        buf.write("\n\2\2\u00f2\35\3\2\2\2\u00f3\u00f4\7(\2\2\u00f4\u00f5")
        buf.write("\7\64\2\2\u00f5\u00f6\7\6\2\2\u00f6\u00f7\5\34\17\2\u00f7")
        buf.write("\u00f8\7\7\2\2\u00f8\u00f9\7\n\2\2\u00f9\37\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb!\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("#\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff%\3\2\2\2\u0100\u0101")
        buf.write("\5*\26\2\u0101\u010d\5 \21\2\u0102\u0103\7\31\2\2\u0103")
        buf.write("\u0107\5\"\22\2\u0104\u0105\7\32\2\2\u0105\u0107\5$\23")
        buf.write("\2\u0106\u0102\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u0109\5*\26\2\u0109\u010a\5 \21\2\u010a")
        buf.write("\u010c\3\2\2\2\u010b\u0106\3\2\2\2\u010c\u010f\3\2\2\2")
        buf.write("\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\'\3\2\2")
        buf.write("\2\u010f\u010d\3\2\2\2\u0110\u0111\3\2\2\2\u0111)\3\2")
        buf.write("\2\2\u0112\u0117\5\62\32\2\u0113\u0114\5B\"\2\u0114\u0115")
        buf.write("\5\62\32\2\u0115\u0116\5(\25\2\u0116\u0118\3\2\2\2\u0117")
        buf.write("\u0113\3\2\2\2\u0117\u0118\3\2\2\2\u0118+\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a-\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("/\3\2\2\2\u011d\u011e\3\2\2\2\u011e\61\3\2\2\2\u011f\u0120")
        buf.write("\5T+\2\u0120\u012d\5,\27\2\u0121\u0122\7\r\2\2\u0122\u0127")
        buf.write("\5.\30\2\u0123\u0124\7\16\2\2\u0124\u0127\5\60\31\2\u0125")
        buf.write("\u0127\5\22\n\2\u0126\u0121\3\2\2\2\u0126\u0123\3\2\2")
        buf.write("\2\u0126\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129")
        buf.write("\5T+\2\u0129\u012a\5,\27\2\u012a\u012c\3\2\2\2\u012b\u0126")
        buf.write("\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\63\3\2\2\2\u012f\u012d\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\65\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\67\3\2\2\2\u0134\u0135\7\3\2\2\u0135\u0136\5\64\33\2")
        buf.write("\u0136\u0137\5&\24\2\u0137\u0138\5\66\34\2\u0138\u0139")
        buf.write("\7\5\2\2\u0139\u013f\3\2\2\2\u013a\u013c\t\3\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013f\5\24\13\2\u013e\u0134\3\2\2\2\u013e\u013b")
        buf.write("\3\2\2\2\u013f9\3\2\2\2\u0140\u0143\5V,\2\u0141\u0143")
        buf.write("\5f\64\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u014e\7\65\2\2\u0145\u0148\7\4\2")
        buf.write("\2\u0146\u0149\5V,\2\u0147\u0149\5f\64\2\u0148\u0146\3")
        buf.write("\2\2\2\u0148\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b")
        buf.write("\7\65\2\2\u014b\u014d\3\2\2\2\u014c\u0145\3\2\2\2\u014d")
        buf.write("\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write("\u014f;\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0152\t\2\2")
        buf.write("\2\u0152\u0154\7\21\2\2\u0153\u0151\3\2\2\2\u0153\u0154")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\7\65\2\2\u0156")
        buf.write("\u0158\7\3\2\2\u0157\u0159\5\4\3\2\u0158\u0157\3\2\2\2")
        buf.write("\u0158\u0159\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\7")
        buf.write("\5\2\2\u015b=\3\2\2\2\u015c\u015d\3\2\2\2\u015d?\3\2\2")
        buf.write("\2\u015e\u015f\5X-\2\u015f\u0160\7\65\2\2\u0160\u0162")
        buf.write("\7\3\2\2\u0161\u0163\5:\36\2\u0162\u0161\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\7\5\2\2")
        buf.write("\u0165\u0169\7\6\2\2\u0166\u0168\5\b\5\2\u0167\u0166\3")
        buf.write("\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u0170\3\2\2\2\u016b\u0169\3\2\2\2\u016c")
        buf.write("\u016d\7+\2\2\u016d\u016e\5&\24\2\u016e\u016f\7\n\2\2")
        buf.write("\u016f\u0171\3\2\2\2\u0170\u016c\3\2\2\2\u0170\u0171\3")
        buf.write("\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\7\7\2\2\u0173\u0174")
        buf.write("\5> \2\u0174\u0175\7\n\2\2\u0175A\3\2\2\2\u0176\u0177")
        buf.write("\t\4\2\2\u0177C\3\2\2\2\u0178\u0179\7)\2\2\u0179\u017c")
        buf.write("\7\24\2\2\u017a\u017d\5V,\2\u017b\u017d\5b\62\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017f\7\26\2\2\u017f\u0180\7\65\2\2\u0180\u0181")
        buf.write("\7\n\2\2\u0181E\3\2\2\2\u0182\u0183\5X-\2\u0183\u0184")
        buf.write("\7\65\2\2\u0184\u0186\7\3\2\2\u0185\u0187\5:\36\2\u0186")
        buf.write("\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u0189\7\5\2\2\u0189\u018a\7\n\2\2\u018aG\3\2\2")
        buf.write("\2\u018b\u018c\7*\2\2\u018c\u018d\7\64\2\2\u018d\u0191")
        buf.write("\7\6\2\2\u018e\u0190\5F$\2\u018f\u018e\3\2\2\2\u0190\u0193")
        buf.write("\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192")
        buf.write("\u0194\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195\7\7\2\2")
        buf.write("\u0195\u0196\7\n\2\2\u0196I\3\2\2\2\u0197\u0198\5V,\2")
        buf.write("\u0198\u0199\7\65\2\2\u0199\u019c\7\17\2\2\u019a\u019d")
        buf.write("\5\26\f\2\u019b\u019d\5&\24\2\u019c\u019a\3\2\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019dK\3\2\2\2\u019e\u01a4\5<\37\2\u019f")
        buf.write("\u01a4\5\6\4\2\u01a0\u01a4\5J&\2\u01a1\u01a4\5`\61\2\u01a2")
        buf.write("\u01a4\5\22\n\2\u01a3\u019e\3\2\2\2\u01a3\u019f\3\2\2")
        buf.write("\2\u01a3\u01a0\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2")
        buf.write("\3\2\2\2\u01a4M\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6O\3\2")
        buf.write("\2\2\u01a7\u01a8\3\2\2\2\u01a8Q\3\2\2\2\u01a9\u01aa\3")
        buf.write("\2\2\2\u01aaS\3\2\2\2\u01ab\u01ac\58\35\2\u01ac\u01b8")
        buf.write("\5N(\2\u01ad\u01ae\7\13\2\2\u01ae\u01b2\5P)\2\u01af\u01b0")
        buf.write("\7\f\2\2\u01b0\u01b2\5R*\2\u01b1\u01ad\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\58\35\2\u01b4")
        buf.write("\u01b5\5N(\2\u01b5\u01b7\3\2\2\2\u01b6\u01b1\3\2\2\2\u01b7")
        buf.write("\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2")
        buf.write("\u01b9U\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01be\5X-\2")
        buf.write("\u01bc\u01be\5Z.\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2")
        buf.write("\2\2\u01beW\3\2\2\2\u01bf\u01c0\t\5\2\2\u01c0Y\3\2\2\2")
        buf.write("\u01c1\u01c2\t\6\2\2\u01c2[\3\2\2\2\u01c3\u01c4\3\2\2")
        buf.write("\2\u01c4]\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6_\3\2\2\2\u01c7")
        buf.write("\u01c8\7\60\2\2\u01c8\u01c9\5^\60\2\u01c9\u01ca\7\3\2")
        buf.write("\2\u01ca\u01cb\5&\24\2\u01cb\u01cc\7\5\2\2\u01cc\u01cd")
        buf.write("\5\f\7\2\u01cd\u01d1\7\6\2\2\u01ce\u01d0\5\b\5\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01d1\3")
        buf.write("\2\2\2\u01d4\u01d5\7\7\2\2\u01d5\u01d6\5\\/\2\u01d6a\3")
        buf.write("\2\2\2\u01d7\u01d8\5V,\2\u01d8\u01d9\7\b\2\2\u01d9\u01da")
        buf.write("\7\66\2\2\u01da\u01db\7\t\2\2\u01dbc\3\2\2\2\u01dc\u01dd")
        buf.write("\t\7\2\2\u01dd\u01df\7\21\2\2\u01de\u01dc\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\7\65\2")
        buf.write("\2\u01e1\u01e2\7\b\2\2\u01e2\u01e3\7\66\2\2\u01e3\u01e4")
        buf.write("\7\t\2\2\u01e4e\3\2\2\2\u01e5\u01e6\5V,\2\u01e6\u01e7")
        buf.write("\7\b\2\2\u01e7\u01e8\7\t\2\2\u01e8g\3\2\2\2,kmv{\177\u0084")
        buf.write("\u008f\u0095\u009c\u00b1\u00bb\u00c0\u00cc\u00d2\u00db")
        buf.write("\u00e2\u00ee\u0106\u010d\u0117\u0126\u012d\u013b\u013e")
        buf.write("\u0142\u0148\u014e\u0153\u0158\u0162\u0169\u0170\u017c")
        buf.write("\u0186\u0191\u019c\u01a3\u01b1\u01b8\u01bd\u01d1\u01de")
        return buf.getvalue()


class MoMParser ( Parser ):

    grammarFileName = "MoM.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'{'", "'}'", "'['", 
                     "']'", "';'", "'*'", "'/'", "'+'", "'-'", "'='", "'_'", 
                     "'.'", "'!'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'&&'", "'||'", "'this'", "'if'", "'else'", 
                     "'Component'", "'Int'", "'Text'", "'Real'", "'Set'", 
                     "'Map'", "'Size'", "'Nothing'", "'class'", "'new'", 
                     "'enumerate'", "'field'", "'specification'", "'return'", 
                     "'Boolean'", "'type'", "'of_type'", "'is_a'", "'while'", 
                     "'TRUE'", "'FALSE'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "OPEN_PAREN", "COMMA", "CLOSE_PAREN", 
                      "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_SBRACKET", 
                      "CLOSE_SBRACKET", "SEMI_COLON", "STAR", "SLASH", "PLUS", 
                      "MINUS", "EQUALS", "UNDERSCORE", "PERIOD", "NOT", 
                      "NOT_EQUALS", "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", 
                      "GREATER_EQUAL", "EQUAL_EQUAL", "AND", "OR", "THIS", 
                      "IF", "ELSE", "COMPONENT", "INT", "TEXT", "FLOAT", 
                      "SET", "MAP", "SIZE", "NOTHING", "CLASS", "NEW", "ENUMERATE", 
                      "FIELD", "SPEC", "RETURN", "BOOLEAN", "TYPE", "OF_TYPE", 
                      "IS_A", "WHILE", "TRUE", "FALSE", "CAPITALID", "CLASSID", 
                      "VARID", "INTEGER", "REAL", "WHITESPACE", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_arguments = 1
    RULE_assignation = 2
    RULE_block = 3
    RULE_class_rule = 4
    RULE_exit_if_check = 5
    RULE_condition_end = 6
    RULE_enter_else = 7
    RULE_condition = 8
    RULE_constant = 9
    RULE_construct_call = 10
    RULE_exit_con_def = 11
    RULE_construct_def = 12
    RULE_enum = 13
    RULE_enumeration = 14
    RULE_exit_sexp = 15
    RULE_and_op = 16
    RULE_or_op = 17
    RULE_ss_exp = 18
    RULE_exit_exp = 19
    RULE_s_exp = 20
    RULE_exit_term = 21
    RULE_plus_op = 22
    RULE_minus_op = 23
    RULE_expression = 24
    RULE_open_paren = 25
    RULE_close_paren = 26
    RULE_factor = 27
    RULE_function_args = 28
    RULE_function_call = 29
    RULE_exit_func_def = 30
    RULE_function_def = 31
    RULE_operand = 32
    RULE_field = 33
    RULE_spec_function = 34
    RULE_specification = 35
    RULE_assignation_def = 36
    RULE_statute = 37
    RULE_exit_factor = 38
    RULE_star_op = 39
    RULE_div_op = 40
    RULE_term = 41
    RULE_super_type = 42
    RULE_simple_type = 43
    RULE_complex_type = 44
    RULE_end_while = 45
    RULE_after_while = 46
    RULE_while_loop = 47
    RULE_array_def = 48
    RULE_array_var = 49
    RULE_array_arg = 50

    ruleNames =  [ "program", "arguments", "assignation", "block", "class_rule", 
                   "exit_if_check", "condition_end", "enter_else", "condition", 
                   "constant", "construct_call", "exit_con_def", "construct_def", 
                   "enum", "enumeration", "exit_sexp", "and_op", "or_op", 
                   "ss_exp", "exit_exp", "s_exp", "exit_term", "plus_op", 
                   "minus_op", "expression", "open_paren", "close_paren", 
                   "factor", "function_args", "function_call", "exit_func_def", 
                   "function_def", "operand", "field", "spec_function", 
                   "specification", "assignation_def", "statute", "exit_factor", 
                   "star_op", "div_op", "term", "super_type", "simple_type", 
                   "complex_type", "end_while", "after_while", "while_loop", 
                   "array_def", "array_var", "array_arg" ]

    EOF = Token.EOF
    OPEN_PAREN=1
    COMMA=2
    CLOSE_PAREN=3
    OPEN_BRACKET=4
    CLOSE_BRACKET=5
    OPEN_SBRACKET=6
    CLOSE_SBRACKET=7
    SEMI_COLON=8
    STAR=9
    SLASH=10
    PLUS=11
    MINUS=12
    EQUALS=13
    UNDERSCORE=14
    PERIOD=15
    NOT=16
    NOT_EQUALS=17
    LESS_THAN=18
    LESS_EQUAL=19
    GREATER_THAN=20
    GREATER_EQUAL=21
    EQUAL_EQUAL=22
    AND=23
    OR=24
    THIS=25
    IF=26
    ELSE=27
    COMPONENT=28
    INT=29
    TEXT=30
    FLOAT=31
    SET=32
    MAP=33
    SIZE=34
    NOTHING=35
    CLASS=36
    NEW=37
    ENUMERATE=38
    FIELD=39
    SPEC=40
    RETURN=41
    BOOLEAN=42
    TYPE=43
    OF_TYPE=44
    IS_A=45
    WHILE=46
    TRUE=47
    FALSE=48
    CAPITALID=49
    CLASSID=50
    VARID=51
    INTEGER=52
    REAL=53
    WHITESPACE=54
    STRING=55
    WS=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MoMParser.EOF, 0)

        def class_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Class_ruleContext)
            else:
                return self.getTypedRuleContext(MoMParser.Class_ruleContext,i)


        def enumeration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.EnumerationContext)
            else:
                return self.getTypedRuleContext(MoMParser.EnumerationContext,i)


        def specification(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.SpecificationContext)
            else:
                return self.getTypedRuleContext(MoMParser.SpecificationContext,i)


        def getRuleIndex(self):
            return MoMParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MoMParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 105
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.CLASS]:
                    self.state = 102
                    self.class_rule()
                    pass
                elif token in [MoMParser.ENUMERATE]:
                    self.state = 103
                    self.enumeration()
                    pass
                elif token in [MoMParser.SPEC]:
                    self.state = 104
                    self.specification()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.CLASS) | (1 << MoMParser.ENUMERATE) | (1 << MoMParser.SPEC))) != 0)):
                    break

            self.state = 109
            self.match(MoMParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ss_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Ss_expContext)
            else:
                return self.getTypedRuleContext(MoMParser.Ss_expContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.COMMA)
            else:
                return self.getToken(MoMParser.COMMA, i)

        def getRuleIndex(self):
            return MoMParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = MoMParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.ss_exp()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 112
                self.match(MoMParser.COMMA)
                self.state = 113
                self.ss_exp()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(MoMParser.EQUALS, 0)

        def VARID(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.VARID)
            else:
                return self.getToken(MoMParser.VARID, i)

        def array_var(self):
            return self.getTypedRuleContext(MoMParser.Array_varContext,0)


        def construct_call(self):
            return self.getTypedRuleContext(MoMParser.Construct_callContext,0)


        def ss_exp(self):
            return self.getTypedRuleContext(MoMParser.Ss_expContext,0)


        def PERIOD(self):
            return self.getToken(MoMParser.PERIOD, 0)

        def THIS(self):
            return self.getToken(MoMParser.THIS, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_assignation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignation" ):
                listener.enterAssignation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignation" ):
                listener.exitAssignation(self)




    def assignation(self):

        localctx = MoMParser.AssignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 119
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.VARID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self.match(MoMParser.PERIOD)


            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 123
                self.match(MoMParser.VARID)
                pass

            elif la_ == 2:
                self.state = 124
                self.array_var()
                pass


            self.state = 127
            self.match(MoMParser.EQUALS)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 128
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 129
                self.ss_exp()
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

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statute(self):
            return self.getTypedRuleContext(MoMParser.StatuteContext,0)


        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = MoMParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.statute()
            self.state = 133
            self.match(MoMParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(MoMParser.CLASS, 0)

        def CLASSID(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.CLASSID)
            else:
                return self.getToken(MoMParser.CLASSID, i)

        def IS_A(self):
            return self.getToken(MoMParser.IS_A, 0)

        def complex_type(self):
            return self.getTypedRuleContext(MoMParser.Complex_typeContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(MoMParser.OPEN_BRACKET, 0)

        def construct_def(self):
            return self.getTypedRuleContext(MoMParser.Construct_defContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def OF_TYPE(self):
            return self.getToken(MoMParser.OF_TYPE, 0)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.FieldContext)
            else:
                return self.getTypedRuleContext(MoMParser.FieldContext,i)


        def function_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Function_defContext)
            else:
                return self.getTypedRuleContext(MoMParser.Function_defContext,i)


        def getRuleIndex(self):
            return MoMParser.RULE_class_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_rule" ):
                listener.enterClass_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_rule" ):
                listener.exitClass_rule(self)




    def class_rule(self):

        localctx = MoMParser.Class_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MoMParser.CLASS)
            self.state = 136
            self.match(MoMParser.CLASSID)
            self.state = 137
            self.match(MoMParser.IS_A)
            self.state = 138
            self.complex_type()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.OF_TYPE:
                self.state = 139
                self.match(MoMParser.OF_TYPE)
                self.state = 140
                self.match(MoMParser.CLASSID)


            self.state = 143
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.FIELD:
                self.state = 144
                self.field()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.construct_def()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 151
                self.function_def()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 158
            self.match(MoMParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exit_if_checkContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_exit_if_check

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit_if_check" ):
                listener.enterExit_if_check(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit_if_check" ):
                listener.exitExit_if_check(self)




    def exit_if_check(self):

        localctx = MoMParser.Exit_if_checkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exit_if_check)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Condition_endContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_condition_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_end" ):
                listener.enterCondition_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_end" ):
                listener.exitCondition_end(self)




    def condition_end(self):

        localctx = MoMParser.Condition_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition_end)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enter_elseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_enter_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnter_else" ):
                listener.enterEnter_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnter_else" ):
                listener.exitEnter_else(self)




    def enter_else(self):

        localctx = MoMParser.Enter_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_enter_else)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MoMParser.IF, 0)

        def OPEN_PAREN(self):
            return self.getToken(MoMParser.OPEN_PAREN, 0)

        def ss_exp(self):
            return self.getTypedRuleContext(MoMParser.Ss_expContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(MoMParser.CLOSE_PAREN, 0)

        def exit_if_check(self):
            return self.getTypedRuleContext(MoMParser.Exit_if_checkContext,0)


        def OPEN_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.OPEN_BRACKET)
            else:
                return self.getToken(MoMParser.OPEN_BRACKET, i)

        def CLOSE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.CLOSE_BRACKET)
            else:
                return self.getToken(MoMParser.CLOSE_BRACKET, i)

        def condition_end(self):
            return self.getTypedRuleContext(MoMParser.Condition_endContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.BlockContext)
            else:
                return self.getTypedRuleContext(MoMParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MoMParser.ELSE, 0)

        def enter_else(self):
            return self.getTypedRuleContext(MoMParser.Enter_elseContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = MoMParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MoMParser.IF)
            self.state = 167
            self.match(MoMParser.OPEN_PAREN)
            self.state = 168
            self.ss_exp()
            self.state = 169
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 170
            self.exit_if_check()
            self.state = 171
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 172
                self.block()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.ELSE:
                self.state = 179
                self.match(MoMParser.ELSE)
                self.state = 180
                self.enter_else()
                self.state = 181
                self.match(MoMParser.OPEN_BRACKET)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                    self.state = 182
                    self.block()
                    self.state = 187
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 188
                self.match(MoMParser.CLOSE_BRACKET)


            self.state = 192
            self.condition_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MoMParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(MoMParser.REAL, 0)

        def STRING(self):
            return self.getToken(MoMParser.STRING, 0)

        def VARID(self):
            return self.getToken(MoMParser.VARID, 0)

        def array_var(self):
            return self.getTypedRuleContext(MoMParser.Array_varContext,0)


        def TRUE(self):
            return self.getToken(MoMParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MoMParser.FALSE, 0)

        def function_call(self):
            return self.getTypedRuleContext(MoMParser.Function_callContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = MoMParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constant)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(MoMParser.INTEGER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(MoMParser.REAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.match(MoMParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.match(MoMParser.VARID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                self.array_var()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 199
                self.match(MoMParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 200
                self.match(MoMParser.FALSE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 201
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Construct_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(MoMParser.NEW, 0)

        def CLASSID(self):
            return self.getToken(MoMParser.CLASSID, 0)

        def OPEN_PAREN(self):
            return self.getToken(MoMParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(MoMParser.CLOSE_PAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(MoMParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_construct_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstruct_call" ):
                listener.enterConstruct_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstruct_call" ):
                listener.exitConstruct_call(self)




    def construct_call(self):

        localctx = MoMParser.Construct_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_construct_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MoMParser.NEW)
            self.state = 205
            self.match(MoMParser.CLASSID)
            self.state = 206
            self.match(MoMParser.OPEN_PAREN)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 207
                self.arguments()


            self.state = 210
            self.match(MoMParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exit_con_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_exit_con_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit_con_def" ):
                listener.enterExit_con_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit_con_def" ):
                listener.exitExit_con_def(self)




    def exit_con_def(self):

        localctx = MoMParser.Exit_con_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exit_con_def)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Construct_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASSID(self):
            return self.getToken(MoMParser.CLASSID, 0)

        def OPEN_PAREN(self):
            return self.getToken(MoMParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(MoMParser.CLOSE_PAREN, 0)

        def OPEN_BRACKET(self):
            return self.getToken(MoMParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

        def exit_con_def(self):
            return self.getTypedRuleContext(MoMParser.Exit_con_defContext,0)


        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def function_args(self):
            return self.getTypedRuleContext(MoMParser.Function_argsContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.BlockContext)
            else:
                return self.getTypedRuleContext(MoMParser.BlockContext,i)


        def getRuleIndex(self):
            return MoMParser.RULE_construct_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstruct_def" ):
                listener.enterConstruct_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstruct_def" ):
                listener.exitConstruct_def(self)




    def construct_def(self):

        localctx = MoMParser.Construct_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_construct_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MoMParser.CLASSID)
            self.state = 215
            self.match(MoMParser.OPEN_PAREN)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 216
                self.function_args()


            self.state = 219
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 220
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 221
                self.block()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 228
            self.exit_con_def()
            self.state = 229
            self.match(MoMParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAPITALID(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.CAPITALID)
            else:
                return self.getToken(MoMParser.CAPITALID, i)

        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.COMMA)
            else:
                return self.getToken(MoMParser.COMMA, i)

        def getRuleIndex(self):
            return MoMParser.RULE_enum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum" ):
                listener.enterEnum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum" ):
                listener.exitEnum(self)




    def enum(self):

        localctx = MoMParser.EnumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MoMParser.CAPITALID)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 232
                self.match(MoMParser.COMMA)
                self.state = 233
                self.match(MoMParser.CAPITALID)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.match(MoMParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumerationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUMERATE(self):
            return self.getToken(MoMParser.ENUMERATE, 0)

        def CLASSID(self):
            return self.getToken(MoMParser.CLASSID, 0)

        def OPEN_BRACKET(self):
            return self.getToken(MoMParser.OPEN_BRACKET, 0)

        def enum(self):
            return self.getTypedRuleContext(MoMParser.EnumContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_enumeration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumeration" ):
                listener.enterEnumeration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumeration" ):
                listener.exitEnumeration(self)




    def enumeration(self):

        localctx = MoMParser.EnumerationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_enumeration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(MoMParser.ENUMERATE)
            self.state = 242
            self.match(MoMParser.CLASSID)
            self.state = 243
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 244
            self.enum()
            self.state = 245
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 246
            self.match(MoMParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exit_sexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_exit_sexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit_sexp" ):
                listener.enterExit_sexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit_sexp" ):
                listener.exitExit_sexp(self)




    def exit_sexp(self):

        localctx = MoMParser.Exit_sexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exit_sexp)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_and_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_op" ):
                listener.enterAnd_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_op" ):
                listener.exitAnd_op(self)




    def and_op(self):

        localctx = MoMParser.And_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_and_op)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Or_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_or_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_op" ):
                listener.enterOr_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_op" ):
                listener.exitOr_op(self)




    def or_op(self):

        localctx = MoMParser.Or_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_or_op)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ss_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.S_expContext)
            else:
                return self.getTypedRuleContext(MoMParser.S_expContext,i)


        def exit_sexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Exit_sexpContext)
            else:
                return self.getTypedRuleContext(MoMParser.Exit_sexpContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.AND)
            else:
                return self.getToken(MoMParser.AND, i)

        def and_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.And_opContext)
            else:
                return self.getTypedRuleContext(MoMParser.And_opContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.OR)
            else:
                return self.getToken(MoMParser.OR, i)

        def or_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Or_opContext)
            else:
                return self.getTypedRuleContext(MoMParser.Or_opContext,i)


        def getRuleIndex(self):
            return MoMParser.RULE_ss_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSs_exp" ):
                listener.enterSs_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSs_exp" ):
                listener.exitSs_exp(self)




    def ss_exp(self):

        localctx = MoMParser.Ss_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ss_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.s_exp()
            self.state = 255
            self.exit_sexp()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.AND or _la==MoMParser.OR:
                self.state = 260
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.AND]:
                    self.state = 256
                    self.match(MoMParser.AND)
                    self.state = 257
                    self.and_op()
                    pass
                elif token in [MoMParser.OR]:
                    self.state = 258
                    self.match(MoMParser.OR)
                    self.state = 259
                    self.or_op()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 262
                self.s_exp()
                self.state = 263
                self.exit_sexp()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exit_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_exit_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit_exp" ):
                listener.enterExit_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit_exp" ):
                listener.exitExit_exp(self)




    def exit_exp(self):

        localctx = MoMParser.Exit_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exit_exp)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class S_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MoMParser.ExpressionContext,i)


        def operand(self):
            return self.getTypedRuleContext(MoMParser.OperandContext,0)


        def exit_exp(self):
            return self.getTypedRuleContext(MoMParser.Exit_expContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_s_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS_exp" ):
                listener.enterS_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS_exp" ):
                listener.exitS_exp(self)




    def s_exp(self):

        localctx = MoMParser.S_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_s_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.expression()
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.LESS_THAN) | (1 << MoMParser.LESS_EQUAL) | (1 << MoMParser.GREATER_THAN) | (1 << MoMParser.GREATER_EQUAL) | (1 << MoMParser.EQUAL_EQUAL))) != 0):
                self.state = 273
                self.operand()
                self.state = 274
                self.expression()
                self.state = 275
                self.exit_exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exit_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_exit_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit_term" ):
                listener.enterExit_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit_term" ):
                listener.exitExit_term(self)




    def exit_term(self):

        localctx = MoMParser.Exit_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exit_term)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Plus_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_plus_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus_op" ):
                listener.enterPlus_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus_op" ):
                listener.exitPlus_op(self)




    def plus_op(self):

        localctx = MoMParser.Plus_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_plus_op)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Minus_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_minus_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinus_op" ):
                listener.enterMinus_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinus_op" ):
                listener.exitMinus_op(self)




    def minus_op(self):

        localctx = MoMParser.Minus_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_minus_op)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.TermContext)
            else:
                return self.getTypedRuleContext(MoMParser.TermContext,i)


        def exit_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Exit_termContext)
            else:
                return self.getTypedRuleContext(MoMParser.Exit_termContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.PLUS)
            else:
                return self.getToken(MoMParser.PLUS, i)

        def plus_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Plus_opContext)
            else:
                return self.getTypedRuleContext(MoMParser.Plus_opContext,i)


        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.MINUS)
            else:
                return self.getToken(MoMParser.MINUS, i)

        def minus_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Minus_opContext)
            else:
                return self.getTypedRuleContext(MoMParser.Minus_opContext,i)


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MoMParser.ConditionContext,i)


        def getRuleIndex(self):
            return MoMParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = MoMParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.term()
            self.state = 286
            self.exit_term()
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.IF))) != 0):
                self.state = 292
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.PLUS]:
                    self.state = 287
                    self.match(MoMParser.PLUS)
                    self.state = 288
                    self.plus_op()
                    pass
                elif token in [MoMParser.MINUS]:
                    self.state = 289
                    self.match(MoMParser.MINUS)
                    self.state = 290
                    self.minus_op()
                    pass
                elif token in [MoMParser.IF]:
                    self.state = 291
                    self.condition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 294
                self.term()
                self.state = 295
                self.exit_term()
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Open_parenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_open_paren

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpen_paren" ):
                listener.enterOpen_paren(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpen_paren" ):
                listener.exitOpen_paren(self)




    def open_paren(self):

        localctx = MoMParser.Open_parenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_open_paren)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Close_parenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_close_paren

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose_paren" ):
                listener.enterClose_paren(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose_paren" ):
                listener.exitClose_paren(self)




    def close_paren(self):

        localctx = MoMParser.Close_parenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_close_paren)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(MoMParser.OPEN_PAREN, 0)

        def open_paren(self):
            return self.getTypedRuleContext(MoMParser.Open_parenContext,0)


        def ss_exp(self):
            return self.getTypedRuleContext(MoMParser.Ss_expContext,0)


        def close_paren(self):
            return self.getTypedRuleContext(MoMParser.Close_parenContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(MoMParser.CLOSE_PAREN, 0)

        def constant(self):
            return self.getTypedRuleContext(MoMParser.ConstantContext,0)


        def PLUS(self):
            return self.getToken(MoMParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MoMParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MoMParser.NOT, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = MoMParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(MoMParser.OPEN_PAREN)
                self.state = 307
                self.open_paren()
                self.state = 308
                self.ss_exp()
                self.state = 309
                self.close_paren()
                self.state = 310
                self.match(MoMParser.CLOSE_PAREN)
                pass
            elif token in [MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0):
                    self.state = 312
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 315
                self.constant()
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

    class Function_argsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARID(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.VARID)
            else:
                return self.getToken(MoMParser.VARID, i)

        def super_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Super_typeContext)
            else:
                return self.getTypedRuleContext(MoMParser.Super_typeContext,i)


        def array_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Array_argContext)
            else:
                return self.getTypedRuleContext(MoMParser.Array_argContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.COMMA)
            else:
                return self.getToken(MoMParser.COMMA, i)

        def getRuleIndex(self):
            return MoMParser.RULE_function_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_args" ):
                listener.enterFunction_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_args" ):
                listener.exitFunction_args(self)




    def function_args(self):

        localctx = MoMParser.Function_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 318
                self.super_type()
                pass

            elif la_ == 2:
                self.state = 319
                self.array_arg()
                pass


            self.state = 322
            self.match(MoMParser.VARID)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 323
                self.match(MoMParser.COMMA)
                self.state = 326
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 324
                    self.super_type()
                    pass

                elif la_ == 2:
                    self.state = 325
                    self.array_arg()
                    pass


                self.state = 328
                self.match(MoMParser.VARID)
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARID(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.VARID)
            else:
                return self.getToken(MoMParser.VARID, i)

        def OPEN_PAREN(self):
            return self.getToken(MoMParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(MoMParser.CLOSE_PAREN, 0)

        def PERIOD(self):
            return self.getToken(MoMParser.PERIOD, 0)

        def arguments(self):
            return self.getTypedRuleContext(MoMParser.ArgumentsContext,0)


        def THIS(self):
            return self.getToken(MoMParser.THIS, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)




    def function_call(self):

        localctx = MoMParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 335
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.VARID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 336
                self.match(MoMParser.PERIOD)


            self.state = 339
            self.match(MoMParser.VARID)
            self.state = 340
            self.match(MoMParser.OPEN_PAREN)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 341
                self.arguments()


            self.state = 344
            self.match(MoMParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exit_func_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_exit_func_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit_func_def" ):
                listener.enterExit_func_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit_func_def" ):
                listener.exitExit_func_def(self)




    def exit_func_def(self):

        localctx = MoMParser.Exit_func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exit_func_def)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_type(self):
            return self.getTypedRuleContext(MoMParser.Simple_typeContext,0)


        def VARID(self):
            return self.getToken(MoMParser.VARID, 0)

        def OPEN_PAREN(self):
            return self.getToken(MoMParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(MoMParser.CLOSE_PAREN, 0)

        def OPEN_BRACKET(self):
            return self.getToken(MoMParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

        def exit_func_def(self):
            return self.getTypedRuleContext(MoMParser.Exit_func_defContext,0)


        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.SEMI_COLON)
            else:
                return self.getToken(MoMParser.SEMI_COLON, i)

        def function_args(self):
            return self.getTypedRuleContext(MoMParser.Function_argsContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.BlockContext)
            else:
                return self.getTypedRuleContext(MoMParser.BlockContext,i)


        def RETURN(self):
            return self.getToken(MoMParser.RETURN, 0)

        def ss_exp(self):
            return self.getTypedRuleContext(MoMParser.Ss_expContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)




    def function_def(self):

        localctx = MoMParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.simple_type()
            self.state = 349
            self.match(MoMParser.VARID)
            self.state = 350
            self.match(MoMParser.OPEN_PAREN)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 351
                self.function_args()


            self.state = 354
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 355
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 356
                self.block()
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.RETURN:
                self.state = 362
                self.match(MoMParser.RETURN)
                self.state = 363
                self.ss_exp()
                self.state = 364
                self.match(MoMParser.SEMI_COLON)


            self.state = 368
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 369
            self.exit_func_def()
            self.state = 370
            self.match(MoMParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(MoMParser.LESS_THAN, 0)

        def LESS_EQUAL(self):
            return self.getToken(MoMParser.LESS_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(MoMParser.GREATER_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MoMParser.GREATER_EQUAL, 0)

        def EQUAL_EQUAL(self):
            return self.getToken(MoMParser.EQUAL_EQUAL, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = MoMParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.LESS_THAN) | (1 << MoMParser.LESS_EQUAL) | (1 << MoMParser.GREATER_THAN) | (1 << MoMParser.GREATER_EQUAL) | (1 << MoMParser.EQUAL_EQUAL))) != 0)):
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

    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIELD(self):
            return self.getToken(MoMParser.FIELD, 0)

        def LESS_THAN(self):
            return self.getToken(MoMParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(MoMParser.GREATER_THAN, 0)

        def VARID(self):
            return self.getToken(MoMParser.VARID, 0)

        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def super_type(self):
            return self.getTypedRuleContext(MoMParser.Super_typeContext,0)


        def array_def(self):
            return self.getTypedRuleContext(MoMParser.Array_defContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)




    def field(self):

        localctx = MoMParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(MoMParser.FIELD)
            self.state = 375
            self.match(MoMParser.LESS_THAN)
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 376
                self.super_type()
                pass

            elif la_ == 2:
                self.state = 377
                self.array_def()
                pass


            self.state = 380
            self.match(MoMParser.GREATER_THAN)
            self.state = 381
            self.match(MoMParser.VARID)
            self.state = 382
            self.match(MoMParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Spec_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_type(self):
            return self.getTypedRuleContext(MoMParser.Simple_typeContext,0)


        def VARID(self):
            return self.getToken(MoMParser.VARID, 0)

        def OPEN_PAREN(self):
            return self.getToken(MoMParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(MoMParser.CLOSE_PAREN, 0)

        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def function_args(self):
            return self.getTypedRuleContext(MoMParser.Function_argsContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_spec_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpec_function" ):
                listener.enterSpec_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpec_function" ):
                listener.exitSpec_function(self)




    def spec_function(self):

        localctx = MoMParser.Spec_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_spec_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.simple_type()
            self.state = 385
            self.match(MoMParser.VARID)
            self.state = 386
            self.match(MoMParser.OPEN_PAREN)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 387
                self.function_args()


            self.state = 390
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 391
            self.match(MoMParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SpecificationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPEC(self):
            return self.getToken(MoMParser.SPEC, 0)

        def CLASSID(self):
            return self.getToken(MoMParser.CLASSID, 0)

        def OPEN_BRACKET(self):
            return self.getToken(MoMParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def spec_function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Spec_functionContext)
            else:
                return self.getTypedRuleContext(MoMParser.Spec_functionContext,i)


        def getRuleIndex(self):
            return MoMParser.RULE_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecification" ):
                listener.enterSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecification" ):
                listener.exitSpecification(self)




    def specification(self):

        localctx = MoMParser.SpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MoMParser.SPEC)
            self.state = 394
            self.match(MoMParser.CLASSID)
            self.state = 395
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 396
                self.spec_function()
                self.state = 401
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 402
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 403
            self.match(MoMParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignation_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def super_type(self):
            return self.getTypedRuleContext(MoMParser.Super_typeContext,0)


        def VARID(self):
            return self.getToken(MoMParser.VARID, 0)

        def EQUALS(self):
            return self.getToken(MoMParser.EQUALS, 0)

        def construct_call(self):
            return self.getTypedRuleContext(MoMParser.Construct_callContext,0)


        def ss_exp(self):
            return self.getTypedRuleContext(MoMParser.Ss_expContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_assignation_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignation_def" ):
                listener.enterAssignation_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignation_def" ):
                listener.exitAssignation_def(self)




    def assignation_def(self):

        localctx = MoMParser.Assignation_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_assignation_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.super_type()
            self.state = 406
            self.match(MoMParser.VARID)
            self.state = 407
            self.match(MoMParser.EQUALS)
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 408
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 409
                self.ss_exp()
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

    class StatuteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(MoMParser.Function_callContext,0)


        def assignation(self):
            return self.getTypedRuleContext(MoMParser.AssignationContext,0)


        def assignation_def(self):
            return self.getTypedRuleContext(MoMParser.Assignation_defContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(MoMParser.While_loopContext,0)


        def condition(self):
            return self.getTypedRuleContext(MoMParser.ConditionContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_statute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatute" ):
                listener.enterStatute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatute" ):
                listener.exitStatute(self)




    def statute(self):

        localctx = MoMParser.StatuteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_statute)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.assignation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.assignation_def()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.while_loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 416
                self.condition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exit_factorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_exit_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit_factor" ):
                listener.enterExit_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit_factor" ):
                listener.exitExit_factor(self)




    def exit_factor(self):

        localctx = MoMParser.Exit_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exit_factor)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Star_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_star_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStar_op" ):
                listener.enterStar_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStar_op" ):
                listener.exitStar_op(self)




    def star_op(self):

        localctx = MoMParser.Star_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_star_op)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Div_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_div_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv_op" ):
                listener.enterDiv_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv_op" ):
                listener.exitDiv_op(self)




    def div_op(self):

        localctx = MoMParser.Div_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_div_op)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.FactorContext)
            else:
                return self.getTypedRuleContext(MoMParser.FactorContext,i)


        def exit_factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Exit_factorContext)
            else:
                return self.getTypedRuleContext(MoMParser.Exit_factorContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.STAR)
            else:
                return self.getToken(MoMParser.STAR, i)

        def star_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Star_opContext)
            else:
                return self.getTypedRuleContext(MoMParser.Star_opContext,i)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.SLASH)
            else:
                return self.getToken(MoMParser.SLASH, i)

        def div_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Div_opContext)
            else:
                return self.getTypedRuleContext(MoMParser.Div_opContext,i)


        def getRuleIndex(self):
            return MoMParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = MoMParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.factor()
            self.state = 426
            self.exit_factor()
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.STAR or _la==MoMParser.SLASH:
                self.state = 431
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.STAR]:
                    self.state = 427
                    self.match(MoMParser.STAR)
                    self.state = 428
                    self.star_op()
                    pass
                elif token in [MoMParser.SLASH]:
                    self.state = 429
                    self.match(MoMParser.SLASH)
                    self.state = 430
                    self.div_op()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 433
                self.factor()
                self.state = 434
                self.exit_factor()
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Super_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_type(self):
            return self.getTypedRuleContext(MoMParser.Simple_typeContext,0)


        def complex_type(self):
            return self.getTypedRuleContext(MoMParser.Complex_typeContext,0)


        def getRuleIndex(self):
            return MoMParser.RULE_super_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuper_type" ):
                listener.enterSuper_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuper_type" ):
                listener.exitSuper_type(self)




    def super_type(self):

        localctx = MoMParser.Super_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_super_type)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.INT, MoMParser.TEXT, MoMParser.FLOAT, MoMParser.NOTHING, MoMParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.simple_type()
                pass
            elif token in [MoMParser.COMPONENT, MoMParser.SET, MoMParser.MAP, MoMParser.SIZE, MoMParser.CLASSID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.complex_type()
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

    class Simple_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MoMParser.INT, 0)

        def TEXT(self):
            return self.getToken(MoMParser.TEXT, 0)

        def FLOAT(self):
            return self.getToken(MoMParser.FLOAT, 0)

        def NOTHING(self):
            return self.getToken(MoMParser.NOTHING, 0)

        def BOOLEAN(self):
            return self.getToken(MoMParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_simple_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_type" ):
                listener.enterSimple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_type" ):
                listener.exitSimple_type(self)




    def simple_type(self):

        localctx = MoMParser.Simple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_simple_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0)):
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

    class Complex_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(MoMParser.SET, 0)

        def MAP(self):
            return self.getToken(MoMParser.MAP, 0)

        def SIZE(self):
            return self.getToken(MoMParser.SIZE, 0)

        def COMPONENT(self):
            return self.getToken(MoMParser.COMPONENT, 0)

        def CLASSID(self):
            return self.getToken(MoMParser.CLASSID, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_complex_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplex_type" ):
                listener.enterComplex_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplex_type" ):
                listener.exitComplex_type(self)




    def complex_type(self):

        localctx = MoMParser.Complex_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_complex_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.CLASSID))) != 0)):
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

    class End_whileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_end_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_while" ):
                listener.enterEnd_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_while" ):
                listener.exitEnd_while(self)




    def end_while(self):

        localctx = MoMParser.End_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_end_while)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class After_whileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MoMParser.RULE_after_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAfter_while" ):
                listener.enterAfter_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAfter_while" ):
                listener.exitAfter_while(self)




    def after_while(self):

        localctx = MoMParser.After_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_after_while)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_loopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MoMParser.WHILE, 0)

        def after_while(self):
            return self.getTypedRuleContext(MoMParser.After_whileContext,0)


        def OPEN_PAREN(self):
            return self.getToken(MoMParser.OPEN_PAREN, 0)

        def ss_exp(self):
            return self.getTypedRuleContext(MoMParser.Ss_expContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(MoMParser.CLOSE_PAREN, 0)

        def exit_if_check(self):
            return self.getTypedRuleContext(MoMParser.Exit_if_checkContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(MoMParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

        def end_while(self):
            return self.getTypedRuleContext(MoMParser.End_whileContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.BlockContext)
            else:
                return self.getTypedRuleContext(MoMParser.BlockContext,i)


        def getRuleIndex(self):
            return MoMParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)




    def while_loop(self):

        localctx = MoMParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(MoMParser.WHILE)
            self.state = 454
            self.after_while()
            self.state = 455
            self.match(MoMParser.OPEN_PAREN)
            self.state = 456
            self.ss_exp()
            self.state = 457
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 458
            self.exit_if_check()
            self.state = 459
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 460
                self.block()
                self.state = 465
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 466
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 467
            self.end_while()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def super_type(self):
            return self.getTypedRuleContext(MoMParser.Super_typeContext,0)


        def OPEN_SBRACKET(self):
            return self.getToken(MoMParser.OPEN_SBRACKET, 0)

        def INTEGER(self):
            return self.getToken(MoMParser.INTEGER, 0)

        def CLOSE_SBRACKET(self):
            return self.getToken(MoMParser.CLOSE_SBRACKET, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_array_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_def" ):
                listener.enterArray_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_def" ):
                listener.exitArray_def(self)




    def array_def(self):

        localctx = MoMParser.Array_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.super_type()
            self.state = 470
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 471
            self.match(MoMParser.INTEGER)
            self.state = 472
            self.match(MoMParser.CLOSE_SBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARID(self):
            return self.getToken(MoMParser.VARID, 0)

        def OPEN_SBRACKET(self):
            return self.getToken(MoMParser.OPEN_SBRACKET, 0)

        def INTEGER(self):
            return self.getToken(MoMParser.INTEGER, 0)

        def CLOSE_SBRACKET(self):
            return self.getToken(MoMParser.CLOSE_SBRACKET, 0)

        def PERIOD(self):
            return self.getToken(MoMParser.PERIOD, 0)

        def THIS(self):
            return self.getToken(MoMParser.THIS, 0)

        def CLASSID(self):
            return self.getToken(MoMParser.CLASSID, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_array_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_var" ):
                listener.enterArray_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_var" ):
                listener.exitArray_var(self)




    def array_var(self):

        localctx = MoMParser.Array_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_array_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.THIS or _la==MoMParser.CLASSID:
                self.state = 474
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.CLASSID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 475
                self.match(MoMParser.PERIOD)


            self.state = 478
            self.match(MoMParser.VARID)
            self.state = 479
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 480
            self.match(MoMParser.INTEGER)
            self.state = 481
            self.match(MoMParser.CLOSE_SBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_argContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def super_type(self):
            return self.getTypedRuleContext(MoMParser.Super_typeContext,0)


        def OPEN_SBRACKET(self):
            return self.getToken(MoMParser.OPEN_SBRACKET, 0)

        def CLOSE_SBRACKET(self):
            return self.getToken(MoMParser.CLOSE_SBRACKET, 0)

        def getRuleIndex(self):
            return MoMParser.RULE_array_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_arg" ):
                listener.enterArray_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_arg" ):
                listener.exitArray_arg(self)




    def array_arg(self):

        localctx = MoMParser.Array_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.super_type()
            self.state = 484
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 485
            self.match(MoMParser.CLOSE_SBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





