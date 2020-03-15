from math import sqrt

from Individual import Individual
from Node import Node


class GreedyAlgorithm:

    def run(self, initial_node, nodes) -> Individual:
        internal_nodes = nodes[:]
        return Individual(self.__evaluate(initial_node, internal_nodes))

    def __evaluate(self, node, nodes) -> []:
        best_genotype = [node]
        while len(nodes) != 0:
            node = self.__find_closest(nodes, node)
            best_genotype.append(node)
            nodes.remove(node)
        return best_genotype

    def __find_closest(self, nodes, node) -> Node:
        closest_node = (nodes[0], float('inf'))
        for n in nodes:
            distance = sqrt((node.x - n.x) ** 2 + (node.y - n.y) ** 2)
            if closest_node[1] >= distance:
                closest_node = (n, distance)
        return closest_node[0]
