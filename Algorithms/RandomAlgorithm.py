from random import shuffle, choice
from typing import List

from Individual import Individual
from Node import Node


class RandomAlgorithm:
    def run(self, initial_node: Node, nodes: List[Node]) -> Individual:
        shuffled_nodes = nodes[:]
        shuffle(shuffled_nodes)
        shuffled_nodes.insert(0, initial_node)
        return Individual(shuffled_nodes)

    def run_without_initial_node(self, nodes: List[Node]) -> Individual:
        shuffled_nodes = nodes[:]
        shuffle(shuffled_nodes)
        return Individual(shuffled_nodes)
