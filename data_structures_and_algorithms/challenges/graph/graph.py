class Node:
    """
        Instance of a node object
        """

    def __init__(self, value):
        self.value = value
  

class Graph:

    """
    the Common (graph ) data structure.
    """
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """adds a node to the graph
        
        Arguments:
            value {[value]} -- [description]
        
        input:
            value() : new node value
        output: 
            (node) :new node added to graph
        
        Returns:
            node
        """
        node = Node(value)
        self._adjacency_list[node] = []
        return node

    def add_edge(self, start_node, end_node, weight=0):

        """
        Adding edge between two nodes in the graph.
        Input:
        start_node : First node to start edge from
        end_node : Second node to point edge to
        weight: Adds a weight to the edge (default 0).
        """
        if start_node not in self._adjacency_list:
            raise KeyError('Start node is not exist in Graph')

        if end_node not in self._adjacency_list:
            raise KeyError('End node is not exist in Graph')

        adjacencies = self._adjacency_list[start_node]

        adjacencies.append((end_node,weight))

    def get_nodes(self):
        """
        Get collection of all nodes in graph.
        Output:
        (list): Collection of all nodes in graph.
        """
        return self._adjacency_list.keys()

    def get_neighbors(self, node):

        """
        Get collection of neighbors for a node in graph.
        Input:
        node (Node): Get neighbors of the node.
        Output:
        (list): Neighbors of the node.
        """
        return self._adjacency_list[node]


    def size(self):
        """
         Returns: Total number of nodes in the graph

        """
        return len(self._adjacency_list)

