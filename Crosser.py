import random

from Individual import Individual


class Crosser:

    def crossover(self, first_individual, second_individual) -> Individual:
        length = len(first_individual.nodes)
        first_index = random.randrange(start=0, stop=length)
        second_index = random.randrange(start=first_index, stop=length)
        subnodes = first_individual.nodes[first_index:second_index]
        nodes = second_individual.nodes[:]
        for node in subnodes:
            nodes.remove(node)
        pasting_index_start = random.randrange(start=0, stop=(len(nodes)))
        return Individual(nodes[:pasting_index_start] + subnodes + nodes[pasting_index_start:])
