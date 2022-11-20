import graphviz


class Plotter:
    def __init__(self, node=None):
        self.root = node
        self.G = None

    def update_root(self, node):
        self.root = node
        self.update_parents()
        self.create_graph()

    def update_parents(self):
        queue = [self.root]
        while queue:
            node = queue.pop()
            for child in node.children:
                child.parent = node
                queue.append(child)

    def generate_graph_dict(self):
        unique_id = 0
        id_to_node = {}
        node_to_id = {}
        graph_dict = {}
        queue = [self.root]
        while queue:
            node = queue.pop()
            id_to_node[unique_id] = node
            node_to_id[node] = unique_id
            graph_dict[unique_id] = []
            try:
                graph_dict[node_to_id[node.parent]].append(unique_id)
            except KeyError:
                pass
            unique_id += 1
            for child in node.children[::-1]:
                queue.append(child)
        return graph_dict, id_to_node, node_to_id

    def create_graph(self):
        self.G = graphviz.Graph(format='svg')
        graph_dict, id_to_node, node_to_id = self.generate_graph_dict()
        for node_id in range(len(graph_dict)):
            node_type = str(id_to_node[node_id].type)[9:]
            node_value = '' if id_to_node[node_id].value is None else str(id_to_node[node_id].value)
            node_str = node_type + "\n" + node_value
            self.G.node(str(node_id), node_str)
        for node_id in range(len(graph_dict)):
            for child_id in graph_dict[node_id]:
                self.G.edge(str(node_id), str(child_id))

    def plot(self, root_node, filename='graph'):
        self.update_root(root_node)
        directory_ = "graphs/" + filename
        self.G.render(directory=directory_, view=True)


