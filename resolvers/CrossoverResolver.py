from random import randrange

from models.Individual import Individual


class Crosser:
    def crossover(self, first_individual: Individual, second_individual: Individual) -> Individual:
        pass


class CrosserOX(Crosser):
    def crossover(self, first_individual: Individual, second_individual: Individual) -> Individual:
        length = len(first_individual.nodes)
        first_index = randrange(start=0, stop=length)
        second_index = randrange(start=first_index, stop=length)
        subnodes = first_individual.nodes[first_index:second_index]
        nodes = second_individual.nodes[:]
        for node in subnodes:
            nodes.remove(node)
        pasting_index = randrange(start=0, stop=length)
        return Individual(nodes[:pasting_index] + subnodes + nodes[pasting_index:])
