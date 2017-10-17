"""Defines the types and operators supported by the language that can participate in expressions.

The semantic_table is a 3 dimensional matrix which states what is the expected type for a
operation between two parameters and an operator. If the operation is not supported, 'Other' is the
default value used. Any operand that is 'other' will result in an invalid operation.
"""
from enum import IntEnum, unique, auto
import numpy as np


@unique
class Type(IntEnum):
    """The simple types of data that the language supports and that
    can be involved in operations.

    These types will be used to parse and solve expressions correctly, as
    well as ensure that the language semantics are followed to the letter
    during compilation.
    """
    TEXT = 1
    INT = 2
    REAL = 3
    BOOLEAN = 4
    OTHER = 5
    NOTHING = 6


@unique
class Operator(IntEnum):
    """The supported operators that may be used in an expression.

    These operators will be used to parse and solve expressions correctly, as
    well as ensure that the language semantics are followed to the letter
    during compilation.
    """
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDES = 4
    AND = 5
    OR = 6
    NOT = 7
    LESS_THAN = 8
    LESS_EQUAL = 9
    GREATER_THAN = 10
    GREATER_EQUAL = 11
    EQUAL_EQUAL = 12
    OPEN_PAREN = 13
    CLOSE_PAREN = 14
    EQUAL = 15
    WRITE = 19
    READ = 20


class Operation(IntEnum):
    GO_TO_FALSE = 16
    GO_TO_TRUE = 17
    GO_TO = 18


num_types = 6
num_operators = 15
semantic_table = np.zeros((num_types + 1, num_types + 1, num_operators + 1))

semantic_table[Type.TEXT][Type.TEXT][Operator.PLUS] = Type.TEXT
semantic_table[Type.TEXT][Type.INT][Operator.PLUS] = Type.TEXT
semantic_table[Type.TEXT][Type.REAL][Operator.PLUS] = Type.TEXT
semantic_table[Type.TEXT][Type.BOOLEAN][Operator.PLUS] = Type.TEXT
semantic_table[Type.INT][Type.INT][Operator.PLUS] = Type.INT
semantic_table[Type.INT][Type.TEXT][Operator.PLUS] = Type.TEXT
semantic_table[Type.INT][Type.INT][Operator.MINUS] = Type.INT
semantic_table[Type.INT][Type.INT][Operator.TIMES] = Type.INT
semantic_table[Type.INT][Type.INT][Operator.DIVIDES] = Type.INT
semantic_table[Type.INT][Type.INT][Operator.LESS_THAN] = Type.BOOLEAN
semantic_table[Type.INT][Type.INT][Operator.LESS_EQUAL] = Type.BOOLEAN
semantic_table[Type.INT][Type.INT][Operator.GREATER_THAN] = Type.BOOLEAN
semantic_table[Type.INT][Type.INT][Operator.GREATER_EQUAL] = Type.BOOLEAN
semantic_table[Type.INT][Type.INT][Operator.EQUAL_EQUAL] = Type.BOOLEAN
semantic_table[Type.INT][Type.REAL][Operator.PLUS] = Type.REAL
semantic_table[Type.INT][Type.REAL][Operator.MINUS] = Type.REAL
semantic_table[Type.INT][Type.REAL][Operator.TIMES] = Type.REAL
semantic_table[Type.INT][Type.REAL][Operator.DIVIDES] = Type.REAL
semantic_table[Type.INT][Type.REAL][Operator.LESS_THAN] = Type.BOOLEAN
semantic_table[Type.INT][Type.REAL][Operator.LESS_EQUAL] = Type.BOOLEAN
semantic_table[Type.INT][Type.REAL][Operator.GREATER_THAN] = Type.BOOLEAN
semantic_table[Type.INT][Type.REAL][Operator.GREATER_EQUAL] = Type.BOOLEAN
semantic_table[Type.INT][Type.REAL][Operator.EQUAL_EQUAL] = Type.BOOLEAN
semantic_table[Type.REAL][Type.TEXT][Operator.PLUS] = Type.TEXT
semantic_table[Type.REAL][Type.REAL][Operator.PLUS] = Type.REAL
semantic_table[Type.REAL][Type.REAL][Operator.MINUS] = Type.REAL
semantic_table[Type.REAL][Type.REAL][Operator.TIMES] = Type.REAL
semantic_table[Type.REAL][Type.REAL][Operator.DIVIDES] = Type.REAL
semantic_table[Type.REAL][Type.REAL][Operator.LESS_THAN] = Type.BOOLEAN
semantic_table[Type.REAL][Type.REAL][Operator.LESS_EQUAL] = Type.BOOLEAN
semantic_table[Type.REAL][Type.REAL][Operator.GREATER_THAN] = Type.BOOLEAN
semantic_table[Type.REAL][Type.REAL][Operator.GREATER_EQUAL] = Type.BOOLEAN
semantic_table[Type.REAL][Type.REAL][Operator.EQUAL_EQUAL] = Type.BOOLEAN
semantic_table[Type.REAL][Type.INT][Operator.PLUS] = Type.REAL
semantic_table[Type.REAL][Type.INT][Operator.MINUS] = Type.REAL
semantic_table[Type.REAL][Type.INT][Operator.TIMES] = Type.REAL
semantic_table[Type.REAL][Type.INT][Operator.DIVIDES] = Type.REAL
semantic_table[Type.REAL][Type.INT][Operator.LESS_THAN] = Type.BOOLEAN
semantic_table[Type.REAL][Type.INT][Operator.LESS_EQUAL] = Type.BOOLEAN
semantic_table[Type.REAL][Type.INT][Operator.GREATER_THAN] = Type.BOOLEAN
semantic_table[Type.REAL][Type.INT][Operator.GREATER_EQUAL] = Type.BOOLEAN
semantic_table[Type.REAL][Type.INT][Operator.EQUAL_EQUAL] = Type.BOOLEAN
semantic_table[Type.BOOLEAN][Type.BOOLEAN][Operator.AND] = Type.BOOLEAN
semantic_table[Type.BOOLEAN][Type.BOOLEAN][Operator.OR] = Type.BOOLEAN
semantic_table[Type.BOOLEAN][Type.BOOLEAN][Operator.NOT] = Type.BOOLEAN
semantic_table[Type.BOOLEAN][Type.BOOLEAN][Operator.EQUAL_EQUAL] = Type.BOOLEAN

for i in range(num_types + 1):
    for j in range(num_types + 1):
        for k in range(num_operators + 1):
            if semantic_table[i][j][k] == 0:
                semantic_table[i][j][k] = Type.OTHER


def get_type(name: str) -> Type:
    """Returns a simple type instance depending on the name of the type.

    :param name: the name of the type as found in the compiled program verbatim.
    :raises TypeError if the type is not part of the simple types.
    :return: the type object corresponding to the type name.
    """
    if name == 'Boolean':
        return Type.BOOLEAN
    if name == 'Text':
        return Type.TEXT
    if name == 'Int':
        return Type.INT
    if name == 'Nothing':
        return Type.NOTHING
    if name == 'Real':
        return Type.REAL

    print(name + " type is not a simple type.")
    return Type.OTHER


__author__ = "Marco A. Peyrot (mpeyrotc)"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "macpeyrot@hotmail.com"
__status__ = "Development"
