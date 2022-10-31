from enum import Enum
import random
from typing import List

class NodeType(Enum):
    PROGRAM = 0,
    INSTRUCTION = 1,
    CONDITIONAL_STATEMENT = 10,
    CONDITION = 11,
    ARITHMETICAL_EXPR = 20,
    ASSIGNMENT = 21,
    ATOM = 30,
    INT = 31,
    FLOAT = 32,
    VAR_NAME = 33,
    TWO_ARG_OPERATOR = 40,
    ADD = 41,
    DIV = 42,


class Node:
    max_nr_of_children = 5

    def __init__(self, node_type: NodeType) -> None:
        self.type = node_type
        self.children = [] # List[Node]
    
    @staticmethod
    def generate_random_children(parent: NodeType) -> List[NodeType]:
        possible_combinations = len(Node.get_possible_children(parent))
        # print("possible combinations: ", possible_combinations)
        if possible_combinations == 0:
            return []
        idx = random.randint(0, possible_combinations-1)
        # print("idx: ", idx)
        nr_of_children, children_types = Node.get_possible_children(parent)[idx]
        # print("nr of children: ", nr_of_children)
        if nr_of_children != -1:
            return children_types
        else:
            nr_of_children = random.randint(0, Node.max_nr_of_children-1)
            # print("nr of children: ", nr_of_children)
            children = []
            for idx in range(nr_of_children):
                idx = random.randint(0, len(children_types)-1)
                children.append(children_types[idx])
            return children
    
    @staticmethod
    def get_possible_children(node_type: NodeType):
        if node_type == NodeType.PROGRAM:
            return [(-1, [NodeType.INSTRUCTION])]
        elif node_type == NodeType.INSTRUCTION:
            return [(1, [NodeType.CONDITIONAL_STATEMENT, NodeType.ASSIGNMENT])]
        elif node_type == NodeType.CONDITIONAL_STATEMENT:
            return [(2, [NodeType.CONDITION, NodeType.INSTRUCTION])]
        elif node_type == NodeType.CONDITION:
            return [] # not implemented
        elif node_type == NodeType.ARITHMETICAL_EXPR:
            return [(1, [NodeType.ATOM]), 
            (3, [NodeType.ATOM, NodeType.TWO_ARG_OPERATOR, NodeType.ATOM])]
        else:
            return [] # not implemented


class GP:
    def __init__(self) -> None:
        self.max_depth = 5
        self.population_size = 10
        self.population = [] # List[Node]
        self.fitness = [] # List[float]
        self.tournament_size = 2
    
    # TODO
    # możliwość testowania programów 
    def compute_fitness(self, individual:Node) -> float:
        """
        How to compute:
        fit += Math.abs(result - targets[i][varnumber]);
        """
        return 2137

    # TODO
    # generowanie losowych programów (drzew) o zadanej wielkości
    def create_random_individual(self) -> Node:
        """
        return tree root
        """
        root = Node(NodeType.PROGRAM)
        root.children = Node.generate_random_children(root.type)
        return root
    
    # TODO
    def create_random_population(self):
        for idx in range(self.population_size):
            self.population.append(self.create_random_individual)
            self.fitness.append(self.compute_fitness(self.population[idx]))

    # TODO
    # możliwość testowania programów 
    # return idx of the best individual
    def perform_tournament(self) -> int:
        pass

    # TODO
    # operację krzyżowania dwóch drzew/programów
    def perform_crossover(self, parent1: Node, parent2: None) -> Node:
        pass

    # TODO
    # operację mutacji
    def perform_mutation(self, parent: Node, pmut: float) -> Node:
        pass

    def display_program(self, root: Node):
        print("Root: ", root.type, " nr of children:", len(root.children))
        for child in root.children:
            print(child)


print("---RUN---")
gp = GP()
root = gp.create_random_individual()
gp.display_program(root)