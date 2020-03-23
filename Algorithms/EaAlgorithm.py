from typing import List
from math import ceil
from random import random

import copy

from Algorithms.GreedyAlgorithm import GreedyAlgorithm
from Algorithms.RandomAlgorithm import RandomAlgorithm
from CrossoverResolver import Crosser
from Individual import Individual
from MutationResolver import Mutator
from Node import Node
from ProbabilitiesCounter import ProbabilitiesCounter
from SelectionResolver import Selector
from StatisticsCalculator import StatisticsCalculator, Statistic


class EaAlgorithm:

    def __init__(self, nodes: List[Node], iteration_number: int, population_size: int,
                 population_fraction_from_greedy_indicator: float, best_population_fraction_to_next_generation_indicator,
                 selector: Selector, probabilities_counter: ProbabilitiesCounter, crossover_indicator: float,
                 mutation_indicator: float, mutator: Mutator, crosser: Crosser):
        self.nodes = nodes
        self.iteration_number = iteration_number
        self.population_size = population_size
        self.population_fraction_from_greedy = population_fraction_from_greedy_indicator
        self.best_population_fraction_to_next_generation = best_population_fraction_to_next_generation_indicator
        self.selector = selector
        self.probabilities_counter = probabilities_counter
        self.crossover_indicator = crossover_indicator
        self.mutation_indicator = mutation_indicator
        self.mutator = mutator
        self.crosser = crosser

    def __initialize(self) -> List[Individual]:
        random_algorithm = RandomAlgorithm()
        from_greedy = []
        if self.population_fraction_from_greedy != 0:
            greedy_algorithm = GreedyAlgorithm()
            from_greedy = [greedy_algorithm.run_without_initial_node(self.nodes)
                           for _ in range(0, ceil(self.population_fraction_from_greedy * len(self.nodes)))]
        return [random_algorithm.run_without_initial_node(self.nodes) for _ in
                range(0, self.population_size - len(from_greedy))] + from_greedy

    def run(self) -> List[Statistic]:
        statistics_calculator = StatisticsCalculator()
        current_population = self.__initialize()
        past_populations = [copy.deepcopy(current_population)]

        for current_iteration in range(0, self.iteration_number):
            previous_population = current_population
            probabilities = self.probabilities_counter.count(previous_population)
            if self.best_population_fraction_to_next_generation > 0:
                previous_population.sort(key=lambda t: t.distance)
                current_population = previous_population[
                                     0:(int(self.population_size * self.best_population_fraction_to_next_generation))]
            else:
                current_population = []
            while len(current_population) < self.population_size:
                first_parent = self.selector.select(previous_population, probabilities)
                second_parent = self.selector.select(previous_population, probabilities)
                if self.crossover_indicator > random():
                    new_population_part = [self.crosser.crossover(first_parent, second_parent)]
                else:
                    new_population_part = [first_parent, second_parent]
                if self.mutation_indicator > random():
                    new_population_part = [self.mutator.mutate(individual) for individual in new_population_part]
                current_population.extend(new_population_part)
            past_populations.append(current_population[:])
        statistics = [statistics_calculator.calculate(past_populations[iteration_number], iteration_number) for
                      iteration_number in range(0, len(past_populations))]
        return statistics
