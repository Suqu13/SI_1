from math import sqrt
from typing import List

from Node import Node


class Individual:
    def __init__(self, nodes: List[Node], distance: float) -> None:
        self.nodes = nodes
        self.distance = distance

    def resolve(self) -> float:
        nodes = self.nodes + [self.nodes[0]]
        distances = [self.__count_geo_distance(nodes_pair[0], nodes_pair[1]) for nodes_pair in
                     zip(nodes, nodes[1:])]
        return sum(distances)

    def __count_geo_distance(self, first_node: Node, second_node: Node) -> float:
        return sqrt((first_node.x - second_node.x) ** 2 + (first_node.y - second_node.y) ** 2)



    # def __swap_mutation(self) -> None:
    #     length = len(self.nodes)
    #     first_index = randrange(start=0, stop=length)
    #     second_index = randrange(start=0, stop=length)
    #     self.nodes[first_index], self.nodes[second_index] = self.nodes[second_index], self.nodes[first_index]

    # def __inversion_mutation(self) -> None:
    #     length = len(self.nodes)
    #     first_index = randrange(start=0, stop=length)
    #     second_index = randrange(start=first_index, stop=length)
    #     self.nodes = self.nodes[:first_index - 1] + self.nodes[first_index:second_index][::-1] + self.nodes[
    #                                                                                              second_index - 1:]
