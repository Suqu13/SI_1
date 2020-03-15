from Algorithms.GreedyAlgorithm import GreedyAlgorithm
from Algorithms.RandomAlgorithm import RandomAlgorithm
from Crosser import Crosser
from Loader import Loader

if __name__ == '__main__':
    loader = Loader()
    nodes = loader.load('TSP/kroA100.tsp')

    randomAlgorithm = RandomAlgorithm()
    greedyAlgorithm = GreedyAlgorithm()
    crosser = Crosser()

    greedyAlgorithmResult = greedyAlgorithm.run(nodes[0], nodes[1:])
    # print(greedyAlgorithmResult.resolve())

    randomAlgorithmResult = randomAlgorithm.run(nodes[0], nodes[1:])
    # print(randomAlgorithmResult.resolve())

    print(len(crosser.crossover(greedyAlgorithmResult, randomAlgorithmResult).nodes))

