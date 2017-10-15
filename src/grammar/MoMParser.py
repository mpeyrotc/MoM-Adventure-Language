# Generated from src/grammar/MoM.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u01db\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\3\2\3\2\6\2d\n\2\r\2\16\2e\3\2\3\2")
        buf.write("\3\3\3\3\3\3\7\3m\n\3\f\3\16\3p\13\3\3\4\3\4\5\4t\n\4")
        buf.write("\3\4\3\4\5\4x\n\4\3\4\3\4\3\4\5\4}\n\4\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6\u0088\n\6\3\6\3\6\7\6\u008c\n")
        buf.write("\6\f\6\16\6\u008f\13\6\3\6\3\6\7\6\u0093\n\6\f\6\16\6")
        buf.write("\u0096\13\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\7\n\u00a8\n\n\f\n\16\n\u00ab\13")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\7\n\u00b2\n\n\f\n\16\n\u00b5\13")
        buf.write("\n\3\n\3\n\5\n\u00b9\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00c4\n\13\3\f\3\f\3\f\3\f\5\f\u00ca")
        buf.write("\n\f\3\f\3\f\3\r\3\r\3\r\5\r\u00d1\n\r\3\r\3\r\3\r\7\r")
        buf.write("\u00d6\n\r\f\r\16\r\u00d9\13\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\7\16\u00e1\n\16\f\16\16\16\u00e4\13\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00fb\n")
        buf.write("\23\3\23\3\23\3\23\7\23\u0100\n\23\f\23\16\23\u0103\13")
        buf.write("\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u010c\n\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u0118\n\31\3\31\3\31\3\31\3\31\3\31\5\31\u011f\n\31\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u0125\n\31\7\31\u0127\n\31\f\31")
        buf.write("\16\31\u012a\13\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u0137\n\34\3\34\5\34\u013a\n")
        buf.write("\34\3\35\3\35\5\35\u013e\n\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0144\n\35\3\35\3\35\7\35\u0148\n\35\f\35\16\35\u014b")
        buf.write("\13\35\3\36\3\36\5\36\u014f\n\36\3\36\3\36\3\36\5\36\u0154")
        buf.write("\n\36\3\36\3\36\3\37\3\37\3\37\3\37\5\37\u015c\n\37\3")
        buf.write("\37\3\37\3\37\7\37\u0161\n\37\f\37\16\37\u0164\13\37\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u016a\n\37\3\37\3\37\3\37\3 \3")
        buf.write(" \3!\3!\3!\3!\5!\u0175\n!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\5\"\u017f\n\"\3\"\3\"\3\"\3#\3#\3#\3#\7#\u0188\n#\f#")
        buf.write("\16#\u018b\13#\3#\3#\3#\3$\3$\3$\3$\3$\5$\u0195\n$\3%")
        buf.write("\3%\3%\3%\3%\5%\u019c\n%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)")
        buf.write("\3)\3)\3)\5)\u01aa\n)\3)\3)\3)\7)\u01af\n)\f)\16)\u01b2")
        buf.write("\13)\3*\3*\5*\u01b6\n*\3+\3+\3,\3,\3-\3-\3-\3-\3-\3-\7")
        buf.write("-\u01c2\n-\f-\16-\u01c5\13-\3-\3-\3.\3.\3.\3.\3.\3/\3")
        buf.write("/\5/\u01d0\n/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\2\2\61\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^\2\b\4\2\33\33\65\65")
        buf.write("\4\2\r\16\22\22\4\2\33\33\64\64\3\2\24\30\5\2\37!%%,,")
        buf.write("\5\2\36\36\"$\64\64\2\u01e1\2c\3\2\2\2\4i\3\2\2\2\6s\3")
        buf.write("\2\2\2\b~\3\2\2\2\n\u0081\3\2\2\2\f\u009a\3\2\2\2\16\u009c")
        buf.write("\3\2\2\2\20\u009e\3\2\2\2\22\u00a0\3\2\2\2\24\u00c3\3")
        buf.write("\2\2\2\26\u00c5\3\2\2\2\30\u00cd\3\2\2\2\32\u00dd\3\2")
        buf.write("\2\2\34\u00e7\3\2\2\2\36\u00ee\3\2\2\2 \u00f0\3\2\2\2")
        buf.write("\"\u00f2\3\2\2\2$\u00f4\3\2\2\2&\u0104\3\2\2\2(\u0106")
        buf.write("\3\2\2\2*\u010d\3\2\2\2,\u010f\3\2\2\2.\u0111\3\2\2\2")
        buf.write("\60\u0117\3\2\2\2\62\u012b\3\2\2\2\64\u012d\3\2\2\2\66")
        buf.write("\u0139\3\2\2\28\u013d\3\2\2\2:\u014e\3\2\2\2<\u0157\3")
        buf.write("\2\2\2>\u016e\3\2\2\2@\u0170\3\2\2\2B\u017a\3\2\2\2D\u0183")
        buf.write("\3\2\2\2F\u018f\3\2\2\2H\u019b\3\2\2\2J\u019d\3\2\2\2")
        buf.write("L\u019f\3\2\2\2N\u01a1\3\2\2\2P\u01a3\3\2\2\2R\u01b5\3")
        buf.write("\2\2\2T\u01b7\3\2\2\2V\u01b9\3\2\2\2X\u01bb\3\2\2\2Z\u01c8")
        buf.write("\3\2\2\2\\\u01cf\3\2\2\2^\u01d6\3\2\2\2`d\5\n\6\2ad\5")
        buf.write("\34\17\2bd\5D#\2c`\3\2\2\2ca\3\2\2\2cb\3\2\2\2de\3\2\2")
        buf.write("\2ec\3\2\2\2ef\3\2\2\2fg\3\2\2\2gh\7\2\2\3h\3\3\2\2\2")
        buf.write("in\5$\23\2jk\7\4\2\2km\5$\23\2lj\3\2\2\2mp\3\2\2\2nl\3")
        buf.write("\2\2\2no\3\2\2\2o\5\3\2\2\2pn\3\2\2\2qr\t\2\2\2rt\7\21")
        buf.write("\2\2sq\3\2\2\2st\3\2\2\2tw\3\2\2\2ux\7\65\2\2vx\5\\/\2")
        buf.write("wu\3\2\2\2wv\3\2\2\2xy\3\2\2\2y|\7\17\2\2z}\5\26\f\2{")
        buf.write("}\5$\23\2|z\3\2\2\2|{\3\2\2\2}\7\3\2\2\2~\177\5H%\2\177")
        buf.write("\u0080\7\n\2\2\u0080\t\3\2\2\2\u0081\u0082\7&\2\2\u0082")
        buf.write("\u0083\7\64\2\2\u0083\u0084\7/\2\2\u0084\u0087\5V,\2\u0085")
        buf.write("\u0086\7.\2\2\u0086\u0088\7\64\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008d\7")
        buf.write("\6\2\2\u008a\u008c\5@!\2\u008b\u008a\3\2\2\2\u008c\u008f")
        buf.write("\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0094\5\30\r")
        buf.write("\2\u0091\u0093\5<\37\2\u0092\u0091\3\2\2\2\u0093\u0096")
        buf.write("\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0097\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\7\7\2\2")
        buf.write("\u0098\u0099\7\n\2\2\u0099\13\3\2\2\2\u009a\u009b\3\2")
        buf.write("\2\2\u009b\r\3\2\2\2\u009c\u009d\3\2\2\2\u009d\17\3\2")
        buf.write("\2\2\u009e\u009f\3\2\2\2\u009f\21\3\2\2\2\u00a0\u00a1")
        buf.write("\7\34\2\2\u00a1\u00a2\7\3\2\2\u00a2\u00a3\5$\23\2\u00a3")
        buf.write("\u00a4\7\5\2\2\u00a4\u00a5\5\f\7\2\u00a5\u00a9\7\6\2\2")
        buf.write("\u00a6\u00a8\5\b\5\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3")
        buf.write("\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac")
        buf.write("\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00b8\7\7\2\2\u00ad")
        buf.write("\u00ae\7\35\2\2\u00ae\u00af\5\20\t\2\u00af\u00b3\7\6\2")
        buf.write("\2\u00b0\u00b2\5\b\5\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5")
        buf.write("\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\7\7\2\2")
        buf.write("\u00b7\u00b9\3\2\2\2\u00b8\u00ad\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\5\16\b\2\u00bb")
        buf.write("\23\3\2\2\2\u00bc\u00c4\7\66\2\2\u00bd\u00c4\7\67\2\2")
        buf.write("\u00be\u00c4\79\2\2\u00bf\u00c4\7\65\2\2\u00c0\u00c4\5")
        buf.write("\\/\2\u00c1\u00c4\7\61\2\2\u00c2\u00c4\7\62\2\2\u00c3")
        buf.write("\u00bc\3\2\2\2\u00c3\u00bd\3\2\2\2\u00c3\u00be\3\2\2\2")
        buf.write("\u00c3\u00bf\3\2\2\2\u00c3\u00c0\3\2\2\2\u00c3\u00c1\3")
        buf.write("\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\25\3\2\2\2\u00c5\u00c6")
        buf.write("\7\'\2\2\u00c6\u00c7\7\64\2\2\u00c7\u00c9\7\3\2\2\u00c8")
        buf.write("\u00ca\5\4\3\2\u00c9\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\u00cc\7\5\2\2\u00cc\27\3\2")
        buf.write("\2\2\u00cd\u00ce\7\64\2\2\u00ce\u00d0\7\3\2\2\u00cf\u00d1")
        buf.write("\58\35\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\u00d3\7\5\2\2\u00d3\u00d7\7\6\2\2")
        buf.write("\u00d4\u00d6\5\b\5\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3")
        buf.write("\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db\7\7\2\2\u00db")
        buf.write("\u00dc\7\n\2\2\u00dc\31\3\2\2\2\u00dd\u00e2\7\63\2\2\u00de")
        buf.write("\u00df\7\4\2\2\u00df\u00e1\7\63\2\2\u00e0\u00de\3\2\2")
        buf.write("\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5")
        buf.write("\u00e6\7\n\2\2\u00e6\33\3\2\2\2\u00e7\u00e8\7(\2\2\u00e8")
        buf.write("\u00e9\7\64\2\2\u00e9\u00ea\7\6\2\2\u00ea\u00eb\5\32\16")
        buf.write("\2\u00eb\u00ec\7\7\2\2\u00ec\u00ed\7\n\2\2\u00ed\35\3")
        buf.write("\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\37\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1!\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3#\3\2")
        buf.write("\2\2\u00f4\u00f5\5(\25\2\u00f5\u0101\5\36\20\2\u00f6\u00f7")
        buf.write("\7\31\2\2\u00f7\u00fb\5 \21\2\u00f8\u00f9\7\32\2\2\u00f9")
        buf.write("\u00fb\5\"\22\2\u00fa\u00f6\3\2\2\2\u00fa\u00f8\3\2\2")
        buf.write("\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\5(\25\2\u00fd\u00fe")
        buf.write("\5\36\20\2\u00fe\u0100\3\2\2\2\u00ff\u00fa\3\2\2\2\u0100")
        buf.write("\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102%\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105\3\2\2")
        buf.write("\2\u0105\'\3\2\2\2\u0106\u010b\5\60\31\2\u0107\u0108\5")
        buf.write("> \2\u0108\u0109\5\60\31\2\u0109\u010a\5&\24\2\u010a\u010c")
        buf.write("\3\2\2\2\u010b\u0107\3\2\2\2\u010b\u010c\3\2\2\2\u010c")
        buf.write(")\3\2\2\2\u010d\u010e\3\2\2\2\u010e+\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110-\3\2\2\2\u0111\u0112\3\2\2\2\u0112/\3\2")
        buf.write("\2\2\u0113\u0118\5:\36\2\u0114\u0115\5P)\2\u0115\u0116")
        buf.write("\5*\26\2\u0116\u0118\3\2\2\2\u0117\u0113\3\2\2\2\u0117")
        buf.write("\u0114\3\2\2\2\u0118\u0128\3\2\2\2\u0119\u011a\7\r\2\2")
        buf.write("\u011a\u011f\5,\27\2\u011b\u011c\7\16\2\2\u011c\u011f")
        buf.write("\5.\30\2\u011d\u011f\5\22\n\2\u011e\u0119\3\2\2\2\u011e")
        buf.write("\u011b\3\2\2\2\u011e\u011d\3\2\2\2\u011f\u0124\3\2\2\2")
        buf.write("\u0120\u0125\5:\36\2\u0121\u0122\5P)\2\u0122\u0123\5*")
        buf.write("\26\2\u0123\u0125\3\2\2\2\u0124\u0120\3\2\2\2\u0124\u0121")
        buf.write("\3\2\2\2\u0125\u0127\3\2\2\2\u0126\u011e\3\2\2\2\u0127")
        buf.write("\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129\61\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\3\2")
        buf.write("\2\2\u012c\63\3\2\2\2\u012d\u012e\3\2\2\2\u012e\65\3\2")
        buf.write("\2\2\u012f\u0130\7\3\2\2\u0130\u0131\5\62\32\2\u0131\u0132")
        buf.write("\5$\23\2\u0132\u0133\5\64\33\2\u0133\u0134\7\5\2\2\u0134")
        buf.write("\u013a\3\2\2\2\u0135\u0137\t\3\2\2\u0136\u0135\3\2\2\2")
        buf.write("\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\5")
        buf.write("\24\13\2\u0139\u012f\3\2\2\2\u0139\u0136\3\2\2\2\u013a")
        buf.write("\67\3\2\2\2\u013b\u013e\5R*\2\u013c\u013e\5^\60\2\u013d")
        buf.write("\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013e\u013f\3\2\2\2")
        buf.write("\u013f\u0149\7\65\2\2\u0140\u0143\7\4\2\2\u0141\u0144")
        buf.write("\5R*\2\u0142\u0144\5^\60\2\u0143\u0141\3\2\2\2\u0143\u0142")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\7\65\2\2\u0146")
        buf.write("\u0148\3\2\2\2\u0147\u0140\3\2\2\2\u0148\u014b\3\2\2\2")
        buf.write("\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a9\3\2\2")
        buf.write("\2\u014b\u0149\3\2\2\2\u014c\u014d\t\4\2\2\u014d\u014f")
        buf.write("\7\21\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0151\7\65\2\2\u0151\u0153\7\3\2")
        buf.write("\2\u0152\u0154\5\4\3\2\u0153\u0152\3\2\2\2\u0153\u0154")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\7\5\2\2\u0156")
        buf.write(";\3\2\2\2\u0157\u0158\5T+\2\u0158\u0159\7\65\2\2\u0159")
        buf.write("\u015b\7\3\2\2\u015a\u015c\58\35\2\u015b\u015a\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\7")
        buf.write("\5\2\2\u015e\u0162\7\6\2\2\u015f\u0161\5\b\5\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0169\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0165\u0166\7+\2\2\u0166\u0167\5$\23\2\u0167\u0168\7")
        buf.write("\n\2\2\u0168\u016a\3\2\2\2\u0169\u0165\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\7\7\2\2\u016c")
        buf.write("\u016d\7\n\2\2\u016d=\3\2\2\2\u016e\u016f\t\5\2\2\u016f")
        buf.write("?\3\2\2\2\u0170\u0171\7)\2\2\u0171\u0174\7\24\2\2\u0172")
        buf.write("\u0175\5R*\2\u0173\u0175\5Z.\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\7\26\2")
        buf.write("\2\u0177\u0178\7\65\2\2\u0178\u0179\7\n\2\2\u0179A\3\2")
        buf.write("\2\2\u017a\u017b\5T+\2\u017b\u017c\7\65\2\2\u017c\u017e")
        buf.write("\7\3\2\2\u017d\u017f\58\35\2\u017e\u017d\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\7\5\2\2")
        buf.write("\u0181\u0182\7\n\2\2\u0182C\3\2\2\2\u0183\u0184\7*\2\2")
        buf.write("\u0184\u0185\7\64\2\2\u0185\u0189\7\6\2\2\u0186\u0188")
        buf.write("\5B\"\2\u0187\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018c\u018d\7\7\2\2\u018d\u018e\7")
        buf.write("\n\2\2\u018eE\3\2\2\2\u018f\u0190\5R*\2\u0190\u0191\7")
        buf.write("\65\2\2\u0191\u0194\7\17\2\2\u0192\u0195\5\26\f\2\u0193")
        buf.write("\u0195\5$\23\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195G\3\2\2\2\u0196\u019c\5:\36\2\u0197\u019c\5\6\4")
        buf.write("\2\u0198\u019c\5F$\2\u0199\u019c\5X-\2\u019a\u019c\5\22")
        buf.write("\n\2\u019b\u0196\3\2\2\2\u019b\u0197\3\2\2\2\u019b\u0198")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("I\3\2\2\2\u019d\u019e\3\2\2\2\u019eK\3\2\2\2\u019f\u01a0")
        buf.write("\3\2\2\2\u01a0M\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2O\3\2")
        buf.write("\2\2\u01a3\u01a4\5\66\34\2\u01a4\u01b0\5J&\2\u01a5\u01a6")
        buf.write("\7\13\2\2\u01a6\u01aa\5L\'\2\u01a7\u01a8\7\f\2\2\u01a8")
        buf.write("\u01aa\5N(\2\u01a9\u01a5\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ac\5\66\34\2\u01ac\u01ad\5J&\2")
        buf.write("\u01ad\u01af\3\2\2\2\u01ae\u01a9\3\2\2\2\u01af\u01b2\3")
        buf.write("\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1Q")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b6\5T+\2\u01b4\u01b6")
        buf.write("\5V,\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6S")
        buf.write("\3\2\2\2\u01b7\u01b8\t\6\2\2\u01b8U\3\2\2\2\u01b9\u01ba")
        buf.write("\t\7\2\2\u01baW\3\2\2\2\u01bb\u01bc\7\60\2\2\u01bc\u01bd")
        buf.write("\7\3\2\2\u01bd\u01be\5$\23\2\u01be\u01bf\7\5\2\2\u01bf")
        buf.write("\u01c3\7\6\2\2\u01c0\u01c2\5\b\5\2\u01c1\u01c0\3\2\2\2")
        buf.write("\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7")
        buf.write("\7\7\2\2\u01c7Y\3\2\2\2\u01c8\u01c9\5R*\2\u01c9\u01ca")
        buf.write("\7\b\2\2\u01ca\u01cb\7\66\2\2\u01cb\u01cc\7\t\2\2\u01cc")
        buf.write("[\3\2\2\2\u01cd\u01ce\t\4\2\2\u01ce\u01d0\7\21\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d2\7\65\2\2\u01d2\u01d3\7\b\2\2\u01d3\u01d4")
        buf.write("\7\66\2\2\u01d4\u01d5\7\t\2\2\u01d5]\3\2\2\2\u01d6\u01d7")
        buf.write("\5R*\2\u01d7\u01d8\7\b\2\2\u01d8\u01d9\7\t\2\2\u01d9_")
        buf.write("\3\2\2\2.censw|\u0087\u008d\u0094\u00a9\u00b3\u00b8\u00c3")
        buf.write("\u00c9\u00d0\u00d7\u00e2\u00fa\u0101\u010b\u0117\u011e")
        buf.write("\u0124\u0128\u0136\u0139\u013d\u0143\u0149\u014e\u0153")
        buf.write("\u015b\u0162\u0169\u0174\u017e\u0189\u0194\u019b\u01a9")
        buf.write("\u01b0\u01b5\u01c3\u01cf")
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
    RULE_construct_def = 11
    RULE_enum = 12
    RULE_enumeration = 13
    RULE_exit_sexp = 14
    RULE_and_op = 15
    RULE_or_op = 16
    RULE_ss_exp = 17
    RULE_exit_exp = 18
    RULE_s_exp = 19
    RULE_exit_term = 20
    RULE_plus_op = 21
    RULE_minus_op = 22
    RULE_expression = 23
    RULE_open_paren = 24
    RULE_close_paren = 25
    RULE_factor = 26
    RULE_function_args = 27
    RULE_function_call = 28
    RULE_function_def = 29
    RULE_operand = 30
    RULE_field = 31
    RULE_spec_function = 32
    RULE_specification = 33
    RULE_assignation_def = 34
    RULE_statute = 35
    RULE_exit_factor = 36
    RULE_star_op = 37
    RULE_div_op = 38
    RULE_term = 39
    RULE_super_type = 40
    RULE_simple_type = 41
    RULE_complex_type = 42
    RULE_while_loop = 43
    RULE_array_def = 44
    RULE_array_var = 45
    RULE_array_arg = 46

    ruleNames =  [ "program", "arguments", "assignation", "block", "class_rule", 
                   "exit_if_check", "condition_end", "enter_else", "condition", 
                   "constant", "construct_call", "construct_def", "enum", 
                   "enumeration", "exit_sexp", "and_op", "or_op", "ss_exp", 
                   "exit_exp", "s_exp", "exit_term", "plus_op", "minus_op", 
                   "expression", "open_paren", "close_paren", "factor", 
                   "function_args", "function_call", "function_def", "operand", 
                   "field", "spec_function", "specification", "assignation_def", 
                   "statute", "exit_factor", "star_op", "div_op", "term", 
                   "super_type", "simple_type", "complex_type", "while_loop", 
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
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.CLASS]:
                    self.state = 94
                    self.class_rule()
                    pass
                elif token in [MoMParser.ENUMERATE]:
                    self.state = 95
                    self.enumeration()
                    pass
                elif token in [MoMParser.SPEC]:
                    self.state = 96
                    self.specification()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.CLASS) | (1 << MoMParser.ENUMERATE) | (1 << MoMParser.SPEC))) != 0)):
                    break

            self.state = 101
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
            self.state = 103
            self.ss_exp()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 104
                self.match(MoMParser.COMMA)
                self.state = 105
                self.ss_exp()
                self.state = 110
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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 111
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.VARID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 112
                self.match(MoMParser.PERIOD)


            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 115
                self.match(MoMParser.VARID)
                pass

            elif la_ == 2:
                self.state = 116
                self.array_var()
                pass


            self.state = 119
            self.match(MoMParser.EQUALS)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 120
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 121
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
            self.state = 124
            self.statute()
            self.state = 125
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
            self.state = 127
            self.match(MoMParser.CLASS)
            self.state = 128
            self.match(MoMParser.CLASSID)
            self.state = 129
            self.match(MoMParser.IS_A)
            self.state = 130
            self.complex_type()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.OF_TYPE:
                self.state = 131
                self.match(MoMParser.OF_TYPE)
                self.state = 132
                self.match(MoMParser.CLASSID)


            self.state = 135
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.FIELD:
                self.state = 136
                self.field()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.construct_def()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 143
                self.function_def()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 150
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
            self.state = 158
            self.match(MoMParser.IF)
            self.state = 159
            self.match(MoMParser.OPEN_PAREN)
            self.state = 160
            self.ss_exp()
            self.state = 161
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 162
            self.exit_if_check()
            self.state = 163
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 164
                self.block()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.ELSE:
                self.state = 171
                self.match(MoMParser.ELSE)
                self.state = 172
                self.enter_else()
                self.state = 173
                self.match(MoMParser.OPEN_BRACKET)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                    self.state = 174
                    self.block()
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 180
                self.match(MoMParser.CLOSE_BRACKET)


            self.state = 184
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
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(MoMParser.INTEGER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(MoMParser.REAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.match(MoMParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.match(MoMParser.VARID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.array_var()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 191
                self.match(MoMParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 192
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
        self.enterRule(localctx, 20, self.RULE_construct_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MoMParser.NEW)
            self.state = 196
            self.match(MoMParser.CLASSID)
            self.state = 197
            self.match(MoMParser.OPEN_PAREN)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 198
                self.arguments()


            self.state = 201
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
        self.enterRule(localctx, 22, self.RULE_construct_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(MoMParser.CLASSID)
            self.state = 204
            self.match(MoMParser.OPEN_PAREN)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 205
                self.function_args()


            self.state = 208
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 209
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 210
                self.block()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 217
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
        self.enterRule(localctx, 24, self.RULE_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(MoMParser.CAPITALID)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 220
                self.match(MoMParser.COMMA)
                self.state = 221
                self.match(MoMParser.CAPITALID)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
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
        self.enterRule(localctx, 26, self.RULE_enumeration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MoMParser.ENUMERATE)
            self.state = 230
            self.match(MoMParser.CLASSID)
            self.state = 231
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 232
            self.enum()
            self.state = 233
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 234
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
        self.enterRule(localctx, 28, self.RULE_exit_sexp)
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
        self.enterRule(localctx, 30, self.RULE_and_op)
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
        self.enterRule(localctx, 32, self.RULE_or_op)
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
        self.enterRule(localctx, 34, self.RULE_ss_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.s_exp()
            self.state = 243
            self.exit_sexp()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.AND or _la==MoMParser.OR:
                self.state = 248
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.AND]:
                    self.state = 244
                    self.match(MoMParser.AND)
                    self.state = 245
                    self.and_op()
                    pass
                elif token in [MoMParser.OR]:
                    self.state = 246
                    self.match(MoMParser.OR)
                    self.state = 247
                    self.or_op()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 250
                self.s_exp()
                self.state = 251
                self.exit_sexp()
                self.state = 257
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
        self.enterRule(localctx, 36, self.RULE_exit_exp)
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
        self.enterRule(localctx, 38, self.RULE_s_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.expression()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.LESS_THAN) | (1 << MoMParser.LESS_EQUAL) | (1 << MoMParser.GREATER_THAN) | (1 << MoMParser.GREATER_EQUAL) | (1 << MoMParser.EQUAL_EQUAL))) != 0):
                self.state = 261
                self.operand()
                self.state = 262
                self.expression()
                self.state = 263
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
        self.enterRule(localctx, 40, self.RULE_exit_term)
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
        self.enterRule(localctx, 42, self.RULE_plus_op)
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
        self.enterRule(localctx, 44, self.RULE_minus_op)
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
        self.enterRule(localctx, 46, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 273
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 274
                self.term()
                self.state = 275
                self.exit_term()
                pass


            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.IF))) != 0):
                self.state = 284
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.PLUS]:
                    self.state = 279
                    self.match(MoMParser.PLUS)
                    self.state = 280
                    self.plus_op()
                    pass
                elif token in [MoMParser.MINUS]:
                    self.state = 281
                    self.match(MoMParser.MINUS)
                    self.state = 282
                    self.minus_op()
                    pass
                elif token in [MoMParser.IF]:
                    self.state = 283
                    self.condition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 290
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 286
                    self.function_call()
                    pass

                elif la_ == 2:
                    self.state = 287
                    self.term()
                    self.state = 288
                    self.exit_term()
                    pass


                self.state = 296
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
        self.enterRule(localctx, 48, self.RULE_open_paren)
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
        self.enterRule(localctx, 50, self.RULE_close_paren)
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
        self.enterRule(localctx, 52, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(MoMParser.OPEN_PAREN)
                self.state = 302
                self.open_paren()
                self.state = 303
                self.ss_exp()
                self.state = 304
                self.close_paren()
                self.state = 305
                self.match(MoMParser.CLOSE_PAREN)
                pass
            elif token in [MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0):
                    self.state = 307
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 310
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
        self.enterRule(localctx, 54, self.RULE_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 313
                self.super_type()
                pass

            elif la_ == 2:
                self.state = 314
                self.array_arg()
                pass


            self.state = 317
            self.match(MoMParser.VARID)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 318
                self.match(MoMParser.COMMA)
                self.state = 321
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 319
                    self.super_type()
                    pass

                elif la_ == 2:
                    self.state = 320
                    self.array_arg()
                    pass


                self.state = 323
                self.match(MoMParser.VARID)
                self.state = 329
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
        self.enterRule(localctx, 56, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.THIS or _la==MoMParser.CLASSID:
                self.state = 330
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.CLASSID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 331
                self.match(MoMParser.PERIOD)


            self.state = 334
            self.match(MoMParser.VARID)
            self.state = 335
            self.match(MoMParser.OPEN_PAREN)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 336
                self.arguments()


            self.state = 339
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
        self.enterRule(localctx, 58, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.simple_type()
            self.state = 342
            self.match(MoMParser.VARID)
            self.state = 343
            self.match(MoMParser.OPEN_PAREN)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 344
                self.function_args()


            self.state = 347
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 348
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 349
                self.block()
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.RETURN:
                self.state = 355
                self.match(MoMParser.RETURN)
                self.state = 356
                self.ss_exp()
                self.state = 357
                self.match(MoMParser.SEMI_COLON)


            self.state = 361
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 362
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
        self.enterRule(localctx, 60, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
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
        self.enterRule(localctx, 62, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(MoMParser.FIELD)
            self.state = 367
            self.match(MoMParser.LESS_THAN)
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 368
                self.super_type()
                pass

            elif la_ == 2:
                self.state = 369
                self.array_def()
                pass


            self.state = 372
            self.match(MoMParser.GREATER_THAN)
            self.state = 373
            self.match(MoMParser.VARID)
            self.state = 374
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
        self.enterRule(localctx, 64, self.RULE_spec_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.simple_type()
            self.state = 377
            self.match(MoMParser.VARID)
            self.state = 378
            self.match(MoMParser.OPEN_PAREN)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 379
                self.function_args()


            self.state = 382
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 383
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
        self.enterRule(localctx, 66, self.RULE_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MoMParser.SPEC)
            self.state = 386
            self.match(MoMParser.CLASSID)
            self.state = 387
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 388
                self.spec_function()
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 394
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 395
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
        self.enterRule(localctx, 68, self.RULE_assignation_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.super_type()
            self.state = 398
            self.match(MoMParser.VARID)
            self.state = 399
            self.match(MoMParser.EQUALS)
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 400
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 401
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
        self.enterRule(localctx, 70, self.RULE_statute)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.assignation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.assignation_def()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 407
                self.while_loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 408
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
        self.enterRule(localctx, 72, self.RULE_exit_factor)
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
        self.enterRule(localctx, 74, self.RULE_star_op)
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
        self.enterRule(localctx, 76, self.RULE_div_op)
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
        self.enterRule(localctx, 78, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.factor()
            self.state = 418
            self.exit_factor()
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.STAR or _la==MoMParser.SLASH:
                self.state = 423
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.STAR]:
                    self.state = 419
                    self.match(MoMParser.STAR)
                    self.state = 420
                    self.star_op()
                    pass
                elif token in [MoMParser.SLASH]:
                    self.state = 421
                    self.match(MoMParser.SLASH)
                    self.state = 422
                    self.div_op()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 425
                self.factor()
                self.state = 426
                self.exit_factor()
                self.state = 432
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
        self.enterRule(localctx, 80, self.RULE_super_type)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.INT, MoMParser.TEXT, MoMParser.FLOAT, MoMParser.NOTHING, MoMParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.simple_type()
                pass
            elif token in [MoMParser.COMPONENT, MoMParser.SET, MoMParser.MAP, MoMParser.SIZE, MoMParser.CLASSID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
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
        self.enterRule(localctx, 82, self.RULE_simple_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
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
        self.enterRule(localctx, 84, self.RULE_complex_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
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
        self.enterRule(localctx, 86, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(MoMParser.WHILE)
            self.state = 442
            self.match(MoMParser.OPEN_PAREN)
            self.state = 443
            self.ss_exp()
            self.state = 444
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 445
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 446
                self.block()
                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 452
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
        self.enterRule(localctx, 88, self.RULE_array_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.super_type()
            self.state = 455
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 456
            self.match(MoMParser.INTEGER)
            self.state = 457
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
        self.enterRule(localctx, 90, self.RULE_array_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.THIS or _la==MoMParser.CLASSID:
                self.state = 459
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.CLASSID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 460
                self.match(MoMParser.PERIOD)


            self.state = 463
            self.match(MoMParser.VARID)
            self.state = 464
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 465
            self.match(MoMParser.INTEGER)
            self.state = 466
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
        self.enterRule(localctx, 92, self.RULE_array_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.super_type()
            self.state = 469
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 470
            self.match(MoMParser.CLOSE_SBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





