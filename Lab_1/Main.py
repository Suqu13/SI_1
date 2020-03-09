from Lab_1.Algorithms.GreedyAlgorithm import GreedyAlgorithm
from Lab_1.Algorithms.RandomAlgorithm import RandomAlgorithm
from Lab_1.Loader import Loader

if __name__ == '__main__':
    loader = Loader()
    nodes = loader.load('TSP/kroA100.tsp')

    randomAlgorithm = RandomAlgorithm()
    greedyAlgorithm = GreedyAlgorithm()

    i = 0
    greedyAlgorithmResult = greedyAlgorithm.run(nodes)
    print(greedyAlgorithmResult.resolve())
    print([x.name for x in greedyAlgorithmResult.nodes])
