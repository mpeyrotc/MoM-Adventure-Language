from antlr4 import *
import sys
from Grammar.MoMLexer import MoMLexer
from Grammar.MoMParser import MoMParser
from ErrorListener import MoMErrorListener

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        fileStream = FileStream(file)
        inputStream = InputStream(fileStream)
        lexer = MoMLexer(inputStream)
        # Add your error listener to the lexer if required
        lexer.removeErrorListeners()
        lexer._listeners = [MoMErrorListener()]
        stream = CommonTokenStream(lexer)
        parser = MoMParser(stream)
        parser._listeners = [MoMErrorListener()]
        tree = parser.program()
    except Exception as e:
        print(e)
        exit(1)

    print("OK")
