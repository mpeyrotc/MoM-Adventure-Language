from antlr4 import *

from src.ErrorListener import MoMErrorListener
from src.grammar import MoMLexer
from src.grammar import MoMParser
from src.grammar.MoMListener import MoMListener
import src.MasterTables as master_tables
from src.structures.SemanticTable import Type


def general_function(file):
    master_tables.classes = {}
    master_tables.specifications = {}
    master_tables.enumerations = {}

    try:
        file_stream = FileStream(file)
        input_stream = InputStream(str(file_stream))
        lexer = MoMLexer.MoMLexer(input_stream)
        lexer.removeErrorListeners()
        lexer._listeners = [MoMErrorListener()]
        stream = CommonTokenStream(lexer)
        parser = MoMParser.MoMParser(stream)
        parser._listeners = [MoMErrorListener()]
        tree = parser.program()

        walker = ParseTreeWalker()
        walker.walk(MoMListener(), tree)
        return True
    except Exception as e:
        print(e)

    return False


class TestGrammar(object):
    def test_single_class(self):
        assert general_function("C:\\Users\\Elias Mera\\Documents\\MoM-Adventure-Language\\resources\\single_class.mom"), "Parsing errors"
        classes = master_tables.classes

        assert len(classes) == 1, "more classes than expected."
        assert classes["Character"].name == "Character"
        assert classes["Character"].parent == "Card"
        assert len(classes["Character"].specifications) == 1
        assert "Player" in classes["Character"].specifications
        assert len(classes["Character"].methods) == 3

        for method in classes["Character"].methods:
            methods = classes["Character"].methods
            if method == "Character":
                assert str(methods[method].return_type) == "Character"
                assert len(methods[method].variables) == 0
            elif method == "name":
                assert methods[method].return_type == Type.TEXT
                assert len(methods[method].variables) == 1, "HAHAHA: " + str(methods[method].variables)
            elif method == "addCommonCard":
                assert methods[method].return_type == Type.NOTHING
                assert len(methods[method].variables) == 0
            else:
                assert False

    def test_single_specification(self):
        assert general_function("C:\\Users\\Elias Mera\\Documents\\MoM-Adventure-Language\\resources\\specification.mom")

    def test_single_enumeration(self):
        assert general_function("C:\\Users\\Elias Mera\\Documents\\MoM-Adventure-Language\\resources\\enumeration.mom")

    def test_two_classes(self):
        assert general_function("C:\\Users\\Elias Mera\\Documents\\MoM-Adventure-Language\\resources\\two_classes.mom")

    def test_multiple_segments(self):
        assert general_function("C:\\Users\\Elias Mera\\Documents\\MoM-Adventure-Language\\resources\\class_enum_specification.mom")

    def test_complex_class(self):
        assert general_function("C:\\Users\\Elias Mera\\Documents\\MoM-Adventure-Language\\resources\\complex_class.mom")

    def test_types(self):
        assert general_function("resources/type_test.mom")

TestGrammar().test_single_class()