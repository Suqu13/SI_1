from math import sqrt


class Individual:
    def __init__(self, nodes) -> None:
        self.nodes = nodes

    def resolve(self) -> float:
        distances = [self.__count_geo_distance(nodes_pair[0], nodes_pair[1]) for nodes_pair in
                     zip(self.nodes, self.nodes[1:])]
        return sum(distances)

    def __count_geo_distance(self, first_node, second_node) -> float:
        return sqrt((first_node.x - second_node.x) ** 2 + (first_node.y - second_node.y) ** 2)
