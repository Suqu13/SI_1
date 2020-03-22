from typing import List

from Individual import Individual


class ProbabilitiesCounter:
    def count(self, population: List[Individual]) -> List[float]:
        pass


class SimpleProbabilitiesCounter(ProbabilitiesCounter):
    def count(self, population: List[Individual]) -> List[float]:
        distances = [individual.resolve() for individual in population]
        sum_distances = sum(distances)
        return [distance / sum_distances for distance in distances]
