import sys

sys.setrecursionlimit(5000)
in_constants = True
in_classes = False
main_called = False

constants = [[], [], [], []]
params = []

class_stack = list()
classes = {}
current_class: str
# noinspection SpellCheckingInspection
quadrupoles = []

counter = 0


class Class:
    methods = {}
    name = ""
    size = []


class Method:
    name = ""
    size = []


class ClassInstance:
    def __init__(self):
        self.memory = [[], [], [], [], []]
        self.method_stack = list()
        self.pc = list()
        self.classes = {}
        self.name = ""


class MethodInstance:
    def __init__(self):
        self.local_memory = [[], [], [], [], []]
        self.temporal_memory = [[], [], [], []]
        self.classes = {}


new_class = list()

CONST_INT_TOP = 22_000
CONST_REAL_TOP = 23_000
CONST_TEXT_TOP = 24_000
CONST_BOOLEAN_TOP = 25_000
CONST_INT_BOTTOM = 22_999
CONST_REAL_BOTTOM = 23_999
CONST_TEXT_BOTTOM = 24_999
CONST_BOOLEAN_BOTTOM = 25_100

GLOBAL_INT_TOP = 10_000
GLOBAL_REAL_TOP = 11_000
GLOBAL_BOOLEAN_TOP = 12_000
GLOBAL_TEXT_TOP = 13_000
GLOBAL_OBJECT_TOP = 50_000
GLOBAL_INT_BOTTOM = 10_999
GLOBAL_REAL_BOTTOM = 11_999
GLOBAL_BOOLEAN_BOTTOM = 12_999
GLOBAL_TEXT_BOTTOM = 13_999
GLOBAL_OBJECT_BOTTOM = 59_999

LOCAL_INT_TOP = 14_000
LOCAL_REAL_TOP = 15_000
LOCAL_BOOLEAN_TOP = 16_000
LOCAL_TEXT_TOP = 17_000
LOCAL_OBJECT_TOP = 60_000
LOCAL_INT_BOTTOM = 14_999
LOCAL_REAL_BOTTOM = 15_999
LOCAL_BOOLEAN_BOTTOM = 16_999
LOCAL_TEXT_BOTTOM = 17_999
LOCAL_OBJECT_BOTTOM = 69_999

TEMP_INT_BOTTOM = 18_999
TEMP_REAL_BOTTOM = 19_999
TEMP_BOOLEAN_BOTTOM = 20_999
TEMP_TEXT_BOTTOM = 21_999
TEMP_INT_TOP = 18_000
TEMP_REAL_TOP = 19_000
TEMP_BOOLEAN_TOP = 20_000
TEMP_TEXT_TOP = 21_000


def is_absolute(address: str) -> bool:
    address = str(address)
    return address.find("$") != -1


def is_indirect(address: str) -> bool:
    return address.find("&") != -1


def is_temporal(address: int) -> bool:
    return TEMP_INT_TOP <= address <= TEMP_TEXT_BOTTOM


def is_local(address: int) -> bool:
    return LOCAL_INT_TOP <= address <= LOCAL_TEXT_BOTTOM or LOCAL_OBJECT_TOP <= address <= LOCAL_OBJECT_BOTTOM


def is_global(address: int) -> bool:
    return GLOBAL_INT_TOP <= address <= GLOBAL_TEXT_BOTTOM or GLOBAL_OBJECT_TOP <= address <= GLOBAL_OBJECT_BOTTOM


def is_constant(address: int) -> bool:
    return CONST_INT_TOP <= address <= CONST_BOOLEAN_BOTTOM


