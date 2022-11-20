# Generated from ./antlr/PP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PPParser import PPParser
else:
    from PPParser import PPParser

# This class defines a complete generic visitor for a parse tree produced by PPParser.


class PPVisitor(ParseTreeVisitor):
    variables = {}  # mapps names to values

    def visitProgram(self, ctx: PPParser.ProgramContext):
        self.visitChildren(ctx)
        PPVisitor.display_variables()

    def visitInstruction(self, ctx: PPParser.InstructionContext):
        return self.visitChildren(ctx)

    def visitPrintExpression(self, ctx: PPParser.PrintExpressionContext):
        print("print:", self.visitChildren(ctx))

    def visitInputExpression(self, ctx: PPParser.InputExpressionContext):
        # only inputs of type: integer, variableName are accepted
        value = input("input:")
        if value.isnumeric():
            value = int(input)
        else:  # str -> syntax should be checked
            if not PPVisitor.variables.get(input):
                PPVisitor.variables[input] = 0
            value = PPVisitor.variables.get(input)
        return value

    # Visit a parse tree produced by PPParser#conditionalStatement.
    def visitConditionalStatement(self, ctx: PPParser.ConditionalStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PPParser#condition.
    def visitCondition(self, ctx: PPParser.ConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PPParser#logicalExpression.
    def visitLogicalExpression(self, ctx: PPParser.LogicalExpressionContext):
        return self.visitChildren(ctx)

    def visitArithmeticalExpression(self, ctx: PPParser.ArithmeticalExpressionContext):
        if ctx.integer_:
            return self.visit(ctx.integer_)
        if ctx.variable_name_:
            varname = self.visit(ctx.variable_name_)
            if not PPVisitor.variables.get(varname):
                PPVisitor.variables[varname] = 0
            return PPVisitor.variables.get(varname)

        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        operation = {
            '+': lambda: left + right,
            '-': lambda: left - right,
            '*': lambda: left * right,
            '/': lambda: left / right,
        }
        return operation.get(op, lambda: None)()

    # Visit a parse tree produced by PPParser#loop.
    def visitLoop(self, ctx: PPParser.LoopContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: PPParser.AssignmentContext):
        varname = self.visit(ctx.children[0])
        PPVisitor.variables[str(varname)] = self.visit(ctx.art_expr) if ctx.art_expr else self.visit(ctx.input_)

    def visitVariableName(self, ctx: PPParser.VariableNameContext):
        return ctx.getText()

    def visitInteger(self, ctx: PPParser.IntegerContext):
        return int(ctx.getText())

    # Visit a parse tree produced by PPParser#conditionBody.
    def visitConditionBody(self, ctx: PPParser.ConditionBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PPParser#loopBody.
    def visitLoopBody(self, ctx: PPParser.LoopBodyContext):
        return self.visitChildren(ctx)

    @staticmethod
    def display_variables():
        print("Variables:")
        for key, value in PPVisitor.variables.items():
            print(key, " = ", value)


del PPParser
