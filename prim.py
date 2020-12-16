#!/bin/python

class Node :
    def __init__(self, name=None, neighbours=[]):
        self.name = name
        self.neighbours = neighbours
        self.key = None

    def print_neigbours(self):
        neighbours = [f"{self.name} --> {neighbour} \n" for neighbour in self.neighbours]
        for neighbour in neighbours:
            print(neighbour)


class Graph :
    def __init__(self):
        self.nodes=[]
        self.weights={}

    def add_node(self, node, neighbours):
        n = Node(node, neighbours)
        self.nodes.append(n)

    def print_nodes(self):
        for nodes in self.nodes:
            nodes.print_neigbours()

    def add_weight(self, node1, node2, edge_weight):
        edge_name = '-'.join([node1, node2])
        self.weights[edge_name] = edge_weight

    def get_neighbours(self, node_name):
        for nodes in self.nodes:
            if(nodes.name == node_name):
                neighbours = nodes.neighbours
        return neighbours

    def prim_algorithm(self, root):
        queue={}
        for nodes in self.nodes :
            nodes.key = 0 if nodes.name ==root else float('inf')
            queue[nodes.name] = nodes.key

        while queue :
            min_key_node = min(queue, key=queue.get)
            del queue[min_key_node]
            print(min_key_node)

            target_neighbours = self.get_neighbours(min_key_node)

            for n in target_neighbours:
                if n not in queue :
                    target_neighbours.remove(n)

            for n in target_neighbours:
                edge_name = '-'.join([min_key_node, n])

                if edge_name not in self.weights:
                    edge_name = '-'.join([n, min_key_node])
                
                for nodes in self.nodes:
                    if nodes.name == n and self.weights[edge_name] < nodes.key:
                        nodes.key = self.weights[edge_name]
                        queue[nodes.name] = nodes.key


if __name__ == "__main__":
    g = Graph()
    g.add_node('v1', ['v2', 'v3'])
    g.add_node('v2', ['v1', 'v3', 'v4'])
    g.add_node('v3', ['v1', 'v2', 'v4', 'v5'])
    g.add_node('v4', ['v2', 'v3'])
    g.add_node('v5', ['v4'])

    g.add_weight('v1', 'v2', 4)
    g.add_weight('v1', 'v3', 6)
    g.add_weight('v3', 'v2', 7)
    g.add_weight('v3', 'v4', 14)
    g.add_weight('v3', 'v5', 3)
    g.add_weight('v2', 'v4', 5)

    g.print_nodes()
    print(g.weights)

    g.prim_algorithm('v4')
