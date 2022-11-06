from Node import *


class GP:
    def __init__(self) -> None:
        self.max_depth = 4
        self.population_size = 6
        self.population = []  # List[Node]
        self.fitness = []  # List[float]
        self.tournament_size = 2
        self.mutation_rate = 0.5
        self.crossover_rate = 1
        self.nr_of_generations = 1
        self.max_traverse_tries = 10

    def compute_fitness(self, individual: Node) -> float:
        return -random.randint(0, 2137)

    def create_random_population(self):
        for idx in range(self.population_size):
            self.population.append(self.create_random_individual())
            self.fitness.append(self.compute_fitness(self.population[idx]))

    def create_random_individual(self) -> Node:
        root, level = Node(NodeType.PROGRAM, [], None), 0
        queue = [(level, root)]  # (int, Node)
        while queue:
            level, node = queue.pop(0)
            if level == self.max_depth and Node.is_pseudo_type(node.type):
                new_node = Node.get_random_terminal_node(node.type)
                node.type = new_node.type
                node.value = new_node.value
                node.children = []
            elif level < self.max_depth:
                types = Node.generate_random_children_types(node.type)
                for idx in range(len(types)):
                    node.children.append(Node(types[idx], [], None))
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
        for i in range(self.max_traverse_tries):
            node1 = self.get_random_node(parent1)
            for j in range(self.max_traverse_tries):
                node2 = self.get_random_node(parent2)
                if node2.type in Node.get_possible_crossover(node1.type):
                    print("Node1:", node1.type, node1.value, "  Node2:", node2.type, node2.value)
                    print("Crossover", node1.type, node1.value, node2.type, node2.value)
                    print("Parent1:")
                    self.display_program(parent1)
                    print("Parent2:")
                    self.display_program(parent2)
                    node1.type = node2.type
                    node1.value = node2.value
                    node1.children = node2.children
                    for child in node1.children:
                        child.parent = node1
                    return parent1

        return parent1 if self.compute_fitness(parent1) > self.compute_fitness(parent2) else parent2

    @staticmethod
    def perform_point_mutation(parent: Node) -> Node:
        """
        Mutates provided node with other randomly chosen.
        Not all nodes have alternatives for mutations and such nodes cannot
        be mutated using point mutation.
        """
        possibilities = Node.get_possible_point_mutations(parent.type)
        if len(possibilities) == 0:  # node cannot be mutated
            return parent
        else:
            idx = random.randint(0, len(possibilities)-1)
            new_node = Node(possibilities[idx], parent.children, None)
            print("Mutation (", parent.type, ", ", parent.value,
                  ") -> (", new_node.type, ", ", new_node.value, ")")
            return new_node

    def mutate(self, root: Node) -> Node:
        """
        Performs point mutation on all nodes starting from root 
        with probability of self.mutation_rate=10%. 
        Returns the root of mutated tree
        """

        queue = [root]
        while queue:
            node = queue.pop()
            if random.random() < self.mutation_rate:  # 10%
                new_node = self.perform_point_mutation(node)
                node.type = new_node.type
                node.value = new_node.value
                node.children = new_node.children
            for child in node.children:
                queue.append(child)
        return root
    
    def get_random_node(self, root: Node) -> Node:
        queue = [root]
        node_set = []
        while queue:
            node = queue.pop()
            if node != root:
                node_set.append(node)
            for child in node.children:
                queue.append(child)
        
        return random.choice(node_set)

    def display_program(self, root: Node):
        level = 0
        stack = [(level, root)]
        while stack:
            level, node = stack.pop(-1)
            level_display = "".join(["  " for nr in range(level)]) + "|"
            print(level_display, level, node.type, node.print_value())
            for child in reversed(node.children):
                stack.append((level + 1, child))

    def evolve(self, copy=False):
        for generation in range(self.nr_of_generations):
            print("\n\nGeneration", generation,
                  " ----------------------------")
            if max(self.fitness)/len(self.population) > -0.1:
                print("Solution found in generation", generation)
                break

            if copy:
                population_copy = self.population.copy()
                fitness_copy = self.fitness.copy()

            for i in range(self.population_size):
                print("\nIndividual nr", i)
                self.display_program(self.population[i])
                print("Fitness", self.fitness[i])

            print("\n***** Operations ***")
            for idx in range(len(self.population)):
                if random.random() < self.crossover_rate:  # 50%
                    parent1 = self.perform_tournament()
                    parent2 = self.perform_tournament()
                    child = self.perform_crossover(
                        self.population[parent1], self.population[parent2])
                    print("Crossover", parent1, parent2, end=' ')
                    print("Child:")
                    self.display_program(child)
                else:
                    parent1 = self.perform_tournament()
                    child = self.mutate(self.population[parent1])

                weakest_idx = self.perform_negative_tournament()
                if copy:
                    population_copy[weakest_idx] = child
                    fitness_copy[weakest_idx] = self.compute_fitness(child)
                else:
                    self.population[weakest_idx] = child
                    self.fitness[weakest_idx] = self.compute_fitness(child)
                print("-> weakest idx:", weakest_idx)
            print("\nBest fitness:", max(self.fitness), "worst fitness:", min(
                self.fitness), "avg fitness:", sum(self.fitness)/len(self.fitness))


if __name__ == "__main__":
    gp = GP()
    gp.create_random_population()
    gp.evolve(copy=False)
    print("\nBest individual:")
    gp.display_program(gp.population[gp.fitness.index(max(gp.fitness))])
