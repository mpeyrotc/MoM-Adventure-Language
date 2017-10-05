import sys

import ErrorListener
from antlr4 import *
from grammar import MoMLexer
from grammar import MoMParser

from src.grammar.MoMListener import MoMListener

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        file_stream = FileStream(file)
        input_stream = InputStream(str(file_stream))
        lexer = MoMLexer.MoMLexer(input_stream)
        # Add your error listener to the lexer if required
        lexer.removeErrorListeners()
        lexer._listeners = [ErrorListener.MoMErrorListener()]
        stream = CommonTokenStream(lexer)
        parser = MoMParser.MoMParser(stream)
        parser._listeners = [ErrorListener.MoMErrorListener()]
        tree = parser.program()

        walker = ParseTreeWalker()
        walker.walk(MoMListener(), tree)
    except Exception as e:
        print(e)
        exit(1)

    print("OK")
