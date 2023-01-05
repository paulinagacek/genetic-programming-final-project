# Generated from ./antlr/PP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PPParser import PPParser
else:
    from PPParser import PPParser

# This class defines a complete generic visitor for a parse tree produced by PPParser.


class PPVisitor(ParseTreeVisitor):

    def __init__(self, input_var=None, max_nr_of_ticks: int = 500) -> None:
        self.variables = {}  # mapps names to values
        self.max_nr_of_ticks = max_nr_of_ticks
        self.ticks = 0
        self.input_var = input_var if input_var else []
        self.prints = []

    def visitProgram(self, ctx: PPParser.ProgramContext):
        self.visitChildren(ctx)
        return self.prints
        self.display_variables()

    def visitInstruction(self, ctx: PPParser.InstructionContext):
        return self.visitChildren(ctx)

    def visitPrintExpression(self, ctx: PPParser.PrintExpressionContext):
        value_to_print = self.visitChildren(ctx)
        print("print:", value_to_print)
        self.prints.append(value_to_print)

    def visitInputExpression(self, ctx: PPParser.InputExpressionContext):
        self.ticks += 1
        # only inputs of type: integer, variableName are accepted
        value = self.input_var.pop(0) if self.input_var else 1
        # print("input value: ", value)
        if type(value) == int:
            return value
        else:  # str -> syntax should be checked
            if not self.variables.get(value):
                self.variables[value] = 1
            value = self.variables.get(value)
        return value
    
    def visitReadExpression(self, ctx:PPParser.ReadExpressionContext):
        return self.visitChildren(ctx)

    def visitConditionalStatement(self, ctx: PPParser.ConditionalStatementContext):
        self.ticks += 1
        if self.ticks >= self.max_nr_of_ticks:
            return
        if self.visit(ctx.cond):
            self.visit(ctx.con_body)

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
        if ctx.read_:
            return self.visit(ctx.read_)
        if ctx.integer_:
            return self.visit(ctx.integer_)
        if ctx.variable_name_:
            varname = self.visit(ctx.variable_name_)
            if not self.variables.get(varname):
                self.variables[varname] = 1
            return self.variables.get(varname)

        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        
        if op == "/" and right == 0: # division by 0
            right = 0.001
        
        operation = {
            '+': lambda: left + right,
            '-': lambda: left - right,
            '*': lambda: int(left * right),
            '/': lambda: int(left // right),
        }
        return operation.get(op, lambda: None)()

    def visitLoop(self, ctx: PPParser.LoopContext):
        self.ticks += 1
        while self.ticks < self.max_nr_of_ticks and self.visit(ctx.cond):
            self.visit(ctx.loop_body)
            self.ticks += 1

    def visitAssignment(self, ctx: PPParser.AssignmentContext):
        self.ticks += 1
        if self.ticks >= self.max_nr_of_ticks:
            return
        varname = self.visit(ctx.children[0])
        if not self.variables.get(str(varname)):
            self.variables[str(varname)] = 1
        self.variables[str(varname)] = self.visit(
            ctx.art_expr) if ctx.art_expr else self.visit(ctx.input_)

    def visitVariableName(self, ctx: PPParser.VariableNameContext):
        varname = ctx.getText()
        if not self.variables.get(varname):
            self.variables[varname] = 1
        return varname

    def visitInteger(self, ctx: PPParser.IntegerContext):
        return int(ctx.getText())
    
    def visitPositiveInteger(self, ctx:PPParser.PositiveIntegerContext):
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
