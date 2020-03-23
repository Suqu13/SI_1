from math import sqrt
from typing import List

from Node import Node


class Individual:
    def __init__(self, nodes: List[Node], distance = -1) -> None:
        self.nodes = nodes
        self.distance = self.__resolve() if distance == -1 else distance

    def __resolve(self) -> float:
        nodes = self.nodes + [self.nodes[0]]
        distances = [self.__count_geo_distance(nodes_pair[0], nodes_pair[1]) for nodes_pair in
                     zip(nodes, nodes[1:])]
        return sum(distances)

    def __count_geo_distance(self, first_node: Node, second_node: Node) -> float:
        return sqrt((first_node.x - second_node.x) ** 2 + (first_node.y - second_node.y) ** 2)

