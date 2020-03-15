from random import shuffle

from Individual import Individual


class RandomAlgorithm:

    def run(self, initial_node, nodes) -> Individual:
        shuffled_nodes = nodes[:]
        shuffle(shuffled_nodes)
        shuffled_nodes.insert(0, initial_node)
        return Individual(shuffled_nodes)
