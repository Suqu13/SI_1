from Lab_1.Node import Node


class Loader:
    def load(self, file_name) -> list:
        f = open(file_name, 'r')
        all_data = [element.strip() for element in f.readlines()]
        nodes_data = all_data[7:len(all_data) - 1]
        nodes = [self.__create_node(node_data) for node_data in nodes_data]
        f.close()
        return nodes

    def __create_node(self, text) -> Node:
        x = [float(num) for num in text.split()]
        return Node(x[0], x[1], x[2])
