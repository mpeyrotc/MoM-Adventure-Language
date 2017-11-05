from src.structures.SemanticTable import Operator, Operation

in_constants = True
in_classes = False
constants = [[], [], [], []]
call_stack = list()
classes = {}

CONST_INT_TOP = 22_000
CONST_REAL_TOP = 23_000
CONST_TEXT_TOP = 24_000
CONST_BOOLEAN_TOP = 25_000
CONST_INT_BOTTOM = 22_999
CONST_REAL_BOTTOM = 23_999
CONST_TEXT_BOTTOM = 24_999
CONST_BOOLEAN_BOTTOM = 25_100


def is_constant(address: int) -> bool:
    return CONST_INT_TOP <= address <= CONST_BOOLEAN_BOTTOM


def get_constant(address: int):
    if CONST_INT_TOP <= address <= CONST_INT_BOTTOM:
        return constants[0][address - CONST_INT_TOP]
    if CONST_REAL_TOP <= address <= CONST_REAL_BOTTOM:
        return constants[1][address - CONST_REAL_TOP]
    if CONST_TEXT_TOP <= address <= CONST_TEXT_BOTTOM:
        return constants[2][address - CONST_TEXT_TOP][1:-1]
    else:
        return constants[3][address - CONST_BOOLEAN_TOP]


def set_constant(address: int, value) -> None:
    if CONST_INT_TOP <= address <= CONST_INT_BOTTOM:
        constants[0].append(-1)
        constants[0][address - CONST_INT_TOP] = value
    elif CONST_REAL_TOP <= address <= CONST_REAL_BOTTOM:
        constants[1].append(-1)
        constants[1][address - CONST_REAL_TOP] = value
    elif CONST_TEXT_TOP <= address <= CONST_TEXT_BOTTOM:
        constants[2].append(-1)
        constants[2][address - CONST_TEXT_TOP] = value
    else:
        constants[3].append(-1)
        constants[3][address - CONST_BOOLEAN_TOP] = value


def operation(op: int, left, right, dest):
    if op == 1:  # PLUS
        pass
    elif op == 2:  # MINUS
        pass
    elif op == 3:  # TIMES
        pass
    elif op == 4:  # DIVIDES
        pass
    elif op == 5:  # AND
        pass
    elif op == 6:  # OR
        pass
    elif op == 7:  # NOT
        pass
    elif op == 8:  # LESS_THAN
        pass
    elif op == 9:  # LESS_EQUAL
        pass
    elif op == 10:  # GREATER_THAN
        pass
    elif op == 11:  # GREATER_EQUAL
        pass
    elif op == 12:  # EQUAL_EQUAL
        pass
    elif op == 13:  # OPEN_PAREN
        pass
    elif op == 14:  # CLOSE_PAREN
        pass
    elif op == 15:  # EQUAL
        pass
    elif op == 16:  # GO_TO_FALSE
        pass
    elif op == 17:  # GO_TO_TRUE
        pass
    elif op == 18:  # GO_TO
        pass
    elif op == 19:  # RETURN
        pass
    elif op == 20:  # ERA
        pass
    elif op == 21:  # PARAM
        pass
    elif op == 22:  # GO_SUB
        pass
    elif op == 23:  # GO_CONSTRUCTOR
        pass
    elif op == 24:  # ERA_CONSTRUCTOR
        pass
    elif op == 25:  # END
        pass
    elif op == 26:  # END_CLASS
        pass
    elif op == 27:  # WRITE
        print(get_constant(int(dest)))
    elif op == 28:  # READ_INT
        pass
    elif op == 29:  # READ_REAL
        pass
    elif op == 30:  # READ_TEXT
        pass
    elif op == 31:  # READ_BOOL
        pass
    elif op == 32:  # OPEN_SPAREN
        pass
    elif op == 33:  # CLOSE_SPAREN
        pass
    elif op == 34:  # VERIFY
        pass
    else:
        raise NameError("operation " + str(op) + " not recognized.")


class Class:
    methods = {}
    name = ""
    size = 0
    call_stack = list()


class Method:
    name = ""
    size = 0


if __name__ == "__main__":
    with open("temp.obj") as f:
        c = None
        num_methods = 0
        for line in f:
            line = line.strip()

            if in_constants:
                if line == "%%":
                    in_constants = False
                    in_classes = True
                else:
                    # noinspection SpellCheckingInspection
                    addr, val = line.split(',')
                    set_constant(int(addr), val)
            elif in_classes:
                if line == "%%":
                    in_classes = False
                else:
                    if num_methods == 0:
                        name, size, num_methods = line.split(',')
                        num_methods = int(num_methods)
                        c = Class()
                        c.size = int(size)
                        c.name = name
                        classes[name] = c
                    else:
                        name, size = line.split(',')
                        m = Method()
                        m.name = name
                        m.size = int(size)
                        c.methods[name] = m

                        num_methods -= 1
            else:
                op, left, right, destination = line.split(",")
                operation(int(op), left, right, destination)
