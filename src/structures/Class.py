from src.structures import Method


class Class:
    GLOBAL_INT_TOP = 4_000
    GLOBAL_REAL_TOP = 5_000
    GLOBAL_BOOLEAN_TOP = 6_000
    GLOBAL_TEXT_TOP = 7_000
    TEMP_INT_TOP = 18_000
    TEMP_REAL_TOP = 20_000
    TEMP_BOOLEAN_TOP = 22_000
    TEMP_TEXT_TOP = 24_000
    CONST_INT_TOP = 26_000
    CONST_REAL_TOP = 28_000
    CONST_TEXT_TOP = 30_000
    CONST_BOOLEAN_TOP = 32_000

    GLOBAL_INT_BOTTOM = 4_999
    GLOBAL_REAL_BOTTOM = 5_999
    GLOBAL_BOOLEAN_BOTTOM = 6_999
    GLOBAL_TEXT_BOTTOM = 9_999
    TEMP_INT_BOTTOM = 19_999
    TEMP_REAL_BOTTOM = 21_999
    TEMP_BOOLEAN_BOTTOM = 23_999
    TEMP_TEXT_BOTTOM = 25_999
    CONST_INT_BOTTOM = 27_999
    CONST_REAL_BOTTOM = 29_999
    CONST_TEXT_BOTTOM = 31_999
    CONST_BOOLEAN_BOTTOM = 32_100

    def __init__(self, class_name: str, class_parent: str, class_specifications: set):
        self._class_name = class_name
        self._class_parent = class_parent
        self._class_specifications = class_specifications
        self._methods = {}
        self.cur_global_int = self.GLOBAL_INT_TOP
        self.cur_global_real = self.GLOBAL_REAL_TOP
        self.cur_global_bool = self.GLOBAL_BOOLEAN_TOP
        self.cur_global_text = self.GLOBAL_TEXT_TOP
        self.cur_temp_int = self.TEMP_INT_TOP
        self.cur_temp_real = self.TEMP_REAL_TOP
        self.cur_temp_bool = self.TEMP_BOOLEAN_TOP
        self.cur_temp_text = self.TEMP_TEXT_TOP
        self.cur_const_int = self.CONST_INT_TOP
        self.cur_const_real = self.CONST_REAL_TOP
        self.cur_const_bool = self.CONST_BOOLEAN_TOP
        self.cur_const_text = self.CONST_TEXT_TOP

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
