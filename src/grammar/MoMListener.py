# Generated from MoM.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MoMParser import MoMParser
else:
    from MoMParser import MoMParser

# This class defines a complete listener for a parse tree produced by MoMParser.
class MoMListener(ParseTreeListener):

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


    # Enter a parse tree produced by MoMParser#class_rule.
    def enterClass_rule(self, ctx:MoMParser.Class_ruleContext):
        pass

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


    # Enter a parse tree produced by MoMParser#construct_def.
    def enterConstruct_def(self, ctx:MoMParser.Construct_defContext):
        pass

    # Exit a parse tree produced by MoMParser#construct_def.
    def exitConstruct_def(self, ctx:MoMParser.Construct_defContext):
        pass


    # Enter a parse tree produced by MoMParser#enum.
    def enterEnum(self, ctx:MoMParser.EnumContext):
        pass

    # Exit a parse tree produced by MoMParser#enum.
    def exitEnum(self, ctx:MoMParser.EnumContext):
        pass


    # Enter a parse tree produced by MoMParser#enumeration.
    def enterEnumeration(self, ctx:MoMParser.EnumerationContext):
        pass

    # Exit a parse tree produced by MoMParser#enumeration.
    def exitEnumeration(self, ctx:MoMParser.EnumerationContext):
        pass


    # Enter a parse tree produced by MoMParser#ss_exp.
    def enterSs_exp(self, ctx:MoMParser.Ss_expContext):
        pass

    # Exit a parse tree produced by MoMParser#ss_exp.
    def exitSs_exp(self, ctx:MoMParser.Ss_expContext):
        pass


    # Enter a parse tree produced by MoMParser#s_exp.
    def enterS_exp(self, ctx:MoMParser.S_expContext):
        pass

    # Exit a parse tree produced by MoMParser#s_exp.
    def exitS_exp(self, ctx:MoMParser.S_expContext):
        pass


    # Enter a parse tree produced by MoMParser#expression.
    def enterExpression(self, ctx:MoMParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MoMParser#expression.
    def exitExpression(self, ctx:MoMParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MoMParser#factor.
    def enterFactor(self, ctx:MoMParser.FactorContext):
        pass

    # Exit a parse tree produced by MoMParser#factor.
    def exitFactor(self, ctx:MoMParser.FactorContext):
        pass


    # Enter a parse tree produced by MoMParser#function_args.
    def enterFunction_args(self, ctx:MoMParser.Function_argsContext):
        pass

    # Exit a parse tree produced by MoMParser#function_args.
    def exitFunction_args(self, ctx:MoMParser.Function_argsContext):
        pass


    # Enter a parse tree produced by MoMParser#function_call.
    def enterFunction_call(self, ctx:MoMParser.Function_callContext):
        pass

    # Exit a parse tree produced by MoMParser#function_call.
    def exitFunction_call(self, ctx:MoMParser.Function_callContext):
        pass


    # Enter a parse tree produced by MoMParser#function_def.
    def enterFunction_def(self, ctx:MoMParser.Function_defContext):
        pass

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


    # Enter a parse tree produced by MoMParser#spec_function.
    def enterSpec_function(self, ctx:MoMParser.Spec_functionContext):
        pass

    # Exit a parse tree produced by MoMParser#spec_function.
    def exitSpec_function(self, ctx:MoMParser.Spec_functionContext):
        pass


    # Enter a parse tree produced by MoMParser#specification.
    def enterSpecification(self, ctx:MoMParser.SpecificationContext):
        pass

    # Exit a parse tree produced by MoMParser#specification.
    def exitSpecification(self, ctx:MoMParser.SpecificationContext):
        pass


    # Enter a parse tree produced by MoMParser#assignation_def.
    def enterAssignation_def(self, ctx:MoMParser.Assignation_defContext):
        pass

    # Exit a parse tree produced by MoMParser#assignation_def.
    def exitAssignation_def(self, ctx:MoMParser.Assignation_defContext):
        pass


    # Enter a parse tree produced by MoMParser#statute.
    def enterStatute(self, ctx:MoMParser.StatuteContext):
        pass

    # Exit a parse tree produced by MoMParser#statute.
    def exitStatute(self, ctx:MoMParser.StatuteContext):
        pass


    # Enter a parse tree produced by MoMParser#term.
    def enterTerm(self, ctx:MoMParser.TermContext):
        pass

    # Exit a parse tree produced by MoMParser#term.
    def exitTerm(self, ctx:MoMParser.TermContext):
        pass


    # Enter a parse tree produced by MoMParser#super_type.
    def enterSuper_type(self, ctx:MoMParser.Super_typeContext):
        pass

    # Exit a parse tree produced by MoMParser#super_type.
    def exitSuper_type(self, ctx:MoMParser.Super_typeContext):
        pass


    # Enter a parse tree produced by MoMParser#simple_type.
    def enterSimple_type(self, ctx:MoMParser.Simple_typeContext):
        pass

    # Exit a parse tree produced by MoMParser#simple_type.
    def exitSimple_type(self, ctx:MoMParser.Simple_typeContext):
        pass


    # Enter a parse tree produced by MoMParser#complex_type.
    def enterComplex_type(self, ctx:MoMParser.Complex_typeContext):
        pass

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

    # Exit a parse tree produced by MoMParser#array_arg.
    def exitArray_arg(self, ctx:MoMParser.Array_argContext):
        pass


