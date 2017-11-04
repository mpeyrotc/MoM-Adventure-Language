from src.structures.SemanticTable import Type


class Method:
    """Represents a method contained within a class.

    It holds a name, a return type, and if required the arguments it receives.
    """

    LOCAL_INT_TOP = 14_000
    LOCAL_REAL_TOP = 15_000
    LOCAL_BOOLEAN_TOP = 16_000
    LOCAL_TEXT_TOP = 17_000
    TEMP_INT_TOP = 18_000
    TEMP_REAL_TOP = 19_000
    TEMP_BOOLEAN_TOP = 20_000
    TEMP_TEXT_TOP = 21_000

    LOCAL_OBJECT_TOP = 60_000
    LOCAL_OBJECT_BOTTOM = 69_999

    LOCAL_INT_BOTTOM = 14_999
    LOCAL_REAL_BOTTOM = 15_999
    LOCAL_BOOLEAN_BOTTOM = 16_999
    LOCAL_TEXT_BOTTOM = 17_999
    TEMP_INT_BOTTOM = 18_999
    TEMP_REAL_BOTTOM = 19_999
    TEMP_BOOLEAN_BOTTOM = 20_999
    TEMP_TEXT_BOTTOM = 21_999

    def __init__(self, name: str, return_type: Type) -> None:
        """The de facto constructor for a method definition.

        :param return_type: the return type for this specific method. It can be any value from the Type enum
            except for Other.
        :param name: a str value that represents the name of this method.
        """
        self._name = name
        self._return_type = return_type
        self._variables = {}
        self._argument_types = []
        self._start_quad = -1
        self.temp_count = 0

        self.cur_local_int = self.LOCAL_INT_TOP
        self.cur_local_real = self.LOCAL_REAL_TOP
        self.cur_local_boolean = self.LOCAL_BOOLEAN_TOP
        self.cur_local_text = self.LOCAL_TEXT_TOP
        self.cur_local_object = self.LOCAL_OBJECT_TOP
        self.cur_temp_int = self.TEMP_INT_TOP
        self.cur_temp_real = self.TEMP_REAL_TOP
        self.cur_temp_boolean = self.TEMP_BOOLEAN_TOP
        self.cur_temp_text = self.TEMP_TEXT_TOP

    def add_argument(self, arg_name: str, arg_type, is_array: bool, address: int, mem_size: int, dim=[], p_type="") -> None:
        """Add argument to variable dictionary along with its type.

        :param dim: Structure representing dimension
        :param p_type: if the argument is of type CLASS, this field holds the name of the class or specification.
        :param address: the virtual address for this argument, according to its type, in the VM.
        :param is_array: a boolean argument that specifies if the argument is an array.
        :param arg_type: the type of the argument, may be simple or complex (a.k.a a super type in the grammar).
        :param arg_name: the name of the argument, must be unique among the rest of the arguments and
            the local variables of the method.
        :param mem_size: size in memory, default 1
        :return: None.
        """
        if arg_name in self._variables:
            raise NameError("Method name already defined within scope.")

        self._variables[arg_name] = {'type': arg_type,
                                     'is_array': is_array,
                                     'address': address,
                                     'mem_size': mem_size,
                                     'dim': dim,
                                     'p_type': p_type}

    def add_argument_type(self, arg_type, is_array: bool):
        self._argument_types.append({"arg_type": arg_type, "is_array": is_array})

    def reset_address_counters(self):
        self.cur_local_int = self.LOCAL_INT_TOP
        self.cur_local_real = self.LOCAL_REAL_TOP
        self.cur_local_boolean = self.LOCAL_BOOLEAN_TOP
        self.cur_local_text = self.LOCAL_TEXT_TOP
        self.cur_temp_int = self.TEMP_INT_TOP
        self.cur_temp_real = self.TEMP_REAL_TOP
        self.cur_temp_boolean = self.TEMP_BOOLEAN_TOP
        self.cur_temp_text = self.TEMP_TEXT_TOP

    @property
    def name(self):
        return self._name

    @property
    def return_type(self):
        return self._return_type

    @property
    def variables(self):
        return self._variables

    @property
    def argument_types(self):
        return self._argument_types

    @property
    def num_of_params(self):
        return len(self._argument_types)

    @property
    def num_local_vars(self):
        return len(self._variables) - len(self._argument_types)

    @property
    def start(self):
        return self._start_quad

    @start.setter
    def start(self, start):
        self._start_quad = start

    @property
    def size(self):
        return self.temp_count + self.num_local_vars + self.num_of_params


__author__ = "Marco A. Peyrot (mpeyrotc)"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "macpeyrot@hotmail.com"
__status__ = "Development"
