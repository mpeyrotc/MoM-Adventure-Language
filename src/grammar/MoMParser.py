# Generated from src/grammar/MoM.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u016c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\3\2\3\2\3\2\6\2F\n\2\r\2\16\2G")
        buf.write("\3\2\3\2\3\3\3\3\3\3\7\3O\n\3\f\3\16\3R\13\3\3\4\3\4\5")
        buf.write("\4V\n\4\3\4\3\4\3\4\3\4\5\4\\\n\4\3\5\3\5\3\5\7\5a\n\5")
        buf.write("\f\5\16\5d\13\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6l\n\6\3\6\3")
        buf.write("\6\3\6\3\6\7\6r\n\6\f\6\16\6u\13\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0086\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u008f\n\b\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u0095\n\t\3\t\3\t\3\n\3\n\3\n\5\n\u009c\n\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13\u00a7\n\13")
        buf.write("\f\13\16\13\u00aa\13\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\7\r\u00b8\n\r\f\r\16\r\u00bb\13\r")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00c1\n\16\3\17\3\17\5\17\u00c5")
        buf.write("\n\17\3\17\3\17\3\17\5\17\u00ca\n\17\3\17\3\17\5\17\u00ce")
        buf.write("\n\17\7\17\u00d0\n\17\f\17\16\17\u00d3\13\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00da\n\20\3\20\5\20\u00dd\n\20\3")
        buf.write("\21\3\21\5\21\u00e1\n\21\3\21\3\21\3\21\3\21\5\21\u00e7")
        buf.write("\n\21\3\21\3\21\7\21\u00eb\n\21\f\21\16\21\u00ee\13\21")
        buf.write("\3\22\3\22\5\22\u00f2\n\22\3\22\3\22\3\22\5\22\u00f7\n")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00ff\n\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0108\n\23\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u0113\n\25")
        buf.write("\3\25\3\25\3\25\3\25\7\25\u0119\n\25\f\25\16\25\u011c")
        buf.write("\13\25\3\26\3\26\3\26\3\26\5\26\u0122\n\26\3\26\3\26\3")
        buf.write("\26\6\26\u0127\n\26\r\26\16\26\u0128\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u012f\n\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u0139\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u0140")
        buf.write("\n\31\3\32\3\32\3\32\7\32\u0145\n\32\f\32\16\32\u0148")
        buf.write("\13\32\3\33\3\33\5\33\u014c\n\33\3\34\3\34\3\35\3\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \5 \u0161\n \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\2\2\"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@\2\n\4\2\33\33\65\65\3\2\31\32\4")
        buf.write("\2\r\16\22\22\4\2\33\33\64\64\3\2\24\30\3\2\13\f\5\2\37")
        buf.write("!%%,,\5\2\36\36\"$\64\64\2\u017b\2E\3\2\2\2\4K\3\2\2\2")
        buf.write("\6U\3\2\2\2\bb\3\2\2\2\ne\3\2\2\2\fy\3\2\2\2\16\u008e")
        buf.write("\3\2\2\2\20\u0090\3\2\2\2\22\u0098\3\2\2\2\24\u00a3\3")
        buf.write("\2\2\2\26\u00ad\3\2\2\2\30\u00b4\3\2\2\2\32\u00bc\3\2")
        buf.write("\2\2\34\u00c4\3\2\2\2\36\u00dc\3\2\2\2 \u00e0\3\2\2\2")
        buf.write("\"\u00f1\3\2\2\2$\u00fa\3\2\2\2&\u010c\3\2\2\2(\u011a")
        buf.write("\3\2\2\2*\u0126\3\2\2\2,\u012a\3\2\2\2.\u0133\3\2\2\2")
        buf.write("\60\u013f\3\2\2\2\62\u0141\3\2\2\2\64\u014b\3\2\2\2\66")
        buf.write("\u014d\3\2\2\28\u014f\3\2\2\2:\u0151\3\2\2\2<\u0159\3")
        buf.write("\2\2\2>\u0160\3\2\2\2@\u0167\3\2\2\2BF\5\n\6\2CF\5\26")
        buf.write("\f\2DF\5,\27\2EB\3\2\2\2EC\3\2\2\2ED\3\2\2\2FG\3\2\2\2")
        buf.write("GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\7\2\2\3J\3\3\2\2\2KP")
        buf.write("\5\30\r\2LM\7\4\2\2MO\5\30\r\2NL\3\2\2\2OR\3\2\2\2PN\3")
        buf.write("\2\2\2PQ\3\2\2\2Q\5\3\2\2\2RP\3\2\2\2ST\t\2\2\2TV\7\21")
        buf.write("\2\2US\3\2\2\2UV\3\2\2\2VW\3\2\2\2WX\7\65\2\2X[\7\17\2")
        buf.write("\2Y\\\5\20\t\2Z\\\5\30\r\2[Y\3\2\2\2[Z\3\2\2\2\\\7\3\2")
        buf.write("\2\2]^\5\60\31\2^_\7\n\2\2_a\3\2\2\2`]\3\2\2\2ad\3\2\2")
        buf.write("\2b`\3\2\2\2bc\3\2\2\2c\t\3\2\2\2db\3\2\2\2ef\7&\2\2f")
        buf.write("g\7\64\2\2gh\7/\2\2hk\58\35\2ij\7.\2\2jl\7\64\2\2ki\3")
        buf.write("\2\2\2kl\3\2\2\2lm\3\2\2\2mn\7\6\2\2no\5(\25\2os\5\22")
        buf.write("\n\2pr\5$\23\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2")
        buf.write("tv\3\2\2\2us\3\2\2\2vw\7\7\2\2wx\7\n\2\2x\13\3\2\2\2y")
        buf.write("z\7\34\2\2z{\7\3\2\2{|\5\30\r\2|}\7\5\2\2}~\7\6\2\2~\177")
        buf.write("\5\b\5\2\177\u0085\7\7\2\2\u0080\u0081\7\35\2\2\u0081")
        buf.write("\u0082\7\6\2\2\u0082\u0083\5\b\5\2\u0083\u0084\7\7\2\2")
        buf.write("\u0084\u0086\3\2\2\2\u0085\u0080\3\2\2\2\u0085\u0086\3")
        buf.write("\2\2\2\u0086\r\3\2\2\2\u0087\u008f\7\66\2\2\u0088\u008f")
        buf.write("\7\67\2\2\u0089\u008f\79\2\2\u008a\u008f\7\65\2\2\u008b")
        buf.write("\u008f\5> \2\u008c\u008f\7\61\2\2\u008d\u008f\7\62\2\2")
        buf.write("\u008e\u0087\3\2\2\2\u008e\u0088\3\2\2\2\u008e\u0089\3")
        buf.write("\2\2\2\u008e\u008a\3\2\2\2\u008e\u008b\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008d\3\2\2\2\u008f\17\3\2\2\2\u0090\u0091")
        buf.write("\7\'\2\2\u0091\u0092\7\64\2\2\u0092\u0094\7\3\2\2\u0093")
        buf.write("\u0095\5\4\3\2\u0094\u0093\3\2\2\2\u0094\u0095\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0097\7\5\2\2\u0097\21\3\2")
        buf.write("\2\2\u0098\u0099\7\64\2\2\u0099\u009b\7\3\2\2\u009a\u009c")
        buf.write("\5 \21\2\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009e\7\5\2\2\u009e\u009f\7\6\2\2")
        buf.write("\u009f\u00a0\5\b\5\2\u00a0\u00a1\7\7\2\2\u00a1\u00a2\7")
        buf.write("\n\2\2\u00a2\23\3\2\2\2\u00a3\u00a8\7\63\2\2\u00a4\u00a5")
        buf.write("\7\4\2\2\u00a5\u00a7\7\63\2\2\u00a6\u00a4\3\2\2\2\u00a7")
        buf.write("\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ac\7")
        buf.write("\n\2\2\u00ac\25\3\2\2\2\u00ad\u00ae\7(\2\2\u00ae\u00af")
        buf.write("\7\64\2\2\u00af\u00b0\7\6\2\2\u00b0\u00b1\5\24\13\2\u00b1")
        buf.write("\u00b2\7\7\2\2\u00b2\u00b3\7\n\2\2\u00b3\27\3\2\2\2\u00b4")
        buf.write("\u00b9\5\32\16\2\u00b5\u00b6\t\3\2\2\u00b6\u00b8\5\32")
        buf.write("\16\2\u00b7\u00b5\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7")
        buf.write("\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\31\3\2\2\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bc\u00c0\5\34\17\2\u00bd\u00be\5&\24\2\u00be")
        buf.write("\u00bf\5\34\17\2\u00bf\u00c1\3\2\2\2\u00c0\u00bd\3\2\2")
        buf.write("\2\u00c0\u00c1\3\2\2\2\u00c1\33\3\2\2\2\u00c2\u00c5\5")
        buf.write("\"\22\2\u00c3\u00c5\5\62\32\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00d1\3\2\2\2\u00c6\u00ca\7\r\2\2")
        buf.write("\u00c7\u00ca\7\16\2\2\u00c8\u00ca\5\f\7\2\u00c9\u00c6")
        buf.write("\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca")
        buf.write("\u00cd\3\2\2\2\u00cb\u00ce\5\"\22\2\u00cc\u00ce\5\62\32")
        buf.write("\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00d0")
        buf.write("\3\2\2\2\u00cf\u00c9\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\35\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d4\u00d5\7\3\2\2\u00d5\u00d6\5\30\r")
        buf.write("\2\u00d6\u00d7\7\5\2\2\u00d7\u00dd\3\2\2\2\u00d8\u00da")
        buf.write("\t\4\2\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00dd\5\16\b\2\u00dc\u00d4\3\2\2")
        buf.write("\2\u00dc\u00d9\3\2\2\2\u00dd\37\3\2\2\2\u00de\u00e1\5")
        buf.write("\64\33\2\u00df\u00e1\5@!\2\u00e0\u00de\3\2\2\2\u00e0\u00df")
        buf.write("\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00ec\7\65\2\2\u00e3")
        buf.write("\u00e6\7\4\2\2\u00e4\u00e7\5\64\33\2\u00e5\u00e7\5@!\2")
        buf.write("\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3")
        buf.write("\2\2\2\u00e8\u00e9\7\65\2\2\u00e9\u00eb\3\2\2\2\u00ea")
        buf.write("\u00e3\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2")
        buf.write("\u00ec\u00ed\3\2\2\2\u00ed!\3\2\2\2\u00ee\u00ec\3\2\2")
        buf.write("\2\u00ef\u00f0\t\5\2\2\u00f0\u00f2\7\21\2\2\u00f1\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f4\7\65\2\2\u00f4\u00f6\7\3\2\2\u00f5\u00f7\5\4\3")
        buf.write("\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8")
        buf.write("\3\2\2\2\u00f8\u00f9\7\5\2\2\u00f9#\3\2\2\2\u00fa\u00fb")
        buf.write("\5\66\34\2\u00fb\u00fc\7\65\2\2\u00fc\u00fe\7\3\2\2\u00fd")
        buf.write("\u00ff\5 \21\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u0101\7\5\2\2\u0101\u0102\7")
        buf.write("\6\2\2\u0102\u0107\5\b\5\2\u0103\u0104\7+\2\2\u0104\u0105")
        buf.write("\5\30\r\2\u0105\u0106\7\n\2\2\u0106\u0108\3\2\2\2\u0107")
        buf.write("\u0103\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\3\2\2\2")
        buf.write("\u0109\u010a\7\7\2\2\u010a\u010b\7\n\2\2\u010b%\3\2\2")
        buf.write("\2\u010c\u010d\t\6\2\2\u010d\'\3\2\2\2\u010e\u010f\7)")
        buf.write("\2\2\u010f\u0112\7\24\2\2\u0110\u0113\5\64\33\2\u0111")
        buf.write("\u0113\5<\37\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2")
        buf.write("\u0113\u0114\3\2\2\2\u0114\u0115\7\26\2\2\u0115\u0116")
        buf.write("\7\65\2\2\u0116\u0117\7\n\2\2\u0117\u0119\3\2\2\2\u0118")
        buf.write("\u010e\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b)\3\2\2\2\u011c\u011a\3\2\2")
        buf.write("\2\u011d\u011e\5\66\34\2\u011e\u011f\7\65\2\2\u011f\u0121")
        buf.write("\7\3\2\2\u0120\u0122\5 \21\2\u0121\u0120\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\7\5\2\2")
        buf.write("\u0124\u0125\7\n\2\2\u0125\u0127\3\2\2\2\u0126\u011d\3")
        buf.write("\2\2\2\u0127\u0128\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129")
        buf.write("\3\2\2\2\u0129+\3\2\2\2\u012a\u012b\7*\2\2\u012b\u012c")
        buf.write("\7\64\2\2\u012c\u012e\7\6\2\2\u012d\u012f\5*\26\2\u012e")
        buf.write("\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\3\2\2\2")
        buf.write("\u0130\u0131\7\7\2\2\u0131\u0132\7\n\2\2\u0132-\3\2\2")
        buf.write("\2\u0133\u0134\5\64\33\2\u0134\u0135\7\65\2\2\u0135\u0138")
        buf.write("\7\17\2\2\u0136\u0139\5\20\t\2\u0137\u0139\5\30\r\2\u0138")
        buf.write("\u0136\3\2\2\2\u0138\u0137\3\2\2\2\u0139/\3\2\2\2\u013a")
        buf.write("\u0140\5\"\22\2\u013b\u0140\5\6\4\2\u013c\u0140\5.\30")
        buf.write("\2\u013d\u0140\5:\36\2\u013e\u0140\5\f\7\2\u013f\u013a")
        buf.write("\3\2\2\2\u013f\u013b\3\2\2\2\u013f\u013c\3\2\2\2\u013f")
        buf.write("\u013d\3\2\2\2\u013f\u013e\3\2\2\2\u0140\61\3\2\2\2\u0141")
        buf.write("\u0146\5\36\20\2\u0142\u0143\t\7\2\2\u0143\u0145\5\36")
        buf.write("\20\2\u0144\u0142\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\63\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0149\u014c\5\66\34\2\u014a\u014c\58\35\2\u014b")
        buf.write("\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c\65\3\2\2\2\u014d")
        buf.write("\u014e\t\b\2\2\u014e\67\3\2\2\2\u014f\u0150\t\t\2\2\u0150")
        buf.write("9\3\2\2\2\u0151\u0152\7\60\2\2\u0152\u0153\7\3\2\2\u0153")
        buf.write("\u0154\5\30\r\2\u0154\u0155\7\5\2\2\u0155\u0156\7\6\2")
        buf.write("\2\u0156\u0157\5\b\5\2\u0157\u0158\7\7\2\2\u0158;\3\2")
        buf.write("\2\2\u0159\u015a\5\64\33\2\u015a\u015b\7\b\2\2\u015b\u015c")
        buf.write("\7\66\2\2\u015c\u015d\7\t\2\2\u015d=\3\2\2\2\u015e\u015f")
        buf.write("\t\5\2\2\u015f\u0161\7\21\2\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\7\65\2")
        buf.write("\2\u0163\u0164\7\b\2\2\u0164\u0165\7\66\2\2\u0165\u0166")
        buf.write("\7\t\2\2\u0166?\3\2\2\2\u0167\u0168\5\64\33\2\u0168\u0169")
        buf.write("\7\b\2\2\u0169\u016a\7\t\2\2\u016aA\3\2\2\2(EGPU[bks\u0085")
        buf.write("\u008e\u0094\u009b\u00a8\u00b9\u00c0\u00c4\u00c9\u00cd")
        buf.write("\u00d1\u00d9\u00dc\u00e0\u00e6\u00ec\u00f1\u00f6\u00fe")
        buf.write("\u0107\u0112\u011a\u0121\u0128\u012e\u0138\u013f\u0146")
        buf.write("\u014b\u0160")
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
    RULE_condition = 5
    RULE_constant = 6
    RULE_construct_call = 7
    RULE_construct_def = 8
    RULE_enum = 9
    RULE_enumeration = 10
    RULE_ss_exp = 11
    RULE_s_exp = 12
    RULE_expression = 13
    RULE_factor = 14
    RULE_function_args = 15
    RULE_function_call = 16
    RULE_function_def = 17
    RULE_operand = 18
    RULE_field = 19
    RULE_spec_function = 20
    RULE_specification = 21
    RULE_assignation_def = 22
    RULE_statute = 23
    RULE_term = 24
    RULE_super_type = 25
    RULE_simple_type = 26
    RULE_complex_type = 27
    RULE_while_loop = 28
    RULE_array_def = 29
    RULE_array_var = 30
    RULE_array_arg = 31

    ruleNames =  [ "program", "arguments", "assignation", "block", "class_rule", 
                   "condition", "constant", "construct_call", "construct_def", 
                   "enum", "enumeration", "ss_exp", "s_exp", "expression", 
                   "factor", "function_args", "function_call", "function_def", 
                   "operand", "field", "spec_function", "specification", 
                   "assignation_def", "statute", "term", "super_type", "simple_type", 
                   "complex_type", "while_loop", "array_def", "array_var", 
                   "array_arg" ]

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
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.CLASS]:
                    self.state = 64
                    self.class_rule()
                    pass
                elif token in [MoMParser.ENUMERATE]:
                    self.state = 65
                    self.enumeration()
                    pass
                elif token in [MoMParser.SPEC]:
                    self.state = 66
                    self.specification()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.CLASS) | (1 << MoMParser.ENUMERATE) | (1 << MoMParser.SPEC))) != 0)):
                    break

            self.state = 71
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
            self.state = 73
            self.ss_exp()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 74
                self.match(MoMParser.COMMA)
                self.state = 75
                self.ss_exp()
                self.state = 80
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

        def VARID(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.VARID)
            else:
                return self.getToken(MoMParser.VARID, i)

        def EQUALS(self):
            return self.getToken(MoMParser.EQUALS, 0)

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
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 81
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.VARID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 82
                self.match(MoMParser.PERIOD)


            self.state = 85
            self.match(MoMParser.VARID)
            self.state = 86
            self.match(MoMParser.EQUALS)
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 87
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 88
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

        def statute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.StatuteContext)
            else:
                return self.getTypedRuleContext(MoMParser.StatuteContext,i)


        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.SEMI_COLON)
            else:
                return self.getToken(MoMParser.SEMI_COLON, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 91
                self.statute()
                self.state = 92
                self.match(MoMParser.SEMI_COLON)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def field(self):
            return self.getTypedRuleContext(MoMParser.FieldContext,0)


        def construct_def(self):
            return self.getTypedRuleContext(MoMParser.Construct_defContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def OF_TYPE(self):
            return self.getToken(MoMParser.OF_TYPE, 0)

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
            self.state = 99
            self.match(MoMParser.CLASS)
            self.state = 100
            self.match(MoMParser.CLASSID)
            self.state = 101
            self.match(MoMParser.IS_A)
            self.state = 102
            self.complex_type()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.OF_TYPE:
                self.state = 103
                self.match(MoMParser.OF_TYPE)
                self.state = 104
                self.match(MoMParser.CLASSID)


            self.state = 107
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 108
            self.field()
            self.state = 109
            self.construct_def()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 110
                self.function_def()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 117
            self.match(MoMParser.SEMI_COLON)
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

        def OPEN_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.OPEN_BRACKET)
            else:
                return self.getToken(MoMParser.OPEN_BRACKET, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.BlockContext)
            else:
                return self.getTypedRuleContext(MoMParser.BlockContext,i)


        def CLOSE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.CLOSE_BRACKET)
            else:
                return self.getToken(MoMParser.CLOSE_BRACKET, i)

        def ELSE(self):
            return self.getToken(MoMParser.ELSE, 0)

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
        self.enterRule(localctx, 10, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MoMParser.IF)
            self.state = 120
            self.match(MoMParser.OPEN_PAREN)
            self.state = 121
            self.ss_exp()
            self.state = 122
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 123
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 124
            self.block()
            self.state = 125
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.ELSE:
                self.state = 126
                self.match(MoMParser.ELSE)
                self.state = 127
                self.match(MoMParser.OPEN_BRACKET)
                self.state = 128
                self.block()
                self.state = 129
                self.match(MoMParser.CLOSE_BRACKET)


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
        self.enterRule(localctx, 12, self.RULE_constant)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(MoMParser.INTEGER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(MoMParser.REAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(MoMParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.match(MoMParser.VARID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.array_var()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.match(MoMParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 139
                self.match(MoMParser.FALSE)
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
        self.enterRule(localctx, 14, self.RULE_construct_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(MoMParser.NEW)
            self.state = 143
            self.match(MoMParser.CLASSID)
            self.state = 144
            self.match(MoMParser.OPEN_PAREN)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 145
                self.arguments()


            self.state = 148
            self.match(MoMParser.CLOSE_PAREN)
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

        def block(self):
            return self.getTypedRuleContext(MoMParser.BlockContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

        def SEMI_COLON(self):
            return self.getToken(MoMParser.SEMI_COLON, 0)

        def function_args(self):
            return self.getTypedRuleContext(MoMParser.Function_argsContext,0)


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
        self.enterRule(localctx, 16, self.RULE_construct_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(MoMParser.CLASSID)
            self.state = 151
            self.match(MoMParser.OPEN_PAREN)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 152
                self.function_args()


            self.state = 155
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 156
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 157
            self.block()
            self.state = 158
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 159
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
        self.enterRule(localctx, 18, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MoMParser.CAPITALID)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 162
                self.match(MoMParser.COMMA)
                self.state = 163
                self.match(MoMParser.CAPITALID)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
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
        self.enterRule(localctx, 20, self.RULE_enumeration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MoMParser.ENUMERATE)
            self.state = 172
            self.match(MoMParser.CLASSID)
            self.state = 173
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 174
            self.enum()
            self.state = 175
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 176
            self.match(MoMParser.SEMI_COLON)
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


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.AND)
            else:
                return self.getToken(MoMParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.OR)
            else:
                return self.getToken(MoMParser.OR, i)

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
        self.enterRule(localctx, 22, self.RULE_ss_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.s_exp()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.AND or _la==MoMParser.OR:
                self.state = 179
                _la = self._input.LA(1)
                if not(_la==MoMParser.AND or _la==MoMParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 180
                self.s_exp()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 24, self.RULE_s_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.expression()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.LESS_THAN) | (1 << MoMParser.LESS_EQUAL) | (1 << MoMParser.GREATER_THAN) | (1 << MoMParser.GREATER_EQUAL) | (1 << MoMParser.EQUAL_EQUAL))) != 0):
                self.state = 187
                self.operand()
                self.state = 188
                self.expression()


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

        def function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Function_callContext)
            else:
                return self.getTypedRuleContext(MoMParser.Function_callContext,i)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.TermContext)
            else:
                return self.getTypedRuleContext(MoMParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.PLUS)
            else:
                return self.getToken(MoMParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.MINUS)
            else:
                return self.getToken(MoMParser.MINUS, i)

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
        self.enterRule(localctx, 26, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 192
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 193
                self.term()
                pass


            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.IF))) != 0):
                self.state = 199
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.PLUS]:
                    self.state = 196
                    self.match(MoMParser.PLUS)
                    pass
                elif token in [MoMParser.MINUS]:
                    self.state = 197
                    self.match(MoMParser.MINUS)
                    pass
                elif token in [MoMParser.IF]:
                    self.state = 198
                    self.condition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 203
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 201
                    self.function_call()
                    pass

                elif la_ == 2:
                    self.state = 202
                    self.term()
                    pass


                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ss_exp(self):
            return self.getTypedRuleContext(MoMParser.Ss_expContext,0)


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
        self.enterRule(localctx, 28, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(MoMParser.OPEN_PAREN)
                self.state = 211
                self.ss_exp()
                self.state = 212
                self.match(MoMParser.CLOSE_PAREN)
                pass
            elif token in [MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0):
                    self.state = 214
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 217
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
        self.enterRule(localctx, 30, self.RULE_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 220
                self.super_type()
                pass

            elif la_ == 2:
                self.state = 221
                self.array_arg()
                pass


            self.state = 224
            self.match(MoMParser.VARID)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 225
                self.match(MoMParser.COMMA)
                self.state = 228
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 226
                    self.super_type()
                    pass

                elif la_ == 2:
                    self.state = 227
                    self.array_arg()
                    pass


                self.state = 230
                self.match(MoMParser.VARID)
                self.state = 236
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

        def VARID(self):
            return self.getToken(MoMParser.VARID, 0)

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

        def CLASSID(self):
            return self.getToken(MoMParser.CLASSID, 0)

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
        self.enterRule(localctx, 32, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.THIS or _la==MoMParser.CLASSID:
                self.state = 237
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.CLASSID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
                self.match(MoMParser.PERIOD)


            self.state = 241
            self.match(MoMParser.VARID)
            self.state = 242
            self.match(MoMParser.OPEN_PAREN)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 243
                self.arguments()


            self.state = 246
            self.match(MoMParser.CLOSE_PAREN)
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

        def block(self):
            return self.getTypedRuleContext(MoMParser.BlockContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.SEMI_COLON)
            else:
                return self.getToken(MoMParser.SEMI_COLON, i)

        def function_args(self):
            return self.getTypedRuleContext(MoMParser.Function_argsContext,0)


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
        self.enterRule(localctx, 34, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.simple_type()
            self.state = 249
            self.match(MoMParser.VARID)
            self.state = 250
            self.match(MoMParser.OPEN_PAREN)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 251
                self.function_args()


            self.state = 254
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 255
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 256
            self.block()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.RETURN:
                self.state = 257
                self.match(MoMParser.RETURN)
                self.state = 258
                self.ss_exp()
                self.state = 259
                self.match(MoMParser.SEMI_COLON)


            self.state = 263
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 264
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
        self.enterRule(localctx, 36, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
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

        def FIELD(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.FIELD)
            else:
                return self.getToken(MoMParser.FIELD, i)

        def LESS_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.LESS_THAN)
            else:
                return self.getToken(MoMParser.LESS_THAN, i)

        def GREATER_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.GREATER_THAN)
            else:
                return self.getToken(MoMParser.GREATER_THAN, i)

        def VARID(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.VARID)
            else:
                return self.getToken(MoMParser.VARID, i)

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.SEMI_COLON)
            else:
                return self.getToken(MoMParser.SEMI_COLON, i)

        def super_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Super_typeContext)
            else:
                return self.getTypedRuleContext(MoMParser.Super_typeContext,i)


        def array_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Array_defContext)
            else:
                return self.getTypedRuleContext(MoMParser.Array_defContext,i)


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
        self.enterRule(localctx, 38, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.FIELD:
                self.state = 268
                self.match(MoMParser.FIELD)
                self.state = 269
                self.match(MoMParser.LESS_THAN)
                self.state = 272
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 270
                    self.super_type()
                    pass

                elif la_ == 2:
                    self.state = 271
                    self.array_def()
                    pass


                self.state = 274
                self.match(MoMParser.GREATER_THAN)
                self.state = 275
                self.match(MoMParser.VARID)
                self.state = 276
                self.match(MoMParser.SEMI_COLON)
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def simple_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Simple_typeContext)
            else:
                return self.getTypedRuleContext(MoMParser.Simple_typeContext,i)


        def VARID(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.VARID)
            else:
                return self.getToken(MoMParser.VARID, i)

        def OPEN_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.OPEN_PAREN)
            else:
                return self.getToken(MoMParser.OPEN_PAREN, i)

        def CLOSE_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.CLOSE_PAREN)
            else:
                return self.getToken(MoMParser.CLOSE_PAREN, i)

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.SEMI_COLON)
            else:
                return self.getToken(MoMParser.SEMI_COLON, i)

        def function_args(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.Function_argsContext)
            else:
                return self.getTypedRuleContext(MoMParser.Function_argsContext,i)


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
        self.enterRule(localctx, 40, self.RULE_spec_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 283
                self.simple_type()
                self.state = 284
                self.match(MoMParser.VARID)
                self.state = 285
                self.match(MoMParser.OPEN_PAREN)
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                    self.state = 286
                    self.function_args()


                self.state = 289
                self.match(MoMParser.CLOSE_PAREN)
                self.state = 290
                self.match(MoMParser.SEMI_COLON)
                self.state = 294 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0)):
                    break

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

        def spec_function(self):
            return self.getTypedRuleContext(MoMParser.Spec_functionContext,0)


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
        self.enterRule(localctx, 42, self.RULE_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(MoMParser.SPEC)
            self.state = 297
            self.match(MoMParser.CLASSID)
            self.state = 298
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 299
                self.spec_function()


            self.state = 302
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 303
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
        self.enterRule(localctx, 44, self.RULE_assignation_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.super_type()
            self.state = 306
            self.match(MoMParser.VARID)
            self.state = 307
            self.match(MoMParser.EQUALS)
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 308
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 309
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
        self.enterRule(localctx, 46, self.RULE_statute)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.assignation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.assignation_def()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
                self.while_loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
                self.condition()
                pass


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


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.STAR)
            else:
                return self.getToken(MoMParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.SLASH)
            else:
                return self.getToken(MoMParser.SLASH, i)

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
        self.enterRule(localctx, 48, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.factor()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.STAR or _la==MoMParser.SLASH:
                self.state = 320
                _la = self._input.LA(1)
                if not(_la==MoMParser.STAR or _la==MoMParser.SLASH):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 321
                self.factor()
                self.state = 326
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
        self.enterRule(localctx, 50, self.RULE_super_type)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.INT, MoMParser.TEXT, MoMParser.FLOAT, MoMParser.NOTHING, MoMParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.simple_type()
                pass
            elif token in [MoMParser.COMPONENT, MoMParser.SET, MoMParser.MAP, MoMParser.SIZE, MoMParser.CLASSID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
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
        self.enterRule(localctx, 52, self.RULE_simple_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
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
        self.enterRule(localctx, 54, self.RULE_complex_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
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

    class While_loopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MoMParser.WHILE, 0)

        def OPEN_PAREN(self):
            return self.getToken(MoMParser.OPEN_PAREN, 0)

        def ss_exp(self):
            return self.getTypedRuleContext(MoMParser.Ss_expContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(MoMParser.CLOSE_PAREN, 0)

        def OPEN_BRACKET(self):
            return self.getToken(MoMParser.OPEN_BRACKET, 0)

        def block(self):
            return self.getTypedRuleContext(MoMParser.BlockContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

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
        self.enterRule(localctx, 56, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MoMParser.WHILE)
            self.state = 336
            self.match(MoMParser.OPEN_PAREN)
            self.state = 337
            self.ss_exp()
            self.state = 338
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 339
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 340
            self.block()
            self.state = 341
            self.match(MoMParser.CLOSE_BRACKET)
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
        self.enterRule(localctx, 58, self.RULE_array_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.super_type()
            self.state = 344
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 345
            self.match(MoMParser.INTEGER)
            self.state = 346
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
        self.enterRule(localctx, 60, self.RULE_array_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.THIS or _la==MoMParser.CLASSID:
                self.state = 348
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.CLASSID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 349
                self.match(MoMParser.PERIOD)


            self.state = 352
            self.match(MoMParser.VARID)
            self.state = 353
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 354
            self.match(MoMParser.INTEGER)
            self.state = 355
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
        self.enterRule(localctx, 62, self.RULE_array_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.super_type()
            self.state = 358
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 359
            self.match(MoMParser.CLOSE_SBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





