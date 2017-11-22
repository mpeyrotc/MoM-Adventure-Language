# Generated from MoM.g4 by ANTLR 4.7
from enum import IntEnum, auto, unique

from antlr4 import *

import src.MasterTables as master_tables
from src.structures.Class import Class
from src.structures.Enumeration import Enumeration
from src.structures.Method import Method
from src.structures.Quadrupole import Quadrupole
from src.structures.SemanticTable import get_type, Type, Operator, semantic_table, Operation, get_name
from src.structures.Specification import Specification

if __name__ is not None and "." in __name__:
    from .MoMParser import MoMParser
else:
    from MoMParser import MoMParser


@unique
class StructureType(IntEnum):
    CLASS = auto()
    SPECIFICATION = auto()
    ENUMERATION = auto()


class Variable:
    var_type = ""
    is_array = False
    mem_size = 1

    def __init__(self):
        self.is_array = False


CONST_INT_TOP = 22_000
CONST_REAL_TOP = 23_000
CONST_TEXT_TOP = 24_000
CONST_BOOLEAN_TOP = 25_000

CONST_INT_BOTTOM = 22_999
CONST_REAL_BOTTOM = 23_999
CONST_TEXT_BOTTOM = 24_999
CONST_BOOLEAN_BOTTOM = 25_100


