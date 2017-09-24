from antlr4 import *
from src.ErrorListener import ErrorListener
from src.grammar import MoMLexer
from src.grammar import MoMParser


class TestGrammar(object):
    def test_single_class(self):
        try:
            file = "../resources/single_class.mom"
            file_stream = FileStream(file)
            input_stream = InputStream(str(file_stream))
            lexer = MoMLexer(input_stream)
            # Add your error listener to the lexer if required
            lexer.removeErrorListeners()
            lexer._listeners = [ErrorListener.MoMErrorListener()]
            stream = CommonTokenStream(lexer)
            parser = MoMParser(stream)
            parser._listeners = [ErrorListener.ErrMoMErrorListener()]
            parser.program()
            assert True
        except Exception:
            # do nothing
            pass

        assert False


