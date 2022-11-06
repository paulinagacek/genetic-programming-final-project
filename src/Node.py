from enum import Enum
import random
from typing import List


class NodeType(Enum):
    PROGRAM = 0,
    CONDITIONAL_STATEMENT = 10,
    CONDITION = 11,
    CONDITIONAL_EXPR = 12,
    AND = 13,
    OR = 14,
    NOT_EQ = 15,
    GREATER_THAN = 16,
    LESS_THAN = 17,
    EQ = 18,
    TRUE = 19,
    FALSE = 20,
    ASSIGNMENT = 21,
    ARITHMETICAL_EXPR = 22,
    INT = 31,
    VAR_NAME = 33,
    VAR_NAME_IMMUTABLE = 34,
    ADD = 41,
    DIV = 42,
    MUL = 43,
    SUB = 44,
    LOOP = 50,
    LEFT_BRACKET = 60,
    RIGHT_BRACKET = 61,


class Node:
    nr_of_variables = 0

    def __init__(self, node_type: NodeType, children, value=None) -> None:
        self.type = node_type
        self.children = children  # List[Node]
        self.parent = None  # Node
        self.value = None
        if not value:
            self.value = Node.generate_random_value(self.type)
            if self.value == "ERROR":  # calling variable before assignment
                self.type = NodeType.INT
                self.value = random.randint(Node.min_val_int, Node.max_val_int)
        else:
            self.value = value

    def print_value(self) -> str:
        return str(self.value) if self.value else ""

    @staticmethod
    def generate_random_value(type_: NodeType):
        if type_ == NodeType.INT:
            return random.randint(Node.min_val_int, Node.max_val_int)
        elif type_ == NodeType.VAR_NAME:  # existing
            if Node.nr_of_variables == 0:  # create new
                return "ERROR"
            else:
                idx = random.randint(1, Node.nr_of_variables)
                return "X" + str(idx)
        elif type_ == NodeType.VAR_NAME_IMMUTABLE:
            if random.random() < 0.2 or Node.nr_of_variables == 0:  # create new
                Node.nr_of_variables += 1
                return "X" + str(Node.nr_of_variables)
            else:
                idx = random.randint(1, Node.nr_of_variables)
                return "X" + str(idx)
        else:
            return None

    @staticmethod
    def is_non_terminal(type_: NodeType) -> bool:
        return type_ in [NodeType.ARITHMETICAL_EXPR, NodeType.PROGRAM, NodeType.CONDITIONAL_STATEMENT,
                         NodeType.ASSIGNMENT, NodeType.LOOP, NodeType.CONDITIONAL_EXPR, NodeType.CONDITION]

    @staticmethod
    def generate_random_children_types(parent: NodeType) -> List[NodeType]:
        possible_combinations = len(Node.get_possible_children(parent))
        if possible_combinations == 0:
            return []
        idx = random.randint(0, possible_combinations-1)
        nr_of_children, children_types = Node.get_possible_children(parent)[
            idx]

        if nr_of_children != -1:
            return children_types
        else:
            nr_of_children = random.randint(1, Node.max_nr_of_children)
            children = []
            for idx in range(nr_of_children):
                idx = random.randint(0, len(children_types)-1)
                children.append(children_types[idx])
            return children

    @staticmethod
    def get_possible_children(node_type: NodeType):
        return Node.type_to_children.get(node_type, [])

    @staticmethod
    def get_possible_point_mutations(node_type: NodeType):
        return Node.type_to_point_mutation.get(node_type, [])

    @staticmethod
    def get_possible_crossover(node_type: NodeType):
        return Node.type_to_cross_over.get(node_type, [])

    @staticmethod
    def get_children_to_finish(node_type: NodeType):
        """
        Returns such children set to finish as fast as possible
        """
        possible_combinations = len(Node.type_to_finish.get(node_type, []))
        if possible_combinations == 0:
            return []
        idx = random.randint(0, possible_combinations-1)
        nr_of_children, children_types = Node.type_to_finish.get(node_type, [])[
            idx]
        return children_types

    @staticmethod
    def get_random_program_substitute():
        """
        It returns node type which can be placed in the tree instead of PROGRAMM 
        if it is leaf parent (we want to finish as fast as possible)
        """
        return random.choice([NodeType.CONDITIONAL_STATEMENT, NodeType.ASSIGNMENT, NodeType.LOOP])

    # static attributes

    max_nr_of_children = 5
    max_val_int = 100
    min_val_int = 0
    variables = []
    max_nr_of_variables = 100

    type_to_children = {
        NodeType.PROGRAM: [(-1, [NodeType.CONDITIONAL_STATEMENT, NodeType.ASSIGNMENT, NodeType.LOOP])],

        # CONDITIONAL STATEMENTS, LOOPS
        NodeType.CONDITIONAL_STATEMENT: [(2, [NodeType.CONDITION, NodeType.PROGRAM])],
        NodeType.CONDITIONAL_EXPR: [(1, [NodeType.CONDITION]),
                                    (3, [NodeType.CONDITIONAL_EXPR,
                                     NodeType.AND, NodeType.CONDITIONAL_EXPR]),
                                    (3, [NodeType.CONDITIONAL_EXPR, NodeType.OR, NodeType.CONDITIONAL_EXPR])],
        NodeType.CONDITION: [(3, [NodeType.ARITHMETICAL_EXPR, NodeType.EQ, NodeType.ARITHMETICAL_EXPR]),
                             (3, [NodeType.ARITHMETICAL_EXPR,
                              NodeType.NOT_EQ, NodeType.ARITHMETICAL_EXPR]),
                             (3, [NodeType.ARITHMETICAL_EXPR,
                              NodeType.LESS_THAN, NodeType.ARITHMETICAL_EXPR]),
                             (3, [NodeType.ARITHMETICAL_EXPR,
                              NodeType.GREATER_THAN, NodeType.ARITHMETICAL_EXPR]),
                             (1, [NodeType.FALSE]),
                             (1, [NodeType.TRUE])],

        NodeType.LOOP: [(2, [NodeType.CONDITION, NodeType.PROGRAM])],

        # ARITHMETICAL EXPR
        NodeType.ASSIGNMENT: [(2, [NodeType.VAR_NAME_IMMUTABLE, NodeType.INT])],
        NodeType.ARITHMETICAL_EXPR: [(3, [NodeType.ARITHMETICAL_EXPR, NodeType.ADD, NodeType.ARITHMETICAL_EXPR]),
                                     (3, [NodeType.ARITHMETICAL_EXPR,
                                      NodeType.SUB, NodeType.ARITHMETICAL_EXPR]),
                                     (3, [NodeType.ARITHMETICAL_EXPR,
                                      NodeType.DIV, NodeType.ARITHMETICAL_EXPR]),
                                     (3, [NodeType.ARITHMETICAL_EXPR,
                                      NodeType.MUL, NodeType.ARITHMETICAL_EXPR]),
                                     (1, [NodeType.INT]),
                                     (1, [NodeType.VAR_NAME])]
    }

    type_to_point_mutation = {
        NodeType.INT: [NodeType.VAR_NAME, NodeType.INT],
        NodeType.VAR_NAME: [NodeType.VAR_NAME, NodeType.INT],
        NodeType.ADD: [NodeType.DIV, NodeType.SUB, NodeType.MUL],
        NodeType.DIV: [NodeType.ADD, NodeType.SUB, NodeType.MUL],
        NodeType.SUB: [NodeType.DIV, NodeType.ADD, NodeType.MUL],
        NodeType.MUL: [NodeType.ADD, NodeType.SUB, NodeType.DIV],
        NodeType.EQ: [NodeType.NOT_EQ, NodeType.LESS_THAN, NodeType.GREATER_THAN],
        NodeType.NOT_EQ: [NodeType.EQ, NodeType.LESS_THAN, NodeType.GREATER_THAN],
        NodeType.LESS_THAN: [NodeType.NOT_EQ, NodeType.NOT_EQ, NodeType.GREATER_THAN],
        NodeType.GREATER_THAN: [NodeType.NOT_EQ, NodeType.LESS_THAN, NodeType.NOT_EQ],
        NodeType.TRUE: [NodeType.FALSE],
        NodeType.FALSE: [NodeType.TRUE],
        NodeType.LOOP: [NodeType.CONDITIONAL_STATEMENT],
        NodeType.CONDITIONAL_STATEMENT: [NodeType.LOOP],
        NodeType.AND: [NodeType.OR],
        NodeType.OR: [NodeType.AND]
    }

    type_to_cross_over = {
        NodeType.PROGRAM: [NodeType.CONDITIONAL_STATEMENT, NodeType.PROGRAM, NodeType.LOOP, NodeType.ASSIGNMENT],
        NodeType.CONDITIONAL_STATEMENT: [NodeType.CONDITIONAL_STATEMENT, NodeType.PROGRAM, NodeType.LOOP, NodeType.ASSIGNMENT],
        NodeType.CONDITION: [NodeType.CONDITION, NodeType.CONDITIONAL_EXPR],
        NodeType.CONDITIONAL_EXPR: [NodeType.CONDITIONAL_EXPR, NodeType.CONDITION],
        NodeType.LOOP: [NodeType.LOOP, NodeType.PROGRAM, NodeType.CONDITIONAL_STATEMENT, NodeType.ASSIGNMENT],
        NodeType.ASSIGNMENT: [NodeType.ASSIGNMENT, NodeType.PROGRAM, NodeType.CONDITIONAL_STATEMENT, NodeType.LOOP],
        NodeType.ARITHMETICAL_EXPR: [NodeType.ARITHMETICAL_EXPR, NodeType.INT, NodeType.VAR_NAME],
        NodeType.VAR_NAME: [NodeType.VAR_NAME, NodeType.ARITHMETICAL_EXPR, NodeType.INT],
        NodeType.INT: [NodeType.INT, NodeType.ARITHMETICAL_EXPR, NodeType.VAR_NAME],
        NodeType.VAR_NAME_IMMUTABLE: [NodeType.VAR_NAME_IMMUTABLE],
        NodeType.TRUE: [NodeType.TRUE, NodeType.FALSE, NodeType.CONDITIONAL_EXPR, NodeType.CONDITION],
        NodeType.FALSE: [NodeType.FALSE, NodeType.TRUE, NodeType.CONDITIONAL_EXPR, NodeType.CONDITION],
        NodeType.AND: [NodeType.AND, NodeType.OR],
        NodeType.OR: [NodeType.OR, NodeType.AND],
        NodeType.EQ: [NodeType.EQ, NodeType.NOT_EQ, NodeType.LESS_THAN, NodeType.GREATER_THAN],
        NodeType.NOT_EQ: [NodeType.NOT_EQ, NodeType.EQ, NodeType.LESS_THAN, NodeType.GREATER_THAN],
        NodeType.LESS_THAN: [NodeType.LESS_THAN, NodeType.NOT_EQ, NodeType.EQ, NodeType.GREATER_THAN],
        NodeType.GREATER_THAN: [NodeType.GREATER_THAN, NodeType.NOT_EQ, NodeType.LESS_THAN, NodeType.EQ],
        NodeType.ADD: [NodeType.ADD, NodeType.SUB, NodeType.DIV, NodeType.MUL],
        NodeType.SUB: [NodeType.SUB, NodeType.ADD, NodeType.DIV, NodeType.MUL],
        NodeType.DIV: [NodeType.DIV, NodeType.SUB, NodeType.ADD, NodeType.MUL],
        NodeType.MUL: [NodeType.MUL, NodeType.SUB, NodeType.DIV, NodeType.ADD],
    }

    type_to_finish = {
        NodeType.ARITHMETICAL_EXPR: [(3, [NodeType.INT, NodeType.ADD, NodeType.INT]),
                                     (3, [NodeType.INT, NodeType.SUB, NodeType.INT]),
                                     (3, [NodeType.INT, NodeType.DIV, NodeType.INT]),
                                     (3, [NodeType.INT, NodeType.MUL, NodeType.INT]),

                                     (3, [NodeType.INT, NodeType.ADD,
                                      NodeType.VAR_NAME]),
                                     (3, [NodeType.INT, NodeType.SUB,
                                      NodeType.VAR_NAME]),
                                     (3, [NodeType.INT, NodeType.DIV,
                                      NodeType.VAR_NAME]),
                                     (3, [NodeType.INT, NodeType.MUL,
                                      NodeType.VAR_NAME]),

                                     (3, [NodeType.VAR_NAME,
                                      NodeType.ADD, NodeType.VAR_NAME]),
                                     (3, [NodeType.VAR_NAME,
                                      NodeType.SUB, NodeType.VAR_NAME]),
                                     (3, [NodeType.VAR_NAME,
                                      NodeType.DIV, NodeType.VAR_NAME]),
                                     (3, [NodeType.VAR_NAME,
                                      NodeType.MUL, NodeType.VAR_NAME]),

                                     (3, [NodeType.VAR_NAME,
                                      NodeType.ADD, NodeType.INT]),
                                     (3, [NodeType.VAR_NAME,
                                      NodeType.SUB, NodeType.INT]),
                                     (3, [NodeType.VAR_NAME,
                                      NodeType.DIV, NodeType.INT]),
                                     (3, [NodeType.VAR_NAME, NodeType.MUL, NodeType.INT]), ],
        NodeType.PROGRAM: [(1, [NodeType.ASSIGNMENT])],
        NodeType.CONDITIONAL_STATEMENT: [(2, [NodeType.CONDITION, NodeType.ASSIGNMENT])],
        NodeType.CONDITION: [(3, [NodeType.INT, NodeType.EQ, NodeType.INT]),
                             (3, [NodeType.INT, NodeType.NOT_EQ, NodeType.INT]),
                             (3, [NodeType.INT, NodeType.LESS_THAN, NodeType.INT]),
                             (3, [NodeType.INT, NodeType.GREATER_THAN, NodeType.INT]),

                             (3, [NodeType.VAR_NAME, NodeType.EQ, NodeType.INT]),
                             (3, [NodeType.VAR_NAME, NodeType.NOT_EQ, NodeType.INT]),
                             (3, [NodeType.VAR_NAME,
                              NodeType.LESS_THAN, NodeType.INT]),
                             (3, [NodeType.VAR_NAME,
                              NodeType.GREATER_THAN, NodeType.INT]),

                             (3, [NodeType.INT, NodeType.EQ, NodeType.VAR_NAME]),
                             (3, [NodeType.INT, NodeType.NOT_EQ, NodeType.VAR_NAME]),
                             (3, [NodeType.INT, NodeType.LESS_THAN, NodeType.VAR_NAME]),
                             (3, [NodeType.INT, NodeType.GREATER_THAN,
                              NodeType.VAR_NAME]),

                             (3, [NodeType.VAR_NAME, NodeType.EQ, NodeType.VAR_NAME]),
                             (3, [NodeType.VAR_NAME,
                              NodeType.NOT_EQ, NodeType.VAR_NAME]),
                             (3, [NodeType.VAR_NAME,
                              NodeType.LESS_THAN, NodeType.VAR_NAME]),
                             (3, [NodeType.VAR_NAME,
                              NodeType.GREATER_THAN, NodeType.VAR_NAME]),

                             (1, [NodeType.FALSE]),
                             (1, [NodeType.TRUE])],
        NodeType.ASSIGNMENT: [(2, [NodeType.VAR_NAME_IMMUTABLE, NodeType.INT])],
        NodeType.LOOP: [(2, [NodeType.CONDITION, NodeType.ASSIGNMENT])],
    }
