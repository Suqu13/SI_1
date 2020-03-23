from random import randrange

from models.Individual import Individual


class Mutator:
    def mutate(self, individual: Individual) -> Individual:
        pass


class SwapMutator(Mutator):
    def mutate(self, individual: Individual) -> Individual:
        length = len(individual.nodes)
        first_index = randrange(start=0, stop=length)
        second_index = randrange(start=0, stop=length)
        mutated_nodes = individual.nodes[:]
        mutated_nodes[first_index], mutated_nodes[second_index] = mutated_nodes[second_index], mutated_nodes[
            first_index]
        return Individual(mutated_nodes)


class InversionMutator(Mutator):
    def mutate(self, individual: Individual) -> Individual:
        length = len(individual.nodes)
        first_index = randrange(start=0, stop=length)
        second_index = randrange(start=first_index, stop=length)
        mutated_nodes = individual.nodes[:first_index] + individual.nodes[first_index:second_index][
                                                             ::-1] + individual.nodes[second_index:]
        return Individual(mutated_nodes)
