class Graph():
   

    def __init__(self):
       

        self._adjacency_list = {}


    def add_node(self, value):
        

        node = Node(value)

        self._adjacency_list[node] = []

        return node


    def add_edge(self, start_node, end_node, weight=0):
        

        if start_node not in self._adjacency_list:
            raise KeyError('No start node.')

        if end_node not in self._adjacency_list:
            raise KeyError('No end node.')

        self._adjacency_list[start_node].append((end_node, weight))


    def get_nodes(self):
        

        return self._adjacency_list.keys()


    def get_neighbors(self, start_node):
      

        return self._adjacency_list[start_node]


    def size(self):
       

        return len(self._adjacency_list)


class Node():
   

    def __init__(self, value):
        

        self.value = value