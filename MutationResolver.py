from random import randrange

from Individual import Individual


class Mutator:
    def mutate(self, individual: Individual) -> Individual:
        pass

class SwapMutator(Mutator):
    distance_resolver = 
    def mutate(self, individual: Individual) -> Individual:
        length = len(individual.nodes)
        first_index = randrange(start=0, stop=length)
        second_index = randrange(start=0, stop=length)
        mutated_individual = Individual(individual.nodes, 0)
        mutated_individual.nodes[first_index], mutated_individual.nodes[second_index] = mutated_individual.nodes[
                                                                                            second_index], \
                                                                                        mutated_individual.nodes[
                                                                                            first_index]
        mutated_individual.distance =
        return mutated_individual


class InversionMutator(Mutator):
    def mutate(self, individual: Individual) -> Individual:
        length = len(individual.nodes)
        first_index = randrange(start=0, stop=length)
        second_index = randrange(start=first_index, stop=length)
        mutated_individual = Individual(individual.nodes)
        mutated_individual.nodes = mutated_individual.nodes[:first_index - 1] + mutated_individual.nodes[
                                                                                first_index:second_index][::-1] + \
                                   mutated_individual.nodes[second_index - 1:]
        return mutated_individual
