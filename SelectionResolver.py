from typing import List
import numpy as np

from Individual import Individual


class Selector:
    def select(self, population: List[Individual], probabilities: List[float]) -> Individual:
        pass


class RouletteSelector(Selector):
    def select(self, population: List[Individual], probabilities: List[float]) -> Individual:
        return np.random.choice(population, p=probabilities)