def get_type(address: int) -> str:
    if is_constant(int(address)):
        if CONST_INT_TOP <= address <= CONST_INT_BOTTOM:
            return "Int"
        if CONST_REAL_TOP <= address <= CONST_REAL_BOTTOM:
            return "Real"
        if CONST_TEXT_TOP <= address <= CONST_TEXT_BOTTOM:
            return "Text"
        else:
            return "Bool"
    elif is_global(int(address)):
        if GLOBAL_INT_TOP <= address <= GLOBAL_INT_BOTTOM:
            return "Int"
        if GLOBAL_REAL_TOP <= address <= GLOBAL_REAL_BOTTOM:
            return "Real"
        if GLOBAL_TEXT_TOP <= address <= GLOBAL_TEXT_BOTTOM:
            return "Text"
        if GLOBAL_BOOLEAN_TOP <= address <= GLOBAL_BOOLEAN_BOTTOM:
            return "Bool"
        else:
            return "Obj"
    elif is_local(int(address)):
        if LOCAL_INT_TOP <= address <= LOCAL_INT_BOTTOM:
            return "Int"
        if LOCAL_REAL_TOP <= address <= LOCAL_REAL_BOTTOM:
            return "Real"
        if LOCAL_TEXT_TOP <= address <= LOCAL_TEXT_BOTTOM:
            return "Text"
        if LOCAL_BOOLEAN_TOP <= address <= LOCAL_BOOLEAN_BOTTOM:
            return "Bool"
        else:
            return "Obj"
    elif is_temporal(int(address)):
        if TEMP_INT_TOP <= address <= TEMP_INT_BOTTOM:
            return "Int"
        if TEMP_REAL_TOP <= address <= TEMP_REAL_BOTTOM:
            return "Real"
        if TEMP_TEXT_TOP <= address <= TEMP_TEXT_BOTTOM:
            return "Text"
        else:
            return "Bool"
    else:
        raise IndexError("No memory location defined.")


def get_constant(address: int):
    if CONST_INT_TOP <= address <= CONST_INT_BOTTOM:
        return constants[0][address - CONST_INT_TOP]
    if CONST_REAL_TOP <= address <= CONST_REAL_BOTTOM:
        return constants[1][address - CONST_REAL_TOP]
    if CONST_TEXT_TOP <= address <= CONST_TEXT_BOTTOM:
        return constants[2][address - CONST_TEXT_TOP]
    else:
        return constants[3][address - CONST_BOOLEAN_TOP]


def get_temporal(mi, address: int):
    if TEMP_INT_TOP <= address <= TEMP_INT_BOTTOM:
        return mi.temporal_memory[0][address - TEMP_INT_TOP]
    if TEMP_REAL_TOP <= address <= TEMP_REAL_BOTTOM:
        return mi.temporal_memory[1][address - TEMP_REAL_TOP]
    if TEMP_TEXT_TOP <= address <= TEMP_TEXT_BOTTOM:
        return mi.temporal_memory[2][address - TEMP_TEXT_TOP]
    else:
        return mi.temporal_memory[3][address - TEMP_BOOLEAN_TOP]


def get_global(ci, address: int):
    if GLOBAL_INT_TOP <= address <= GLOBAL_INT_BOTTOM:
        return ci.memory[0][address - GLOBAL_INT_TOP]
    if GLOBAL_REAL_TOP <= address <= GLOBAL_REAL_BOTTOM:
        return ci.memory[1][address - GLOBAL_REAL_TOP]
    if GLOBAL_TEXT_TOP <= address <= GLOBAL_TEXT_BOTTOM:
        return ci.memory[2][address - GLOBAL_TEXT_TOP]
    if GLOBAL_BOOLEAN_TOP <= address <= GLOBAL_BOOLEAN_BOTTOM:
        return ci.memory[3][address - GLOBAL_BOOLEAN_TOP]
    else:
        return ci.memory[4][address - GLOBAL_OBJECT_TOP]


