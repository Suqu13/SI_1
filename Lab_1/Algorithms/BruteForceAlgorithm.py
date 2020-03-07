from math import sqrt
from random import choice

from Lab_1.Individual import Individual
from Lab_1.Node import Node


class BrutForceAlgorithm:

    def run(self, nodes) -> Individual:
        node = choice(nodes)
        internal_nodes = nodes[:]
        internal_nodes.remove(node)
        return Individual(self.__evaluate(node, internal_nodes))

    def __evaluate(self, node, nodes) -> []:
        best_genotype = []
        while len(nodes) != 0:
            node = self.__find_closest(nodes, node)
            best_genotype.append(node)
            nodes.remove(node)
        return best_genotype

    def __find_closest(self, nodes, node) -> Node:
        closest_node = (nodes[0], float('inf'))
        for n in nodes:
            distance = sqrt((node.x - n.x) ** 2 + (node.y - n.y) ** 2)
            if closest_node[1] > distance:
                closest_node = (n, distance)
        return closest_node[0]
