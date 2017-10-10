# Generated from MoM.g4 by ANTLR 4.7
from enum import IntEnum, auto, unique

from antlr4 import *

import src.MasterTables as master_tables
from src.structures.Class import Class
from src.structures.Enumeration import Enumeration
from src.structures.Method import Method
from src.structures.SemanticTable import get_type
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

    def __init__(self):
        self.is_array = False


class MoMListener(ParseTreeListener):
    current_enumeration = ""
    current_type = ""
    current_class = ""
    current_specification = ""
    current_method = ""
    arguments = []
    argument_names = []
    in_signature = False

    current_structure = StructureType.CLASS

    # Enter a parse tree produced by MoMParser#program.
    def enterProgram(self, ctx:MoMParser.ProgramContext):
        pass

    # Exit a parse tree produced by MoMParser#program.
    def exitProgram(self, ctx:MoMParser.ProgramContext):
        pass


    # Enter a parse tree produced by MoMParser#arguments.
    def enterArguments(self, ctx:MoMParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by MoMParser#arguments.
    def exitArguments(self, ctx:MoMParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by MoMParser#assignation.
    def enterAssignation(self, ctx:MoMParser.AssignationContext):
        pass

    # Exit a parse tree produced by MoMParser#assignation.
    def exitAssignation(self, ctx:MoMParser.AssignationContext):
        pass


    # Enter a parse tree produced by MoMParser#block.
    def enterBlock(self, ctx:MoMParser.BlockContext):
        pass

    # Exit a parse tree produced by MoMParser#block.
    def exitBlock(self, ctx:MoMParser.BlockContext):
        pass

    def enterClass_rule(self, ctx: MoMParser.Class_ruleContext) -> None:
        """This listener manages registering the classes that the user defines within a program.

        This listener is in charge of creating the class objects, specifying their names, parents
        and possible specifications.

        :param ctx: the context for this specific class instance.
        :return: None.
        """
        class_specifications = set()

        # It is a class with at least one specification
        # TODO: the grammar only supports one specification, there should be the possibility for several later
        class_name = ctx.CLASSID()[0].getText()

        for i in range(1, len(ctx.CLASSID())):
            class_specifications.add(ctx.CLASSID()[i].getText())

        self.current_class = class_name
        self.current_structure = StructureType.CLASS

        if class_name in master_tables.classes:
            raise NameError("Redefinition of class '" + class_name + "' found. This is not supported by the language.")

        # TODO: determine if need to check existence of parent or will be done in second stage
        # get the parent of this class
        self.enterComplex_type(ctx.complex_type())
        class_parent = self.current_type

        master_tables.classes[class_name] = Class(class_name, class_parent, class_specifications)

    # Exit a parse tree produced by MoMParser#class_rule.
    def exitClass_rule(self, ctx:MoMParser.Class_ruleContext):
        pass


    # Enter a parse tree produced by MoMParser#condition.
    def enterCondition(self, ctx:MoMParser.ConditionContext):
        pass

    # Exit a parse tree produced by MoMParser#condition.
    def exitCondition(self, ctx:MoMParser.ConditionContext):
        pass


    # Enter a parse tree produced by MoMParser#constant.
    def enterConstant(self, ctx:MoMParser.ConstantContext):
        pass

    # Exit a parse tree produced by MoMParser#constant.
    def exitConstant(self, ctx:MoMParser.ConstantContext):
        pass


    # Enter a parse tree produced by MoMParser#construct_call.
    def enterConstruct_call(self, ctx:MoMParser.Construct_callContext):
        pass

    # Exit a parse tree produced by MoMParser#construct_call.
    def exitConstruct_call(self, ctx:MoMParser.Construct_callContext):
        pass

    def enterConstruct_def(self, ctx: MoMParser.Construct_defContext) -> None:
        print("Entered constructor")
        method_name = ctx.CLASSID().getText()
        self.current_method = method_name

        new_method = Method(method_name, method_name)
        master_tables.classes[self.current_class].add_method(new_method)

    def exitConstruct_def(self, ctx: MoMParser.Construct_defContext):
        print("Exited constructor")

    def enterEnum(self, ctx: MoMParser.EnumContext) -> None:
        """Takes each value defined in the enumeration and assigns it to its
        corresponding enumeration.

        :param ctx: the parser context for this enumeration, holds the values of the enumeration.
        :return: None.
        """
        for value in ctx.CAPITALID():
            master_tables.enumerations[self.current_enumeration].add_value(value.getText())

    # Exit a parse tree produced by MoMParser#enum.
    def exitEnum(self, ctx:MoMParser.EnumContext):
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
    def exitEnumeration(self, ctx:MoMParser.EnumerationContext):
        pass


    # Enter a parse tree produced by MoMParser#exit_sexp.
    def enterExit_sexp(self, ctx:MoMParser.Exit_sexpContext):
        pass

    # Exit a parse tree produced by MoMParser#exit_sexp.
    def exitExit_sexp(self, ctx:MoMParser.Exit_sexpContext):
        pass


    # Enter a parse tree produced by MoMParser#and_op.
    def enterAnd_op(self, ctx:MoMParser.And_opContext):
        pass

    # Exit a parse tree produced by MoMParser#and_op.
    def exitAnd_op(self, ctx:MoMParser.And_opContext):
        pass


    # Enter a parse tree produced by MoMParser#or_op.
    def enterOr_op(self, ctx:MoMParser.Or_opContext):
        pass

    # Exit a parse tree produced by MoMParser#or_op.
    def exitOr_op(self, ctx:MoMParser.Or_opContext):
        pass


    # Enter a parse tree produced by MoMParser#ss_exp.
    def enterSs_exp(self, ctx:MoMParser.Ss_expContext):
        pass

    # Exit a parse tree produced by MoMParser#ss_exp.
    def exitSs_exp(self, ctx:MoMParser.Ss_expContext):
        pass


    # Enter a parse tree produced by MoMParser#exit_exp.
    def enterExit_exp(self, ctx:MoMParser.Exit_expContext):
        pass

    # Exit a parse tree produced by MoMParser#exit_exp.
    def exitExit_exp(self, ctx:MoMParser.Exit_expContext):
        pass


    # Enter a parse tree produced by MoMParser#s_exp.
    def enterS_exp(self, ctx:MoMParser.S_expContext):
        pass

    # Exit a parse tree produced by MoMParser#s_exp.
    def exitS_exp(self, ctx:MoMParser.S_expContext):
        pass


    # Enter a parse tree produced by MoMParser#exit_term.
    def enterExit_term(self, ctx:MoMParser.Exit_termContext):
        pass

    # Exit a parse tree produced by MoMParser#exit_term.
    def exitExit_term(self, ctx:MoMParser.Exit_termContext):
        pass


    # Enter a parse tree produced by MoMParser#plus_op.
    def enterPlus_op(self, ctx:MoMParser.Plus_opContext):
        pass

    # Exit a parse tree produced by MoMParser#plus_op.
    def exitPlus_op(self, ctx:MoMParser.Plus_opContext):
        pass


    # Enter a parse tree produced by MoMParser#minus_op.
    def enterMinus_op(self, ctx:MoMParser.Minus_opContext):
        pass

    # Exit a parse tree produced by MoMParser#minus_op.
    def exitMinus_op(self, ctx:MoMParser.Minus_opContext):
        pass


    # Enter a parse tree produced by MoMParser#expression.
    def enterExpression(self, ctx:MoMParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MoMParser#expression.
    def exitExpression(self, ctx:MoMParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MoMParser#open_paren.
    def enterOpen_paren(self, ctx:MoMParser.Open_parenContext):
        pass

    # Exit a parse tree produced by MoMParser#open_paren.
    def exitOpen_paren(self, ctx:MoMParser.Open_parenContext):
        pass


    # Enter a parse tree produced by MoMParser#close_paren.
    def enterClose_paren(self, ctx:MoMParser.Close_parenContext):
        pass

    # Exit a parse tree produced by MoMParser#close_paren.
    def exitClose_paren(self, ctx:MoMParser.Close_parenContext):
        pass


    # Enter a parse tree produced by MoMParser#factor.
    def enterFactor(self, ctx:MoMParser.FactorContext):
        pass

    # Exit a parse tree produced by MoMParser#factor.
    def exitFactor(self, ctx:MoMParser.FactorContext):
        pass

    def enterFunction_args(self, ctx: MoMParser.Function_argsContext) -> None:
        self.in_signature = True
        self.arguments = []
        self.argument_names = []

        print("Enter args for " + self.current_method)

        for var_name in ctx.VARID():
            self.argument_names.append(var_name.getText())

    def exitFunction_args(self, ctx: MoMParser.Function_argsContext) -> None:
        self.in_signature = False

        print("Exit args for " + self.current_method)

        for name, var in zip(self.argument_names, self.arguments):
            if self.current_structure == StructureType.CLASS:
                print(name + " " + var.var_type + " &&&&& " + self.current_class + " %%%%%% " + self.current_method)
                master_tables.classes[self.current_class].methods[self.current_method].add_argument(name, var.var_type,
                                                                                                    var.is_array)
                # print(master_tables.classes[self.current_class].methods[self.current_method].variables)
            elif self.current_structure == StructureType.SPECIFICATION:
                master_tables.specifications[self.current_specification].methods[
                    self.current_method].add_argument(name, var.var_type, var.is_array)

    # Enter a parse tree produced by MoMParser#function_call.
    def enterFunction_call(self, ctx:MoMParser.Function_callContext):
        pass

    # Exit a parse tree produced by MoMParser#function_call.
    def exitFunction_call(self, ctx:MoMParser.Function_callContext):
        pass

    def enterFunction_def(self, ctx: MoMParser.Function_defContext) -> None:
        """This listener gets called for the methods defined inside a class body.

        It reads the names and return types of the methods and adds them to the class in which
        they belong.

        :param ctx: ctx: the parser context for all the read methods, holds things like names and return
            type contexts.
        :return: None.
        """
        return_type, method_name = ctx.simple_type(), ctx.VARID()
        # refresh simple type to take it into account when creating the new method
        self.enterSimple_type(return_type)
        method_name = method_name.getText()
        self.current_method = method_name
        print("Current self.Method: " + self.current_method + ", current method in f: " + method_name)

        new_method = Method(method_name, get_type(self.current_type))

        if method_name in master_tables.classes[self.current_class].methods:
            raise NameError("Method '" + method_name + "' redefined in class '"
                            + self.current_class + "', this is not supported at language level.")

        master_tables.classes[self.current_class].add_method(new_method)

    # Exit a parse tree produced by MoMParser#function_def.
    def exitFunction_def(self, ctx:MoMParser.Function_defContext):
        pass


    # Enter a parse tree produced by MoMParser#operand.
    def enterOperand(self, ctx:MoMParser.OperandContext):
        pass

    # Exit a parse tree produced by MoMParser#operand.
    def exitOperand(self, ctx:MoMParser.OperandContext):
        pass


    # Enter a parse tree produced by MoMParser#field.
    def enterField(self, ctx:MoMParser.FieldContext):
        pass

    # Exit a parse tree produced by MoMParser#field.
    def exitField(self, ctx:MoMParser.FieldContext):
        pass

    def enterSpec_function(self, ctx: MoMParser.Spec_functionContext) -> None:
        name, return_type = ctx.VARID(), ctx.simple_type()
        method = Method(name.getText(), get_type(return_type.getText()))
        self.current_method = method.name

        if method.name in master_tables.specifications[self.current_specification].methods:
            raise NameError("Method '" + method.name + "' redefined in specification '" +
                            self.current_specification + "', this is not supported at language level.")

        master_tables.specifications[self.current_specification].add_method(method)

    # Exit a parse tree produced by MoMParser#spec_function.
    def exitSpec_function(self, ctx:MoMParser.Spec_functionContext):
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

    def enterAssignation_def(self, ctx: MoMParser.Assignation_defContext):
        self.in_signature = True
        self.arguments = []
        self.argument_names = []
        print("Enter assign locally " + self.current_method)

        var_name = ctx.VARID()
        self.argument_names.append(var_name.getText())

    def exitAssignation_def(self, ctx: MoMParser.Assignation_defContext):
        self.in_signature = False
        for name, var in zip(self.argument_names, self.arguments):
            if self.current_structure == StructureType.CLASS:
                print(name + " " + var.var_type + " &&&&& " + self.current_class + " %%%%%% " + self.current_method)
                master_tables.classes[self.current_class].methods[self.current_method].add_argument(name, var.var_type,
                                                                                                    var.is_array)

    # Enter a parse tree produced by MoMParser#statute.
    def enterStatute(self, ctx:MoMParser.StatuteContext):
        pass

    # Exit a parse tree produced by MoMParser#statute.
    def exitStatute(self, ctx:MoMParser.StatuteContext):
        pass


    # Enter a parse tree produced by MoMParser#exit_factor.
    def enterExit_factor(self, ctx:MoMParser.Exit_factorContext):
        pass

    # Exit a parse tree produced by MoMParser#exit_factor.
    def exitExit_factor(self, ctx:MoMParser.Exit_factorContext):
        pass


    # Enter a parse tree produced by MoMParser#star_op.
    def enterStar_op(self, ctx:MoMParser.Star_opContext):
        pass

    # Exit a parse tree produced by MoMParser#star_op.
    def exitStar_op(self, ctx:MoMParser.Star_opContext):
        pass


    # Enter a parse tree produced by MoMParser#div_op.
    def enterDiv_op(self, ctx:MoMParser.Div_opContext):
        pass

    # Exit a parse tree produced by MoMParser#div_op.
    def exitDiv_op(self, ctx:MoMParser.Div_opContext):
        pass


    # Enter a parse tree produced by MoMParser#term.
    def enterTerm(self, ctx:MoMParser.TermContext):
        pass

    # Exit a parse tree produced by MoMParser#term.
    def exitTerm(self, ctx:MoMParser.TermContext):
        pass

    def enterSuper_type(self, ctx: MoMParser.Super_typeContext) -> None:
        if self.in_signature:
            self.arguments.append(Variable())
            self.arguments[-1].var_type = ctx.getText()

    # Exit a parse tree produced by MoMParser#super_type.
    def exitSuper_type(self, ctx:MoMParser.Super_typeContext):
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
    def exitSimple_type(self, ctx:MoMParser.Simple_typeContext):
        pass

    def enterComplex_type(self, ctx: MoMParser.Complex_typeContext) -> None:
        """Sets the current type temp with the name of the last complex type read
        by the parser.

        :param ctx: the context from which this listener was called.
        :return: None
        """
        self.current_type = ctx.getText()

    # Exit a parse tree produced by MoMParser#complex_type.
    def exitComplex_type(self, ctx:MoMParser.Complex_typeContext):
        pass


    # Enter a parse tree produced by MoMParser#while_loop.
    def enterWhile_loop(self, ctx:MoMParser.While_loopContext):
        pass

    # Exit a parse tree produced by MoMParser#while_loop.
    def exitWhile_loop(self, ctx:MoMParser.While_loopContext):
        pass


    # Enter a parse tree produced by MoMParser#array_def.
    def enterArray_def(self, ctx:MoMParser.Array_defContext):
        pass

    # Exit a parse tree produced by MoMParser#array_def.
    def exitArray_def(self, ctx:MoMParser.Array_defContext):
        pass


    # Enter a parse tree produced by MoMParser#array_var.
    def enterArray_var(self, ctx:MoMParser.Array_varContext):
        pass

    # Exit a parse tree produced by MoMParser#array_var.
    def exitArray_var(self, ctx:MoMParser.Array_varContext):
        pass


    # Enter a parse tree produced by MoMParser#array_arg.
    def enterArray_arg(self, ctx:MoMParser.Array_argContext):
        pass

    def exitArray_arg(self, ctx: MoMParser.Array_argContext) -> None:
        if self.in_signature:
            self.arguments[-1].is_array = True
