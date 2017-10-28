from src.structures import Method


class Class:
    GLOBAL_INT_TOP = 10_000
    GLOBAL_REAL_TOP = 11_000
    GLOBAL_BOOLEAN_TOP = 12_000
    GLOBAL_TEXT_TOP = 13_000

    CONST_INT_TOP = 22_000
    CONST_REAL_TOP = 23_000
    CONST_TEXT_TOP = 24_000
    CONST_BOOLEAN_TOP = 25_000

    GLOBAL_INT_BOTTOM = 10_999
    GLOBAL_REAL_BOTTOM = 11_999
    GLOBAL_BOOLEAN_BOTTOM = 12_999
    GLOBAL_TEXT_BOTTOM = 13_999

    CONST_INT_BOTTOM = 22_999
    CONST_REAL_BOTTOM = 23_999
    CONST_TEXT_BOTTOM = 24_999
    CONST_BOOLEAN_BOTTOM = 25_100

    def __init__(self, class_name: str, class_parent: str, class_specifications: set):
        self._class_name = class_name
        self._class_parent = class_parent
        self._class_specifications = class_specifications
        self._methods = {}
        self._variables = {}
        self.cur_global_int = self.GLOBAL_INT_TOP
        self.cur_global_real = self.GLOBAL_REAL_TOP
        self.cur_global_boolean = self.GLOBAL_BOOLEAN_TOP
        self.cur_global_text = self.GLOBAL_TEXT_TOP
        self.cur_const_int = self.CONST_INT_TOP
        self.cur_const_real = self.CONST_REAL_TOP
        self.cur_const_boolean = self.CONST_BOOLEAN_TOP
        self.cur_const_text = self.CONST_TEXT_TOP

    def add_method(self, method: Method):
        self._methods[method.name] = method

    def reset_address_counters(self):
        self.cur_global_int = self.GLOBAL_INT_TOP
        self.cur_global_real = self.GLOBAL_REAL_TOP
        self.cur_global_boolean = self.GLOBAL_BOOLEAN_TOP
        self.cur_global_text = self.GLOBAL_TEXT_TOP
        self.cur_const_int = self.CONST_INT_TOP
        self.cur_const_real = self.CONST_REAL_TOP
        self.cur_const_boolean = self.CONST_BOOLEAN_TOP
        self.cur_const_text = self.CONST_TEXT_TOP

    def add_argument(self, arg_name: str, arg_type, is_array: bool, address: int, mem_size: int) -> None:
        """Add argument to variable dictionary along with its type.

        :param address: the virtual address for this argument, according to its type, in the VM.
        :param is_array: a boolean argument that specifies if the argument is an array.
        :param arg_type: the type of the argument, may be simple or complex (a.k.a a super type in the grammar).
        :param arg_name: the name of the argument, must be unique among the rest of the arguments and
            the local variables of the method.
        :param mem_size : the size in memory, by default 1
        :return: None.
        """
        if arg_name in self._variables:
            raise NameError("Variable name in class already defined within scope.")

        self._variables[arg_name] = {'name': arg_name,
                                     'type': arg_type,
                                     'is_array': is_array,
                                     'address': address,
                                     'mem_size': mem_size}

    @property
    def name(self):
        return self._class_name

    @property
    def parent(self):
        return self._class_parent

    @property
    def specifications(self):
        return self._class_specifications

    @property
    def methods(self):
        return self._methods

    @property
    def variables(self):
        return self._variables