class MoMListener(ParseTreeListener):
    current_enumeration = ""
    current_type = ""
    current_class = ""
    current_specification = ""
    current_method = ""
    current_method_instance = ""
    current_counter = 0
    class_reference = ""
    constructor_called = ""
    destination_type = []
    source_type = []
    arguments = []
    argument_names = []
    in_signature = False
    main_found = False
    cur_const_int = CONST_INT_TOP
    cur_const_real = CONST_REAL_TOP
    cur_const_boolean = CONST_BOOLEAN_TOP
    cur_const_text = CONST_TEXT_TOP

    current_structure = StructureType.CLASS

    pending_operands = list()
    pending_types = list()
    pending_operators = list()
    pending_jumps = list()
    pending_dims = list()
    quads = list()

    @staticmethod
    def get_address_by_type(m: Method, t: Type):
        if t == Type.INT:
            return m.cur_local_int
        elif t == Type.REAL:
            return m.cur_local_real
        elif t == Type.TEXT:
            return m.cur_local_text
        elif t == Type.BOOLEAN:
            return m.cur_local_boolean
        elif t == Type.OTHER:
            raise TypeError("Local variable assignment not supported for OTHER (1).")
        elif t == Type.CLASS:
            return m.cur_local_object
        else:
            raise TypeError("Local variable assignment not supported for <INVALID> (2): " + str(t))

    @staticmethod
    def get_global_address_by_type(c: Class, t: Type):
        if t == Type.INT:
            return c.cur_global_int
        elif t == Type.REAL:
            return c.cur_global_real
        elif t == Type.TEXT:
            return c.cur_global_text
        elif t == Type.BOOLEAN:
            return c.cur_global_boolean
        elif t == Type.OTHER:
            raise TypeError("Global variable assignment not supported for OTHER (2).")
        elif t == Type.CLASS:
            return c.cur_global_object
        elif t == Type.NOTHING:
            return c.nothing_address
        else:
            raise TypeError("Global variable assignment not supported for <INVALID> (2): " + str(t))

    @staticmethod
    def get_temp_address_by_type(m: Method, t: Type):
        if t == Type.INT:
            return m.cur_temp_int
        elif t == Type.REAL:
            return m.cur_temp_real
        elif t == Type.TEXT:
            return m.cur_temp_text
        elif t == Type.BOOLEAN:
            return m.cur_temp_boolean
        elif t == Type.OTHER:
            raise TypeError("Temporal variable assignment not supported for OTHER (3).")
        elif t == Type.CLASS:
            raise TypeError("No CLASS types supported for temporal variables (3): " + str(t))
        else:
            raise TypeError("Temporal variable assignment not supported for <INVALID> (3): " + str(t))

    def get_const_address_by_type(self, t: Type):
        if t == Type.INT:
            return self.cur_const_int
        elif t == Type.REAL:
            return self.cur_const_real
        elif t == Type.TEXT:
            return self.cur_const_text
        elif t == Type.BOOLEAN:
            return self.cur_const_boolean
        else:
            raise TypeError("Constant assignment not supported for <INVALID> (4): " + str(t))

    @staticmethod
    def increment_address_by_type(m: Method, t: Type, s: int):
        if t == Type.INT:
            m.cur_local_int += s
        elif t == Type.REAL:
            m.cur_local_real += s
        elif t == Type.TEXT:
            m.cur_local_text += s
        elif t == Type.BOOLEAN:
            m.cur_local_boolean += s
        elif t == Type.CLASS:
            m.cur_local_object += s
        else:
            raise TypeError("Local increment for OTHER or <INVALID> not supported (5): " + str(t))

    @staticmethod
    def increment_global_address_by_type(c: Class, t: Type, s: int):
        if t == Type.INT:
            c.cur_global_int += s
        elif t == Type.REAL:
            c.cur_global_real += s
        elif t == Type.TEXT:
            c.cur_global_text += s
        elif t == Type.BOOLEAN:
            c.cur_global_boolean += s
        elif t == Type.CLASS:
            c.cur_global_object += s
        elif t == Type.NOTHING:
            pass  # the address for nothing (void) never changes
        else:
            raise TypeError("Global increment for OTHER or <INVALID> not supported (6): " + str(t))

    @staticmethod
    def increment_temp_address_by_type(m: Method, t: Type):
        if t == Type.INT:
            m.cur_temp_int += 1
        elif t == Type.REAL:
            m.cur_temp_real += 1
        elif t == Type.TEXT:
            m.cur_temp_text += 1
        elif t == Type.BOOLEAN:
            m.cur_temp_boolean += 1
        else:
            raise TypeError("Temporal increment for OTHER, CLASS or <INVALID> not supported (7): " + str(t))

        m.temp_count += 1

    def increment_const_address_by_type(self, t: Type):
        if t == Type.INT:
            self.cur_const_int += 1
        elif t == Type.REAL:
            self.cur_const_real += 1
        elif t == Type.TEXT:
            self.cur_const_text += 1
        elif t == Type.BOOLEAN:
            self.cur_const_boolean += 1
        else:
            raise TypeError("Local increment for OTHER or <INVALID> not supported (8): " + str(t))

    def fill(self, end: int, next_quad: int) -> None:
        quad = self.quads[end]
        quad.result = next_quad

    @staticmethod
    def debug(quad: Quadrupole):
        print(str(quad.operator) + ", " + str(quad.left_operand) + ", " + str(quad.right_operand) + ", " + str(
            quad.result))

    def create_method_field(self, field_name: str, return_type: Type):
        c = master_tables.classes[self.current_class]
        address = self.get_global_address_by_type(c, return_type)
        c.add_argument(field_name, return_type, False, address, 1, [])
        self.increment_global_address_by_type(c, return_type, 1)

    def create_method_field_aux(self, name: str, field_name: str, return_type: Type):
        c = master_tables.classes[name]
        address = self.get_global_address_by_type(c, return_type)
        c.add_argument(field_name, return_type, False, address, 1, [])
        self.increment_global_address_by_type(c, return_type, 1)

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterProgram(self, ctx: MoMParser.ProgramContext) -> None:
        """ This is the first listener of a program where the class declarations,
                    specifications and enums are declared and managed.
                :param ctx: Context generated by antlr4.
                :return: None.
        """
        # Create quadrupole that points to main method.
        quad = Quadrupole(Operation.GO_CONSTRUCTOR, None, None, None)
        self.quads.append(quad)
        quad = Quadrupole(Operation.GO_MAIN, None, None, None)
        self.quads.append(quad)

        # Register in tables the Component class, which is the base class of the language
        class_specifications = set()
        class_name = "Component"
        class_parent = ""
        master_tables.classes[class_name] = Class(class_name, class_parent, class_specifications)

        # reset virtual memory counters
        Method.cur_local_boolean = Method.LOCAL_BOOLEAN_TOP
        Method.cur_local_real = Method.LOCAL_REAL_TOP
        Method.cur_local_int = Method.LOCAL_INT_TOP
        Method.cur_local_text = Method.LOCAL_TEXT_TOP

        method_name = class_name
        self.current_method = method_name
        new_method = Method(method_name, Type.CLASS)
        new_method.start = len(self.quads)
        master_tables.classes[class_name].add_method(new_method)
        self.create_method_field_aux(class_name, new_method.name, new_method.return_type)

        quad = Quadrupole(Operation.RETURN, None, None, None)

        self.quads.append(quad)

        # The basic methods for the base class are width and height
        # reset virtual memory counters
        Method.cur_local_boolean = Method.LOCAL_BOOLEAN_TOP
        Method.cur_local_real = Method.LOCAL_REAL_TOP
        Method.cur_local_int = Method.LOCAL_INT_TOP
        Method.cur_local_text = Method.LOCAL_TEXT_TOP

        return_type, method_name = "Real", "getWidth"
        new_method = Method(method_name, get_type(return_type))
        new_method.start = len(self.quads)
        master_tables.classes[class_name].add_method(new_method)
        self.create_method_field_aux(class_name, new_method.name, new_method.return_type)

        # create width method quadrupoles
        quad = Quadrupole(Operation.RETURN, None, None, master_tables.classes[class_name].cur_global_real)

        self.quads.append(quad)

        Method.cur_local_boolean = Method.LOCAL_BOOLEAN_TOP
        Method.cur_local_real = Method.LOCAL_REAL_TOP
        Method.cur_local_int = Method.LOCAL_INT_TOP
        Method.cur_local_text = Method.LOCAL_TEXT_TOP

        return_type, method_name = "Real", "getHeight"
        new_method = Method(method_name, get_type(return_type))
        new_method.start = len(self.quads)
        master_tables.classes[class_name].add_method(new_method)
        self.create_method_field_aux(class_name, new_method.name, new_method.return_type)

        # create height method quadrupoles
        quad = Quadrupole(Operation.RETURN, None, None, master_tables.classes[class_name].cur_global_real + 1)

        self.quads.append(quad)

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitProgram(self, ctx: MoMParser.ProgramContext) -> None:
        """ Exit of the first listener.
                :param ctx: Context generated by antlr4.
                :return: None
        """
        quad = Quadrupole(Operation.END, None, None, None)
        self.quads.append(quad)

        if not self.main_found:
            raise RuntimeError("Main method not found, please define program entry point.")

        for index, quad in enumerate(MoMListener.quads):
            print(str(index) + ") " + str(quad.operator) + ", " + str(quad.left_operand) + ", "
            + str(quad.right_operand) + ", " + str(quad.result))

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterAfter_argument(self, ctx: MoMParser.After_argumentContext) -> None:
        pass

    # noinspection PyPep8Naming
    def exitAfter_argument(self, ctx: MoMParser.After_argumentContext):
        """ Neuralgic point after an argument of a function.
                    This helps to check if the parameter matches in type.
                :return: None.
        """
        argument = self.pending_operands.pop()
        argument_type = self.pending_types.pop()
        expected_type = self.current_method_instance.argument_types[self.current_counter]

        if argument_type == Type.OTHER:
            # Special case, object parameters not supported
            raise TypeError("Object arguments not supported by functions.")
        else:
            argument_type = argument_type

        if not argument_type == expected_type['arg_type']:
            raise TypeError("Argument for method `" + self.current_method + "` call wrong. "
                                                                            "Argument should be of type " +
                            str(expected_type["arg_type"]) +
                            ", instead got: " + str(argument_type))
        quad = Quadrupole(Operation.PARAM, argument, None, self.current_counter)

        self.quads.append(quad)

    # noinspection PyPep8Naming
    def enterAdvance_count(self, ctx: MoMParser.Advance_countContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitAdvance_count(self, ctx: MoMParser.Advance_countContext) -> None:
        self.current_counter += 1

    # noinspection PyPep8Naming
    def enterArguments(self, ctx: MoMParser.ArgumentsContext):
        pass

    # noinspection PyPep8Naming
    def exitArguments(self, ctx: MoMParser.ArgumentsContext):
        pass

    # noinspection PyPep8Naming
    def enterAssignation(self, ctx: MoMParser.AssignationContext) -> None:
        pass

    # noinspection PyPep8Naming
    def exitAssignation(self, ctx: MoMParser.AssignationContext) -> None:
        """ Listener after an assignation occurs.
                    Manages both: assignation of atomic variable and array variable assignation.

                :param ctx: Context generated by antlr4.
                :return: None
        """
        if ctx.VARID() is None:
            # array assign
            holder = self.pending_operands.pop()
            type_holder = self.pending_types.pop()
            destination = self.pending_operands.pop()
            type_dest = self.pending_types.pop()
            if type_holder != type_dest:
                raise NameError("Cannot assign type " + get_name(type_holder) + " to type " + get_name(type_dest))
            quad = Quadrupole(Operator.EQUAL, holder, None, destination)

            self.quads.append(quad)
            return
        else:
            var = ctx.VARID().getText()

        c = master_tables.classes[self.current_class]
        m = c.methods[self.current_method]

        # Look in local variables, if not, look in global variables
        if var in m.variables:
            destination = m.variables[var]["address"]
            holder = self.pending_operands.pop()
            self.pending_types.pop()
            quad = Quadrupole(Operator.EQUAL, holder, None, destination)

            self.quads.append(quad)
        elif var in c.variables:
            destination = c.variables[var]["address"]
            holder = self.pending_operands.pop()
            self.pending_types.pop()
            quad = Quadrupole(Operator.EQUAL, holder, None, destination)

            self.quads.append(quad)
        else:
            # if not present report error.
            raise NameError("Variable ' " + var + " is undefined.")

    # noinspection PyPep8Naming
    def enterBlock(self, ctx: MoMParser.BlockContext):
        pass

    # noinspection PyPep8Naming
    def exitBlock(self, ctx: MoMParser.BlockContext):
        pass

    # noinspection PyPep8Naming
    def enterClass_rule(self, ctx: MoMParser.Class_ruleContext) -> None:
        """This listener manages registering the classes that the user defines within a program.

        This listener is in charge of creating the class objects, specifying their names, parents
        and possible specifications.

        :param ctx: the context for this specific class instance.
        :return: None.
        """
        class_specifications = set()
        class_name = ctx.CLASSID()[0].getText()

        # It is a class with at least one specification
        for i in range(1, len(ctx.CLASSID())):
            specification_name = ctx.CLASSID()[i].getText()

            if specification_name not in master_tables.specifications:
                raise NameError("Specification with name `" + specification_name + "` for class `" + class_name +
                                "` is undefined.")

            class_specifications.add(specification_name)

        self.current_class = class_name
        self.current_structure = StructureType.CLASS

        if class_name in master_tables.classes:
            raise NameError("Redefinition of class '" + class_name + "' found. This is not supported by the language.")

        if class_name in master_tables.classes:
            raise NameError("Name collision with interface '" + class_name +
                            "'. Classes cannot have the same name as interfaces.")

        # get the parent of this class
        self.enterComplex_type(ctx.complex_type())
        class_parent = self.current_type

        master_tables.classes[class_name] = Class(class_name, class_parent, class_specifications)

        ancestor = master_tables.classes[class_name].parent
        methods = master_tables.classes[ancestor].methods
        variables = master_tables.classes[ancestor].variables

        for var_n in variables:
            v = variables[var_n]
            if var_n not in methods:
                t = self.get_global_address_by_type(master_tables.classes[class_name], v["type"])
                self.increment_global_address_by_type(master_tables.classes[class_name], v["type"], v["mem_size"])
                master_tables.classes[class_name].add_argument(v["name"], v["type"], v["is_array"],
                                                               t, v["mem_size"], v["dim"], v["class_type"])

        for method_n in methods:
            method = methods[method_n]
            master_tables.classes[class_name].add_method(method)
            self.create_method_field(method.name, method.return_type)

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitClass_rule(self, ctx: MoMParser.Class_ruleContext) -> None:
        """ For all interfaces declared for current class,
                    check that their methods are defined in the body of the class

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        # for all interfaces declared for current class, check that their methods are defined in the body of the class
        class_instance = master_tables.classes[self.current_class]
        specifications = class_instance.specifications

        for specification_name in specifications:
            specification = master_tables.specifications[specification_name]
            for method_name in specification.methods:
                if method_name not in class_instance.methods:
                    raise NameError("The method `" + method_name +
                                    "` is not implemented by the class: " + class_instance.name)

                class_method = class_instance.methods[method_name]

                for s_var, c_var in zip(specification.methods[method_name].variables, class_method.argument_types):
                    t = specification.methods[method_name].variables[s_var]["type"]
                    is_arr = specification.methods[method_name].variables[s_var]["is_array"]
                    if not t == c_var['arg_type']:
                        raise TypeError("Argument type mismatch in class `" + class_instance.name +
                                        "`, method `" + method_name + "`. Expected: " + t +
                                        ", got " + c_var['arg_type'] + " instead.")

                    if not is_arr == c_var["is_array"]:
                        raise TypeError("Argument type mismatch in class `" + class_instance.name +
                                        "`, method `" + method_name + "`. Expected: " + t +
                                        "[], got " + c_var['arg_type'] + " instead.")

                # TODO: check for return type, num arguments, name, type arguments, if they are arrays or not in tests
                r = specification.methods[method_name].return_type
                if not r == class_method.return_type:
                    raise TypeError("Return type mismatch in class `" + class_instance.name +
                                    "`, method `" + method_name + "`. Expected: " + str(r) +
                                    ", got " + str(class_method.return_type) + " instead.")

        quad = Quadrupole(Operation.END_CLASS, None, None, None)

        self.quads.append(quad)

    # noinspection PyPep8Naming
    def enterCondition(self, ctx: MoMParser.ConditionContext):
        pass

    # noinspection PyPep8Naming
    def exitCondition(self, ctx: MoMParser.ConditionContext) -> None:
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterExit_if_check(self, ctx: MoMParser.Exit_if_checkContext) -> None:
        """ Listener to check if the expression inside a condition is of type boolean

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        exp_type = self.pending_types.pop()

        if exp_type is not Type.BOOLEAN:
            assert TypeError("Condition in if statement is not boolean. It is: " + str(exp_type))

        result = self.pending_operands.pop()
        quad = Quadrupole(Operation.GO_TO_FALSE, result, None, None)

        self.quads.append(quad)
        self.pending_jumps.append(len(self.quads) - 1)

    # noinspection PyPep8Naming
    def exitExit_if_check(self, ctx: MoMParser.Exit_if_checkContext):
        pass

    # noinspection PyPep8Naming
    def enterCondition_end(self, ctx: MoMParser.Condition_endContext):
        pass

    # noinspection PyUnusedLocal,PyPep8Naming
    def exitCondition_end(self, ctx: MoMParser.Condition_endContext) -> None:
        end = self.pending_jumps.pop()
        self.fill(end, len(self.quads))

    # noinspection PyPep8Naming
    def enterEnter_else(self, ctx: MoMParser.Enter_elseContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitEnter_else(self, ctx: MoMParser.Enter_elseContext) -> None:
        quad = Quadrupole(Operation.GO_TO, None, None, None)

        self.quads.append(quad)
        false = self.pending_jumps.pop()
        self.pending_jumps.append(len(self.quads) - 1)
        self.fill(false, len(self.quads))

    # noinspection PyPep8Naming
    def enterConstant(self, ctx: MoMParser.ConstantContext) -> None:
        """ Listener for our different type of constants
            It manages individually depending on the type.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        if ctx.INTEGER() is not None:
            num = int(ctx.getText())

            if num in master_tables.constants:
                address = master_tables.constants[num]
            else:
                address = self.get_const_address_by_type(Type.INT)
                self.increment_const_address_by_type(Type.INT)
                master_tables.constants[num] = address

            self.pending_operands.append(address)
            self.pending_types.append(Type.INT)
        elif ctx.REAL() is not None:
            num = float(ctx.getText())
            if num in master_tables.constants:
                address = master_tables.constants[num]
            else:
                address = self.get_const_address_by_type(Type.REAL)
                self.increment_const_address_by_type(Type.REAL)
                master_tables.constants[num] = address

            self.pending_operands.append(address)
            self.pending_types.append(Type.REAL)
        elif ctx.TRUE() is not None:
            num = "!@#$%^&*()"
            if num in master_tables.constants:
                address = master_tables.constants[num]
            else:
                address = self.get_const_address_by_type(Type.BOOLEAN)
                self.increment_const_address_by_type(Type.BOOLEAN)
                master_tables.constants[num] = address

            self.pending_operands.append(address)
            self.pending_types.append(Type.BOOLEAN)
        elif ctx.FALSE() is not None:
            num = ")(*&^%$#@!"
            if num in master_tables.constants:
                address = master_tables.constants[num]
            else:
                address = self.get_const_address_by_type(Type.BOOLEAN)
                self.increment_const_address_by_type(Type.BOOLEAN)
                master_tables.constants[num] = address

            self.pending_operands.append(address)
            self.pending_types.append(Type.BOOLEAN)
        elif ctx.STRING() is not None:
            num = ctx.getText()
            if num in master_tables.constants:
                address = master_tables.constants[num]
            else:
                address = self.get_const_address_by_type(Type.TEXT)
                self.increment_const_address_by_type(Type.TEXT)
                master_tables.constants[num] = address

            self.pending_operands.append(address)
            self.pending_types.append(Type.TEXT)
        elif ctx.VARID() is not None:
            var = ctx.VARID().getText()
            c = master_tables.classes[self.current_class]
            m = c.methods[self.current_method]

            # Look in local variables, if not, look in global variables
            if var in m.variables:
                t = m.variables[var]["type"]
                self.pending_operands.append(m.variables[var]["address"])
            elif var in c.variables:
                t = c.variables[var]["type"]
                self.pending_operands.append(c.variables[var]["address"])
            else:
                raise NameError("Variable ' " + var + " is undefined.")

            if type(t) == str:
                self.pending_types.append(get_type(t))
            else:
                self.pending_types.append(t)

        elif ctx.CAPITALID() is not None:
            # it's an enum
            name = ctx.CAPITALID().getText()
            was_found = False
            for enum in master_tables.enumerations:
                if name in master_tables.enumerations[enum].values:
                    was_found = True
                    pos = master_tables.enumerations[enum].values.get(name)
                    break

            if was_found:
                # creates a constant variable for that enum
                num = int(pos)
                if num in master_tables.constants:
                    address = master_tables.constants[num]
                else:
                    address = self.get_const_address_by_type(Type.INT)
                    self.increment_const_address_by_type(Type.INT)
                    master_tables.constants[num] = address

                self.pending_operands.append(address)
                self.pending_types.append(Type.INT)
            else:
                raise NameError("Enum not found")
        else:
            # See array_var listener
            pass

    # noinspection PyPep8Naming
    def exitConstant(self, ctx: MoMParser.ConstantContext):
        pass

    # noinspection PyPep8Naming
    def enterConstruct_call(self, ctx: MoMParser.Construct_callContext) -> None:
        """ Listener when a Construct is called.
            Checks if the Constructor exists.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        method_name = ctx.CLASSID().getText()
        self.source_type.append(method_name)

        found = False
        for class_name in master_tables.classes:
            if method_name in master_tables.classes[class_name].methods:
                self.current_counter = 0
                self.current_method_instance = master_tables.classes[class_name].methods[method_name]
                self.constructor_called = class_name
                found = True
                break

        if not found:
            raise NameError("Constructor name `" + method_name + "` not defined for class: " + self.current_class)

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitConstruct_call(self, ctx: MoMParser.Construct_callContext) -> None:
        """ Neuralgic point after a constructor is called.
            Generates quadruple GoConstructor.
            Checks if the exact number of parameters were given.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        if not self.current_counter == self.current_method_instance.num_of_params:
            raise IllegalStateException("Constructor `" + self.current_method_instance.name +
                                        "` has wrong number of arguments. Should be " +
                                        str(self.current_method_instance.num_of_params) +
                                        ", got " + str(self.current_counter) + " instead.")

        quad = Quadrupole(Operation.GO_CONSTRUCTOR, self.constructor_called, self.current_method_instance.name,
                          self.current_method_instance.start)
        self.debug(quad)
        c = master_tables.classes[self.constructor_called]

        self.quads.append(quad)

        var = self.current_method_instance.name
        t = c.variables[var]["type"]
        self.pending_operands.append(c.variables[var]["address"])
        self.pending_types.append(t)

    # noinspection PyPep8Naming
    def enterExit_con_def(self, ctx: MoMParser.Exit_con_defContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitExit_con_def(self, ctx: MoMParser.Exit_con_defContext) -> None:
        address = master_tables.classes[self.current_class].variables[self.current_class]["address"]
        quad = Quadrupole(Operation.RETURN, None, None, address)

        self.quads.append(quad)

    # noinspection PyPep8Naming
    def enterConstruct_def(self, ctx: MoMParser.Construct_defContext) -> None:
        """ Neuralgic point when a Constructor is defined.
            Checks that there is only 1 Constructor of a Class.
            Generates quadruple GO_SUB that helps us find where the class begins.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        # reset virtual memory counters
        Method.cur_local_boolean = Method.LOCAL_BOOLEAN_TOP
        Method.cur_local_real = Method.LOCAL_REAL_TOP
        Method.cur_local_int = Method.LOCAL_INT_TOP
        Method.cur_local_text = Method.LOCAL_TEXT_TOP

        method_name = ctx.CLASSID().getText()
        self.current_method = method_name
        new_method = Method(method_name, Type.CLASS)
        new_method.start = len(self.quads)

        c = master_tables.classes[self.current_class]
        if method_name in c.methods:
            raise NameError("Method '" + method_name + "' redefined in class '"
                            + self.current_class + "', this is not supported at language level.")

        c.add_method(new_method)
        self.create_method_field(new_method.name, new_method.return_type)

        # Implicit calls to ancestor constructors
        if not c.name == "Component":
            p = master_tables.classes[c.parent]
            quad = Quadrupole(Operation.GO_SUB, self.current_class, c.parent, p.methods[p.name].start)

            self.quads.append(quad)

    # noinspection PyPep8Naming
    def exitConstruct_def(self, ctx: MoMParser.Construct_defContext):
        pass

    # noinspection PyPep8Naming
    def enterEnum(self, ctx: MoMParser.EnumContext) -> None:
        """Takes each value defined in the enumeration and assigns it to its
        corresponding enumeration.

        :param ctx: the parser context for this enumeration, holds the values of the enumeration.
        :return: None.
        """
        for value in ctx.CAPITALID():
            master_tables.enumerations[self.current_enumeration].add_value(value.getText())

    # noinspection PyPep8Naming
    def exitEnum(self, ctx: MoMParser.EnumContext):
        pass

    # noinspection PyPep8Naming
    def enterEnumeration(self, ctx: MoMParser.EnumerationContext) -> None:
        """Enumeration listener, creates a new instance and saves it in the registry.

        :param ctx: the parser context for this enumeration, holds the enumeration name.
        :return: None.
        """
        name = ctx.CLASSID().getText()
        new_enumeration = Enumeration(name)
        master_tables.enumerations[name] = new_enumeration
        self.current_enumeration = name
        self.current_structure = StructureType.ENUMERATION

    # noinspection PyPep8Naming
    def exitEnumeration(self, ctx: MoMParser.EnumerationContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterExit_sexp(self, ctx: MoMParser.Exit_sexpContext) -> None:
        """ Enters super expression
            This level gives priority to ANDs and ORs.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        if not len(self.pending_operators) == 0:
            if self.pending_operators[-1] == Operator.AND or self.pending_operators[-1] == Operator.OR:
                right_operand = self.pending_operands.pop()
                right_type = self.pending_types.pop()
                left_operand = self.pending_operands.pop()
                left_type = self.pending_types.pop()
                operator = self.pending_operators.pop()
                result_type = semantic_table[left_type][right_type][operator]

                if result_type == Type.OTHER:
                    raise TypeError("Type mismatch for expression.")
                else:
                    m = master_tables.classes[self.current_class].methods[self.current_method]
                    result = self.get_temp_address_by_type(m, result_type)
                    self.increment_temp_address_by_type(m, result_type)
                    quad = Quadrupole(operator, left_operand, right_operand, result)

                    self.quads.append(quad)
                    self.pending_operands.append(result)
                    self.pending_types.append(result_type)

    # noinspection PyPep8Naming
    def exitExit_sexp(self, ctx: MoMParser.Exit_sexpContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterAnd_op(self, ctx: MoMParser.And_opContext) -> None:
        self.pending_operators.append(Operator.AND)

    # noinspection PyPep8Naming
    def exitAnd_op(self, ctx: MoMParser.And_opContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterOr_op(self, ctx: MoMParser.Or_opContext) -> None:
        self.pending_operators.append(Operator.OR)

    # noinspection PyPep8Naming
    def exitOr_op(self, ctx: MoMParser.Or_opContext):
        pass

    # noinspection PyPep8Naming
    def enterSs_exp(self, ctx: MoMParser.Ss_expContext):
        pass

    # noinspection PyPep8Naming
    def exitSs_exp(self, ctx: MoMParser.Ss_expContext):
        pass

    # noinspection PyUnusedLocal,PyPep8Naming
    def enterExit_exp(self, ctx: MoMParser.Exit_expContext) -> None:
        """ Exit Expression
            This level gives priority to binary operators like: ==, <=, >=.
            Associates to the left these operations.
        :param ctx: Context generated by antlr4.
        :return: None.
        """
        if not len(self.pending_operators) == 0:
            op = self.pending_operators[-1]
            if op == Operator.EQUAL_EQUAL or op == Operator.LESS_THAN or op == Operator.LESS_EQUAL \
                    or op == Operator.GREATER_THAN or op == Operator.GREATER_EQUAL:
                right_operand = self.pending_operands.pop()
                right_type = self.pending_types.pop()
                left_operand = self.pending_operands.pop()
                left_type = self.pending_types.pop()
                operator = self.pending_operators.pop()
                result_type = semantic_table[left_type][right_type][operator]

                if result_type == Type.OTHER:
                    raise TypeError("Type mismatch for expression.")
                else:
                    m = master_tables.classes[self.current_class].methods[self.current_method]
                    result = self.get_temp_address_by_type(m, result_type)
                    self.increment_temp_address_by_type(m, result_type)
                    quad = Quadrupole(operator, left_operand, right_operand, result)

                    self.quads.append(quad)
                    self.pending_operands.append(result)
                    self.pending_types.append(result_type)

    # noinspection PyPep8Naming
    def exitExit_exp(self, ctx: MoMParser.Exit_expContext):
        pass

    # noinspection PyPep8Naming
    def enterS_exp(self, ctx: MoMParser.S_expContext):
        pass

    # noinspection PyPep8Naming
    def exitS_exp(self, ctx: MoMParser.S_expContext):
        pass

    # noinspection PyUnusedLocal,PyPep8Naming
    def enterExit_term(self, ctx: MoMParser.Exit_termContext) -> None:
        """ Enters term
            This level gives priority to additions and subtractions on an expression.
            Associates to the left these operations.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        if not len(self.pending_operators) == 0:
            if self.pending_operators[-1] == Operator.PLUS or self.pending_operators[-1] == Operator.MINUS:
                right_operand = self.pending_operands.pop()
                right_type = self.pending_types.pop()
                left_operand = self.pending_operands.pop()
                left_type = self.pending_types.pop()
                operator = self.pending_operators.pop()
                result_type = Type(semantic_table[int(left_type)][int(right_type)][int(operator)])
                if result_type == Type.OTHER:
                    raise TypeError("Type mismatch for expression.")
                else:
                    m = master_tables.classes[self.current_class].methods[self.current_method]
                    result = self.get_temp_address_by_type(m, result_type)
                    self.increment_temp_address_by_type(m, result_type)
                    quad = Quadrupole(operator, left_operand, right_operand, result)

                    self.quads.append(quad)
                    self.pending_operands.append(result)
                    self.pending_types.append(result_type)

    # noinspection PyPep8Naming
    def exitExit_term(self, ctx: MoMParser.Exit_termContext):
        pass

    # noinspection PyPep8Naming
    def enterAfter_while(self, ctx: MoMParser.After_whileContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitAfter_while(self, ctx: MoMParser.After_whileContext) -> None:
        self.pending_jumps.append(len(self.quads))

    # noinspection PyPep8Naming
    def enterEnd_while(self, ctx: MoMParser.End_whileContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitEnd_while(self, ctx: MoMParser.End_whileContext) -> None:
        """ Neuralgic point at the end of a while loop .
            Fills pending GOTOF quadruple.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        end = self.pending_jumps.pop()
        go_back = self.pending_jumps.pop()
        quad = Quadrupole(Operation.GO_TO, None, None, go_back)

        self.quads.append(quad)
        self.fill(end, len(self.quads))

    # noinspection PyUnusedLocal,PyPep8Naming
    def enterPlus_op(self, ctx: MoMParser.Plus_opContext) -> None:
        self.pending_operators.append(Operator.PLUS)

    # noinspection PyPep8Naming
    def exitPlus_op(self, ctx: MoMParser.Plus_opContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterMinus_op(self, ctx: MoMParser.Minus_opContext) -> None:
        self.pending_operators.append(Operator.MINUS)

    # noinspection PyPep8Naming
    def exitMinus_op(self, ctx: MoMParser.Minus_opContext):
        pass

    # noinspection PyPep8Naming
    def enterExpression(self, ctx: MoMParser.ExpressionContext):
        pass

    # noinspection PyPep8Naming
    def exitExpression(self, ctx: MoMParser.ExpressionContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterOpen_paren(self, ctx: MoMParser.Open_parenContext) -> None:
        self.pending_operators.append(Operator.OPEN_PAREN)

    # noinspection PyPep8Naming
    def exitOpen_paren(self, ctx: MoMParser.Open_parenContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterClose_paren(self, ctx: MoMParser.Close_parenContext):
        self.pending_operators.pop()

    # noinspection PyPep8Naming
    def exitClose_paren(self, ctx: MoMParser.Close_parenContext):
        pass

    # noinspection PyPep8Naming
    def enterFactor(self, ctx: MoMParser.FactorContext):
        pass

    # noinspection PyPep8Naming
    def exitFactor(self, ctx: MoMParser.FactorContext):
        """ Neuralgic point after a factor used to handle unary operators.
            Checks if there is a pending unary operator for a factor.
            Generates corresponding quadruples.

        :return: None.
        """
        m = master_tables.classes[self.current_class].methods[self.current_method]
        if self.pending_operators and self.pending_operators[-1] == Operator.NOT:
            type = self.pending_types.pop()
            holder = self.pending_operands.pop()
            dest = self.get_temp_address_by_type(m, type)
            self.pending_operands.append(dest)
            self.pending_types.append(type)
            quad = Quadrupole(Operator.EQUAL, holder, None, dest)
            self.quads.append(quad)
            self.increment_temp_address_by_type(m, type)
            self.pending_operators.pop()
            quad = Quadrupole(Operator.NOT, None, None, dest)
            self.quads.append(quad)
        elif self.pending_operators and self.pending_operators[-1] == Operator.UNARY_MINUS:
            type = self.pending_types.pop()
            holder = self.pending_operands.pop()
            dest = self.get_temp_address_by_type(m, type)
            self.pending_operands.append(dest)
            self.pending_types.append(type)
            quad = Quadrupole(Operator.EQUAL, holder, None, dest)
            self.quads.append(quad)
            self.increment_temp_address_by_type(m, type)
            self.pending_operators.pop()
            quad = Quadrupole(Operator.UNARY_MINUS, None, None, dest)
            self.quads.append(quad)
        elif self.pending_operators and  self.pending_operators[-1] == Operator.UNARY_PLUS:
            type = self.pending_types.pop()
            holder = self.pending_operands.pop()
            dest = self.get_temp_address_by_type(m, type)
            self.pending_operators.pop()
            quad = Quadrupole(Operator.UNARY_PLUS, None, None, dest)
            self.quads.append(quad)

    # noinspection PyPep8Naming
    def enterFunction_args(self, ctx: MoMParser.Function_argsContext) -> None:
        """ Listener for arguments of a function.
            Saves the arguments names for future use on the exit listener.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        self.in_signature = True
        self.arguments = []
        self.argument_names = []

        for var_name in ctx.VARID():
            self.argument_names.append(var_name.getText())

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitFunction_args(self, ctx: MoMParser.Function_argsContext) -> None:
        """ Listener for exiting arguments of a function.
            Assigns memory for every variable depending on its type.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        self.in_signature = False

        for name, var in zip(self.argument_names, self.arguments):
            if self.current_structure == StructureType.CLASS:
                m = master_tables.classes[self.current_class].methods[self.current_method]
                address = self.get_address_by_type(m, get_type(var.var_type))
                t = get_type(var.var_type)

                if t == Type.CLASS:
                    m.add_argument(name, t, var.is_array, address, var.mem_size, [], var.var_type)
                else:
                    m.add_argument(name, t, var.is_array, address, var.mem_size, [])

                m.add_argument_type(get_type(var.var_type), var.is_array)
                self.increment_address_by_type(m, get_type(var.var_type), var.mem_size)
            elif self.current_structure == StructureType.SPECIFICATION:
                master_tables.specifications[self.current_specification].methods[
                    self.current_method].add_argument(name, get_type(var.var_type), var.is_array, -2, var.mem_size)

    # noinspection PyPep8Naming
    def enterFunction_call(self, ctx: MoMParser.Function_callContext) -> None:
        """ Listener when a function is called.
            Handles both scenarios: when the method is local/inherited and when it's from another class.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        class_instance = master_tables.classes[self.current_class]
        self.pending_operators.append(Operator.OPEN_PAREN)

        if ctx.THIS() is not None or len(ctx.VARID()) == 1:  # it is a local method, or inherited
            method_name = ctx.VARID()[0].getText()

            if method_name not in class_instance.methods:
                raise NameError("Method name `" + method_name + "` not defined for class: " + self.current_class)
            else:
                self.current_method_instance = class_instance.methods[method_name]

            self.current_counter = 0
        else:  # it is a method from another class instance
            self.current_counter = 0

            var_name = ctx.VARID()[0].getText()
            func_name = ctx.VARID()[1].getText()
            if var_name in class_instance.methods[self.current_method].variables:
                c_ref = master_tables.classes[class_instance.methods[self.current_method].variables[var_name]["p_type"]]
                if func_name not in c_ref.methods:
                    raise NameError("Method name `" + func_name + "` not defined for class: " + c_ref.name)

                self.current_method_instance = c_ref.methods[func_name]
            elif var_name in class_instance.variables:
                if not class_instance.variables[var_name]["type"] == Type.CLASS:
                    raise TypeError("Funcion call not made from class reference.")

                c_ref = master_tables.classes[class_instance.variables[var_name]["class_type"]]
                if func_name not in c_ref.methods:
                    raise NameError("Method name `" + func_name + "` not defined for class: " + c_ref.name)

                self.current_method_instance = c_ref.methods[func_name]
            else:
                raise NameError("Variable `" + var_name + "` not defined in class: " + class_instance.name)

            self.class_reference = c_ref.name

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitFunction_call(self, ctx: MoMParser.Function_callContext) -> None:
        """ Neuralgic point after a function is called.
            Checks if it was a same-class call or was another's class function.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        self.pending_operators.pop()
        if not self.current_counter == self.current_method_instance.num_of_params:
            raise IllegalStateException("Method `" + self.current_method_instance.name +
                                        "` has wrong number of arguments. Should be " +
                                        str(self.current_method_instance.num_of_params) +
                                        ", got " + str(self.current_counter) + " instead.")

        if self.class_reference == "":
            quad = Quadrupole(Operation.GO_SUB, self.current_class, self.current_method_instance.name,
                              self.current_method_instance.start)
            self.quads.append(quad)

            if not self.current_method_instance.return_type == Type.NOTHING:
                m = master_tables.classes[self.current_class].methods[self.current_method]
                result = self.get_temp_address_by_type(m, self.current_method_instance.return_type)
                self.increment_temp_address_by_type(m, self.current_method_instance.return_type)
                # noinspection SpellCheckingInspection
                addr = master_tables.classes[self.current_class].variables[self.current_method_instance.name]["address"]

                quad = Quadrupole(Operator.EQUAL, addr, None, result)
                self.quads.append(quad)
                self.pending_operands.append(result)
                self.pending_types.append(self.current_method_instance.return_type)
        else:
            var = ctx.VARID()[0].getText()
            c = master_tables.classes[self.current_class]
            m = c.methods[self.current_method]

            # Look in local variables, if not, look in global variables
            if var in m.variables:
                address = m.variables[var]["address"]
            elif var in c.variables:
                address = c.variables[var]["address"]
            else:
                # if not present report error.
                raise NameError("Variable ' " + var + " is undefined.")
            quad = Quadrupole(Operation.GO_SUB, str(address)+":"+self.class_reference, self.current_method_instance.name,
                              self.current_method_instance.start)
            c = master_tables.classes[self.class_reference]
            self.class_reference = ""
            self.quads.append(quad)

            if not self.current_method_instance.return_type == Type.NOTHING:
                m = master_tables.classes[self.current_class].methods[self.current_method]
                result = self.get_temp_address_by_type(m, self.current_method_instance.return_type)
                self.increment_temp_address_by_type(m, self.current_method_instance.return_type)

                quad = Quadrupole(Operation.RETRIEVE, str(address) + ":" + str(c.variables[self.current_method_instance.name]["address"]),
                                  self.current_method_instance.name,
                                  result)

                self.quads.append(quad)
                self.pending_operands.append(result)
                self.pending_types.append(self.current_method_instance.return_type)

    # noinspection PyPep8Naming
    def enterFunction_def(self, ctx: MoMParser.Function_defContext) -> None:
        """This listener gets called for the methods defined inside a class body.

        It reads the names and return types of the methods and adds them to the class in which
        they belong.

        :param ctx: ctx: the parser context for all the read methods, holds things like names and return
            type contexts.
        :return: None.
        """
        # reset virtual memory counters
        Method.cur_local_boolean = Method.LOCAL_BOOLEAN_TOP
        Method.cur_local_real = Method.LOCAL_REAL_TOP
        Method.cur_local_int = Method.LOCAL_INT_TOP
        Method.cur_local_text = Method.LOCAL_TEXT_TOP

        return_type, method_name = ctx.simple_type(), ctx.VARID()
        # refresh simple type to take it into account when creating the new method
        self.enterSimple_type(return_type)
        method_name = method_name.getText()
        self.current_method = method_name

        new_method = Method(method_name, get_type(self.current_type))
        new_method.start = len(self.quads)

        if method_name == "main":
            self.quads[0] = Quadrupole(Operation.GO_CONSTRUCTOR, self.current_class, self.current_class,
                                       master_tables.classes[self.current_class].methods[self.current_class].start)
            self.quads[1] = Quadrupole(Operation.GO_MAIN, self.current_class, method_name, new_method.start)
            self.main_found = True

        if method_name in master_tables.classes[self.current_class].methods:
            raise NameError("Method '" + method_name + "' redefined in class '"
                            + self.current_class + "', this is not supported at language level.")

        master_tables.classes[self.current_class].add_method(new_method)
        self.create_method_field(self.current_method, new_method.return_type)

    # noinspection PyPep8Naming
    def exitFunction_def(self, ctx: MoMParser.Function_defContext):
        pass

    # noinspection PyPep8Naming
    def enterExit_func_def(self, ctx: MoMParser.Exit_func_defContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitExit_func_def(self, ctx: MoMParser.Exit_func_defContext) -> None:
        """ Neuralgic point after a function is defined.
            Generates quadruple that holds the return variable's address for future calls.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        address = master_tables.classes[self.current_class].variables[self.current_method]["address"]
        quad = Quadrupole(Operation.RETURN, None, None, address)

        self.quads.append(quad)

    # noinspection PyPep8Naming
    def enterOperand(self, ctx: MoMParser.OperandContext) -> None:
        if ctx.EQUAL_EQUAL() is not None:
            self.pending_operators.append(Operator.EQUAL_EQUAL)
        elif ctx.GREATER_EQUAL() is not None:
            self.pending_operators.append(Operator.GREATER_EQUAL)
        elif ctx.GREATER_THAN() is not None:
            self.pending_operators.append(Operator.GREATER_THAN)
        elif ctx.LESS_EQUAL() is not None:
            self.pending_operators.append(Operator.LESS_EQUAL)
        else:
            self.pending_operators.append(Operator.LESS_THAN)

    # noinspection PyPep8Naming
    def exitOperand(self, ctx: MoMParser.OperandContext):
        pass

    # noinspection PyPep8Naming
    def enterField(self, ctx: MoMParser.FieldContext) -> None:
        self.in_signature = True
        self.arguments = []
        self.argument_names = []
        var_name = ctx.VARID()
        self.argument_names.append(var_name.getText())

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitField(self, ctx: MoMParser.FieldContext) -> None:
        """ Listener after a field is declared.
            Generates the corresponding memory to every field in the class.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        for name, var in zip(self.argument_names, self.arguments):
            if self.current_structure == StructureType.CLASS:
                c = master_tables.classes[self.current_class]
                address = self.get_global_address_by_type(c, get_type(var.var_type))
                t = get_type(var.var_type)
                if t == Type.CLASS:
                    c.add_argument(name, t, var.is_array, address, var.mem_size, var.dim, var.var_type)
                else:
                    c.add_argument(name, t, var.is_array, address, var.mem_size, var.dim)
                self.increment_global_address_by_type(c, get_type(var.var_type), var.mem_size)

            elif self.current_structure == StructureType.SPECIFICATION:
                master_tables.specifications[self.current_specification].methods[
                    self.current_method].add_argument(name, get_type(var.var_type), var.is_array, -2, var.mem_size, var.dim)

    # noinspection PyPep8Naming
    def enterSpec_function(self, ctx: MoMParser.Spec_functionContext) -> None:
        """ Listener when a specification is declared.
            Checks there is no repetition on method names.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        name, return_type = ctx.VARID(), ctx.simple_type()
        method = Method(name.getText(), get_type(return_type.getText()))
        self.current_method = method.name

        if method.name in master_tables.specifications[self.current_specification].methods:
            raise NameError("Method '" + method.name + "' redefined in specification '" +
                            self.current_specification + "', this is not supported at language level.")

        master_tables.specifications[self.current_specification].add_method(method)

    # noinspection PyPep8Naming
    def exitSpec_function(self, ctx: MoMParser.Spec_functionContext):
        pass

    # noinspection PyPep8Naming
    def enterSpecification(self, ctx: MoMParser.SpecificationContext) -> None:
        """Creates a new Specification if the parser encounters one while
        reading the source code.

        :param ctx: the context in which the specification definition was found.
        :return: None.
        """
        spec_name = ctx.CLASSID().getText()

        if spec_name in master_tables.specifications:
            raise NameError("Specification '" + spec_name + "' is already defined. Redefinition of specifications"
                                                            " is not supported at language level.")

        if spec_name in master_tables.classes:
            raise NameError("Specification '" + spec_name + "' cannot have the same name as an existing class.")

        master_tables.specifications[spec_name] = Specification(spec_name)
        self.current_specification = spec_name
        self.current_structure = StructureType.SPECIFICATION

    # noinspection PyPep8Naming
    def exitSpecification(self, ctx: MoMParser.SpecificationContext):
        pass

    # noinspection PyPep8Naming
    def enterAssignation_def(self, ctx: MoMParser.Assignation_defContext) -> None:
        """ Neuralgic point after an assignation is done.
            Generates the memory for the new variable and copies values from the original one.
            Handles both assignations: primitive and object assignation.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        self.destination_type = []
        self.source_type = []
        self.in_signature = True
        self.arguments = []
        self.argument_names = []
        self.destination_type.append(ctx.super_type().getText())
        var_name = ctx.VARID()
        self.argument_names.append(var_name.getText())

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitAssignation_def(self, ctx: MoMParser.Assignation_defContext) -> None:
        self.in_signature = False
        counter = 0
        for name, var in zip(self.argument_names, self.arguments):
            if self.current_structure == StructureType.CLASS:
                m = master_tables.classes[self.current_class].methods[self.current_method]
                address = self.get_address_by_type(m, get_type(var.var_type))
                t = get_type(var.var_type)
                if t == Type.CLASS:
                    if not self.source_type[counter] == self.destination_type[counter]:
                        if not self.destination_type[counter] in \
                                master_tables.classes[self.current_class].specifications:
                            raise TypeError("Source '" + self.source_type[counter] + "' and destination '" + self.destination_type[counter] + "' types not compatible.")

                    m.add_argument(name, t, var.is_array, address, var.mem_size, [], self.source_type[counter])

                    counter += 1
                else:
                    m.add_argument(name, t, var.is_array, address, var.mem_size, [])

                self.increment_address_by_type(m, get_type(var.var_type), var.mem_size)
                destination = m.variables[name]["address"]

                dest_type = get_type(var.var_type)
                src_type = self.pending_types.pop()

                if not src_type == dest_type:
                    raise TypeError("Cannot assign value of type " + str(src_type) + " to " + str(dest_type))

                holder = self.pending_operands.pop()
                quad = Quadrupole(Operator.EQUAL, holder, None, destination)
                self.quads.append(quad)

        self.source_type = []
        self.destination_type = []

    # noinspection PyPep8Naming
    def enterStatute(self, ctx: MoMParser.StatuteContext):
        pass

    # noinspection PyPep8Naming
    def exitStatute(self, ctx: MoMParser.StatuteContext):
        """ Listener after an statute is ended.
            Checks if it is a return statute to retrieve the return value from the corresponding method.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        if ctx.RETURN() is not None:
            c = master_tables.classes[self.current_class]
            m = c.methods[self.current_method]

            if ctx.ss_exp() is not None:
                # Found return with an expression
                r_type = self.pending_types.pop()
                if not r_type == m.return_type:
                    raise TypeError("Wrong return type for method `" + m.name + "` in class: " + c.name)

                r_value = self.pending_operands.pop()
                address = master_tables.classes[self.current_class].variables[self.current_method]["address"]
                quad = Quadrupole(Operator.EQUAL, r_value, None, address)

                self.quads.append(quad)
                quad = Quadrupole(Operation.RETURN, None, None, address)

                self.quads.append(quad)
            else:
                # Found single return
                if not m.return_type == Type.NOTHING:
                    raise TypeError("Wrong return type for method `" + m.name + "` in class: " + c.name)

                quad = Quadrupole(Operation.RETURN, None, None, c.nothing_address)

                self.quads.append(quad)

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterExit_factor(self, ctx: MoMParser.Exit_factorContext) -> None:
        if not len(self.pending_operators) == 0:
            if self.pending_operators[-1] == Operator.TIMES or self.pending_operators[-1] == Operator.DIVIDES:
                right_operand = self.pending_operands.pop()
                right_type = self.pending_types.pop()
                left_operand = self.pending_operands.pop()
                left_type = self.pending_types.pop()
                operator = self.pending_operators.pop()
                result_type = Type(semantic_table[int(left_type)][int(right_type)][int(operator)])

                if result_type == Type.OTHER:
                    raise TypeError("Type mismatch for expression.")
                else:
                    m = master_tables.classes[self.current_class].methods[self.current_method]
                    result = self.get_temp_address_by_type(m, result_type)
                    self.increment_temp_address_by_type(m, result_type)
                    quad = Quadrupole(operator, left_operand, right_operand, result)

                    self.quads.append(quad)
                    self.pending_operands.append(result)
                    self.pending_types.append(result_type)

    # noinspection PyPep8Naming
    def exitExit_factor(self, ctx: MoMParser.Exit_factorContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterStar_op(self, ctx: MoMParser.Star_opContext) -> None:
        self.pending_operators.append(Operator.TIMES)

    # noinspection PyPep8Naming
    def exitStar_op(self, ctx: MoMParser.Star_opContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterDiv_op(self, ctx: MoMParser.Div_opContext) -> None:
        self.pending_operators.append(Operator.DIVIDES)

    # noinspection PyPep8Naming
    def exitDiv_op(self, ctx: MoMParser.Div_opContext):
        pass

    # noinspection PyPep8Naming
    def enterTerm(self, ctx: MoMParser.TermContext):
        pass

    # noinspection PyPep8Naming
    def exitTerm(self, ctx: MoMParser.TermContext):
        pass

    # noinspection PyPep8Naming
    def enterSuper_type(self, ctx: MoMParser.Super_typeContext) -> None:
        if self.in_signature:
            self.arguments.append(Variable())
            self.arguments[-1].var_type = ctx.getText()
            self.arguments[-1].dim = []

    # noinspection PyPep8Naming
    def exitSuper_type(self, ctx: MoMParser.Super_typeContext):
        pass

    # noinspection PyPep8Naming
    def enterSimple_type(self, ctx: MoMParser.Simple_typeContext) -> None:
        """Listener that is called each time a simple type is visited, like for return types
        inside a method definition.

        Sets the self.current_type with the name of the current type that passed through this
        listener.

        :param ctx: the context that called the simple type lexeme.
        :return: None.
        """
        self.current_type = ctx.getText()

    # noinspection PyPep8Naming
    def exitSimple_type(self, ctx: MoMParser.Simple_typeContext):
        pass

    # noinspection PyPep8Naming
    def enterComplex_type(self, ctx: MoMParser.Complex_typeContext) -> None:
        """Sets the current type temp with the name of the last complex type read
        by the parser.

        :param ctx: the context from which this listener was called.
        :return: None
        """
        self.current_type = ctx.getText()

    # noinspection PyPep8Naming
    def exitComplex_type(self, ctx: MoMParser.Complex_typeContext):
        pass

    # noinspection PyPep8Naming
    def enterWhile_loop(self, ctx: MoMParser.While_loopContext):
        pass

    # noinspection PyPep8Naming
    def exitWhile_loop(self, ctx: MoMParser.While_loopContext):
        pass

    # noinspection PyPep8Naming
    def enterVdim(self, ctx: MoMParser.VdimContext):
        """ Neuralgic point for a declared n-dimension array.
            Calculates r and then Mi as seen in class with 2 sweeps.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        self.in_signature = True
        self.arguments = []
        self.argument_names = []
        var_name = ctx.VARID()
        self.argument_names.append(var_name.getText())

    # noinspection PyPep8Naming
    def exitVdim(self, ctx: MoMParser.VdimContext):
        if self.in_signature:
            self.arguments[-1].is_array = True
        self.in_signature = False

        text = ctx.getText()
        dim = []
        r = 1
        pos_open = text.find("[")
        while pos_open != -1:
            pos_close = text.find("]", pos_open + 1)
            size = int(text[pos_open + 1:pos_close].strip())
            dim.append(size)
            r = r * size
            pos_open = text.find("[", pos_open + 1)

        dim_real = []
        self.arguments[-1].mem_size = r
        for d in dim:
            dim_real.append((d, int(r / d)))
            r = r / d
        self.arguments[-1].dim = dim_real

        for name, var in zip(self.argument_names, self.arguments):
            if self.current_structure == StructureType.CLASS:
                m = master_tables.classes[self.current_class].methods[self.current_method]
                address = self.get_address_by_type(m, get_type(var.var_type))
                t = get_type(var.var_type)

                if t == Type.CLASS:
                    m.add_argument(name, t, var.is_array, address, var.mem_size, var.dim, var.var_type)
                else:
                    m.add_argument(name, t, var.is_array, address, var.mem_size, var.dim)
                m.add_argument_type(get_type(var.var_type), var.is_array)
                self.increment_address_by_type(m, get_type(var.var_type), var.mem_size)
            elif self.current_structure == StructureType.SPECIFICATION:
                master_tables.specifications[self.current_specification].methods[
                    self.current_method].add_argument(name, get_type(var.var_type), var.is_array, -2, var.mem_size)

    # noinspection PyPep8Naming, PyUnusedLocal
    def enterArray_def(self, ctx: MoMParser.Array_defContext) -> None:
        self.in_signature = True

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitArray_def(self, ctx: MoMParser.Array_defContext) -> None:
        """ Listener after an array is defined.
            Calculates r and Mi as seen in class with 2 sweeps.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        if self.in_signature:
            self.arguments[-1].is_array = True
        self.in_signature = False
        text = ctx.getText()
        dim = []
        r = 1
        pos_open = text.find("[")
        while pos_open != -1:
            pos_close = text.find("]", pos_open + 1)
            size = int(text[pos_open + 1:pos_close].strip())
            dim.append(size)
            r = r * size
            pos_open = text.find("[", pos_open + 1)

        dim_real = []
        self.arguments[-1].mem_size = r
        for d in dim:
            dim_real.append((d, int(r / d)))
            r = r / d
        self.arguments[-1].dim = dim_real

    # noinspection PyPep8Naming
    def enterArray_var(self, ctx: MoMParser.Array_varContext) -> None:
        """ Neuralgic point before an array is access.
            Generates a dimension and pushes it to the pending dims stack.
            Verifies that the acceded variable has the same dimensions.
        :param ctx: Context generated by antlr4.
        :return: None.
        """
        var = ctx.VARID().getText()
        text = ctx.getText()
        c = master_tables.classes[self.current_class]
        m = c.methods[self.current_method]

        # Look in local variables, if not, look in global variables
        if var in m.variables:
            dim = m.variables[var]["dim"]
        elif var in c.variables:
            dim = c.variables[var]["dim"]
        else:
            # if not present report error.
            raise NameError("Variable ' " + var + " is undefined.")

        # if there is nesting
        self.pending_dims.append((var, 1))
        self.pending_operators.append(Operator.OPEN_SPAREN)
        original_dim = len(dim)

        # count dimensions of accessed array
        actual_dim = 0
        stack_brackets = list()
        for c in text:
            if c == '[':
                stack_brackets.append('[')
            if c == ']':
                stack_brackets.pop()
                if len(stack_brackets) == 0:
                    actual_dim = actual_dim + 1

        if original_dim != actual_dim:
            raise NameError("Cannot convert var " + var + " of " + str(original_dim) + " dimensions to " + str(
                actual_dim) + " dimensions")

    # noinspection PyPep8Naming
    def exitArray_var(self, ctx: MoMParser.Array_varContext):
        """ Neuralgic point when a array access was done.
            Checks that the variable exists in any context.
            Generates quadruple to save (T)

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        aux1 = self.pending_operands.pop()
        type1 = self.pending_types.pop()
        c = master_tables.classes[self.current_class]
        m = c.methods[self.current_method]
        t = self.get_temp_address_by_type(m, Type.INT)
        self.increment_temp_address_by_type(m, Type.INT)

        var = ctx.VARID().getText()
        # Look in local variables, if not, look in global variables
        if var in m.variables:
            destination_base = m.variables[var]["address"]
            type_arr = m.variables[var]["type"]
        elif var in c.variables:
            destination_base = c.variables[var]["address"]
            type_arr = c.variables[var]["type"]

        quad = Quadrupole(Operator.PLUS, aux1, "$" + str(destination_base), t)

        self.quads.append(quad)

        self.pending_operands.append("&" + str(t))
        self.pending_types.append(type_arr)
        self.pending_dims.pop()
        self.pending_operators.pop()

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterWrite_func(self, ctx: MoMParser.Write_funcContext):
        self.pending_operators.append(Operator.WRITE)

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitWrite_func(self, ctx: MoMParser.Write_funcContext):
        op = self.pending_operators.pop()
        result = self.pending_operands.pop()
        self.pending_types.pop()
        quad = Quadrupole(op, None, None, result)

        self.quads.append(quad)

    # function to generalize checking valid read for any type
    def checkRead(self, var: str, check_type: Type):
        """ Helper function that validates that a given variable is
            of the expected type before reading it.

        :param var: Variable that's gonna read.
        :param check_type: Expected type.
        :return: None.
        """
        op = self.pending_operators.pop()
        c = master_tables.classes[self.current_class]
        m = c.methods[self.current_method]

        # Look in local variables, if not, look in global variables
        # verifies that variable is of that type
        if var in m.variables:
            type_var = m.variables[var]["type"]
            address = m.variables[var]["address"]
            is_array = m.variables[var]["is_array"]
        elif var in c.variables:
            type_var = c.variables[var]["type"]
            address = c.variables[var]["address"]
            is_array = c.variables[var]["is_array"]
        else:
            raise NameError("Variable ' " + var + " is undefined.")

        # if type matches and is not an array, print it
        if (type_var == check_type) & (not is_array):
            quad = Quadrupole(op, None, None, address)

            self.quads.append(quad)
        else:
            raise NameError("Type mismatch. " + var + " is not a " + str(check_type))

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterRead_int_func(self, ctx: MoMParser.Read_int_funcContext):
        self.pending_operators.append(Operator.READ_INT)

    # noinspection PyPep8Naming
    def exitRead_int_func(self, ctx: MoMParser.Read_int_funcContext):
        var = ctx.VARID().getText()
        self.checkRead(var, Type.INT)

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterRead_real_func(self, ctx: MoMParser.Read_real_funcContext):
        self.pending_operators.append(Operator.READ_REAL)

    # noinspection PyPep8Naming
    def exitRead_real_func(self, ctx: MoMParser.Read_real_funcContext):
        var = ctx.VARID().getText()
        self.checkRead(var, Type.REAL)

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterRead_text_func(self, ctx: MoMParser.Read_text_funcContext):
        self.pending_operators.append(Operator.READ_TEXT)

    # noinspection PyPep8Naming
    def exitRead_text_func(self, ctx: MoMParser.Read_text_funcContext):
        var = ctx.VARID().getText()
        self.checkRead(var, Type.TEXT)

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterRead_bool_func(self, ctx: MoMParser.Read_bool_funcContext):
        self.pending_operators.append(Operator.READ_BOOL)

    # noinspection PyPep8Naming
    def exitRead_bool_func(self, ctx: MoMParser.Read_bool_funcContext):
        var = ctx.VARID().getText()
        self.checkRead(var, Type.BOOLEAN)

    # noinspection PyPep8Naming
    def enterOpen_sbracket(self, ctx: MoMParser.Open_sbracketContext):
        pass

    # noinspection PyPep8Naming
    def exitOpen_sbracket(self, ctx: MoMParser.Open_sbracketContext):
        pass

    # noinspection PyPep8Naming,PyUnusedLocal
    def enterClose_sbracket(self, ctx: MoMParser.Close_sbracketContext):
        """ Neuralgic point for every dimension when a vector is called.
            Verifies that the pointed value is in the range.
            Checks that the index is integer.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        check = self.pending_operands[-1]
        type = self.pending_types[-1]
        current_array = self.pending_dims[-1][0]
        current_dim = self.pending_dims[-1][1] - 1

        if type != Type.INT:
            raise NameError("Non integer index [1]")

        c = master_tables.classes[self.current_class]
        m = c.methods[self.current_method]

        # Look in local variables, if not, look in global variables
        if current_array in m.variables:
            dim_size = m.variables[current_array]["dim"][current_dim][0]
            dim_m = m.variables[current_array]["dim"][current_dim][1]
        elif current_array in c.variables:
            dim_size = c.variables[current_array]["dim"][current_dim][0]
            dim_m = c.variables[current_array]["dim"][current_dim][1]

        quad = Quadrupole(Operator.VERIFY, check, 0, dim_size)

        self.quads.append(quad)

        aux = self.pending_operands.pop()
        type = self.pending_types.pop()
        t = self.get_temp_address_by_type(m, Type.INT)
        self.increment_temp_address_by_type(m, Type.INT)
        quad = Quadrupole(Operator.TIMES, aux, "$" + str(dim_m), t)

        self.quads.append(quad)
        self.pending_operands.append(t)
        self.pending_types.append(Type.INT)
        result_type = semantic_table[type][Type.INT][Operator.TIMES]
        if result_type != Type.INT:
            raise NameError("Non integer index [2]")

        if current_dim > 0:
            aux2 = self.pending_operands.pop()
            type2 = self.pending_types.pop()
            aux1 = self.pending_operands.pop()
            type1 = self.pending_types.pop()
            t = self.get_temp_address_by_type(m, Type.INT)
            self.increment_temp_address_by_type(m, Type.INT)
            quad = Quadrupole(Operator.PLUS, aux1, aux2, t)

            self.quads.append(quad)
            result_type = semantic_table[type1][type2][Operator.PLUS]
            if result_type != Type.INT:
                raise NameError("Non integer index [3]")

            self.pending_types.append(Type.INT)
            self.pending_operands.append(t)

    # noinspection PyPep8Naming,PyUnusedLocal
    def exitClose_sbracket(self, ctx: MoMParser.Close_sbracketContext):
        """ Updates pending dimensions stack.
            Increments the dimension of the current dimensioned variable.

        :param ctx: Context generated by antlr4.
        :return: None.
        """
        dim = self.pending_dims.pop()
        self.pending_dims.append((dim[0], dim[1] + 1))

    # Enter a parse tree produced by MoMParser#write_line_func.
    def enterWrite_line_func(self, ctx:MoMParser.Write_line_funcContext):
        self.pending_operators.append(Operator.WRITE_LINE)

    # Exit a parse tree produced by MoMParser#write_line_func.
    def exitWrite_line_func(self, ctx:MoMParser.Write_line_funcContext):
        op = self.pending_operators.pop()
        result = self.pending_operands.pop()
        self.pending_types.pop()
        quad = Quadrupole(op, None, None, result)
        self.quads.append(quad)

    # Enter a parse tree produced by MoMParser#not_op.
    def enterNot_op(self, ctx:MoMParser.Not_opContext):
        self.pending_operators.append(Operator.NOT)

    # Exit a parse tree produced by MoMParser#not_op.
    def exitNot_op(self, ctx:MoMParser.Not_opContext):
        pass

    # Enter a parse tree produced by MoMParser#unary_plus.
    def enterUnary_plus(self, ctx:MoMParser.Unary_plusContext):
        self.pending_operators.append(Operator.UNARY_PLUS)

    # Exit a parse tree produced by MoMParser#unary_plus.
    def exitUnary_plus(self, ctx:MoMParser.Unary_plusContext):
        pass


    # Enter a parse tree produced by MoMParser#unary_minus.
    def enterUnary_minus(self, ctx:MoMParser.Unary_minusContext):
        self.pending_operators.append(Operator.UNARY_MINUS)

    # Exit a parse tree produced by MoMParser#unary_minus.
    def exitUnary_minus(self, ctx:MoMParser.Unary_minusContext):
        pass
