from random import shuffle

from Lab_1.Individual import Individual


class RandomAlgorithm:

    def run(self, nodes) -> Individual:
        shuffled_nodes = nodes[:]
        shuffle(shuffled_nodes)
        return Individual(shuffled_nodes)
