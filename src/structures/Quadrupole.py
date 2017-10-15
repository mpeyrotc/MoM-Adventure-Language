from src.structures.SemanticTable import Operator, Operation


class Quadrupole:
    def __init__(self, operator, left_operand, right_operand, result):
        self._operator = operator
        self._left_operand = left_operand
        self._right_operand = right_operand
        self._result = result

    @property
    def operator(self):
        return self._operator

    @property
    def left_operand(self):
        return self._left_operand

    @property
    def right_operand(self):
        return self._right_operand

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value: int):
        self._result = value

