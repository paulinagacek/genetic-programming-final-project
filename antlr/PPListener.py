# Generated from ./antlr/PP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PPParser import PPParser
else:
    from antlr.PPParser import PPParser

# This class defines a complete listener for a parse tree produced by PPParser.
class PPListener(ParseTreeListener):

    # Enter a parse tree produced by PPParser#program.
    def enterProgram(self, ctx:PPParser.ProgramContext):
        pass

    # Exit a parse tree produced by PPParser#program.
    def exitProgram(self, ctx:PPParser.ProgramContext):
        pass


    # Enter a parse tree produced by PPParser#instruction.
    def enterInstruction(self, ctx:PPParser.InstructionContext):
        pass

    # Exit a parse tree produced by PPParser#instruction.
    def exitInstruction(self, ctx:PPParser.InstructionContext):
        pass


    # Enter a parse tree produced by PPParser#printExpression.
    def enterPrintExpression(self, ctx:PPParser.PrintExpressionContext):
        pass

    # Exit a parse tree produced by PPParser#printExpression.
    def exitPrintExpression(self, ctx:PPParser.PrintExpressionContext):
        pass


    # Enter a parse tree produced by PPParser#inputExpression.
    def enterInputExpression(self, ctx:PPParser.InputExpressionContext):
        pass

    # Exit a parse tree produced by PPParser#inputExpression.
    def exitInputExpression(self, ctx:PPParser.InputExpressionContext):
        pass


    # Enter a parse tree produced by PPParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:PPParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by PPParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:PPParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by PPParser#condition.
    def enterCondition(self, ctx:PPParser.ConditionContext):
        pass

    # Exit a parse tree produced by PPParser#condition.
    def exitCondition(self, ctx:PPParser.ConditionContext):
        pass


    # Enter a parse tree produced by PPParser#logicalExpression.
    def enterLogicalExpression(self, ctx:PPParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by PPParser#logicalExpression.
    def exitLogicalExpression(self, ctx:PPParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by PPParser#arithmeticalExpression.
    def enterArithmeticalExpression(self, ctx:PPParser.ArithmeticalExpressionContext):
        pass

    # Exit a parse tree produced by PPParser#arithmeticalExpression.
    def exitArithmeticalExpression(self, ctx:PPParser.ArithmeticalExpressionContext):
        pass


    # Enter a parse tree produced by PPParser#loop.
    def enterLoop(self, ctx:PPParser.LoopContext):
        pass

    # Exit a parse tree produced by PPParser#loop.
    def exitLoop(self, ctx:PPParser.LoopContext):
        pass


    # Enter a parse tree produced by PPParser#assignment.
    def enterAssignment(self, ctx:PPParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PPParser#assignment.
    def exitAssignment(self, ctx:PPParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PPParser#variableName.
    def enterVariableName(self, ctx:PPParser.VariableNameContext):
        pass

    # Exit a parse tree produced by PPParser#variableName.
    def exitVariableName(self, ctx:PPParser.VariableNameContext):
        pass


    # Enter a parse tree produced by PPParser#integer.
    def enterInteger(self, ctx:PPParser.IntegerContext):
        pass

    # Exit a parse tree produced by PPParser#integer.
    def exitInteger(self, ctx:PPParser.IntegerContext):
        pass


    # Enter a parse tree produced by PPParser#conditionBody.
    def enterConditionBody(self, ctx:PPParser.ConditionBodyContext):
        pass

    # Exit a parse tree produced by PPParser#conditionBody.
    def exitConditionBody(self, ctx:PPParser.ConditionBodyContext):
        pass


    # Enter a parse tree produced by PPParser#loopBody.
    def enterLoopBody(self, ctx:PPParser.LoopBodyContext):
        pass

    # Exit a parse tree produced by PPParser#loopBody.
    def exitLoopBody(self, ctx:PPParser.LoopBodyContext):
        pass



del PPParser