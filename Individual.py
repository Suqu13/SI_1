import random
from math import sqrt


class Individual:
    def __init__(self, nodes) -> None:
        self.nodes = nodes

    def resolve(self) -> float:
        nodes = self.nodes + [self.nodes[0]]
        distances = [self.__count_geo_distance(nodes_pair[0], nodes_pair[1]) for nodes_pair in
                     zip(nodes, nodes[1:])]
        return sum(distances)

    def __count_geo_distance(self, first_node, second_node) -> float:
        return sqrt((first_node.x - second_node.x) ** 2 + (first_node.y - second_node.y) ** 2)

    def mutate(self) -> None:
        if random.randrange(start=0, stop=1) == 1:
            self.__inversion_mutation()
        else:
            self.__swap_mutation()

    def __swap_mutation(self) -> None:
        length = len(self.nodes)
        first_index = random.randrange(start=0, stop=length)
        second_index = random.randrange(start=0, stop=length)
        self.nodes[first_index], self.nodes[second_index] = self.nodes[second_index], self.nodes[first_index]
        print(len(self.nodes))

    def __inversion_mutation(self) -> None:
        length = len(self.nodes)
        first_index = random.randrange(start=0, stop=length)
        second_index = random.randrange(start=first_index, stop=length)
        self.nodes = self.nodes[:first_index - 1] + self.nodes[first_index:second_index][::-1] + self.nodes[
                                                                                                 second_index - 1:]
