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


class MoMListener(ParseTreeListener):
    current_enumeration = ""
    current_type = ""
    current_class = ""
    current_specification = ""
    current_method = ""
    current_method_instance = ""
    current_counter = 0
    arguments = []
    argument_names = []
    in_signature = False

    current_structure = StructureType.CLASS

    pending_operands = list()
    pending_types = list()
    pending_operators = list()
    pending_jumps = list()
    quads = list()

    @staticmethod
    def get_address_by_type(m: Method, t: Type):
        # TODO: should be treated as String or Type variable?
        if t == "Int":
            return m.cur_local_int
        elif t == "Real":
            return m.cur_local_real
        elif t == "Text":
            return m.cur_local_text
        elif t == "Boolean":
            return m.cur_local_boolean
        else:
            print("SPECIAL CASE FOR get_address_by_type: " + str(t))
            return -1

    @staticmethod
    def get_global_address_by_type(c: Class, t: Type):
        # TODO: should be treated as String or Type variable?
        if t == "Int":
            return c.cur_global_int
        elif t == "Real":
            return c.cur_global_real
        elif t == "Text":
            return c.cur_global_text
        elif t == "Boolean":
            return c.cur_global_boolean
        else:
            print("SPECIAL CASE FOR get_global_address_by_type: " + str(t))
            return -1

    @staticmethod
    def get_temp_address_by_type(m: Method, t: Type):
        # TODO: should be treated as String or Type variable?
        if t == Type.INT:
            return m.cur_temp_int
        elif t == Type.REAL:
            return m.cur_temp_real
        elif t == Type.TEXT:
            return m.cur_temp_text
        elif t == Type.BOOLEAN:
            return m.cur_temp_boolean
        else:
            print("SPECIAL CASE FOR get_temp_address_by_type: " + str(t))
            return -1

    @staticmethod
    def get_const_address_by_type(c: Class, t: Type):
        if t == Type.INT:
            return c.cur_const_int
        elif t == Type.REAL:
            return c.cur_const_real
        elif t == Type.TEXT:
            return c.cur_const_text
        elif t == Type.BOOLEAN:
            return c.cur_const_boolean
        else:
            print("SPECIAL CASE FOR GET get_const_address_by_type: " + str(t))
            return -1

    @staticmethod
    def increment_address_by_type(m: Method, t: Type, s: int):
        # print("incrementing local " + str(s) + " of " + m._name)
        if t == "Int":
            m.cur_local_int += s
        elif t == "Real":
            m.cur_local_real += s
        elif t == "Text":
            m.cur_local_text += s
        elif t == "Boolean":
            m.cur_local_boolean += s
        else:
            print("SPECIAL CASE FOR increment_address_by_type: " + str(t))

    @staticmethod
    def increment_global_address_by_type(c: Class, t: Type, s: int):
        # print("incrementing global " + str(s))
        if t == "Int":
            c.cur_global_int += s
        elif t == "Real":
            c.cur_global_real += s
        elif t == "Text":
            c.cur_global_text += s
        elif t == "Boolean":
            c.cur_global_boolean += s
        else:
            print("SPECIAL CASE FOR increment_global_address_by_type: " + str(t))

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
            print("SPECIAL CASE FOR increment_temp_address_by_type: " + str(t))

    @staticmethod
    def increment_const_address_by_type(c: Class, t: Type):
        if t == Type.INT:
            c.cur_const_int += 1
        elif t == Type.REAL:
            c.cur_const_real += 1
        elif t == Type.TEXT:
            c.cur_const_text += 1
        elif t == Type.BOOLEAN:
            c.cur_const_boolean += 1
        else:
            print("SPECIAL CASE FOR CONST increment_const_address_by_type: " + str(t))

    def fill(self, end: int, next_quad: int) -> None:
        quad = self.quads[end]
        quad.result = next_quad

    # Enter a parse tree produced by MoMParser#program.
    def enterProgram(self, ctx: MoMParser.ProgramContext):
        pass

    # Exit a parse tree produced by MoMParser#program.
    def exitProgram(self, ctx: MoMParser.ProgramContext) -> None:
        for index, quad in enumerate(MoMListener.quads):
            print(str(index) + ") " + str(quad.operator) + ", " + str(quad.left_operand) + ", "
                  + str(quad.right_operand) + ", " + str(quad.result))

        print("#######################################################")

        for class_name in master_tables.classes:
            class_instance = master_tables.classes[class_name]

            for method_name in class_instance.methods:
                method_instance = class_instance.methods[method_name]

                print("Name: " + method_instance.name + ", start: " + str(method_instance.start))

    def enterAfter_argument(self, ctx: MoMParser.After_argumentContext) -> None:
        argument = self.pending_operands.pop()
        argument_type = self.pending_types.pop()
        expected_type = self.current_method_instance.argument_types[self.current_counter]

        if argument_type == Type.OTHER:
            # Special case TODO: check what to do with objects IMPORTANT
            return
        else:
            argument_type = get_name(argument_type)

        if not argument_type == expected_type['arg_type']:
            raise TypeError("Argument for method `" + self.current_method + "` call wrong. "
                                                                            "Argument should be of type " +
                            expected_type["arg_type"] +
                            ", instead got: " + str(argument_type))

        quad = Quadrupole(Operation.PARAM, argument, None, "DEST" + str(self.current_counter))
        self.quads.append(quad)

    # Exit a parse tree produced by MoMParser#after_argument.
    def exitAfter_argument(self, ctx: MoMParser.After_argumentContext):
        pass

    # Enter a parse tree produced by MoMParser#advance_count.
    def enterAdvance_count(self, ctx: MoMParser.Advance_countContext):
        pass

    def exitAdvance_count(self, ctx: MoMParser.Advance_countContext) -> None:
        self.current_counter += 1

    # Enter a parse tree produced by MoMParser#arguments.
    def enterArguments(self, ctx: MoMParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by MoMParser#arguments.
    def exitArguments(self, ctx: MoMParser.ArgumentsContext):
        pass

    def enterAssignation(self, ctx: MoMParser.AssignationContext) -> None:
        pass

    def exitAssignation(self, ctx: MoMParser.AssignationContext) -> None:
        isArray = 0
        if len(ctx.VARID()) == 0:
            # array assign
            text = ctx.getText()
            abre = text.find("[")
            cierra = text.find("]")
            indexOf = int(text[abre + 1:cierra].strip())
            var = text[:abre].strip()
            isArray = 1
        elif len(ctx.VARID()) == 1:
            var = ctx.VARID()[0].getText()
        else:
            var = ctx.VARID()[1].getText()

        c = master_tables.classes[self.current_class]
        m = c.methods[self.current_method]

        # Look in local variables, if not, look in global variables
        if var in m.variables:
            destination = m.variables[var]["address"]
            if isArray == 1:
                destination += indexOf
            holder = self.pending_operands.pop()
            quad = Quadrupole(Operator.EQUAL, holder, None, destination)
            self.quads.append(quad)
        elif var in c.variables:
            destination = c.variables[var]["address"]
            if isArray == 1:
                destination += indexOf
            holder = self.pending_operands.pop()
            quad = Quadrupole(Operator.EQUAL, holder, None, destination)
            self.quads.append(quad)
        else:
            raise NameError("Variable ' " + var + " is undefined.")

    # Enter a parse tree produced by MoMParser#block.
    def enterBlock(self, ctx: MoMParser.BlockContext):
        pass

    # Exit a parse tree produced by MoMParser#block.
    def exitBlock(self, ctx: MoMParser.BlockContext):
        pass

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

        # TODO: determine if need to check existence of parent or will be done in second stage
        # get the parent of this class
        self.enterComplex_type(ctx.complex_type())
        class_parent = self.current_type

        master_tables.classes[class_name] = Class(class_name, class_parent, class_specifications)

    def exitClass_rule(self, ctx: MoMParser.Class_ruleContext) -> None:
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

    # Enter a parse tree produced by MoMParser#condition.
    def enterCondition(self, ctx: MoMParser.ConditionContext):
        pass

    def exitCondition(self, ctx: MoMParser.ConditionContext) -> None:
        pass

    def enterExit_if_check(self, ctx: MoMParser.Exit_if_checkContext) -> None:
        exp_type = self.pending_types.pop()

        if exp_type is not Type.BOOLEAN:
            assert TypeError("Condition in if statement is not boolean. It is: " + str(exp_type))

        result = self.pending_operands.pop()
        quad = Quadrupole(Operation.GO_TO_FALSE, result, None, None)
        self.quads.append(quad)
        self.pending_jumps.append(len(self.quads) - 1)

    # Exit a parse tree produced by MoMParser#exit_if_check.
    def exitExit_if_check(self, ctx: MoMParser.Exit_if_checkContext):
        pass

    # Enter a parse tree produced by MoMParser#condition_end.
    def enterCondition_end(self, ctx: MoMParser.Condition_endContext):
        pass

    def exitCondition_end(self, ctx: MoMParser.Condition_endContext) -> None:
        end = self.pending_jumps.pop()
        self.fill(end, len(self.quads))

    # Enter a parse tree produced by MoMParser#enter_else.
    def enterEnter_else(self, ctx: MoMParser.Enter_elseContext):
        pass

    def exitEnter_else(self, ctx: MoMParser.Enter_elseContext) -> None:
        quad = Quadrupole(Operation.GO_TO, None, None, None)
        self.quads.append(quad)
        false = self.pending_jumps.pop()
        self.pending_jumps.append(len(self.quads) - 1)
        self.fill(false, len(self.quads))

    def enterConstant(self, ctx: MoMParser.ConstantContext) -> None:
        c = master_tables.classes[self.current_class]
        if ctx.INTEGER() is not None:
            address = self.get_const_address_by_type(c, Type.INT)
            self.pending_operands.append(address)
            self.increment_const_address_by_type(c, Type.INT)
            self.pending_types.append(Type.INT)
        elif ctx.REAL() is not None:
            address = self.get_const_address_by_type(c, Type.REAL)
            self.pending_operands.append(address)
            self.increment_const_address_by_type(c, Type.REAL)
            self.pending_types.append(Type.REAL)
        elif ctx.TRUE() is not None:
            address = self.get_const_address_by_type(c, Type.BOOLEAN)
            self.pending_operands.append(address)
            self.increment_const_address_by_type(c, Type.BOOLEAN)
            self.pending_types.append(Type.BOOLEAN)
        elif ctx.FALSE() is not None:
            address = self.get_const_address_by_type(c, Type.BOOLEAN)
            self.pending_operands.append(address)
            self.increment_const_address_by_type(c, Type.BOOLEAN)
            self.pending_types.append(Type.BOOLEAN)
        elif ctx.STRING() is not None:
            address = self.get_const_address_by_type(c, Type.TEXT)
            self.pending_operands.append(address)
            self.increment_const_address_by_type(c, Type.TEXT)
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

            self.pending_types.append(get_type(t))
        elif ctx.array_var() is not None:
            # See array_var listener
            pass

    # Exit a parse tree produced by MoMParser#constant.
    def exitConstant(self, ctx: MoMParser.ConstantContext):
        pass

    def enterConstruct_call(self, ctx: MoMParser.Construct_callContext) -> None:
        method_name = ctx.CLASSID().getText()
        class_instance = master_tables.classes[method_name]

        if method_name not in class_instance.methods:
            raise NameError("Constructor name `" + method_name + "` not defined for class: " + self.current_class)

        self.current_counter = 0
        self.current_method_instance = class_instance.methods[method_name]

    def exitConstruct_call(self, ctx: MoMParser.Construct_callContext) -> None:
        if not self.current_counter == self.current_method_instance.num_of_params:
            raise IllegalStateException("Constructor `" + self.current_method_instance.name +
                                        "` has wrong number of arguments. Should be " +
                                        str(self.current_method_instance.num_of_params) +
                                        ", got " + str(self.current_counter) + " instead.")

        quad = Quadrupole(Operation.GO_CONSTRUCTOR, self.current_class, self.current_method_instance.name,
                          self.current_method_instance.start)
        self.quads.append(quad)

        # TODO: remove this statement after expression support classes
        self.pending_operands.append("CONSTRUCTOR")

    # Enter a parse tree produced by MoMParser#exit_con_def.
    def enterExit_con_def(self, ctx: MoMParser.Exit_con_defContext):
        pass

    def exitExit_con_def(self, ctx: MoMParser.Exit_con_defContext) -> None:
        quad = Quadrupole(Operation.RETURN, None, None, None)
        self.quads.append(quad)

    def enterConstruct_def(self, ctx: MoMParser.Construct_defContext) -> None:
        # reset virtual memory counters
        Method.cur_local_boolean = Method.LOCAL_BOOLEAN_TOP
        Method.cur_local_real = Method.LOCAL_REAL_TOP
        Method.cur_local_int = Method.LOCAL_INT_TOP
        Method.cur_local_text = Method.LOCAL_TEXT_TOP

        method_name = ctx.CLASSID().getText()
        self.current_method = method_name
        new_method = Method(method_name, method_name)
        new_method.start = len(self.quads)

        if method_name in master_tables.classes[self.current_class].methods:
            raise NameError("Method '" + method_name + "' redefined in class '"
                            + self.current_class + "', this is not supported at language level.")

        master_tables.classes[self.current_class].add_method(new_method)

    def exitConstruct_def(self, ctx: MoMParser.Construct_defContext):
        pass

    def enterEnum(self, ctx: MoMParser.EnumContext) -> None:
        """Takes each value defined in the enumeration and assigns it to its
        corresponding enumeration.

        :param ctx: the parser context for this enumeration, holds the values of the enumeration.
        :return: None.
        """
        for value in ctx.CAPITALID():
            master_tables.enumerations[self.current_enumeration].add_value(value.getText())

    # Exit a parse tree produced by MoMParser#enum.
    def exitEnum(self, ctx: MoMParser.EnumContext):
        pass

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

    # Exit a parse tree produced by MoMParser#enumeration.
    def exitEnumeration(self, ctx: MoMParser.EnumerationContext):
        pass

    def enterExit_sexp(self, ctx: MoMParser.Exit_sexpContext) -> None:
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

    # Exit a parse tree produced by MoMParser#exit_sexp.
    def exitExit_sexp(self, ctx: MoMParser.Exit_sexpContext):
        pass

    def enterAnd_op(self, ctx: MoMParser.And_opContext) -> None:
        self.pending_operators.append(Operator.AND)

    # Exit a parse tree produced by MoMParser#and_op.
    def exitAnd_op(self, ctx: MoMParser.And_opContext):
        pass

    def enterOr_op(self, ctx: MoMParser.Or_opContext) -> None:
        self.pending_operators.append(Operator.OR)

    # Exit a parse tree produced by MoMParser#or_op.
    def exitOr_op(self, ctx: MoMParser.Or_opContext):
        pass

    # Enter a parse tree produced by MoMParser#ss_exp.
    def enterSs_exp(self, ctx: MoMParser.Ss_expContext):
        pass

    # Exit a parse tree produced by MoMParser#ss_exp.
    def exitSs_exp(self, ctx: MoMParser.Ss_expContext):
        pass

    def enterExit_exp(self, ctx: MoMParser.Exit_expContext) -> None:
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

    # Exit a parse tree produced by MoMParser#exit_exp.
    def exitExit_exp(self, ctx: MoMParser.Exit_expContext):
        pass

    # Enter a parse tree produced by MoMParser#s_exp.
    def enterS_exp(self, ctx: MoMParser.S_expContext):
        pass

    # Exit a parse tree produced by MoMParser#s_exp.
    def exitS_exp(self, ctx: MoMParser.S_expContext):
        pass

    def enterExit_term(self, ctx: MoMParser.Exit_termContext) -> None:
        if not len(self.pending_operators) == 0:
            if self.pending_operators[-1] == Operator.PLUS or self.pending_operators[-1] == Operator.MINUS:
                right_operand = self.pending_operands.pop()
                right_type = self.pending_types.pop()
                left_operand = self.pending_operands.pop()
                left_type = self.pending_types.pop()
                operator = self.pending_operators.pop()
                # TODO: check why cast was necessary
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

    def exitExit_term(self, ctx: MoMParser.Exit_termContext):
        pass

    # Enter a parse tree produced by MoMParser#after_while.
    def enterAfter_while(self, ctx: MoMParser.After_whileContext):
        pass

    def exitAfter_while(self, ctx: MoMParser.After_whileContext) -> None:
        self.pending_jumps.append(len(self.quads))

    # Enter a parse tree produced by MoMParser#end_while.
    def enterEnd_while(self, ctx: MoMParser.End_whileContext):
        pass

    def exitEnd_while(self, ctx: MoMParser.End_whileContext) -> None:
        end = self.pending_jumps.pop()
        go_back = self.pending_jumps.pop()
        quad = Quadrupole(Operation.GO_TO, None, None, go_back)
        self.quads.append(quad)
        self.fill(end, len(self.quads))

    def enterPlus_op(self, ctx: MoMParser.Plus_opContext) -> None:
        self.pending_operators.append(Operator.PLUS)

    # Exit a parse tree produced by MoMParser#plus_op.
    def exitPlus_op(self, ctx: MoMParser.Plus_opContext):
        pass

    def enterMinus_op(self, ctx: MoMParser.Minus_opContext) -> None:
        self.pending_operators.append(Operator.MINUS)

    # Exit a parse tree produced by MoMParser#minus_op.
    def exitMinus_op(self, ctx: MoMParser.Minus_opContext):
        pass

    # Enter a parse tree produced by MoMParser#expression.
    def enterExpression(self, ctx: MoMParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MoMParser#expression.
    def exitExpression(self, ctx: MoMParser.ExpressionContext):
        pass

    def enterOpen_paren(self, ctx: MoMParser.Open_parenContext) -> None:
        self.pending_operators.append(Operator.OPEN_PAREN)

    # Exit a parse tree produced by MoMParser#open_paren.
    def exitOpen_paren(self, ctx: MoMParser.Open_parenContext):
        pass

    def enterClose_paren(self, ctx: MoMParser.Close_parenContext):
        self.pending_operators.pop()

    # Exit a parse tree produced by MoMParser#close_paren.
    def exitClose_paren(self, ctx: MoMParser.Close_parenContext):
        pass

    # Enter a parse tree produced by MoMParser#factor.
    def enterFactor(self, ctx: MoMParser.FactorContext):
        pass

    # Exit a parse tree produced by MoMParser#factor.
    def exitFactor(self, ctx: MoMParser.FactorContext):
        pass

    def enterFunction_args(self, ctx: MoMParser.Function_argsContext) -> None:
        self.in_signature = True
        self.arguments = []
        self.argument_names = []

        for var_name in ctx.VARID():
            self.argument_names.append(var_name.getText())

    def exitFunction_args(self, ctx: MoMParser.Function_argsContext) -> None:
        self.in_signature = False

        for name, var in zip(self.argument_names, self.arguments):
            if self.current_structure == StructureType.CLASS:
                m = master_tables.classes[self.current_class].methods[self.current_method]
                address = self.get_address_by_type(m, var.var_type)
                m.add_argument(name, var.var_type, var.is_array, address, var.mem_size)
                m.add_argument_type(var.var_type, var.is_array)
                self.increment_address_by_type(m, var.var_type, var.mem_size)
            elif self.current_structure == StructureType.SPECIFICATION:
                master_tables.specifications[self.current_specification].methods[
                    self.current_method].add_argument(name, var.var_type, var.is_array, -2, var.mem_size)

    def enterFunction_call(self, ctx: MoMParser.Function_callContext) -> None:
        if ctx.THIS() is not None or len(ctx.VARID()) == 1:  # it is a local method, or inherited
            method_name = ctx.VARID()[0].getText()
            class_instance = master_tables.classes[self.current_class]

            if method_name not in class_instance.methods:
                if "parent" == method_name:
                    # TODO: handle special case for parent constructor call
                    return
                else:
                    raise NameError("Method name `" + method_name + "` not defined for class: " + self.current_class)

            self.current_counter = 0
            self.current_method_instance = class_instance.methods[method_name]
        else:  # it is a method from another class instance
            self.current_counter = 0

    def exitFunction_call(self, ctx: MoMParser.Function_callContext) -> None:
        if not self.current_counter == self.current_method_instance.num_of_params:
            raise IllegalStateException("Method `" + self.current_method_instance.name +
                                        "` has wrong number of arguments. Should be " +
                                        str(self.current_method_instance.num_of_params) +
                                        ", got " + str(self.current_counter) + " instead.")

        quad = Quadrupole(Operation.GO_SUB, self.current_class, self.current_method_instance.name,
                          self.current_method_instance.start)
        self.quads.append(quad)

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

        if method_name in master_tables.classes[self.current_class].methods:
            raise NameError("Method '" + method_name + "' redefined in class '"
                            + self.current_class + "', this is not supported at language level.")

        master_tables.classes[self.current_class].add_method(new_method)

    # Exit a parse tree produced by MoMParser#function_def.
    def exitFunction_def(self, ctx: MoMParser.Function_defContext):
        pass

    # Enter a parse tree produced by MoMParser#exit_func_def.
    def enterExit_func_def(self, ctx: MoMParser.Exit_func_defContext):
        pass

    def exitExit_func_def(self, ctx: MoMParser.Exit_func_defContext) -> None:
        quad = Quadrupole(Operation.RETURN, None, None, None)
        self.quads.append(quad)

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

    # Exit a parse tree produced by MoMParser#operand.
    def exitOperand(self, ctx: MoMParser.OperandContext):
        pass

    def enterField(self, ctx: MoMParser.FieldContext) -> None:
        self.in_signature = True
        self.arguments = []
        self.argument_names = []
        var_name = ctx.VARID()
        self.argument_names.append(var_name.getText())

    def exitField(self, ctx: MoMParser.FieldContext) -> None:
        for name, var in zip(self.argument_names, self.arguments):
            if self.current_structure == StructureType.CLASS:
                c = master_tables.classes[self.current_class]
                address = self.get_global_address_by_type(c, var.var_type)
                c.add_argument(name, var.var_type, var.is_array, address, var.mem_size)
                self.increment_global_address_by_type(c, var.var_type, var.mem_size)
            elif self.current_structure == StructureType.SPECIFICATION:
                master_tables.specifications[self.current_specification].methods[
                    self.current_method].add_argument(name, var.var_type, var.is_array, -2, var.mem_size)

    def enterSpec_function(self, ctx: MoMParser.Spec_functionContext) -> None:
        name, return_type = ctx.VARID(), ctx.simple_type()
        method = Method(name.getText(), get_type(return_type.getText()))
        self.current_method = method.name

        if method.name in master_tables.specifications[self.current_specification].methods:
            raise NameError("Method '" + method.name + "' redefined in specification '" +
                            self.current_specification + "', this is not supported at language level.")

        master_tables.specifications[self.current_specification].add_method(method)

    # Exit a parse tree produced by MoMParser#spec_function.
    def exitSpec_function(self, ctx: MoMParser.Spec_functionContext):
        pass

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

        master_tables.specifications[spec_name] = Specification(spec_name)
        self.current_specification = spec_name
        self.current_structure = StructureType.SPECIFICATION

    # Exit a parse tree produced by MoMParser#specification.
    def exitSpecification(self, ctx: MoMParser.SpecificationContext):
        pass

    def enterAssignation_def(self, ctx: MoMParser.Assignation_defContext) -> None:
        self.in_signature = True
        self.arguments = []
        self.argument_names = []

        var_name = ctx.VARID()
        self.argument_names.append(var_name.getText())

    def exitAssignation_def(self, ctx: MoMParser.Assignation_defContext) -> None:
        self.in_signature = False
        for name, var in zip(self.argument_names, self.arguments):
            if self.current_structure == StructureType.CLASS:
                m = master_tables.classes[self.current_class].methods[self.current_method]
                address = self.get_address_by_type(m, var.var_type)
                m.add_argument(name, var.var_type, var.is_array, address, var.mem_size)
                self.increment_address_by_type(m, var.var_type, var.mem_size)

                destination = m.variables[name]["address"]

                holder = self.pending_operands.pop()
                quad = Quadrupole(Operator.EQUAL, holder, None, destination)
                self.quads.append(quad)

    # Enter a parse tree produced by MoMParser#statute.
    def enterStatute(self, ctx: MoMParser.StatuteContext):
        pass

    # Exit a parse tree produced by MoMParser#statute.
    def exitStatute(self, ctx: MoMParser.StatuteContext):
        pass

    def enterExit_factor(self, ctx: MoMParser.Exit_factorContext) -> None:
        if not len(self.pending_operators) == 0:
            if self.pending_operators[-1] == Operator.TIMES or self.pending_operators[-1] == Operator.DIVIDES:
                right_operand = self.pending_operands.pop()
                right_type = self.pending_types.pop()
                left_operand = self.pending_operands.pop()
                left_type = self.pending_types.pop()
                operator = self.pending_operators.pop()
                result_type = semantic_table[int(left_type)][int(right_type)][int(operator)]

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

    # Exit a parse tree produced by MoMParser#exit_factor.
    def exitExit_factor(self, ctx: MoMParser.Exit_factorContext):
        pass

    def enterStar_op(self, ctx: MoMParser.Star_opContext) -> None:
        self.pending_operators.append(Operator.TIMES)

    # Exit a parse tree produced by MoMParser#star_op.
    def exitStar_op(self, ctx: MoMParser.Star_opContext):
        pass

    def enterDiv_op(self, ctx: MoMParser.Div_opContext) -> None:
        self.pending_operators.append(Operator.DIVIDES)

    # Exit a parse tree produced by MoMParser#div_op.
    def exitDiv_op(self, ctx: MoMParser.Div_opContext):
        pass

    # Enter a parse tree produced by MoMParser#term.
    def enterTerm(self, ctx: MoMParser.TermContext):
        pass

    # Exit a parse tree produced by MoMParser#term.
    def exitTerm(self, ctx: MoMParser.TermContext):
        pass

    def enterSuper_type(self, ctx: MoMParser.Super_typeContext) -> None:
        if self.in_signature:
            self.arguments.append(Variable())
            self.arguments[-1].var_type = ctx.getText()

    # Exit a parse tree produced by MoMParser#super_type.
    def exitSuper_type(self, ctx: MoMParser.Super_typeContext):
        pass

    def enterSimple_type(self, ctx: MoMParser.Simple_typeContext) -> None:
        """Listener that is called each time a simple type is visited, like for return types
        inside a method definition.

        Sets the self.current_type with the name of the current type that passed through this
        listener.

        :param ctx: the context that called the simple type lexeme.
        :return: None.
        """
        self.current_type = ctx.getText()

    # Exit a parse tree produced by MoMParser#simple_type.
    def exitSimple_type(self, ctx: MoMParser.Simple_typeContext):
        pass

    def enterComplex_type(self, ctx: MoMParser.Complex_typeContext) -> None:
        """Sets the current type temp with the name of the last complex type read
        by the parser.

        :param ctx: the context from which this listener was called.
        :return: None
        """
        self.current_type = ctx.getText()

    # Exit a parse tree produced by MoMParser#complex_type.
    def exitComplex_type(self, ctx: MoMParser.Complex_typeContext):
        pass

    # Enter a parse tree produced by MoMParser#while_loop.
    def enterWhile_loop(self, ctx: MoMParser.While_loopContext):
        pass

    # Exit a parse tree produced by MoMParser#while_loop.
    def exitWhile_loop(self, ctx: MoMParser.While_loopContext):
        pass

    def enterArray_def(self, ctx: MoMParser.Array_defContext) -> None:
        texto = ctx.getText()
        abre = texto.find("[")
        cierra = texto.find("]")
        cuantos = int(texto[abre + 1:cierra].strip())
        tipo = texto[:abre].strip()
        if self.in_signature:
            self.arguments.append(Variable())
            self.arguments[-1].var_type = tipo
            self.arguments[-1].mem_size = cuantos
            self.arguments[-1].is_array = True

    # Exit a parse tree produced by MoMParser#array_def.
    def exitArray_def(self, ctx: MoMParser.Array_defContext) -> None:
        if self.in_signature:
            self.arguments[-1].is_array = True

    def enterArray_var(self, ctx: MoMParser.Array_varContext) -> None:
        texto = ctx.getText()
        abre = texto.find("[")
        cierra = texto.find("]")
        variable = texto[:abre].strip()
        var_index = int(texto[abre + 1:cierra])
        c = master_tables.classes[self.current_class]
        m = c.methods[self.current_method]

        # Look in local variables, if not, look in global variables
        # TODO: check value for type, depending on array declaration, INT type used to avoid errors
        if variable in m.variables:
            t = m.variables[variable]["type"]
            is_array = m.variables[variable]["is_array"]
            mem_size = m.variables[variable]["mem_size"]
            if is_array:
                if 0 <= var_index < mem_size:
                    self.pending_operands.append(m.variables[variable]["address"] + var_index)
                    self.pending_types.append(Type.INT)
                else:
                    raise NameError("Out of bounds")
            else:
                raise NameError("Variable " + variable + " is not an array")
        elif variable in c.variables:
            t = c.variables[variable]["type"]
            is_array = c.variables[variable]["is_array"]
            mem_size = c.variables[variable]["mem_size"]
            if is_array:
                if 0 <= var_index < mem_size:
                    self.pending_operands.append(c.variables[variable]["address"] + var_index)
                    self.pending_types.append(Type.INT)
                else:
                    raise NameError("Out of bounds")
            else:
                raise NameError("Variable " + variable + " is not an array")
        else:
            raise NameError("Variable ' " + variable + " is undefined.")

    # Exit a parse tree produced by MoMParser#array_var.
    def exitArray_var(self, ctx: MoMParser.Array_varContext):
        pass

    # Enter a parse tree produced by MoMParser#array_arg.
    def enterArray_arg(self, ctx: MoMParser.Array_argContext):
        pass

    def exitArray_arg(self, ctx: MoMParser.Array_argContext) -> None:
        if self.in_signature:
            self.arguments[-1].is_array = True

    # Enter a parse tree produced by MoMParser#write_func.
    def enterWrite_func(self, ctx: MoMParser.Write_funcContext):
        self.pending_operators.append(Operator.WRITE)

    # Exit a parse tree produced by MoMParser#write_func.
    def exitWrite_func(self, ctx: MoMParser.Write_funcContext):
        op = self.pending_operators.pop()
        result = self.pending_operands.pop()
        quad = Quadrupole(op, None, None, result)
        self.quads.append(quad)

    # Enter a parse tree produced by MoMParser#read_func.
    def enterRead_func(self, ctx: MoMParser.Read_funcContext):
        self.pending_operators.append(Operator.READ)

    # Exit a parse tree produced by MoMParser#read_func.
    def exitRead_func(self, ctx: MoMParser.Read_funcContext):
        op = self.pending_operators.pop()
        var = ctx.VARID().getText()
        c = master_tables.classes[self.current_class]
        m = c.methods[self.current_method]

        # Look in local variables, if not, look in global variables
        if var in m.variables:
            t = m.variables[var]["type"]
            address = m.variables[var]["address"]
        elif var in c.variables:
            t = c.variables[var]["type"]
            address = c.variables[var]["address"]
        else:
            raise NameError("Variable ' " + var + " is undefined.")

        quad = Quadrupole(op, None, None, address)
        self.quads.append(quad)