def get_local(mi, address: int):
    if LOCAL_INT_TOP <= address <= LOCAL_INT_BOTTOM:
        return mi.local_memory[0][address - LOCAL_INT_TOP]
    if LOCAL_REAL_TOP <= address <= LOCAL_REAL_BOTTOM:
        return mi.local_memory[1][address - LOCAL_REAL_TOP]
    if LOCAL_TEXT_TOP <= address <= LOCAL_TEXT_BOTTOM:
        return mi.local_memory[2][address - LOCAL_TEXT_TOP]
    if LOCAL_BOOLEAN_TOP <= address <= LOCAL_BOOLEAN_BOTTOM:
        return mi.local_memory[3][address - LOCAL_BOOLEAN_TOP]
    else:
        return mi.local_memory[4][address - LOCAL_OBJECT_TOP]


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


def set_global(ci, address: int, value) -> None:
    if GLOBAL_INT_TOP <= address <= GLOBAL_INT_BOTTOM:
        ci.memory[0][address - GLOBAL_INT_TOP] = value
    elif GLOBAL_REAL_TOP <= address <= GLOBAL_REAL_BOTTOM:
        ci.memory[1][address - GLOBAL_REAL_TOP] = value
    elif GLOBAL_TEXT_TOP <= address <= GLOBAL_TEXT_BOTTOM:
        ci.memory[2][address - GLOBAL_TEXT_TOP] = value
    elif GLOBAL_BOOLEAN_TOP <= address <= GLOBAL_BOOLEAN_BOTTOM:
        ci.memory[3][address - GLOBAL_BOOLEAN_TOP] = value
    else:
        ci.memory[4][address - GLOBAL_OBJECT_TOP] = value


def set_local(mi, address: int, value) -> None:
    if LOCAL_INT_TOP <= address <= LOCAL_INT_BOTTOM:
        mi.local_memory[0][address - LOCAL_INT_TOP] = value
    elif LOCAL_REAL_TOP <= address <= LOCAL_REAL_BOTTOM:
        mi.local_memory[1][address - LOCAL_REAL_TOP] = value
    elif LOCAL_TEXT_TOP <= address <= LOCAL_TEXT_BOTTOM:
        mi.local_memory[2][address - LOCAL_TEXT_TOP] = value
    elif LOCAL_BOOLEAN_TOP <= address <= LOCAL_BOOLEAN_BOTTOM:
        mi.local_memory[3][address - LOCAL_BOOLEAN_TOP] = value
    else:
        mi.local_memory[4][address - LOCAL_OBJECT_TOP] = value


def set_temporal(mi, address: int, value) -> None:
    if TEMP_INT_TOP <= address <= TEMP_INT_BOTTOM:
        mi.temporal_memory[0][address - TEMP_INT_TOP] = value
    elif TEMP_REAL_TOP <= address <= TEMP_REAL_BOTTOM:
        mi.temporal_memory[1][address - TEMP_REAL_TOP] = value
    elif TEMP_TEXT_TOP <= address <= TEMP_TEXT_BOTTOM:
        mi.temporal_memory[2][address - TEMP_TEXT_TOP] = value
    else:
        mi.temporal_memory[3][address - TEMP_BOOLEAN_TOP] = value


def do_cast(address: int, value: str):
    if CONST_INT_TOP <= address <= CONST_INT_BOTTOM or \
                            LOCAL_INT_TOP <= address <= LOCAL_INT_BOTTOM or \
                            GLOBAL_INT_TOP <= address <= GLOBAL_INT_BOTTOM or \
                            TEMP_INT_TOP <= address <= TEMP_INT_BOTTOM:
        return int(value)

    if CONST_REAL_TOP <= address <= CONST_REAL_BOTTOM or LOCAL_REAL_TOP <= address <= LOCAL_REAL_BOTTOM or \
                            GLOBAL_REAL_TOP <= address <= GLOBAL_REAL_BOTTOM or \
                            TEMP_REAL_TOP <= address <= TEMP_REAL_BOTTOM:
        return float(value)

    if CONST_BOOLEAN_TOP <= address <= CONST_BOOLEAN_BOTTOM or LOCAL_BOOLEAN_TOP <= address <= LOCAL_BOOLEAN_BOTTOM or \
                            GLOBAL_BOOLEAN_TOP <= address <= GLOBAL_BOOLEAN_BOTTOM or \
                            TEMP_BOOLEAN_TOP <= address <= TEMP_BOOLEAN_BOTTOM:
        if type(value) == bool:
            return value
        else:
            return value == "!@#$%^&*()"

    return value


