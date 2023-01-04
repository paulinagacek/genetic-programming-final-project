from enum import Enum
import random
from typing import List


class NodeType(Enum):
    SEQUENCE = 0,
    INSTRUCTION = 1,
    CONDITIONAL_STATEMENT = 10,
    COMPARISON = 11,
    LOGICAL_OP = 12,
    ASSIGNMENT = 21,
    ARITHMETICAL_OP = 22,
    INT = 31,
    VAR_NAME = 33,
    LOOP = 50,
    PRINT = 70,
    INPUT = 71,

class Prob():
    LOGICAL_OP_PROB = 0.2
    COMPARISON_OP_PROB = 0.8
    COMP_INT_PROB = 0.7
    COMP_ART_PROB = 0.1
    COMP_INT_ART_PROB = 0.2


class Node:
    nr_of_variables = 0
    max_nr_of_variables = 10

    def __init__(self, node_type: NodeType, children, value=None, can_mutate:bool=True, level: int=0, nr_of_children: int=-1, height=-1) -> None:
        self.type = node_type
        self.children = children  # List[Node]
        self.parent = None  # Node
        self.value = None
        self.can_mutate = can_mutate
        self.level = level
        self.height = height
        self.nr_of_children = nr_of_children
        if not value:
            self.value = Node.generate_random_value(self.type)
        else:
            self.value = value

    def print_value(self) -> str:
        return str(self.value) if self.value else ""

    @staticmethod
    def generate_random_value(type_: NodeType):
        if type_ == NodeType.INT:
            return random.randint(Node.min_val_int, Node.max_val_int)
        elif type_ == NodeType.VAR_NAME:  # existing
            if (random.random() < 0.1 and Node.nr_of_variables < Node.max_nr_of_variables) or Node.nr_of_variables == 0:  # create new
                Node.nr_of_variables += 1
                return "X" + str(Node.nr_of_variables)
            else:
                idx = random.randint(1, Node.nr_of_variables)
                return "X" + str(idx)
        else:
            possibilities = Node.type_to_possible_value.get(type_, [])
            if len(possibilities) > 0:
                return random.choice(possibilities)
            else:
                return None

    @staticmethod
    def is_non_terminal(type_: NodeType) -> bool:
        return type_ in [NodeType.ARITHMETICAL_OP, NodeType.SEQUENCE, NodeType.CONDITIONAL_STATEMENT,
                         NodeType.ASSIGNMENT, NodeType.LOOP, NodeType.LOGICAL_OP, NodeType.COMPARISON]

    @staticmethod
    def generate_random_children_types(parent: NodeType) -> List[NodeType]:
        possible_combinations = Node.get_possible_children(parent)
        if len(possible_combinations) == 0:
            return []
        
        weights = list(map(lambda x: x[2], possible_combinations))
        nr_of_children, children_types, prob = random.choices(
            possible_combinations, weights=weights, k=1)[0]

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
        It returns node type which can be placed in the tree instead of SEQUENCE 
        if it is leaf parent (we want to finish as fast as possible)
        """
        return random.choice([NodeType.CONDITIONAL_STATEMENT, NodeType.ASSIGNMENT, NodeType.LOOP])

    # static attributes

    max_nr_of_children = 5
    max_val_int = 100
    min_val_int = 0
    variables = []

    type_to_children = {
        NodeType.SEQUENCE: [(1, [NodeType.INSTRUCTION], 2), 
                            (2, [NodeType.INSTRUCTION, NodeType.INSTRUCTION], 1.8), 
                            (3, [NodeType.INSTRUCTION, NodeType.INSTRUCTION, NodeType.INSTRUCTION], 1.5), 
                            (4, [NodeType.INSTRUCTION, NodeType.INSTRUCTION,NodeType.INSTRUCTION, NodeType.INSTRUCTION], 1),
                            (5, [NodeType.INSTRUCTION, NodeType.INSTRUCTION, NodeType.INSTRUCTION, NodeType.INSTRUCTION, NodeType.INSTRUCTION], 1)],
        NodeType.INSTRUCTION: [(1, [NodeType.CONDITIONAL_STATEMENT], 1),
                               (1, [NodeType.ASSIGNMENT], 1),
                               (1, [NodeType.LOOP], 1),
                               (1, [NodeType.PRINT], 3)],
        # CONDITIONAL STATEMENTS, LOOPS
        NodeType.CONDITIONAL_STATEMENT: [(2, [NodeType.LOGICAL_OP, NodeType.SEQUENCE], 0.1),
                                         (2, [NodeType.COMPARISON, NodeType.SEQUENCE], 0.9)],
        NodeType.LOGICAL_OP: [(2, [NodeType.LOGICAL_OP, NodeType.LOGICAL_OP], 0.04),
                              (2, [NodeType.COMPARISON, NodeType.COMPARISON], 0.8),
                              (2, [NodeType.LOGICAL_OP,
                                   NodeType.COMPARISON], 0.08),
                              (2, [NodeType.COMPARISON, NodeType.LOGICAL_OP], 0.08)],
        NodeType.COMPARISON: [(2, [NodeType.ARITHMETICAL_OP, NodeType.ARITHMETICAL_OP], 0.4),
                              (2, [NodeType.INT, NodeType.VAR_NAME], 0.2),
                              (2, [NodeType.VAR_NAME, NodeType.VAR_NAME], 0.12),
                              (2, [NodeType.VAR_NAME, NodeType.INT], 0.2),
                              (2, [NodeType.INT, NodeType.INT], 0.2),
                              (2, [NodeType.ARITHMETICAL_OP, NodeType.VAR_NAME], 0.12),
                              (2, [NodeType.ARITHMETICAL_OP, NodeType.INT], 0.12)],

        NodeType.LOOP: [(2, [NodeType.LOGICAL_OP, NodeType.SEQUENCE], 0.1),
                        (2, [NodeType.COMPARISON, NodeType.SEQUENCE], 0.9)],

        # ARITHMETICAL EXPR
        NodeType.ASSIGNMENT: [(2, [NodeType.VAR_NAME, NodeType.INT], 0.35),
                              (2, [NodeType.VAR_NAME, NodeType.INPUT], 0.2),
                              (2, [NodeType.VAR_NAME, NodeType.ARITHMETICAL_OP], 0.35),
                              (2, [NodeType.VAR_NAME, NodeType.VAR_NAME], 0.1)],
        NodeType.ARITHMETICAL_OP: [
            (2, [NodeType.ARITHMETICAL_OP, NodeType.ARITHMETICAL_OP], 0.1),
            (2, [NodeType.INT, NodeType.ARITHMETICAL_OP], 0.1),
            (2, [NodeType.ARITHMETICAL_OP, NodeType.INT], 0.1),
            (2, [NodeType.INT, NodeType.INT], 0.3),
            (2, [NodeType.VAR_NAME, NodeType.ARITHMETICAL_OP], 0.05),
            (2, [NodeType.ARITHMETICAL_OP, NodeType.VAR_NAME], 0.05),
            (2, [NodeType.VAR_NAME, NodeType.VAR_NAME], 0.1),
            (2, [NodeType.VAR_NAME, NodeType.INT], 0.2),
            (2, [NodeType.INT, NodeType.VAR_NAME], 0.2)],

        NodeType.PRINT: [(1, [NodeType.ARITHMETICAL_OP], 0.4),
                         (1, [NodeType.INT], 0.3),
                         (1, [NodeType.VAR_NAME], 0.3)]
    }

    type_to_possible_value = {
        NodeType.COMPARISON: ["==", ">", "<", "!="],
        NodeType.LOGICAL_OP: ["AND", "OR"],
        NodeType.ARITHMETICAL_OP: ["+", "-", "/", "*"],
    }

    type_to_point_mutation = {
        NodeType.INT: [NodeType.VAR_NAME, NodeType.INT], # INPUT
        NodeType.VAR_NAME: [NodeType.VAR_NAME, NodeType.INT], # INPUT
        NodeType.INPUT: [NodeType.VAR_NAME, NodeType.INT], # INPUT
        NodeType.COMPARISON: [NodeType.COMPARISON],
        NodeType.LOGICAL_OP: [NodeType.LOGICAL_OP],
        NodeType.LOOP: [NodeType.CONDITIONAL_STATEMENT, NodeType.LOOP],
        NodeType.CONDITIONAL_STATEMENT: [NodeType.LOOP, NodeType.CONDITIONAL_STATEMENT],
    }

    type_to_cross_over = {
        NodeType.SEQUENCE: [NodeType.CONDITIONAL_STATEMENT, NodeType.SEQUENCE, NodeType.LOOP, NodeType.ASSIGNMENT],
        NodeType.CONDITIONAL_STATEMENT: [NodeType.CONDITIONAL_STATEMENT, NodeType.SEQUENCE, NodeType.LOOP, NodeType.ASSIGNMENT],
        NodeType.COMPARISON: [NodeType.COMPARISON, NodeType.LOGICAL_OP],
        NodeType.LOGICAL_OP: [NodeType.LOGICAL_OP, NodeType.COMPARISON],
        NodeType.LOOP: [NodeType.LOOP, NodeType.SEQUENCE, NodeType.CONDITIONAL_STATEMENT, NodeType.ASSIGNMENT],
        NodeType.ASSIGNMENT: [NodeType.ASSIGNMENT, NodeType.SEQUENCE, NodeType.CONDITIONAL_STATEMENT, NodeType.LOOP],
        NodeType.ARITHMETICAL_OP: [NodeType.ARITHMETICAL_OP, NodeType.INT, NodeType.VAR_NAME],
        NodeType.VAR_NAME: [NodeType.VAR_NAME, NodeType.ARITHMETICAL_OP, NodeType.INT],
        NodeType.INT: [NodeType.INT, NodeType.ARITHMETICAL_OP, NodeType.VAR_NAME],
        NodeType.VAR_NAME: [NodeType.VAR_NAME],
        NodeType.INPUT: [NodeType.VAR_NAME, NodeType.ARITHMETICAL_OP, NodeType.INT],
    }

    type_to_finish = {
        NodeType.ARITHMETICAL_OP: [(2, [NodeType.INT, NodeType.INT]),
                                   (2, [NodeType.INT, NodeType.VAR_NAME]),
                                   (2, [NodeType.VAR_NAME, NodeType.VAR_NAME]),
                                   (2, [NodeType.VAR_NAME, NodeType.INT])],
        NodeType.SEQUENCE: [(1, [NodeType.ASSIGNMENT])],
        NodeType.CONDITIONAL_STATEMENT: [(2, [NodeType.COMPARISON, NodeType.ASSIGNMENT])],
        NodeType.COMPARISON: [(2, [NodeType.INT, NodeType.INT]),
                              (2, [NodeType.VAR_NAME, NodeType.INT]),
                              (2, [NodeType.INT,  NodeType.VAR_NAME]),
                              (2, [NodeType.VAR_NAME, NodeType.VAR_NAME])],
        NodeType.ASSIGNMENT: [(2, [NodeType.VAR_NAME, NodeType.INT])],
        NodeType.LOOP: [(2, [NodeType.COMPARISON, NodeType.ASSIGNMENT])],
        NodeType.LOGICAL_OP: [(2, [NodeType.COMPARISON, NodeType.COMPARISON])],
    }
