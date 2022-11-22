# Generated from ./antlr/PP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PPParser import PPParser
else:
    from PPParser import PPParser

# This class defines a complete generic visitor for a parse tree produced by PPParser.


class PPVisitor(ParseTreeVisitor):

    def __init__(self, max_nr_of_ticks: int = 100) -> None:
        self.variables = {}  # mapps names to values
        self.max_nr_of_ticks = max_nr_of_ticks
        self.ticks = 0

    def visitProgram(self, ctx: PPParser.ProgramContext):
        self.visitChildren(ctx)
        self.display_variables()

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
            if not self.variables.get(input):
                self.variables[input] = 0
            value = self.variables.get(input)
        return value

    # to do
    def visitConditionalStatement(self, ctx: PPParser.ConditionalStatementContext):
        if self.visit(ctx.cond):
            self.visit(ctx.con_body)

    # to do
    def visitCondition(self, ctx: PPParser.ConditionContext):
        left_expr = self.visit(ctx.left_expr)
        right_expr = self.visit(ctx.right_expr)
        op = ctx.op.text
        operation = {
            "<": lambda x, y: x < y,
            ">": lambda x, y: x > y,
            "==": lambda x, y: x == y,
            "!=": lambda x, y: x != y,
        }
        return operation[op](left_expr, right_expr)

    def visitLogicalExpression(self, ctx: PPParser.LogicalExpressionContext):
        if ctx.cond:
            return self.visit(ctx.cond)
        left = self.visit(ctx.left_expr)
        right = self.visit(ctx.right_expr)
        op = ctx.op.text
        operation = {
            "AND": lambda x, y: x and y,
            "OR": lambda x, y: x or y,
        }
        return operation[op](left, right)

    def visitArithmeticalExpression(self, ctx: PPParser.ArithmeticalExpressionContext):
        if ctx.integer_:
            return self.visit(ctx.integer_)
        if ctx.variable_name_:
            varname = self.visit(ctx.variable_name_)
            if not self.variables.get(varname):
                self.variables[varname] = 0
            return self.variables.get(varname)

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

    def visitLoop(self, ctx: PPParser.LoopContext):
        while self.ticks < self.max_nr_of_ticks and self.visit(ctx.cond):
            self.visit(ctx.loop_body)
            self.ticks += 1

    def visitAssignment(self, ctx: PPParser.AssignmentContext):
        varname = self.visit(ctx.children[0])
        self.variables[str(varname)] = self.visit(
            ctx.art_expr) if ctx.art_expr else self.visit(ctx.input_)

    def visitVariableName(self, ctx: PPParser.VariableNameContext):
        return ctx.getText()

    def visitInteger(self, ctx: PPParser.IntegerContext):
        return int(ctx.getText())

    def visitConditionBody(self, ctx: PPParser.ConditionBodyContext):
        return self.visitChildren(ctx)

    def visitLoopBody(self, ctx: PPParser.LoopBodyContext):
        return self.visitChildren(ctx)

    def display_variables(self):
        print("Variables:")
        for key, value in self.variables.items():
            print(key, " = ", value)


del PPParser
