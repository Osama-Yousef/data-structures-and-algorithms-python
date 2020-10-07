def depth_first(graph, node):
    """
    Walk through a graph in depth first pre-order.
   
    """

    vertices = set({})

    graph_vertices = graph.get_nodes()

    if not graph_vertices:
        return vertices

    if node not in graph_vertices:
        return vertices

    def walk(graph, node, vertices):

        if node in vertices:
            return

        vertices.add(node)

        neighbors = graph.get_neighbors(node)
        for neighbor in neighbors:
            walk(graph, neighbor[0], vertices)

    walk(graph, node, vertices)

    return vertices