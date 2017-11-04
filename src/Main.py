import sys

import ErrorListener
from antlr4 import *
from grammar import MoMLexer
from grammar import MoMParser
import src.MasterTables as master_tables

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
        listener = MoMListener()
        walker.walk(listener, tree)

        # start writing .obj file for virtual machine
        f = open("temp.obj", "w")

        for constant in master_tables.constants:
            address = master_tables.constants[constant]
            f.write(str(address) + "," + str(constant) + "\n")

        f.write("%%\n")

        for class_name in master_tables.classes:
            c = master_tables.classes[class_name]
            f.write(class_name + "," + str(c.size) + "," + str(len(c.methods)) + "\n")

            for method_name in c.methods:
                m = c.methods[method_name]
                f.write(method_name + "," + str(m.size) + "\n")

        f.write("%%\n")

        for quad in listener.quads:
            op = str(int(quad.operator))

            if quad.left_operand is None:
                left = ""
            else:
                left = str(quad.left_operand)

            if quad.right_operand is None:
                right = ""
            else:
                right = str(quad.right_operand)

            if quad.result is None:
                destination = ""
            else:
                destination = str(quad.result)

            f.write(op + "," + left + "," + right + "," + destination + "\n")

        f.close()
    except Exception as e:
        print(e.with_traceback())
        exit(1)

    print("OK")
