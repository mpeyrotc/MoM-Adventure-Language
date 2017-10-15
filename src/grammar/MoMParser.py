# Generated from src/grammar/MoM.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u01e6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\6\2h\n")
        buf.write("\2\r\2\16\2i\3\2\3\2\3\3\3\3\3\3\7\3q\n\3\f\3\16\3t\13")
        buf.write("\3\3\4\3\4\5\4x\n\4\3\4\3\4\5\4|\n\4\3\4\3\4\3\4\5\4\u0081")
        buf.write("\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008c\n\6")
        buf.write("\3\6\3\6\7\6\u0090\n\6\f\6\16\6\u0093\13\6\3\6\3\6\7\6")
        buf.write("\u0097\n\6\f\6\16\6\u009a\13\6\3\6\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00ac\n\n")
        buf.write("\f\n\16\n\u00af\13\n\3\n\3\n\3\n\3\n\3\n\7\n\u00b6\n\n")
        buf.write("\f\n\16\n\u00b9\13\n\3\n\3\n\5\n\u00bd\n\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00c8\n\13\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00ce\n\f\3\f\3\f\3\r\3\r\3\r\5\r\u00d5\n")
        buf.write("\r\3\r\3\r\3\r\7\r\u00da\n\r\f\r\16\r\u00dd\13\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\7\16\u00e5\n\16\f\16\16\16\u00e8")
        buf.write("\13\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00ff\n\23\3\23\3\23\3\23\7\23\u0104\n\23\f")
        buf.write("\23\16\23\u0107\13\23\3\24\3\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u0110\n\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u011c\n\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0123\n\31\3\31\3\31\3\31\3\31\5\31\u0129\n\31")
        buf.write("\7\31\u012b\n\31\f\31\16\31\u012e\13\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u013b\n")
        buf.write("\34\3\34\5\34\u013e\n\34\3\35\3\35\5\35\u0142\n\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u0148\n\35\3\35\3\35\7\35\u014c\n")
        buf.write("\35\f\35\16\35\u014f\13\35\3\36\3\36\5\36\u0153\n\36\3")
        buf.write("\36\3\36\3\36\5\36\u0158\n\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0160\n\37\3\37\3\37\3\37\7\37\u0165\n\37\f")
        buf.write("\37\16\37\u0168\13\37\3\37\3\37\3\37\3\37\5\37\u016e\n")
        buf.write("\37\3\37\3\37\3\37\3 \3 \3!\3!\3!\3!\5!\u0179\n!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0183\n\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\7#\u018c\n#\f#\16#\u018f\13#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\5$\u0199\n$\3%\3%\3%\3%\3%\5%\u01a0\n%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3)\3)\3)\3)\5)\u01ae\n)\3)\3)\3)\7")
        buf.write(")\u01b3\n)\f)\16)\u01b6\13)\3*\3*\5*\u01ba\n*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\7/\u01cc\n/\f")
        buf.write("/\16/\u01cf\13/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\5\61\u01db\n\61\3\61\3\61\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\2\2\63\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("\2\b\4\2\33\33\65\65\4\2\r\16\22\22\4\2\33\33\64\64\3")
        buf.write("\2\24\30\5\2\37!%%,,\5\2\36\36\"$\64\64\2\u01ea\2g\3\2")
        buf.write("\2\2\4m\3\2\2\2\6w\3\2\2\2\b\u0082\3\2\2\2\n\u0085\3\2")
        buf.write("\2\2\f\u009e\3\2\2\2\16\u00a0\3\2\2\2\20\u00a2\3\2\2\2")
        buf.write("\22\u00a4\3\2\2\2\24\u00c7\3\2\2\2\26\u00c9\3\2\2\2\30")
        buf.write("\u00d1\3\2\2\2\32\u00e1\3\2\2\2\34\u00eb\3\2\2\2\36\u00f2")
        buf.write("\3\2\2\2 \u00f4\3\2\2\2\"\u00f6\3\2\2\2$\u00f8\3\2\2\2")
        buf.write("&\u0108\3\2\2\2(\u010a\3\2\2\2*\u0111\3\2\2\2,\u0113\3")
        buf.write("\2\2\2.\u0115\3\2\2\2\60\u011b\3\2\2\2\62\u012f\3\2\2")
        buf.write("\2\64\u0131\3\2\2\2\66\u013d\3\2\2\28\u0141\3\2\2\2:\u0152")
        buf.write("\3\2\2\2<\u015b\3\2\2\2>\u0172\3\2\2\2@\u0174\3\2\2\2")
        buf.write("B\u017e\3\2\2\2D\u0187\3\2\2\2F\u0193\3\2\2\2H\u019f\3")
        buf.write("\2\2\2J\u01a1\3\2\2\2L\u01a3\3\2\2\2N\u01a5\3\2\2\2P\u01a7")
        buf.write("\3\2\2\2R\u01b9\3\2\2\2T\u01bb\3\2\2\2V\u01bd\3\2\2\2")
        buf.write("X\u01bf\3\2\2\2Z\u01c1\3\2\2\2\\\u01c3\3\2\2\2^\u01d3")
        buf.write("\3\2\2\2`\u01da\3\2\2\2b\u01e1\3\2\2\2dh\5\n\6\2eh\5\34")
        buf.write("\17\2fh\5D#\2gd\3\2\2\2ge\3\2\2\2gf\3\2\2\2hi\3\2\2\2")
        buf.write("ig\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\2\2\3l\3\3\2\2\2mr")
        buf.write("\5$\23\2no\7\4\2\2oq\5$\23\2pn\3\2\2\2qt\3\2\2\2rp\3\2")
        buf.write("\2\2rs\3\2\2\2s\5\3\2\2\2tr\3\2\2\2uv\t\2\2\2vx\7\21\2")
        buf.write("\2wu\3\2\2\2wx\3\2\2\2x{\3\2\2\2y|\7\65\2\2z|\5`\61\2")
        buf.write("{y\3\2\2\2{z\3\2\2\2|}\3\2\2\2}\u0080\7\17\2\2~\u0081")
        buf.write("\5\26\f\2\177\u0081\5$\23\2\u0080~\3\2\2\2\u0080\177\3")
        buf.write("\2\2\2\u0081\7\3\2\2\2\u0082\u0083\5H%\2\u0083\u0084\7")
        buf.write("\n\2\2\u0084\t\3\2\2\2\u0085\u0086\7&\2\2\u0086\u0087")
        buf.write("\7\64\2\2\u0087\u0088\7/\2\2\u0088\u008b\5V,\2\u0089\u008a")
        buf.write("\7.\2\2\u008a\u008c\7\64\2\2\u008b\u0089\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0091\7\6\2\2")
        buf.write("\u008e\u0090\5@!\2\u008f\u008e\3\2\2\2\u0090\u0093\3\2")
        buf.write("\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0098\5\30\r\2\u0095")
        buf.write("\u0097\5<\37\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2")
        buf.write("\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009b\3")
        buf.write("\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\7\7\2\2\u009c\u009d")
        buf.write("\7\n\2\2\u009d\13\3\2\2\2\u009e\u009f\3\2\2\2\u009f\r")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\17\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\21\3\2\2\2\u00a4\u00a5\7\34\2\2\u00a5\u00a6")
        buf.write("\7\3\2\2\u00a6\u00a7\5$\23\2\u00a7\u00a8\7\5\2\2\u00a8")
        buf.write("\u00a9\5\f\7\2\u00a9\u00ad\7\6\2\2\u00aa\u00ac\5\b\5\2")
        buf.write("\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3")
        buf.write("\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00b0\u00bc\7\7\2\2\u00b1\u00b2\7\35\2\2\u00b2")
        buf.write("\u00b3\5\20\t\2\u00b3\u00b7\7\6\2\2\u00b4\u00b6\5\b\5")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00ba\u00bb\7\7\2\2\u00bb\u00bd\3\2\2\2")
        buf.write("\u00bc\u00b1\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3")
        buf.write("\2\2\2\u00be\u00bf\5\16\b\2\u00bf\23\3\2\2\2\u00c0\u00c8")
        buf.write("\7\66\2\2\u00c1\u00c8\7\67\2\2\u00c2\u00c8\79\2\2\u00c3")
        buf.write("\u00c8\7\65\2\2\u00c4\u00c8\5`\61\2\u00c5\u00c8\7\61\2")
        buf.write("\2\u00c6\u00c8\7\62\2\2\u00c7\u00c0\3\2\2\2\u00c7\u00c1")
        buf.write("\3\2\2\2\u00c7\u00c2\3\2\2\2\u00c7\u00c3\3\2\2\2\u00c7")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2")
        buf.write("\u00c8\25\3\2\2\2\u00c9\u00ca\7\'\2\2\u00ca\u00cb\7\64")
        buf.write("\2\2\u00cb\u00cd\7\3\2\2\u00cc\u00ce\5\4\3\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d0\7\5\2\2\u00d0\27\3\2\2\2\u00d1\u00d2\7\64\2\2\u00d2")
        buf.write("\u00d4\7\3\2\2\u00d3\u00d5\58\35\2\u00d4\u00d3\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\7")
        buf.write("\5\2\2\u00d7\u00db\7\6\2\2\u00d8\u00da\5\b\5\2\u00d9\u00d8")
        buf.write("\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00de\u00df\7\7\2\2\u00df\u00e0\7\n\2\2\u00e0\31\3\2")
        buf.write("\2\2\u00e1\u00e6\7\63\2\2\u00e2\u00e3\7\4\2\2\u00e3\u00e5")
        buf.write("\7\63\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9\3\2\2\2")
        buf.write("\u00e8\u00e6\3\2\2\2\u00e9\u00ea\7\n\2\2\u00ea\33\3\2")
        buf.write("\2\2\u00eb\u00ec\7(\2\2\u00ec\u00ed\7\64\2\2\u00ed\u00ee")
        buf.write("\7\6\2\2\u00ee\u00ef\5\32\16\2\u00ef\u00f0\7\7\2\2\u00f0")
        buf.write("\u00f1\7\n\2\2\u00f1\35\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\37\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5!\3\2\2\2\u00f6\u00f7")
        buf.write("\3\2\2\2\u00f7#\3\2\2\2\u00f8\u00f9\5(\25\2\u00f9\u0105")
        buf.write("\5\36\20\2\u00fa\u00fb\7\31\2\2\u00fb\u00ff\5 \21\2\u00fc")
        buf.write("\u00fd\7\32\2\2\u00fd\u00ff\5\"\22\2\u00fe\u00fa\3\2\2")
        buf.write("\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101")
        buf.write("\5(\25\2\u0101\u0102\5\36\20\2\u0102\u0104\3\2\2\2\u0103")
        buf.write("\u00fe\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106%\3\2\2\2\u0107\u0105\3\2\2")
        buf.write("\2\u0108\u0109\3\2\2\2\u0109\'\3\2\2\2\u010a\u010f\5\60")
        buf.write("\31\2\u010b\u010c\5> \2\u010c\u010d\5\60\31\2\u010d\u010e")
        buf.write("\5&\24\2\u010e\u0110\3\2\2\2\u010f\u010b\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110)\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("+\3\2\2\2\u0113\u0114\3\2\2\2\u0114-\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116/\3\2\2\2\u0117\u011c\5:\36\2\u0118\u0119")
        buf.write("\5P)\2\u0119\u011a\5*\26\2\u011a\u011c\3\2\2\2\u011b\u0117")
        buf.write("\3\2\2\2\u011b\u0118\3\2\2\2\u011c\u012c\3\2\2\2\u011d")
        buf.write("\u011e\7\r\2\2\u011e\u0123\5,\27\2\u011f\u0120\7\16\2")
        buf.write("\2\u0120\u0123\5.\30\2\u0121\u0123\5\22\n\2\u0122\u011d")
        buf.write("\3\2\2\2\u0122\u011f\3\2\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("\u0128\3\2\2\2\u0124\u0129\5:\36\2\u0125\u0126\5P)\2\u0126")
        buf.write("\u0127\5*\26\2\u0127\u0129\3\2\2\2\u0128\u0124\3\2\2\2")
        buf.write("\u0128\u0125\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u0122\3")
        buf.write("\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\61\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\63\3\2\2\2\u0131\u0132\3\2\2\2\u0132\65")
        buf.write("\3\2\2\2\u0133\u0134\7\3\2\2\u0134\u0135\5\62\32\2\u0135")
        buf.write("\u0136\5$\23\2\u0136\u0137\5\64\33\2\u0137\u0138\7\5\2")
        buf.write("\2\u0138\u013e\3\2\2\2\u0139\u013b\t\3\2\2\u013a\u0139")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\u013e\5\24\13\2\u013d\u0133\3\2\2\2\u013d\u013a\3\2\2")
        buf.write("\2\u013e\67\3\2\2\2\u013f\u0142\5R*\2\u0140\u0142\5b\62")
        buf.write("\2\u0141\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142\u0143")
        buf.write("\3\2\2\2\u0143\u014d\7\65\2\2\u0144\u0147\7\4\2\2\u0145")
        buf.write("\u0148\5R*\2\u0146\u0148\5b\62\2\u0147\u0145\3\2\2\2\u0147")
        buf.write("\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\7\65\2")
        buf.write("\2\u014a\u014c\3\2\2\2\u014b\u0144\3\2\2\2\u014c\u014f")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("9\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\t\4\2\2\u0151")
        buf.write("\u0153\7\21\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2")
        buf.write("\2\u0153\u0154\3\2\2\2\u0154\u0155\7\65\2\2\u0155\u0157")
        buf.write("\7\3\2\2\u0156\u0158\5\4\3\2\u0157\u0156\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\7\5\2\2")
        buf.write("\u015a;\3\2\2\2\u015b\u015c\5T+\2\u015c\u015d\7\65\2\2")
        buf.write("\u015d\u015f\7\3\2\2\u015e\u0160\58\35\2\u015f\u015e\3")
        buf.write("\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162")
        buf.write("\7\5\2\2\u0162\u0166\7\6\2\2\u0163\u0165\5\b\5\2\u0164")
        buf.write("\u0163\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u016d\3\2\2\2\u0168\u0166\3")
        buf.write("\2\2\2\u0169\u016a\7+\2\2\u016a\u016b\5$\23\2\u016b\u016c")
        buf.write("\7\n\2\2\u016c\u016e\3\2\2\2\u016d\u0169\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\7\7\2\2")
        buf.write("\u0170\u0171\7\n\2\2\u0171=\3\2\2\2\u0172\u0173\t\5\2")
        buf.write("\2\u0173?\3\2\2\2\u0174\u0175\7)\2\2\u0175\u0178\7\24")
        buf.write("\2\2\u0176\u0179\5R*\2\u0177\u0179\5^\60\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u017b\7\26\2\2\u017b\u017c\7\65\2\2\u017c\u017d\7\n\2")
        buf.write("\2\u017dA\3\2\2\2\u017e\u017f\5T+\2\u017f\u0180\7\65\2")
        buf.write("\2\u0180\u0182\7\3\2\2\u0181\u0183\58\35\2\u0182\u0181")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0185\7\5\2\2\u0185\u0186\7\n\2\2\u0186C\3\2\2\2\u0187")
        buf.write("\u0188\7*\2\2\u0188\u0189\7\64\2\2\u0189\u018d\7\6\2\2")
        buf.write("\u018a\u018c\5B\"\2\u018b\u018a\3\2\2\2\u018c\u018f\3")
        buf.write("\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190")
        buf.write("\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\7\7\2\2\u0191")
        buf.write("\u0192\7\n\2\2\u0192E\3\2\2\2\u0193\u0194\5R*\2\u0194")
        buf.write("\u0195\7\65\2\2\u0195\u0198\7\17\2\2\u0196\u0199\5\26")
        buf.write("\f\2\u0197\u0199\5$\23\2\u0198\u0196\3\2\2\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199G\3\2\2\2\u019a\u01a0\5:\36\2\u019b\u01a0")
        buf.write("\5\6\4\2\u019c\u01a0\5F$\2\u019d\u01a0\5\\/\2\u019e\u01a0")
        buf.write("\5\22\n\2\u019f\u019a\3\2\2\2\u019f\u019b\3\2\2\2\u019f")
        buf.write("\u019c\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0I\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2K\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4M\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("O\3\2\2\2\u01a7\u01a8\5\66\34\2\u01a8\u01b4\5J&\2\u01a9")
        buf.write("\u01aa\7\13\2\2\u01aa\u01ae\5L\'\2\u01ab\u01ac\7\f\2\2")
        buf.write("\u01ac\u01ae\5N(\2\u01ad\u01a9\3\2\2\2\u01ad\u01ab\3\2")
        buf.write("\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\5\66\34\2\u01b0\u01b1")
        buf.write("\5J&\2\u01b1\u01b3\3\2\2\2\u01b2\u01ad\3\2\2\2\u01b3\u01b6")
        buf.write("\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5")
        buf.write("Q\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01ba\5T+\2\u01b8")
        buf.write("\u01ba\5V,\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("S\3\2\2\2\u01bb\u01bc\t\6\2\2\u01bcU\3\2\2\2\u01bd\u01be")
        buf.write("\t\7\2\2\u01beW\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0Y\3\2")
        buf.write("\2\2\u01c1\u01c2\3\2\2\2\u01c2[\3\2\2\2\u01c3\u01c4\7")
        buf.write("\60\2\2\u01c4\u01c5\5Z.\2\u01c5\u01c6\7\3\2\2\u01c6\u01c7")
        buf.write("\5$\23\2\u01c7\u01c8\7\5\2\2\u01c8\u01c9\5\f\7\2\u01c9")
        buf.write("\u01cd\7\6\2\2\u01ca\u01cc\5\b\5\2\u01cb\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ce\u01d0\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1")
        buf.write("\7\7\2\2\u01d1\u01d2\5X-\2\u01d2]\3\2\2\2\u01d3\u01d4")
        buf.write("\5R*\2\u01d4\u01d5\7\b\2\2\u01d5\u01d6\7\66\2\2\u01d6")
        buf.write("\u01d7\7\t\2\2\u01d7_\3\2\2\2\u01d8\u01d9\t\4\2\2\u01d9")
        buf.write("\u01db\7\21\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2")
        buf.write("\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\7\65\2\2\u01dd\u01de")
        buf.write("\7\b\2\2\u01de\u01df\7\66\2\2\u01df\u01e0\7\t\2\2\u01e0")
        buf.write("a\3\2\2\2\u01e1\u01e2\5R*\2\u01e2\u01e3\7\b\2\2\u01e3")
        buf.write("\u01e4\7\t\2\2\u01e4c\3\2\2\2.girw{\u0080\u008b\u0091")
        buf.write("\u0098\u00ad\u00b7\u00bc\u00c7\u00cd\u00d4\u00db\u00e6")
        buf.write("\u00fe\u0105\u010f\u011b\u0122\u0128\u012c\u013a\u013d")
        buf.write("\u0141\u0147\u014d\u0152\u0157\u015f\u0166\u016d\u0178")
        buf.write("\u0182\u018d\u0198\u019f\u01ad\u01b4\u01b9\u01cd\u01da")
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
    RULE_end_while = 43
    RULE_after_while = 44
    RULE_while_loop = 45
    RULE_array_def = 46
    RULE_array_var = 47
    RULE_array_arg = 48

    ruleNames =  [ "program", "arguments", "assignation", "block", "class_rule", 
                   "exit_if_check", "condition_end", "enter_else", "condition", 
                   "constant", "construct_call", "construct_def", "enum", 
                   "enumeration", "exit_sexp", "and_op", "or_op", "ss_exp", 
                   "exit_exp", "s_exp", "exit_term", "plus_op", "minus_op", 
                   "expression", "open_paren", "close_paren", "factor", 
                   "function_args", "function_call", "function_def", "operand", 
                   "field", "spec_function", "specification", "assignation_def", 
                   "statute", "exit_factor", "star_op", "div_op", "term", 
                   "super_type", "simple_type", "complex_type", "end_while", 
                   "after_while", "while_loop", "array_def", "array_var", 
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
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 101
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.CLASS]:
                    self.state = 98
                    self.class_rule()
                    pass
                elif token in [MoMParser.ENUMERATE]:
                    self.state = 99
                    self.enumeration()
                    pass
                elif token in [MoMParser.SPEC]:
                    self.state = 100
                    self.specification()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.CLASS) | (1 << MoMParser.ENUMERATE) | (1 << MoMParser.SPEC))) != 0)):
                    break

            self.state = 105
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
            self.state = 107
            self.ss_exp()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 108
                self.match(MoMParser.COMMA)
                self.state = 109
                self.ss_exp()
                self.state = 114
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
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.VARID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                self.match(MoMParser.PERIOD)


            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 119
                self.match(MoMParser.VARID)
                pass

            elif la_ == 2:
                self.state = 120
                self.array_var()
                pass


            self.state = 123
            self.match(MoMParser.EQUALS)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 124
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 125
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
            self.state = 128
            self.statute()
            self.state = 129
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
            self.state = 131
            self.match(MoMParser.CLASS)
            self.state = 132
            self.match(MoMParser.CLASSID)
            self.state = 133
            self.match(MoMParser.IS_A)
            self.state = 134
            self.complex_type()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.OF_TYPE:
                self.state = 135
                self.match(MoMParser.OF_TYPE)
                self.state = 136
                self.match(MoMParser.CLASSID)


            self.state = 139
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.FIELD:
                self.state = 140
                self.field()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.construct_def()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 147
                self.function_def()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 154
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
            self.state = 162
            self.match(MoMParser.IF)
            self.state = 163
            self.match(MoMParser.OPEN_PAREN)
            self.state = 164
            self.ss_exp()
            self.state = 165
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 166
            self.exit_if_check()
            self.state = 167
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 168
                self.block()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 174
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.ELSE:
                self.state = 175
                self.match(MoMParser.ELSE)
                self.state = 176
                self.enter_else()
                self.state = 177
                self.match(MoMParser.OPEN_BRACKET)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                    self.state = 178
                    self.block()
                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 184
                self.match(MoMParser.CLOSE_BRACKET)


            self.state = 188
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
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(MoMParser.INTEGER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(MoMParser.REAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.match(MoMParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 193
                self.match(MoMParser.VARID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 194
                self.array_var()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 195
                self.match(MoMParser.TRUE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 196
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
            self.state = 199
            self.match(MoMParser.NEW)
            self.state = 200
            self.match(MoMParser.CLASSID)
            self.state = 201
            self.match(MoMParser.OPEN_PAREN)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 202
                self.arguments()


            self.state = 205
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
            self.state = 207
            self.match(MoMParser.CLASSID)
            self.state = 208
            self.match(MoMParser.OPEN_PAREN)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 209
                self.function_args()


            self.state = 212
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 213
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 214
                self.block()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 221
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
            self.state = 223
            self.match(MoMParser.CAPITALID)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 224
                self.match(MoMParser.COMMA)
                self.state = 225
                self.match(MoMParser.CAPITALID)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
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
            self.state = 233
            self.match(MoMParser.ENUMERATE)
            self.state = 234
            self.match(MoMParser.CLASSID)
            self.state = 235
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 236
            self.enum()
            self.state = 237
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 238
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
            self.state = 246
            self.s_exp()
            self.state = 247
            self.exit_sexp()
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.AND or _la==MoMParser.OR:
                self.state = 252
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.AND]:
                    self.state = 248
                    self.match(MoMParser.AND)
                    self.state = 249
                    self.and_op()
                    pass
                elif token in [MoMParser.OR]:
                    self.state = 250
                    self.match(MoMParser.OR)
                    self.state = 251
                    self.or_op()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 254
                self.s_exp()
                self.state = 255
                self.exit_sexp()
                self.state = 261
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
            self.state = 264
            self.expression()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.LESS_THAN) | (1 << MoMParser.LESS_EQUAL) | (1 << MoMParser.GREATER_THAN) | (1 << MoMParser.GREATER_EQUAL) | (1 << MoMParser.EQUAL_EQUAL))) != 0):
                self.state = 265
                self.operand()
                self.state = 266
                self.expression()
                self.state = 267
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
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 277
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 278
                self.term()
                self.state = 279
                self.exit_term()
                pass


            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.IF))) != 0):
                self.state = 288
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.PLUS]:
                    self.state = 283
                    self.match(MoMParser.PLUS)
                    self.state = 284
                    self.plus_op()
                    pass
                elif token in [MoMParser.MINUS]:
                    self.state = 285
                    self.match(MoMParser.MINUS)
                    self.state = 286
                    self.minus_op()
                    pass
                elif token in [MoMParser.IF]:
                    self.state = 287
                    self.condition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 294
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 290
                    self.function_call()
                    pass

                elif la_ == 2:
                    self.state = 291
                    self.term()
                    self.state = 292
                    self.exit_term()
                    pass


                self.state = 300
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
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(MoMParser.OPEN_PAREN)
                self.state = 306
                self.open_paren()
                self.state = 307
                self.ss_exp()
                self.state = 308
                self.close_paren()
                self.state = 309
                self.match(MoMParser.CLOSE_PAREN)
                pass
            elif token in [MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0):
                    self.state = 311
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 314
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
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 317
                self.super_type()
                pass

            elif la_ == 2:
                self.state = 318
                self.array_arg()
                pass


            self.state = 321
            self.match(MoMParser.VARID)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.COMMA:
                self.state = 322
                self.match(MoMParser.COMMA)
                self.state = 325
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 323
                    self.super_type()
                    pass

                elif la_ == 2:
                    self.state = 324
                    self.array_arg()
                    pass


                self.state = 327
                self.match(MoMParser.VARID)
                self.state = 333
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
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.THIS or _la==MoMParser.CLASSID:
                self.state = 334
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.CLASSID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 335
                self.match(MoMParser.PERIOD)


            self.state = 338
            self.match(MoMParser.VARID)
            self.state = 339
            self.match(MoMParser.OPEN_PAREN)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.OPEN_PAREN) | (1 << MoMParser.PLUS) | (1 << MoMParser.MINUS) | (1 << MoMParser.NOT) | (1 << MoMParser.THIS) | (1 << MoMParser.TRUE) | (1 << MoMParser.FALSE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID) | (1 << MoMParser.INTEGER) | (1 << MoMParser.REAL) | (1 << MoMParser.STRING))) != 0):
                self.state = 340
                self.arguments()


            self.state = 343
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
            self.state = 345
            self.simple_type()
            self.state = 346
            self.match(MoMParser.VARID)
            self.state = 347
            self.match(MoMParser.OPEN_PAREN)
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 348
                self.function_args()


            self.state = 351
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 352
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 353
                self.block()
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.RETURN:
                self.state = 359
                self.match(MoMParser.RETURN)
                self.state = 360
                self.ss_exp()
                self.state = 361
                self.match(MoMParser.SEMI_COLON)


            self.state = 365
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 366
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
            self.state = 368
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
            self.state = 370
            self.match(MoMParser.FIELD)
            self.state = 371
            self.match(MoMParser.LESS_THAN)
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 372
                self.super_type()
                pass

            elif la_ == 2:
                self.state = 373
                self.array_def()
                pass


            self.state = 376
            self.match(MoMParser.GREATER_THAN)
            self.state = 377
            self.match(MoMParser.VARID)
            self.state = 378
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
            self.state = 380
            self.simple_type()
            self.state = 381
            self.match(MoMParser.VARID)
            self.state = 382
            self.match(MoMParser.OPEN_PAREN)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.CLASSID))) != 0):
                self.state = 383
                self.function_args()


            self.state = 386
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 387
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
            self.state = 389
            self.match(MoMParser.SPEC)
            self.state = 390
            self.match(MoMParser.CLASSID)
            self.state = 391
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN))) != 0):
                self.state = 392
                self.spec_function()
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 398
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 399
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
            self.state = 401
            self.super_type()
            self.state = 402
            self.match(MoMParser.VARID)
            self.state = 403
            self.match(MoMParser.EQUALS)
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.NEW]:
                self.state = 404
                self.construct_call()
                pass
            elif token in [MoMParser.OPEN_PAREN, MoMParser.PLUS, MoMParser.MINUS, MoMParser.NOT, MoMParser.THIS, MoMParser.TRUE, MoMParser.FALSE, MoMParser.CLASSID, MoMParser.VARID, MoMParser.INTEGER, MoMParser.REAL, MoMParser.STRING]:
                self.state = 405
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
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.assignation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 410
                self.assignation_def()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 411
                self.while_loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 412
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
            self.state = 421
            self.factor()
            self.state = 422
            self.exit_factor()
            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MoMParser.STAR or _la==MoMParser.SLASH:
                self.state = 427
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MoMParser.STAR]:
                    self.state = 423
                    self.match(MoMParser.STAR)
                    self.state = 424
                    self.star_op()
                    pass
                elif token in [MoMParser.SLASH]:
                    self.state = 425
                    self.match(MoMParser.SLASH)
                    self.state = 426
                    self.div_op()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 429
                self.factor()
                self.state = 430
                self.exit_factor()
                self.state = 436
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
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MoMParser.INT, MoMParser.TEXT, MoMParser.FLOAT, MoMParser.NOTHING, MoMParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.simple_type()
                pass
            elif token in [MoMParser.COMPONENT, MoMParser.SET, MoMParser.MAP, MoMParser.SIZE, MoMParser.CLASSID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
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
            self.state = 441
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
            self.state = 443
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
        self.enterRule(localctx, 86, self.RULE_end_while)
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
        self.enterRule(localctx, 88, self.RULE_after_while)
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
        self.enterRule(localctx, 90, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(MoMParser.WHILE)
            self.state = 450
            self.after_while()
            self.state = 451
            self.match(MoMParser.OPEN_PAREN)
            self.state = 452
            self.ss_exp()
            self.state = 453
            self.match(MoMParser.CLOSE_PAREN)
            self.state = 454
            self.exit_if_check()
            self.state = 455
            self.match(MoMParser.OPEN_BRACKET)
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MoMParser.THIS) | (1 << MoMParser.IF) | (1 << MoMParser.COMPONENT) | (1 << MoMParser.INT) | (1 << MoMParser.TEXT) | (1 << MoMParser.FLOAT) | (1 << MoMParser.SET) | (1 << MoMParser.MAP) | (1 << MoMParser.SIZE) | (1 << MoMParser.NOTHING) | (1 << MoMParser.BOOLEAN) | (1 << MoMParser.WHILE) | (1 << MoMParser.CLASSID) | (1 << MoMParser.VARID))) != 0):
                self.state = 456
                self.block()
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 462
            self.match(MoMParser.CLOSE_BRACKET)
            self.state = 463
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
        self.enterRule(localctx, 92, self.RULE_array_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.super_type()
            self.state = 466
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 467
            self.match(MoMParser.INTEGER)
            self.state = 468
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
        self.enterRule(localctx, 94, self.RULE_array_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MoMParser.THIS or _la==MoMParser.CLASSID:
                self.state = 470
                _la = self._input.LA(1)
                if not(_la==MoMParser.THIS or _la==MoMParser.CLASSID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 471
                self.match(MoMParser.PERIOD)


            self.state = 474
            self.match(MoMParser.VARID)
            self.state = 475
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 476
            self.match(MoMParser.INTEGER)
            self.state = 477
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
        self.enterRule(localctx, 96, self.RULE_array_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.super_type()
            self.state = 480
            self.match(MoMParser.OPEN_SBRACKET)
            self.state = 481
            self.match(MoMParser.CLOSE_SBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





