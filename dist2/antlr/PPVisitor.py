# Generated from ./antlr/PP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PPParser import PPParser
else:
    from PPParser import PPParser

# This class defines a complete generic visitor for a parse tree produced by PPParser.

class PPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PPParser#program.
    def visitProgram(self, ctx:PPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#instruction.
    def visitInstruction(self, ctx:PPParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#printExpression.
    def visitPrintExpression(self, ctx:PPParser.PrintExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#inputExpression.
    def visitInputExpression(self, ctx:PPParser.InputExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#readExpression.
    def visitReadExpression(self, ctx:PPParser.ReadExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:PPParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#condition.
    def visitCondition(self, ctx:PPParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#logicalExpression.
    def visitLogicalExpression(self, ctx:PPParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#arithmeticalExpression.
    def visitArithmeticalExpression(self, ctx:PPParser.ArithmeticalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#loop.
    def visitLoop(self, ctx:PPParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#assignment.
    def visitAssignment(self, ctx:PPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#variableName.
    def visitVariableName(self, ctx:PPParser.VariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#integer.
    def visitInteger(self, ctx:PPParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#positiveInteger.
    def visitPositiveInteger(self, ctx:PPParser.PositiveIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#conditionBody.
    def visitConditionBody(self, ctx:PPParser.ConditionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PPParser#loopBody.
    def visitLoopBody(self, ctx:PPParser.LoopBodyContext):
        return self.visitChildren(ctx)



del PPParser