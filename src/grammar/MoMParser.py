# Generated from src/grammar/MoM.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u01c7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\3\2")
        buf.write("\3\2\6\2^\n\2\r\2\16\2_\3\2\3\2\3\3\3\3\3\3\7\3g\n\3\f")
        buf.write("\3\16\3j\13\3\3\4\3\4\5\4n\n\4\3\4\3\4\3\4\3\4\5\4t\n")
        buf.write("\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\177\n\6\3\6")
        buf.write("\3\6\7\6\u0083\n\6\f\6\16\6\u0086\13\6\3\6\3\6\7\6\u008a")
        buf.write("\n\6\f\6\16\6\u008d\13\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\7\7\u0098\n\7\f\7\16\7\u009b\13\7\3\7\3\7\3\7\3")
        buf.write("\7\7\7\u00a1\n\7\f\7\16\7\u00a4\13\7\3\7\5\7\u00a7\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00b0\n\b\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u00b6\n\t\3\t\3\t\3\n\3\n\3\n\5\n\u00bd\n\n\3")
        buf.write("\n\3\n\3\n\7\n\u00c2\n\n\f\n\16\n\u00c5\13\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\7\13\u00cd\n\13\f\13\16\13\u00d0\13")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00e7")
        buf.write("\n\20\3\20\3\20\3\20\7\20\u00ec\n\20\f\20\16\20\u00ef")
        buf.write("\13\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u00f8\n")
        buf.write("\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u0104\n\26\3\26\3\26\3\26\3\26\3\26\5\26\u010b\n")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u0111\n\26\7\26\u0113\n\26")
        buf.write("\f\26\16\26\u0116\13\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u0123\n\31\3\31\5\31\u0126")
        buf.write("\n\31\3\32\3\32\5\32\u012a\n\32\3\32\3\32\3\32\3\32\5")
        buf.write("\32\u0130\n\32\3\32\3\32\7\32\u0134\n\32\f\32\16\32\u0137")
        buf.write("\13\32\3\33\3\33\5\33\u013b\n\33\3\33\3\33\3\33\5\33\u0140")
        buf.write("\n\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0148\n\34\3")
        buf.write("\34\3\34\3\34\7\34\u014d\n\34\f\34\16\34\u0150\13\34\3")
        buf.write("\34\3\34\3\34\3\34\5\34\u0156\n\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\5\36\u0161\n\36\3\36\3\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\5\37\u016b\n\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \7 \u0174\n \f \16 \u0177\13 \3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3!\5!\u0181\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0188")
        buf.write("\n\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3&\3&\3&\5&\u0196\n&\3")
        buf.write("&\3&\3&\7&\u019b\n&\f&\16&\u019e\13&\3\'\3\'\5\'\u01a2")
        buf.write("\n\'\3(\3(\3)\3)\3*\3*\3*\3*\3*\3*\7*\u01ae\n*\f*\16*")
        buf.write("\u01b1\13*\3*\3*\3+\3+\3+\3+\3+\3,\3,\5,\u01bc\n,\3,\3")
        buf.write(",\3,\3,\3,\3-\3-\3-\3-\3-\2\2.\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("\2\b\4\2\33\33\65\65\4\2\r\16\22\22\4\2\33\33\64\64\3")
        buf.write("\2\24\30\5\2\37!%%,,\5\2\36\36\"$\64\64\2\u01cf\2]\3\2")
        buf.write("\2\2\4c\3\2\2\2\6m\3\2\2\2\bu\3\2\2\2\nx\3\2\2\2\f\u0091")
        buf.write("\3\2\2\2\16\u00af\3\2\2\2\20\u00b1\3\2\2\2\22\u00b9\3")
        buf.write("\2\2\2\24\u00c9\3\2\2\2\26\u00d3\3\2\2\2\30\u00da\3\2")
        buf.write("\2\2\32\u00dc\3\2\2\2\34\u00de\3\2\2\2\36\u00e0\3\2\2")
        buf.write("\2 \u00f0\3\2\2\2\"\u00f2\3\2\2\2$\u00f9\3\2\2\2&\u00fb")
        buf.write("\3\2\2\2(\u00fd\3\2\2\2*\u0103\3\2\2\2,\u0117\3\2\2\2")
        buf.write(".\u0119\3\2\2\2\60\u0125\3\2\2\2\62\u0129\3\2\2\2\64\u013a")
        buf.write("\3\2\2\2\66\u0143\3\2\2\28\u015a\3\2\2\2:\u015c\3\2\2")
        buf.write("\2<\u0166\3\2\2\2>\u016f\3\2\2\2@\u017b\3\2\2\2B\u0187")
        buf.write("\3\2\2\2D\u0189\3\2\2\2F\u018b\3\2\2\2H\u018d\3\2\2\2")
        buf.write("J\u018f\3\2\2\2L\u01a1\3\2\2\2N\u01a3\3\2\2\2P\u01a5\3")
        buf.write("\2\2\2R\u01a7\3\2\2\2T\u01b4\3\2\2\2V\u01bb\3\2\2\2X\u01c2")
        buf.write("\3\2\2\2Z^\5\n\6\2[^\5\26\f\2\\^\5> \2]Z\3\2\2\2][\3\2")
        buf.write("\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2")
        buf.write("\2ab\7\2\2\3b\3\3\2\2\2ch\5\36\20\2de\7\4\2\2eg\5\36\20")
        buf.write("\2fd\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2i\5\3\2\2\2")
        buf.write("jh\3\2\2\2kl\t\2\2\2ln\7\21\2\2mk\3\2\2\2mn\3\2\2\2no")
        buf.write("\3\2\2\2op\7\65\2\2ps\7\17\2\2qt\5\20\t\2rt\5\36\20\2")
        buf.write("sq\3\2\2\2sr\3\2\2\2t\7\3\2\2\2uv\5B\"\2vw\7\n\2\2w\t")
        buf.write("\3\2\2\2xy\7&\2\2yz\7\64\2\2z{\7/\2\2{~\5P)\2|}\7.\2\2")
        buf.write("}\177\7\64\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2")
        buf.write("\2\u0080\u0084\7\6\2\2\u0081\u0083\5:\36\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0087\3\2\2\2\u0086\u0084\3\2\2\2")
        buf.write("\u0087\u008b\5\22\n\2\u0088\u008a\5\66\34\2\u0089\u0088")
        buf.write("\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2")
        buf.write("\u008e\u008f\7\7\2\2\u008f\u0090\7\n\2\2\u0090\13\3\2")
        buf.write("\2\2\u0091\u0092\7\34\2\2\u0092\u0093\7\3\2\2\u0093\u0094")
        buf.write("\5\36\20\2\u0094\u0095\7\5\2\2\u0095\u0099\7\6\2\2\u0096")
        buf.write("\u0098\5\b\5\2\u0097\u0096\3\2\2\2\u0098\u009b\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\3")
        buf.write("\2\2\2\u009b\u0099\3\2\2\2\u009c\u00a6\7\7\2\2\u009d\u009e")
        buf.write("\7\35\2\2\u009e\u00a2\7\6\2\2\u009f\u00a1\5\b\5\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3")
        buf.write("\2\2\2\u00a5\u00a7\7\7\2\2\u00a6\u009d\3\2\2\2\u00a6\u00a7")
        buf.write("\3\2\2\2\u00a7\r\3\2\2\2\u00a8\u00b0\7\66\2\2\u00a9\u00b0")
        buf.write("\7\67\2\2\u00aa\u00b0\79\2\2\u00ab\u00b0\7\65\2\2\u00ac")
        buf.write("\u00b0\5V,\2\u00ad\u00b0\7\61\2\2\u00ae\u00b0\7\62\2\2")
        buf.write("\u00af\u00a8\3\2\2\2\u00af\u00a9\3\2\2\2\u00af\u00aa\3")
        buf.write("\2\2\2\u00af\u00ab\3\2\2\2\u00af\u00ac\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\17\3\2\2\2\u00b1\u00b2")
        buf.write("\7\'\2\2\u00b2\u00b3\7\64\2\2\u00b3\u00b5\7\3\2\2\u00b4")
        buf.write("\u00b6\5\4\3\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00b8\7\5\2\2\u00b8\21\3\2")
        buf.write("\2\2\u00b9\u00ba\7\64\2\2\u00ba\u00bc\7\3\2\2\u00bb\u00bd")
        buf.write("\5\62\32\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00bf\7\5\2\2\u00bf\u00c3\7\6\2\2")
        buf.write("\u00c0\u00c2\5\b\5\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3")
        buf.write("\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\7\7\2\2\u00c7")
        buf.write("\u00c8\7\n\2\2\u00c8\23\3\2\2\2\u00c9\u00ce\7\63\2\2\u00ca")
        buf.write("\u00cb\7\4\2\2\u00cb\u00cd\7\63\2\2\u00cc\u00ca\3\2\2")
        buf.write("\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1")
        buf.write("\u00d2\7\n\2\2\u00d2\25\3\2\2\2\u00d3\u00d4\7(\2\2\u00d4")
        buf.write("\u00d5\7\64\2\2\u00d5\u00d6\7\6\2\2\u00d6\u00d7\5\24\13")
        buf.write("\2\u00d7\u00d8\7\7\2\2\u00d8\u00d9\7\n\2\2\u00d9\27\3")
        buf.write("\2\2\2\u00da\u00db\3\2\2\2\u00db\31\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\33\3\2\2\2\u00de\u00df\3\2\2\2\u00df\35")
        buf.write("\3\2\2\2\u00e0\u00e1\5\"\22\2\u00e1\u00ed\5\30\r\2\u00e2")
        buf.write("\u00e3\7\31\2\2\u00e3\u00e7\5\32\16\2\u00e4\u00e5\7\32")
        buf.write("\2\2\u00e5\u00e7\5\34\17\2\u00e6\u00e2\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\5\"\22\2\u00e9")
        buf.write("\u00ea\5\30\r\2\u00ea\u00ec\3\2\2\2\u00eb\u00e6\3\2\2")
        buf.write("\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee")
        buf.write("\3\2\2\2\u00ee\37\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1!\3\2\2\2\u00f2\u00f7\5*\26\2\u00f3\u00f4")
        buf.write("\58\35\2\u00f4\u00f5\5*\26\2\u00f5\u00f6\5 \21\2\u00f6")
        buf.write("\u00f8\3\2\2\2\u00f7\u00f3\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8#\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa%\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\'\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe")
        buf.write(")\3\2\2\2\u00ff\u0104\5\64\33\2\u0100\u0101\5J&\2\u0101")
        buf.write("\u0102\5$\23\2\u0102\u0104\3\2\2\2\u0103\u00ff\3\2\2\2")
        buf.write("\u0103\u0100\3\2\2\2\u0104\u0114\3\2\2\2\u0105\u0106\7")
        buf.write("\r\2\2\u0106\u010b\5&\24\2\u0107\u0108\7\16\2\2\u0108")
        buf.write("\u010b\5(\25\2\u0109\u010b\5\f\7\2\u010a\u0105\3\2\2\2")
        buf.write("\u010a\u0107\3\2\2\2\u010a\u0109\3\2\2\2\u010b\u0110\3")
        buf.write("\2\2\2\u010c\u0111\5\64\33\2\u010d\u010e\5J&\2\u010e\u010f")
        buf.write("\5$\23\2\u010f\u0111\3\2\2\2\u0110\u010c\3\2\2\2\u0110")
        buf.write("\u010d\3\2\2\2\u0111\u0113\3\2\2\2\u0112\u010a\3\2\2\2")
        buf.write("\u0113\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3")
        buf.write("\2\2\2\u0115+\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118-\3\2\2\2\u0119\u011a\3\2\2\2\u011a/\3\2")
        buf.write("\2\2\u011b\u011c\7\3\2\2\u011c\u011d\5,\27\2\u011d\u011e")
        buf.write("\5\36\20\2\u011e\u011f\5.\30\2\u011f\u0120\7\5\2\2\u0120")
        buf.write("\u0126\3\2\2\2\u0121\u0123\t\3\2\2\u0122\u0121\3\2\2\2")
        buf.write("\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\5")
        buf.write("\16\b\2\u0125\u011b\3\2\2\2\u0125\u0122\3\2\2\2\u0126")
        buf.write("\61\3\2\2\2\u0127\u012a\5L\'\2\u0128\u012a\5X-\2\u0129")
        buf.write("\u0127\3\2\2\2\u0129\u0128\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u0135\7\65\2\2\u012c\u012f\7\4\2\2\u012d\u0130")
        buf.write("\5L\'\2\u012e\u0130\5X-\2\u012f\u012d\3\2\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\7\65\2\2\u0132")
        buf.write("\u0134\3\2\2\2\u0133\u012c\3\2\2\2\u0134\u0137\3\2\2\2")
        buf.write("\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\63\3\2")
        buf.write("\2\2\u0137\u0135\3\2\2\2\u0138\u0139\t\4\2\2\u0139\u013b")
        buf.write("\7\21\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013c\u013d\7\65\2\2\u013d\u013f\7\3\2")
        buf.write("\2\u013e\u0140\5\4\3\2\u013f\u013e\3\2\2\2\u013f\u0140")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\7\5\2\2\u0142")
        buf.write("\65\3\2\2\2\u0143\u0144\5N(\2\u0144\u0145\7\65\2\2\u0145")
        buf.write("\u0147\7\3\2\2\u0146\u0148\5\62\32\2\u0147\u0146\3\2\2")
        buf.write("\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a")
        buf.write("\7\5\2\2\u014a\u014e\7\6\2\2\u014b\u014d\5\b\5\2\u014c")
        buf.write("\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u0155\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0151\u0152\7+\2\2\u0152\u0153\5\36\20\2\u0153")
        buf.write("\u0154\7\n\2\2\u0154\u0156\3\2\2\2\u0155\u0151\3\2\2\2")
        buf.write("\u0155\u0156\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\7")
        buf.write("\7\2\2\u0158\u0159\7\n\2\2\u0159\67\3\2\2\2\u015a\u015b")
        buf.write("\t\5\2\2\u015b9\3\2\2\2\u015c\u015d\7)\2\2\u015d\u0160")
        buf.write("\7\24\2\2\u015e\u0161\5L\'\2\u015f\u0161\5T+\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0163\7\26\2\2\u0163\u0164\7\65\2\2\u0164\u0165\7\n\2")
        buf.write("\2\u0165;\3\2\2\2\u0166\u0167\5N(\2\u0167\u0168\7\65\2")
        buf.write("\2\u0168\u016a\7\3\2\2\u0169\u016b\5\62\32\2\u016a\u0169")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016d\7\5\2\2\u016d\u016e\7\n\2\2\u016e=\3\2\2\2\u016f")
        buf.write("\u0170\7*\2\2\u0170\u0171\7\64\2\2\u0171\u0175\7\6\2\2")
        buf.write("\u0172\u0174\5<\37\2\u0173\u0172\3\2\2\2\u0174\u0177\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179\7\7\2\2\u0179")
        buf.write("\u017a\7\n\2\2\u017a?\3\2\2\2\u017b\u017c\5L\'\2\u017c")
        buf.write("\u017d\7\65\2\2\u017d\u0180\7\17\2\2\u017e\u0181\5\20")
        buf.write("\t\2\u017f\u0181\5\36\20\2\u0180\u017e\3\2\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0181A\3\2\2\2\u0182\u0188\5\64\33\2\u0183\u0188")
        buf.write("\5\6\4\2\u0184\u0188\5@!\2\u0185\u0188\5R*\2\u0186\u0188")
        buf.write("\5\f\7\2\u0187\u0182\3\2\2\2\u0187\u0183\3\2\2\2\u0187")
        buf.write("\u0184\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2")
        buf.write("\u0188C\3\2\2\2\u0189\u018a\3\2\2\2\u018aE\3\2\2\2\u018b")
        buf.write("\u018c\3\2\2\2\u018cG\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("I\3\2\2\2\u018f\u0190\5\60\31\2\u0190\u019c\5D#\2\u0191")
        buf.write("\u0192\7\13\2\2\u0192\u0196\5F$\2\u0193\u0194\7\f\2\2")
        buf.write("\u0194\u0196\5H%\2\u0195\u0191\3\2\2\2\u0195\u0193\3\2")
        buf.write("\2\2\u0196\u0197\3\2\2\2\u0197\u0198\5\60\31\2\u0198\u0199")
        buf.write("\5D#\2\u0199\u019b\3\2\2\2\u019a\u0195\3\2\2\2\u019b\u019e")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("K\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a2\5N(\2\u01a0")
        buf.write("\u01a2\5P)\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("M\3\2\2\2\u01a3\u01a4\t\6\2\2\u01a4O\3\2\2\2\u01a5\u01a6")
        buf.write("\t\7\2\2\u01a6Q\3\2\2\2\u01a7\u01a8\7\60\2\2\u01a8\u01a9")
        buf.write("\7\3\2\2\u01a9\u01aa\5\36\20\2\u01aa\u01ab\7\5\2\2\u01ab")
        buf.write("\u01af\7\6\2\2\u01ac\u01ae\5\b\5\2\u01ad\u01ac\3\2\2\2")
        buf.write("\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3")
        buf.write("\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3")
        buf.write("\7\7\2\2\u01b3S\3\2\2\2\u01b4\u01b5\5L\'\2\u01b5\u01b6")
        buf.write("\7\b\2\2\u01b6\u01b7\7\66\2\2\u01b7\u01b8\7\t\2\2\u01b8")
        buf.write("U\3\2\2\2\u01b9\u01ba\t\4\2\2\u01ba\u01bc\7\21\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01be\7\65\2\2\u01be\u01bf\7\b\2\2\u01bf\u01c0")
        buf.write("\7\66\2\2\u01c0\u01c1\7\t\2\2\u01c1W\3\2\2\2\u01c2\u01c3")
        buf.write("\5L\'\2\u01c3\u01c4\7\b\2\2\u01c4\u01c5\7\t\2\2\u01c5")
        buf.write("Y\3\2\2\2-]_hms~\u0084\u008b\u0099\u00a2\u00a6\u00af\u00b5")
        buf.write("\u00bc\u00c3\u00ce\u00e6\u00ed\u00f7\u0103\u010a\u0110")
        buf.write("\u0114\u0122\u0125\u0129\u012f\u0135\u013a\u013f\u0147")
        buf.write("\u014e\u0155\u0160\u016a\u0175\u0180\u0187\u0195\u019c")
        buf.write("\u01a1\u01af\u01bb")
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
    RULE_exit_sexp = 11
    RULE_and_op = 12
    RULE_or_op = 13
    RULE_ss_exp = 14
    RULE_exit_exp = 15
    RULE_s_exp = 16
    RULE_exit_term = 17
    RULE_plus_op = 18
    RULE_minus_op = 19
    RULE_expression = 20
    RULE_open_paren = 21
    RULE_close_paren = 22
    RULE_factor = 23
    RULE_function_args = 24
    RULE_function_call = 25
    RULE_function_def = 26
    RULE_operand = 27
    RULE_field = 28
    RULE_spec_function = 29
    RULE_specification = 30
    RULE_assignation_def = 31
    RULE_statute = 32
    RULE_exit_factor = 33
    RULE_star_op = 34
    RULE_div_op = 35
    RULE_term = 36
    RULE_super_type = 37
    RULE_simple_type = 38
    RULE_complex_type = 39
    RULE_while_loop = 40
    RULE_array_def = 41
    RULE_array_var = 42
    RULE_array_arg = 43

    ruleNames =  [ "program", "arguments", "assignation", "block", "class_rule", 
                   "condition", "constant", "construct_call", "construct_def", 
                   "enum", "enumeration", "exit_sexp", "and_op", "or_op", 
                   "ss_exp", "exit_exp", "s_exp", "exit_term", "plus_op", 
                   "minus_op", "expression", "open_paren", "close_paren", 
                   "factor", "function_args", "function_call", "function_def", 
                   "operand", "field", "spec_function", "specification", 
                   "assignation_def", "statute", "exit_factor", "star_op", 
                   "div_op", "term", "super_type", "simple_type", "complex_type", 
                   "while_loop", "array_def", "array_var", "array_arg" ]

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
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 91
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.CLASS]:
                    self.state = 88
                    self.class_rule()
                    pass
                elif token in [MoMParser.ENUMERATE]:
                    self.state = 89
                    self.enumeration()
                    pass
                elif token in [MoMParser.SPEC]:
                    self.state = 90
                    self.specification()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.CLASS) | (1 << MoMParser.ENUMERATE) | (1 << MoMParser.SPEC))) != 0)):
                    break

            self.state = 95
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
            self.state = 97
            self.ss_exp()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 98
                self.match(MoMParser.COMMA)
                self.state = 99
                self.ss_exp()
                self.state = 104
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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.VARID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.match(MoMParser.PERIOD)


            self.state = 109
            self.match(MoMParser.VARID)
            self.state = 110
            self.match(MoMParser.EQUALS)
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 111
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 112
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
            self.state = 115
            self.statute()
            self.state = 116
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
            self.state = 118
            self.match(MoMParser.CLASS)
            self.state = 119
            self.match(MoMParser.CLASSID)
            self.state = 120
            self.match(MoMParser.IS_A)
            self.state = 121
            self.complex_type()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.OF_TYPE:
                self.state = 122
                self.match(MoMParser.OF_TYPE)
                self.state = 123
                self.match(MoMParser.CLASSID)


            self.state = 126
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.FIELD:
                self.state = 127
                self.field()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.construct_def()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 134
                self.function_def()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 141
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

        def CLOSE_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MoMParser.CLOSE_BRACKET)
            else:
                return self.getToken(MoMParser.CLOSE_BRACKET, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MoMParser.BlockContext)
            else:
                return self.getTypedRuleContext(MoMParser.BlockContext,i)


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
            self.state = 143
            self.match(MoMParser.IF)
            self.state = 144
            self.match(MoMParser.OPEN_PAREN)
            self.state = 145
            self.ss_exp()
            self.state = 146
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 147
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 148
                self.block()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.ELSE:
                self.state = 155
                self.match(MoMParser.ELSE)
                self.state = 156
                self.match(MoMParser.OPEN_BRACKET)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                    self.state = 157
                    self.block()
                    self.state = 162
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 163
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
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(MoMParser.INTEGER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(MoMParser.REAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.match(MoMParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                self.match(MoMParser.VARID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 170
                self.array_var()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 171
                self.match(MoMParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 172
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
            self.state = 175
            self.match(MoMParser.NEW)
            self.state = 176
            self.match(MoMParser.CLASSID)
            self.state = 177
            self.match(MoMParser.OPEN_PAREN)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 178
                self.arguments()


            self.state = 181
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

        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

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
        self.enterRule(localctx, 16, self.RULE_construct_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MoMParser.CLASSID)
            self.state = 184
            self.match(MoMParser.OPEN_PAREN)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 185
                self.function_args()


            self.state = 188
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 189
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 190
                self.block()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 196
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 197
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
            self.state = 199
            self.match(MoMParser.CAPITALID)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 200
                self.match(MoMParser.COMMA)
                self.state = 201
                self.match(MoMParser.CAPITALID)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
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
            self.state = 209
            self.match(MoMParser.ENUMERATE)
            self.state = 210
            self.match(MoMParser.CLASSID)
            self.state = 211
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 212
            self.enum()
            self.state = 213
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 214
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
        self.enterRule(localctx, 22, self.RULE_exit_sexp)
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
        self.enterRule(localctx, 24, self.RULE_and_op)
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
        self.enterRule(localctx, 26, self.RULE_or_op)
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
        self.enterRule(localctx, 28, self.RULE_ss_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.s_exp()
            self.state = 223
            self.exit_sexp()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.AND or _la==MoMParser.OR:
                self.state = 228
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.AND]:
                    self.state = 224
                    self.match(MoMParser.AND)
                    self.state = 225
                    self.and_op()
                    pass
                elif token in [MoMParser.OR]:
                    self.state = 226
                    self.match(MoMParser.OR)
                    self.state = 227
                    self.or_op()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 230
                self.s_exp()
                self.state = 231
                self.exit_sexp()
                self.state = 237
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
        self.enterRule(localctx, 30, self.RULE_exit_exp)
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
        self.enterRule(localctx, 32, self.RULE_s_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.expression()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.LESS_THAN) | (1 << MoMParser.LESS_EQUAL) | (1 << MoMParser.GREATER_THAN) | (1 << MoMParser.GREATER_EQUAL) | (1 << MoMParser.EQUAL_EQUAL))) != 0):
                self.state = 241
                self.operand()
                self.state = 242
                self.expression()
                self.state = 243
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
        self.enterRule(localctx, 34, self.RULE_exit_term)
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
        self.enterRule(localctx, 36, self.RULE_plus_op)
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
        self.enterRule(localctx, 38, self.RULE_minus_op)
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
        self.enterRule(localctx, 40, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 253
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 254
                self.term()
                self.state = 255
                self.exit_term()
                pass


            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.IF))) != 0):
                self.state = 264
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.PLUS]:
                    self.state = 259
                    self.match(MoMParser.PLUS)
                    self.state = 260
                    self.plus_op()
                    pass
                elif token in [MoMParser.MINUS]:
                    self.state = 261
                    self.match(MoMParser.MINUS)
                    self.state = 262
                    self.minus_op()
                    pass
                elif token in [MoMParser.IF]:
                    self.state = 263
                    self.condition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 270
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 266
                    self.function_call()
                    pass

                elif la_ == 2:
                    self.state = 267
                    self.term()
                    self.state = 268
                    self.exit_term()
                    pass


                self.state = 276
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
        self.enterRule(localctx, 42, self.RULE_open_paren)
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
        self.enterRule(localctx, 44, self.RULE_close_paren)
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
        self.enterRule(localctx, 46, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(MoMParser.OPEN_PAREN)
                self.state = 282
                self.open_paren()
                self.state = 283
                self.ss_exp()
                self.state = 284
                self.close_paren()
                self.state = 285
                self.match(MoMParser.CLOSE_PAREN)
                pass
            elif token in [MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0):
                    self.state = 287
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 290
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
        self.enterRule(localctx, 48, self.RULE_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 293
                self.super_type()
                pass

            elif la_ == 2:
                self.state = 294
                self.array_arg()
                pass


            self.state = 297
            self.match(MoMParser.VARID)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 298
                self.match(MoMParser.COMMA)
                self.state = 301
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 299
                    self.super_type()
                    pass

                elif la_ == 2:
                    self.state = 300
                    self.array_arg()
                    pass


                self.state = 303
                self.match(MoMParser.VARID)
                self.state = 309
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
        self.enterRule(localctx, 50, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.THIS or _la==MoMParser.CLASSID:
                self.state = 310
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.CLASSID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 311
                self.match(MoMParser.PERIOD)


            self.state = 314
            self.match(MoMParser.VARID)
            self.state = 315
            self.match(MoMParser.OPEN_PAREN)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 316
                self.arguments()


            self.state = 319
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

        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

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
        self.enterRule(localctx, 52, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.simple_type()
            self.state = 322
            self.match(MoMParser.VARID)
            self.state = 323
            self.match(MoMParser.OPEN_PAREN)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 324
                self.function_args()


            self.state = 327
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 328
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 329
                self.block()
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.RETURN:
                self.state = 335
                self.match(MoMParser.RETURN)
                self.state = 336
                self.ss_exp()
                self.state = 337
                self.match(MoMParser.SEMI_COLON)


            self.state = 341
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 342
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
        self.enterRule(localctx, 54, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
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
        self.enterRule(localctx, 56, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(MoMParser.FIELD)
            self.state = 347
            self.match(MoMParser.LESS_THAN)
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 348
                self.super_type()
                pass

            elif la_ == 2:
                self.state = 349
                self.array_def()
                pass


            self.state = 352
            self.match(MoMParser.GREATER_THAN)
            self.state = 353
            self.match(MoMParser.VARID)
            self.state = 354
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
        self.enterRule(localctx, 58, self.RULE_spec_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.simple_type()
            self.state = 357
            self.match(MoMParser.VARID)
            self.state = 358
            self.match(MoMParser.OPEN_PAREN)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 359
                self.function_args()


            self.state = 362
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 363
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
        self.enterRule(localctx, 60, self.RULE_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MoMParser.SPEC)
            self.state = 366
            self.match(MoMParser.CLASSID)
            self.state = 367
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 368
                self.spec_function()
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 374
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 375
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
        self.enterRule(localctx, 62, self.RULE_assignation_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.super_type()
            self.state = 378
            self.match(MoMParser.VARID)
            self.state = 379
            self.match(MoMParser.EQUALS)
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 380
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 381
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
        self.enterRule(localctx, 64, self.RULE_statute)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.assignation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.assignation_def()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.while_loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 388
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
        self.enterRule(localctx, 66, self.RULE_exit_factor)
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
        self.enterRule(localctx, 68, self.RULE_star_op)
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
        self.enterRule(localctx, 70, self.RULE_div_op)
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
        self.enterRule(localctx, 72, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.factor()
            self.state = 398
            self.exit_factor()
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.STAR or _la==MoMParser.SLASH:
                self.state = 403
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.STAR]:
                    self.state = 399
                    self.match(MoMParser.STAR)
                    self.state = 400
                    self.star_op()
                    pass
                elif token in [MoMParser.SLASH]:
                    self.state = 401
                    self.match(MoMParser.SLASH)
                    self.state = 402
                    self.div_op()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 405
                self.factor()
                self.state = 406
                self.exit_factor()
                self.state = 412
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
        self.enterRule(localctx, 74, self.RULE_super_type)
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.INT, MoMParser.TEXT, MoMParser.FLOAT, MoMParser.NOTHING, MoMParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.simple_type()
                pass
            elif token in [MoMParser.COMPONENT, MoMParser.SET, MoMParser.MAP, MoMParser.SIZE, MoMParser.CLASSID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
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
        self.enterRule(localctx, 76, self.RULE_simple_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
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
        self.enterRule(localctx, 78, self.RULE_complex_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
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

        def CLOSE_BRACKET(self):
            return self.getToken(MoMParser.CLOSE_BRACKET, 0)

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
        self.enterRule(localctx, 80, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MoMParser.WHILE)
            self.state = 422
            self.match(MoMParser.OPEN_PAREN)
            self.state = 423
            self.ss_exp()
            self.state = 424
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 425
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 426
                self.block()
                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 432
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
        self.enterRule(localctx, 82, self.RULE_array_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.super_type()
            self.state = 435
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 436
            self.match(MoMParser.INTEGER)
            self.state = 437
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
        self.enterRule(localctx, 84, self.RULE_array_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.THIS or _la==MoMParser.CLASSID:
                self.state = 439
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.CLASSID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 440
                self.match(MoMParser.PERIOD)


            self.state = 443
            self.match(MoMParser.VARID)
            self.state = 444
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 445
            self.match(MoMParser.INTEGER)
            self.state = 446
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
        self.enterRule(localctx, 86, self.RULE_array_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.super_type()
            self.state = 449
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 450
            self.match(MoMParser.CLOSE_SBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





