class Node:
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y

    def sum(self, z):
        print(self.x + self.y + z)
