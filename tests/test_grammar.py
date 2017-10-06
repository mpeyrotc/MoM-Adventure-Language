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
        assert general_function("resources/single_class.mom"), "Parsing errors"
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
                assert len(methods[method].variables) == 2

                assert "a_number" in methods[method].variables
                assert "a_real" in methods[method].variables

                for variable in methods[method].variables:
                    if variable == "a_number":
                        assert methods[method].variables["a_number"]["type"] == "Int"
                        assert not methods[method].variables["a_number"]["is_array"]
                    elif variable == "a_real":
                        assert methods[method].variables["a_real"]["type"] == "Real"
                        assert not methods[method].variables["a_real"]["is_array"]
                    else:
                        assert False
            elif method == "addCommonCard":
                assert methods[method].return_type == Type.NOTHING
                assert len(methods[method].variables) == 0
            else:
                assert False

    def test_single_specification(self):
        assert general_function("resources/specification.mom")
        specifications = master_tables.specifications

        assert len(specifications) == 1
        assert "ComplexNumber" in specifications
        assert specifications["ComplexNumber"].name == "ComplexNumber"

        methods = specifications["ComplexNumber"].methods
        assert len(methods) == 4
        assert "real" in methods
        assert "imaginary" in methods
        assert "convert" in methods
        assert "summary" in methods

        for name in methods:
            method = methods[name]

            if method.name == "real":
                assert method.return_type == Type.INT
            elif method.name == "imaginary":
                assert method.return_type == Type.INT
            elif method.name == "convert":
                assert method.return_type == Type.NOTHING
                assert len(method.variables) == 1
                assert "angle" in method.variables
                assert method.variables["angle"]["type"] == "Int"
                assert not method.variables["angle"]["is_array"]
            else:
                assert method.return_type == Type.REAL
                assert method.name == "summary"
                assert len(method.variables) == 2
                assert "c" in method.variables
                assert method.variables["c"]["type"] == "Component"
                assert method.variables["c"]["is_array"]
                assert "r" in method.variables
                assert method.variables["r"]["type"] == "Real"
                assert not method.variables["r"]["is_array"]

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
