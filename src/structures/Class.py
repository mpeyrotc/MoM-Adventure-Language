from src.structures import Method


class Class:
    def __init__(self, class_name: str, class_parent: str, class_specifications: set):
        self._class_name = class_name
        self._class_parent = class_parent
        self._class_specifications = class_specifications
        self._methods = {}

    def add_method(self, method: Method):
        self._methods[method.name] = method

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
