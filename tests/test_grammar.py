from antlr4 import *
from .context import src
from src.ErrorListener import MoMErrorListener
from src.grammar import MoMLexer
from src.grammar import MoMParser


def general_function(file):
    try:
        file_stream = FileStream(file)
        input_stream = InputStream(str(file_stream))
        lexer = MoMLexer.MoMLexer(input_stream)
        lexer.removeErrorListeners()
        lexer._listeners = [MoMErrorListener()]
        stream = CommonTokenStream(lexer)
        parser = MoMParser.MoMParser(stream)
        parser._listeners = [MoMErrorListener()]
        parser.program()
        return True
    except Exception as e:
        print(e)

    return False


class TestGrammar(object):
    def test_single_class(self):
        assert general_function("resources/single_class.mom")

    def test_single_specification(self):
        assert general_function("resources/specification.mom")

    def test_single_enumeration(self):
        assert general_function("resources/enumeration.mom")

    def test_two_classes(self):
        assert general_function("resources/two_classes.mom")

    def test_multiple_segments(self):
        assert general_function("resources/class_enum_specification.mom")

    def test_complex_class(self):
        assert general_function("resources/complex_class.mom")

    def test_types(self):
        assert general_function("resources/type_test.mom")

