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
        enumerations = master_tables.enumerations

        assert len(enumerations) == 1

        values = enumerations["Days"].values
        assert "MONDAY" in values
        assert values["MONDAY"] == 1
        assert "TUESDAY" in values
        assert values["TUESDAY"] == 2
        assert "WEDNESDAY" in values
        assert values["WEDNESDAY"] == 3
        assert "THURSDAY" in values
        assert values["THURSDAY"] == 4
        assert "FRIDAY" in values
        assert values["FRIDAY"] == 5

    def test_two_classes(self):
        assert general_function("resources/two_classes.mom")
        classes = master_tables.classes
        assert len(classes) == 2, "more classes than expected."

        # Character class
        assert classes["Character"].name == "Character"
        assert classes["Character"].parent == "Card"
        assert len(classes["Character"].specifications) == 1
        assert "Player" in classes["Character"].specifications
        assert len(classes["Character"].methods) == 3

        assert "Character" in classes["Character"].methods
        assert "addCommonCard" in classes["Character"].methods
        assert "name" in classes["Character"].methods

        for name in classes["Character"].methods:
            method = classes["Character"].methods[name]

            if method.name == "Character":
                assert str(method.return_type) == "Character"
                assert len(method.variables) == 2

                assert "physicalLife" in method.variables
                assert "mentalLife" in method.variables

                for var_name in method.variables:
                    variable = method.variables[var_name]
                    if var_name == "physicalLife":
                        assert variable["type"] == "Int"
                        assert variable["is_array"]
                    if var_name == "mental_life":
                        assert variable["type"] == "Real"
                        assert variable["is_array"]
            elif method.name == "addCommonCard":
                assert method.return_type == Type.NOTHING
                assert len(method.variables) == 1
                assert "card" in method.variables
                variable = method.variables["card"]
                assert variable["type"] == "Card"
                assert not variable["is_array"]
            else:
                assert method.return_type == Type.TEXT
                assert len(method.variables) == 1
                assert "greeting" in method.variables
                variable = method.variables["greeting"]
                assert variable["type"] == "Text"
                assert not variable["is_array"]

        # Card class
        assert classes["Card"].name == "Card"
        assert classes["Card"].parent == "Component"
        assert len(classes["Card"].specifications) == 0
        assert len(classes["Card"].methods) == 1

        assert "Card" in classes["Card"].methods
        method = classes["Card"].methods["Card"]
        assert str(method.return_type) == "Card"
        assert len(method.variables) == 2

        assert "physicalLife" in method.variables
        assert "mentalLife" in method.variables

        for var_name in method.variables:
            variable = method.variables[var_name]
            if var_name == "physicalLife":
                assert variable["type"] == "Int"
                assert not variable["is_array"]
            elif var_name == "mentalLife":
                assert variable["type"] == "Int"
                assert not variable["is_array"]
            else:
                assert False

    def test_multiple_segments(self):
        assert general_function("resources/class_enum_specification.mom")

        classes = master_tables.classes
        assert len(classes) == 3, "more classes than expected."
        assert "Character" in classes
        assert "Card" in classes
        assert "Cn" in classes

        # Character class
        assert classes["Character"].name == "Character"
        assert classes["Character"].parent == "Card"
        assert len(classes["Character"].specifications) == 1
        assert "Player" in classes["Character"].specifications
        assert len(classes["Character"].methods) == 1

        assert "Character" in classes["Character"].methods
        method = classes["Character"].methods["Character"]
        assert str(method.return_type) == "Character"
        assert len(method.variables) == 2

        assert "physicalLife" in method.variables
        assert "mentalLife" in method.variables

        for var_name in method.variables:
            variable = method.variables[var_name]
            if var_name == "physicalLife":
                assert variable["type"] == "Int"
                assert not variable["is_array"]
            if var_name == "mental_life":
                assert variable["type"] == "Real"
                assert not variable["is_array"]

        # Card class
        assert classes["Card"].name == "Card"
        assert classes["Card"].parent == "Component"
        assert len(classes["Card"].specifications) == 0
        assert len(classes["Card"].methods) == 1

        assert "Card" in classes["Card"].methods
        method = classes["Card"].methods["Card"]
        assert str(method.return_type) == "Card"
        assert len(method.variables) == 2

        assert "physicalLife" in method.variables
        assert "mentalLife" in method.variables

        for var_name in method.variables:
            variable = method.variables[var_name]
            if var_name == "physicalLife":
                assert variable["type"] == "Int"
                assert not variable["is_array"]
            elif var_name == "mentalLife":
                assert variable["type"] == "Real"
                assert variable["is_array"]
            else:
                assert False

        # Cn class
        assert classes["Cn"].name == "Cn"
        assert classes["Cn"].parent == "Component"
        assert len(classes["Cn"].specifications) == 1
        assert "ComplexNumber" in classes["Cn"].specifications
        assert len(classes["Cn"].methods) == 1

        assert "Cn" in classes["Cn"].methods
        method = classes["Cn"].methods["Cn"]
        assert str(method.return_type) == "Cn"
        assert len(method.variables) == 2

        assert "physicalLife" in method.variables
        assert "mentalLife" in method.variables

        for var_name in method.variables:
            variable = method.variables[var_name]
            if var_name == "physicalLife":
                assert variable["type"] == "Int"
                assert not variable["is_array"]
            elif var_name == "mentalLife":
                assert variable["type"] == "Int"
                assert variable["is_array"]
            else:
                assert False

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
                assert not method.variables["c"]["is_array"]
                assert "r" in method.variables
                assert method.variables["r"]["type"] == "Real"
                assert not method.variables["r"]["is_array"]

        enumerations = master_tables.enumerations
        assert len(enumerations) == 1
        values = enumerations["Days"].values
        assert "MONDAY" in values
        assert values["MONDAY"] == 1
        assert "TUESDAY" in values
        assert values["TUESDAY"] == 2
        assert "WEDNESDAY" in values
        assert values["WEDNESDAY"] == 3
        assert "THURSDAY" in values
        assert values["THURSDAY"] == 4
        assert "FRIDAY" in values
        assert values["FRIDAY"] == 5

    def test_complex_class(self):
        assert general_function("resources/complex_class.mom")

    def test_types(self):
        assert general_function("resources/type_test.mom")
