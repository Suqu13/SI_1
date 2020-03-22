from math import sqrt
from typing import List
from random import choice

from Individual import Individual
from Node import Node


class GreedyAlgorithm:
    def run(self, initial_node: Node, nodes: List[Node]) -> Individual:
        internal_nodes = nodes[:]
        return Individual(self.__evaluate(initial_node, internal_nodes))

    def run_without_initial_node(self, nodes: List[Node]) -> Individual:
        internal_nodes = nodes[:]
        initial_node = choice(internal_nodes)
        internal_nodes.remove(initial_node)
        return Individual(self.__evaluate(initial_node, internal_nodes))

    def __evaluate(self, node: Node, nodes: List[Node]) -> (List[Node], float):
        best_genotype = [node], 0
        while len(nodes) != 0:
            node, distance = self.__find_closest(node, nodes)
            best_genotype = best_genotype[0] + [node], best_genotype[1] + distance
            nodes.remove(node)
        return best_genotype,

    def __find_closest(self, node: Node, nodes: List[Node]) -> Node:
        closest_node = (nodes[0], float('inf'))
        for n in nodes:
            distance = sqrt((node.x - n.x) ** 2 + (node.y - n.y) ** 2)
            if closest_node[1] >= distance:
                closest_node = (n, distance)
        return closest_node
