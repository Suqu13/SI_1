import copy
from math import sqrt
from typing import List
from random import choice

from Individual import Individual
from Node import Node


class GreedyAlgorithm:
    def run(self, initial_node: Node, nodes: List[Node]) -> Individual:
        internal_nodes = nodes[:]
        (nodes, distance) = self.__evaluate(initial_node, internal_nodes)
        return Individual(nodes, distance)

    def run_without_initial_node(self, nodes: List[Node]) -> Individual:
        internal_nodes = nodes[:]
        initial_node = choice(internal_nodes)
        internal_nodes.remove(initial_node)
        (nodes, distance) = self.__evaluate(initial_node, internal_nodes)
        return Individual(nodes, distance)

    def __evaluate(self, node: Node, nodes: List[Node]) -> (List[Node], float):
        best_genotype = [node]
        distance = 0
        length = len(nodes)
        while length != 0:
            closest_node = self.__find_closest(node, nodes)
            best_genotype.append(closest_node[0])
            distance = distance + closest_node[1]
            nodes.remove(closest_node[0])
            length = length -1
        return best_genotype, distance

    def __find_closest(self, node: Node, nodes: List[Node]) -> (Node, float):
        closest_node = (nodes[0], float('inf'))
        for n in nodes:
            distance = sqrt((node.x - n.x) ** 2 + (node.y - n.y) ** 2)
            if closest_node[1] >= distance:
                closest_node = (n, distance)
        return closest_node