def get_raw_value_one(left_arg: str):
    if not left_arg == "":
        if is_constant(int(left_arg)):
            left_value = get_constant(int(left_arg))
        elif is_global(int(left_arg)):
            left_value = get_global(class_stack[-1], int(left_arg))
        elif is_local(int(left_arg)):
            left_value = get_local(class_stack[-1].method_stack[-1], int(left_arg))
        elif is_temporal(int(left_arg)):
            left_value = get_temporal(class_stack[-1].method_stack[-1], int(left_arg))
        else:
            raise IndexError("No memory location defined.")

        return left_value


def get_raw_value(left_arg: str, right_arg: str):
    left_arg = str(left_arg)
    right_arg = str(right_arg)
    left_value = None
    right_value = None
    left_is_absolute = left_arg.find("$")
    right_is_absolute = right_arg.find("$")

    if not left_arg == "":
        if not left_is_absolute == -1:
            left_value = left_arg[left_is_absolute + 1:].strip()
        elif is_constant(int(left_arg)):
            left_value = get_constant(int(left_arg))
        elif is_global(int(left_arg)):
            left_value = get_global(class_stack[-1], int(left_arg))
        elif is_local(int(left_arg)):
            left_value = get_local(class_stack[-1].method_stack[-1], int(left_arg))
        elif is_temporal(int(left_arg)):
            left_value = get_temporal(class_stack[-1].method_stack[-1], int(left_arg))
        else:
            raise IndexError("No memory location defined.")

    if not right_arg == "":
        if not right_is_absolute == -1:
            right_value = right_arg[right_is_absolute + 1:].strip()
        elif is_constant(int(right_arg)):
            right_value = get_constant(int(right_arg))
        elif is_global(int(right_arg)):
            right_value = get_global(class_stack[-1], int(right_arg))
        elif is_local(int(right_arg)):
            right_value = get_local(class_stack[-1].method_stack[-1], int(right_arg))
        elif is_temporal(int(right_arg)):
            right_value = get_temporal(class_stack[-1].method_stack[-1], int(right_arg))
        else:
            raise IndexError("No memory location defined.")

    return left_value, right_value


