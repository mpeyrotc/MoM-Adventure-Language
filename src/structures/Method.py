from src.structures.SemanticTable import Type


class Method:
    """Represents a method contained within a class.

    It holds a name, a return type, and if required the arguments it receives.
    """

    LOCAL_INT_TOP = 10_000
    LOCAL_REAL_TOP = 12_000
    LOCAL_BOOLEAN_TOP = 14_000
    LOCAL_TEXT_TOP = 16_000

    LOCAL_INT_BOTTOM = 11_999
    LOCAL_REAL_BOTTOM = 13_999
    LOCAL_BOOLEAN_BOTTOM = 15_999
    LOCAL_TEXT_BOTTOM = 17_999

    def __init__(self, name: str, return_type: Type) -> None:
        """The de facto constructor for a method definition.

        :param return_type: the return type for this specific method. It can be any value from the Type enum
            except for Other.
        :param name: a str value that represents the name of this method.
        """
        self._name = name
        self._return_type = return_type
        self._variables = {}

    def add_argument(self, arg_name: str, arg_type, is_array: bool) -> None:
        """Add argument to variable dictionary along with its type.

        :param is_array: a boolean argument that specifies if the argument is an array.
        :param arg_type: the type of the argument, may be simple or complex (a.k.a a super type in the grammar).
        :param arg_name: the name of the argument, must be unique among the rest of the arguments and
            the local variables of the method.
        :return: None.
        """
        if arg_name in self._variables:
            raise NameError("Method name already defined within scope.")

        self._variables[arg_name] = {'type': arg_type,
                                     'is_array': is_array}

    @property
    def name(self):
        return self._name

    @property
    def return_type(self):
        return self._return_type

    @property
    def variables(self):
        return self._variables


__author__ = "Marco A. Peyrot (mpeyrotc)"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "macpeyrot@hotmail.com"
__status__ = "Development"
