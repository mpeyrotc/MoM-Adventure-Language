from src.structures import Method


class Specification:
    """This class contains the metadata for the specification structure of the
    MoM language.

    It holds the method signatures that will be acquired by the classes
    that implement a specific implementation.
    """

    def __init__(self, name: str):
        self._name = name
        self._methods = {}

    def add_method(self, method: Method) -> None:
        """Adds a method to this specification's group of registered
        methods.

        :param method: the method object to be added
        :return: None.
        """
        self._methods[method.name] = method

    @property
    def name(self):
        return self._name

    @property
    def methods(self):
        return self._methods