# noinspection PyShadowingNames
def operation(op: int, left, right, dest):
    global main_called, new_class, params

    if op == 1:  # PLUS
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if type(left_value) is str:
            left_value = left_value[1:-1]

        if type(right_value) is str:
            right_value = right_value[1:-1]

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value + right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value + right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value + right_value)
    elif op == 2:  # MINUS
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value - right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value - right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value - right_value)
    elif op == 3:  # TIMES
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value * right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value * right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value * right_value)
    elif op == 4:  # DIVIDES
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value / right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value / right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value / right_value)
    elif op == 5:  # AND
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value and right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value and right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value and right_value)
    elif op == 6:  # OR
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value or right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value or right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value or right_value)
    elif op == 7:  # NOT
        # TODO: implement in listener and here.
        pass
    elif op == 8:  # LESS_THAN
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value < right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value < right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value < right_value)
    elif op == 9:  # LESS_EQUAL
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value <= right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value <= right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value <= right_value)
    elif op == 10:  # GREATER_THAN
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value > right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value > right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value > right_value)
    elif op == 11:  # GREATER_EQUAL
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value >= right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value >= right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value >= right_value)
    elif op == 12:  # EQUAL_EQUAL
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(right):
            right = get_raw_value_one(right[right.find("&") + 1:].strip())
        left_value, right_value = get_raw_value(left, right)
        if not is_absolute(left):
            left_value = do_cast(int(left), left_value)
        else:
            left_value = int(left[left.find("$") + 1:].strip())
        if not is_absolute(right):
            right_value = do_cast(int(right), right_value)
        else:
            right_value = int(right[right.find("$") + 1:].strip())

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), left_value == right_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), left_value == right_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value == right_value)
    elif op == 13:  # OPEN_PAREN
        pass
    elif op == 14:  # CLOSE_PAREN
        pass
    elif op == 15:  # EQUAL
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())
        if is_indirect(dest):
            dest = get_raw_value_one(dest[dest.find("&") + 1:].strip())
        if len(new_class) == 0 or (not LOCAL_OBJECT_TOP <= int(dest) <= LOCAL_OBJECT_BOTTOM or GLOBAL_OBJECT_TOP <= int(
                dest) <= GLOBAL_OBJECT_BOTTOM):
            if is_constant(int(left)):
                left_value = get_constant(int(left))
            elif is_global(int(left)):
                left_value = get_global(class_stack[-1], int(left))
            elif is_local(int(left)):
                left_value = get_local(class_stack[-1].method_stack[-1], int(left))
            elif is_temporal(int(left)):
                left_value = get_temporal(class_stack[-1].method_stack[-1], int(left))
            else:
                raise IndexError("No memory location defined.")

            if is_global(int(dest)):
                set_global(class_stack[-1], int(dest), left_value)
            elif is_local(int(dest)):
                set_local(class_stack[-1].method_stack[-1], int(dest), left_value)
            elif is_temporal(int(dest)):
                set_temporal(class_stack[-1].method_stack[-1], int(dest), left_value)
        else:
            if is_local(int(dest)):
                class_stack[-1].method_stack[-1].classes[int(dest)] = new_class.pop()
            else:
                class_stack[-1].classes[int(dest)] = new_class.pop()
    elif op == 16:  # GO_TO_FALSE
        left_value, _ = get_raw_value(left, right)
        left_value = do_cast(int(left), left_value)

        if not left_value:
            class_stack[-1].pc[-1] = int(dest) - 1
    elif op == 17:  # GO_TO_TRUE
        left_value, _ = get_raw_value(left, right)
        left_value = do_cast(int(left), left_value)

        if left_value:
            class_stack[-1].pc[-1] = int(dest) - 1
    elif op == 18:  # GO_TO
        class_stack[-1].pc[-1] = int(dest) - 1
    elif op == 19:  # RETURN
        class_stack[-1].pc.pop()
        class_stack[-1].method_stack.pop()
        if len(class_stack[-1].pc) == 0:
            class_stack.pop()

        if len(class_stack) == 0:
            exit(22)
    elif op == 20:  # ERA
        pass
    elif op == 21:  # PARAM
        # print("PARAM = " + str(class_stack[-1].method_stack[-1].local_memory[0]))
        params.append(int(left))
    elif op == 22:  # GO_SUB
        if ":" in left:  # composition call
            class_var = int(left[:left.find(":")])
            # noinspection PyShadowingNames
            left = left[left.find(":") + 1:]
            if is_local(class_var):
                if class_var not in class_stack[-1].method_stack[-1].classes:
                    raise RuntimeError("No class instance found.")

                class_stack.append(class_stack[-1].method_stack[-1].classes[class_var])
            else:
                if class_var not in class_stack[-1].classes:
                    raise RuntimeError("No class instance found.")

                class_stack.append(class_stack[-1].classes[class_var])

        mi = MethodInstance()
        class_stack[-1].pc.append(int(dest) - 1)
        class_stack[-1].method_stack.append(mi)

        for j, s in enumerate(classes[left].methods[right].size):
            for k in range(s):
                if j <= 4:
                    mi.local_memory[j].append(-1)
                else:
                    mi.temporal_memory[j - 5].append(-1)

        if len(params) > 0:
            c_i = c_r = c_t = c_b = c_o = 0
            for param_dir in params:
                dir_type = get_type(param_dir)
                if is_constant(int(param_dir)):
                    left_value = get_constant(int(param_dir))
                elif is_global(int(param_dir)):
                    left_value = get_global(class_stack[-1], int(param_dir))
                elif is_local(int(param_dir)):
                    left_value = get_local(class_stack[-1].method_stack[-2], int(param_dir))
                elif is_temporal(int(param_dir)):
                    left_value = get_temporal(class_stack[-1].method_stack[-2], int(param_dir))
                else:
                    raise IndexError("No memory location defined.")

                if dir_type == "Int":
                    class_stack[-1].method_stack[-1].local_memory[0][c_i] = left_value
                    c_i += 1
                elif dir_type == "Real":
                    class_stack[-1].method_stack[-1].local_memory[1][c_r] = left_value
                    c_r += 1
                elif dir_type == "Text":
                    class_stack[-1].method_stack[-1].local_memory[2][c_t] = left_value
                    c_t += 1
                elif dir_type == "Bool":
                    class_stack[-1].method_stack[-1].local_memory[3][c_b] = left_value
                    c_b += 1
                else:
                    class_stack[-1].method_stack[-1].classes[int(param_dir)] = class_stack[-1].method_stack[-2].classes[int(param_dir)]
                    class_stack[-1].method_stack[-1].local_memory[4][c_o] = left_value
                    c_o += 1

            params = []

    elif op == 23:  # GO_CONSTRUCTOR
        if len(class_stack) == 0:
            # Create class instance
            ci = ClassInstance()
            ci.name = left

            for j, s in enumerate(classes[ci.name].size):
                for k in range(s):
                    ci.memory[j].append(-1)

            class_stack.append(ci)

            # Call constructor
            mi = MethodInstance()
            # Define pc for constructor
            ci.pc.append(0)
            ci.pc.append(int(dest) - 1)
            ci.method_stack.append(mi)
            ci.method_stack.append(mi)

            for j, s in enumerate(classes[left].methods[right].size):
                for k in range(s):
                    if j <= 4:
                        mi.local_memory[j].append(-1)
                    else:
                        mi.temporal_memory[j - 5].append(-1)
        else:
            ci_child = ClassInstance()
            ci_child.name = left

            for j, s in enumerate(classes[ci_child.name].size):
                for k in range(s):
                    ci_child.memory[j].append(-1)

            # Call constructor
            mi = MethodInstance()
            # Define pc for constructor
            ci_child.pc.append(int(dest) - 1)
            ci_child.method_stack.append(mi)

            for j, s in enumerate(classes[left].methods[right].size):
                for k in range(s):
                    if j <= 4:
                        mi.local_memory[j].append(-1)
                    else:
                        mi.temporal_memory[j - 5].append(-1)

            new_class.append(ci_child)

    elif op == 24:  # ERA_CONSTRUCTOR
        pass
    elif op == 25:  # END
        pass
    elif op == 26:  # END_CLASS
        pass
    elif op == 27:  # WRITE
        if is_indirect(dest):
            dest = get_raw_value_one(dest[dest.find("&") + 1:].strip())
        if is_constant(int(dest)):
            value = get_constant(int(dest))
        elif is_global(int(dest)):
            value = get_global(class_stack[-1], int(dest))
        elif is_local(int(dest)):
            value = get_local(class_stack[-1].method_stack[-1], int(dest))
        elif is_temporal(int(dest)):
            value = get_temporal(class_stack[-1].method_stack[-1], int(dest))
        else:
            raise TypeError("Type cannot be printed.")

        value = do_cast(int(dest), str(value))

        if type(value) is str:
            print(value[1:-1], end='')
        else:
            print(value, end='')
    elif op == 28:  # READ_INT
        new_value = input()

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), int(new_value))
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), int(new_value))
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), int(new_value))
    elif op == 29:  # READ_REAL
        new_value = input()

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), float(new_value))
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), float(new_value))
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), float(new_value))
    elif op == 30:  # READ_TEXT
        new_value = input()

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), new_value)
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), new_value)
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), new_value)
    elif op == 31:  # READ_BOOL
        new_value = input()

        if is_global(int(dest)):
            set_global(class_stack[-1], int(dest), new_value.lower() == "true")
        elif is_local(int(dest)):
            set_local(class_stack[-1].method_stack[-1], int(dest), new_value.lower() == "true")
        elif is_temporal(int(dest)):
            set_temporal(class_stack[-1].method_stack[-1], int(dest), new_value.lower() == "true")
    elif op == 32:  # OPEN_SPAREN
        pass
    elif op == 33:  # CLOSE_SPAREN
        pass
    elif op == 34:  # VERIFY
        if is_indirect(left):
            left = get_raw_value_one(left[left.find("&") + 1:].strip())

        if is_constant(int(left)):
            value = get_constant(int(left))
        elif is_global(int(left)):
            value = get_global(class_stack[-1], int(left))
        elif is_local(int(left)):
            value = get_local(class_stack[-1].method_stack[-1], int(left))
        elif is_temporal(int(left)):
            value = get_temporal(class_stack[-1].method_stack[-1], int(left))
        else:
            raise TypeError("Type cannot be verified.")

        if int(right) <= int(value) < int(dest):
            pass
        else:
            raise TypeError("Error, Out of bounds")

    elif op == 35:  # WRITE_LINE
        if is_indirect(dest):
            dest = get_raw_value_one(dest[dest.find("&") + 1:].strip())
        if is_constant(int(dest)):
            value = get_constant(int(dest))
        elif is_global(int(dest)):
            value = get_global(class_stack[-1], int(dest))
        elif is_local(int(dest)):
            value = get_local(class_stack[-1].method_stack[-1], int(dest))
        elif is_temporal(int(dest)):
            value = get_temporal(class_stack[-1].method_stack[-1], int(dest))
        else:
            raise TypeError("Type cannot be printed.")
        value = do_cast(int(dest), str(value))

        if type(value) is str:
            print(value[1:-1])
        else:
            print(value)
    elif op == 36:  # GO_MAIN
        main_called = True

        mi = MethodInstance()
        class_stack[-1].pc.append(int(dest) - 1)
        class_stack[-1].method_stack.append(mi)

        for j, s in enumerate(classes[left].methods[right].size):
            for k in range(s):
                if j <= 4:
                    mi.local_memory[j].append(-1)
                else:
                    mi.temporal_memory[j - 5].append(-1)
    elif op == 37:  # RETRIEVE
        class_var = int(left[:left.find(":")])
        # noinspection PyShadowingNames
        left = left[left.find(":") + 1:]

        if is_local(class_var):
            if class_var not in class_stack[-1].method_stack[-1].classes:
                raise RuntimeError("No class instance found.")

            var = get_global(class_stack[-1].method_stack[-1].classes[class_var], int(left))
            set_temporal(class_stack[-1].method_stack[-1], int(dest), var)
        else:
            if class_var not in class_stack[-1].classes:
                raise RuntimeError("No class instance found.")

            raise RuntimeError("SHOULD NEVER BE CALLED")
    else:
        raise NameError("operation " + str(op) + " not recognized.")

    class_stack[-1].pc[-1] += 1
    op, left, right, destination = quadrupoles[class_stack[-1].pc[-1]]
    operation(int(op), left, right, destination)


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
                        name, num_methods, i, r, t, b, o = line.split(',')
                        num_methods = int(num_methods)
                        c = Class()
                        c.name = name
                        c.size = [int(i), int(r), int(t), int(b), int(o)]
                        classes[name] = c
                    else:
                        name, size, li, lr, lt, lb, lo, ti, tr, tt, tb = line.split(',')
                        m = Method()
                        m.name = name
                        m.size = [int(li), int(lr), int(lt), int(lb), int(lo), int(ti), int(tr), int(tt), int(tb)]
                        c.methods[name] = m

                        num_methods -= 1
            else:
                quadrupoles.append(line.split(","))

        op, left, right, destination = quadrupoles[0]
        operation(int(op), left, right, destination)
