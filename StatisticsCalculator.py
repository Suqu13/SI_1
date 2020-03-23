from typing import List

from Individual import Individual


class Statistic:
    def __init__(self, iteration_number: int, best: float, avg: float, worst: float) -> None:
        self.iteration_number = iteration_number
        self.best = best
        self.avg = avg
        self.worst = worst


class StatisticsCalculator:
    def calculate(self, population: List[Individual], iteration_number: int) -> Statistic:
        distances = [individual.distance for individual in population]
        return Statistic(iteration_number, min(distances), sum(distances) / len(distances), max(distances))
