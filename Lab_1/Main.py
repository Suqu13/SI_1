from Lab_1.Algorithms.BruteForceAlgorithm import BrutForceAlgorithm
from Lab_1.Algorithms.RandomAlgorithm import RandomAlgorithm
from Lab_1.Loader import Loader

if __name__ == '__main__':
    loader = Loader()
    nodes = loader.load('TSP/pr2392.tsp')

    randomAlgorithm = RandomAlgorithm()
    brutForceAlgorithm = BrutForceAlgorithm()

    i = 0
    while i < 100:
        randomAlgorithmResult = randomAlgorithm.run(nodes)
        print(randomAlgorithmResult.resolve())
        brutForceAlgorithmResult = brutForceAlgorithm.run(nodes)
        print(brutForceAlgorithmResult.resolve())
        i = i + 1
