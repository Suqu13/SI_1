import math
from typing import List

from Individual import Individual


class ProbabilitiesCounter:
    def count(self, population: List[Individual]) -> List[float]:
        pass


class SimpleProbabilitiesCounter(ProbabilitiesCounter):
    def count(self, population: List[Individual]) -> List[float]:
        squared_distances = [math.sqrt(individual.distance) for individual in population]
        sum_distances = sum(squared_distances)
        return [distance / sum_distances for distance in squared_distances]
