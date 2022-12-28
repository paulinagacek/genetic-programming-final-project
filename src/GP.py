from src.Node import *
from src.Converter import *
from src.Plotter import *
from antlr.PPVisitor import *
from antlr.PPListener import *
from antlr.PPLexer import *
from antlr.PPParser import *
from antlr.PPErrorListener import *
import pickle
import numpy as np
import copy


def sum_calculator(received_outs, expected_outs):
    """
    Returns fitness of received outputs realitvely to expected outputs.
    Fitness function was created for problems in which the output is expected to consist
    certain number - specified in expected_outs[0].
    """
    fitness = 0
    if len(received_outs) == 0:
        fitness += -10e+9
        return fitness
    try:
        fitness += -abs((np.min(np.array(received_outs) -
                        expected_outs[0]))*100//expected_outs[0])  # int division to prevent Overflow error
    except ValueError:
        fitness += -10e+9

    return fitness


class GP:
    def __init__(self, inputs=None, outputs=None) -> None:
        self.max_depth = 5
        self.population_size = 100
        self.population = []  # List[Node]
        self.fitness = []  # List[float]
        # self.program_strings = []  # List[str]
        self.program_input = inputs if inputs else []
        self.expected_output = outputs if outputs else []
        self.tournament_size = 2
        self.mutation_rate = 0.4
        self.crossover_rate = 0.9
        self.nr_of_generations = 100
        self.max_traverse_tries = 10
        self.best_indiv_idx = 0
        self.best_fitness = -1000000
        self.patience = 5  # nr of epochs without improvement in fitness
        self.epochs_without_improvement = 0
        self.nr_of_regenerations = 0

    def get_train_data(self, filename):
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    x, y = line.split(';')
                    x = x.strip().split(' ')
                    x = [int(val) for val in x]
                    y = y.strip().split(' ')
                    y = [int(val) for val in y]
                    self.program_input.append(x)
                    self.expected_output.append(y)
        print("Inputs: ", self.program_input)
        print("Outputs: ", self.expected_output)

    def compute_fitness(self, program: str, pr=False) -> float:
        fitness = 0  # max is 0, should be negative besides
        epochs = len(self.program_input)
        for example_idx in range(epochs):
            data = InputStream(program)
            prints = self.interprateInput(
                data, self.program_input[example_idx].copy())
            if pr:
                print(
                    prints, self.program_input[example_idx], self.expected_output[example_idx])
            fitness += sum_calculator(prints,
                                      self.expected_output[example_idx])
        return fitness

    def create_random_population(self):
        for idx in range(self.population_size):
            self.population.append(self.create_random_individual())
            program_str = self.generate_program_str(self.population[idx])
            # self.program_strings.append(program_str)
            self.fitness.append(self.compute_fitness(program_str))
        print("Max initial depth: ", self.max_depth)
        print("Population size: ", self.population_size)
        print("Crossover rate: ", self.crossover_rate,
              "  Mutation rate: ", self.mutation_rate)
        print("Random population generated")

    def create_random_individual(self) -> Node:
        Node.nr_of_variables = 0  # no global variables
        root, level = Node(NodeType.SEQUENCE, [], None), 0
        queue = [(level, root)]  # (int, Node)
        while queue:
            level, node = queue.pop(0)
            if level >= self.max_depth-1 and Node.is_non_terminal(node.type):
                if node.type == NodeType.SEQUENCE:
                    node.type = Node.get_random_program_substitute()
                children_types = Node.get_children_to_finish(node.type)
                for idx in range(len(children_types)):
                    can_mutate = True
                    if node.type == NodeType.ASSIGNMENT and idx == 0:
                        can_mutate = False
                    node.children.append(
                        Node(children_types[idx], [], None, can_mutate))
                    queue.append((level+1, node.children[idx]))

            elif level < self.max_depth:
                types = Node.generate_random_children_types(node.type)
                for idx in range(len(types)):
                    can_mutate = True
                    if node.type == NodeType.ASSIGNMENT and idx == 0:
                        can_mutate = False
                    node.children.append(
                        Node(types[idx], [], None, can_mutate))
                    queue.append((level+1, node.children[idx]))
        return root

    def perform_tournament(self) -> int:
        """
        Returns idx of the best individual
        """
        fbest = -1.0e34
        best = random.randint(0, self.population_size-1)
        for idx in range(self.tournament_size):
            competitor = random.randint(0, self.population_size-1)
            if self.fitness[competitor] > fbest:
                fbest = self.fitness[competitor]
                best = competitor
        return best

    def perform_negative_tournament(self) -> int:
        """
        Returns idx of the worst individual
        """
        fworst = 1.0e34
        worst = random.randint(0, self.population_size-1)
        for idx in range(self.tournament_size):
            competitor = random.randint(0, self.population_size-1)
            if self.fitness[competitor] < fworst:
                fworst = self.fitness[competitor]
                worst = competitor
        return worst

    def perform_crossover(self, parent1: Node, parent2: Node) -> Node:
        if parent1 == parent2:
            return parent1
        for i in range(self.max_traverse_tries):
            node1 = GP.get_random_node(parent1)
            for j in range(self.max_traverse_tries):
                node2 = GP.get_random_node(parent2)
                if node2.type in Node.get_possible_crossover(node1.type):
                    node1.type = node2.type
                    node1.value = node2.value
                    node1.children = node2.children
                    for child in node1.children:
                        child.parent = node1
                    return parent1

        parent1_str = self.generate_program_str(parent1)
        parent2_str = self.generate_program_str(parent2)

        return parent1 if self.compute_fitness(parent1_str) > self.compute_fitness(parent2_str) else parent2

    @staticmethod
    def perform_point_mutation(curr_node: Node) -> Node:
        """
        Mutates provided node with other randomly chosen.
        Not all nodes have alternatives for mutations and such nodes cannot
        be mutated using point mutation.
        """
        if not curr_node.can_mutate:
            return curr_node

        possibilities = Node.get_possible_point_mutations(curr_node.type)
        if len(possibilities) == 0:  # node cannot be mutated
            return curr_node
        else:
            idx = random.randint(0, len(possibilities)-1)
            new_node = Node(possibilities[idx], curr_node.children, None)
            if new_node.type == NodeType.INPUT:
                new_node.value = "input"
            # print("Mutation (", curr_node.type, ", ", curr_node.value,
            #       ") -> (", new_node.type, ", ", new_node.value, ")")
            return new_node

    def mutate(self, root: Node) -> Node:
        """
        Performs point or subtree mutation on all nodes starting from root 
        with probability of self.mutation_rate=10%. 
        Returns the root of mutated tree
        """
        # print("Before mutation:", self.generate_program_str(root))
        queue = [root]
        while queue:
            node = queue.pop()
            if random.random() < self.mutation_rate:  # 10%
                # if random.random() < 0.5 else self.perform_subtree_mutation(node)
                new_node = GP.perform_point_mutation(node)
                node.type = new_node.type
                node.value = new_node.value
                node.children = new_node.children
            for child in node.children:
                queue.append(child)
        # print("After mutation:",  self.generate_program_str(root))
        return root

    @staticmethod
    def get_random_node(root: Node) -> Node:
        queue = [root]
        node_set = []
        while queue:
            node = queue.pop()
            if node != root:
                node_set.append(node)
            for child in node.children:
                queue.append(child)

        return random.choice(node_set) if node_set else root

    def display_program(self, root: Node):
        level = 0
        stack = [(level, root)]
        while stack:
            level, node = stack.pop(-1)
            level_display = "".join(["  " for nr in range(level)]) + "|"
            print(level_display, level, node.type, node.print_value())
            for child in reversed(node.children):
                stack.append((level + 1, child))

    def deepcopy_tree(self, root: Node) -> Node:
        new_node = Node(root.type, list([]), None, root.can_mutate)
        new_node.value = root.value
        try:
            for child in root.children:
                new_node.children.append(self.deepcopy_tree(child))
        except RecursionError:
            print("Recursion error")
            # return root
        return new_node

    def evolve(self, steps=-1):
        if steps == -1:
            steps = self.nr_of_generations
        for generation in range(steps):
            print("Generation", generation, " ------------------------")
            print("Epochs without improvement:",
                  self.epochs_without_improvement)
            if self.best_fitness/len(self.population) > -0.0001:
                print("Solution found in generation", generation)
                break

            population_copy = copy.deepcopy(self.population)
            fitness_copy = copy.deepcopy(self.fitness)

            for idx in range(len(self.population)):
                if random.random() < self.crossover_rate:  # 50%
                    parent1 = self.perform_tournament()
                    parent2 = self.perform_tournament()
                    if parent1 == parent2:
                        parent_copy = self.deepcopy_tree(
                            self.population[parent1])
                        child = self.mutate(parent_copy)
                    else:
                        parent1_copy = self.deepcopy_tree(
                            self.population[parent1])
                        parent2_copy = self.deepcopy_tree(
                            self.population[parent2])
                        child = self.perform_crossover(
                            parent1_copy, parent2_copy)
                else:
                    parent1 = self.perform_tournament()
                    parent1_copy = self.deepcopy_tree(self.population[parent1])
                    child = self.mutate(parent1_copy)

                weakest_idx = self.perform_negative_tournament()
                population_copy[weakest_idx] = child
                child_str = self.generate_program_str(child)
                fitness_copy[weakest_idx] = self.compute_fitness(child_str)

            # best indiv always survives
            previous_best_indiv = self.deepcopy_tree(self.population[self.best_indiv_idx])
            previous_best_fitness = self.fitness[self.best_indiv_idx]

            self.population = copy.deepcopy(population_copy)
            self.fitness = copy.deepcopy(fitness_copy)

            weakest_idx = self.perform_negative_tournament()
            self.population[weakest_idx] = previous_best_indiv
            self.fitness[weakest_idx] = previous_best_fitness
            self.best_indiv_idx = np.argmax(self.fitness)

            self.update_best_fitness()
            
            print("\nBest fitness:", self.best_fitness, " best indiv:")
            best_prog = self.generate_program_str(
                self.population[self.best_indiv_idx])
            best_fit = self.compute_fitness(best_prog, pr=True)
            print(best_prog, " = ", best_fit)

            self.escape_local_optimum()
    
    def update_best_fitness(self):
        new_best_fitness = self.fitness[self.best_indiv_idx]
        if new_best_fitness <= self.best_fitness:
            self.epochs_without_improvement += 1
        else:
            self.epochs_without_improvement = 0
        self.best_fitness = new_best_fitness

    def escape_local_optimum(self):
        if self.epochs_without_improvement >= self.patience:
            self.epochs_without_improvement = 0
            self.nr_of_regenerations += 1
            ratio_to_generate = min(0.4 + 0.05 * self.nr_of_regenerations, 0.9)
            for idx in range(0, int(ratio_to_generate * self.population_size)):
                if idx == self.best_indiv_idx:
                    continue  # leave the best indiv
                self.population[idx] = self.create_random_individual()
                program_str = self.generate_program_str(
                    self.population[idx])
                self.fitness[idx] = self.compute_fitness(program_str)
            print(int(ratio_to_generate * self.population_size),
                  "  generated again")

    @staticmethod
    def generate_program_str(root: Node) -> str:
        """
        Converts program tree to program string and returns it.
        """
        return Converter.get_proper_node(root)

    @staticmethod
    def dump_individual(root_node=None, filename='individual.txt'):
        with open(filename, 'wb') as f:
            pickle.dump(root_node, f)

    @staticmethod
    def load_individual(filename='individual.txt'):
        with open(filename, 'rb') as f:
            return pickle.load(f)

    def interprateInput(self, data, input_variables):
        # lexer
        lexer = PPLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = PPParser(stream)
        parser.addErrorListener(PPErrorListener())  # add error listener
        try:
            tree = parser.program()
        except Exception as e:
            print(e)
            return

        # evaluator
        visitor = PPVisitor()
        return visitor.visit(tree)


def demonstrate_load_save():
    genetic = GP()
    plott = Plotter()
    root = genetic.create_random_individual()
    plott.plot(root, filename="plot2")
    GP.dump_individual(root, filename='individual1.txt')
    root2 = GP.load_individual(filename='individual1.txt')
    plott.plot(root2, filename="plot3")


def demonstrate_mutation():
    genetic = GP()
    plotter = Plotter()
    root = genetic.create_random_individual()
    plotter.plot(root, filename="mut1")
    root = genetic.mutate(root)
    plotter.plot(root, filename="mut2")


def demonstrate_crossover():
    genetic = GP()
    plotter = Plotter()
    root1 = genetic.create_random_individual()
    root2 = genetic.create_random_individual()
    plotter.plot(root1, filename="cross1")
    plotter.plot(root2, filename="ross2")
    root = genetic.perform_crossover(root1, root2)
    plotter.plot(root, filename="cross3")


if __name__ == "__main__":
    # gp = GP()
    # gp.get_train_data('input.txt')
    # plotter = Plotter()
    # gp.create_random_population()
    # gp.evolve(copy=True)
    # gp.display_program(gp.population[0])
    # print(GP.generate_program_str(gp.population[0]))
    # plotter.plot(gp.population[0], filename="plot1")
    # print("\nBest individual:")
    # gp.display_program(gp.population[gp.fitness.index(max(gp.fitness))])
    demonstrate_load_save()
    demonstrate_mutation()
    demonstrate_crossover()
