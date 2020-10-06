from data_structures_and_algorithms.challenges.get_edge.graph import Graph


def get_edge(graph, cities):
    """
    See if a trip through a graph can happen and at what cost.
    
    """

    price = 0
    is_neighbor = False

    if not len(cities):
        return f'{is_neighbor}:${price}'

    nodes = graph.get_nodes()

    if not nodes:
        return f'{is_neighbor}:${price}'

    city_nodes = []
    city_counter = 0

    for city in cities:
        city_counter += 1

        for node in nodes:
            if city == node.value:
                city_nodes.append(node)

        if not city_counter == len(city_nodes):
            return f'{is_neighbor}:${price}'

    neighbors = graph.get_neighbors(city_nodes[0])

    for i in range(1, len(city_nodes)):
        is_neighbor = False

        for neighbor in neighbors:
            if neighbor[0] == city_nodes[i]:
                price += neighbor[1]
                is_neighbor = True
                break

        if not is_neighbor:
            return 'False:$0'

        neighbors = graph.get_neighbors(city_nodes[i])

    return f'{is_neighbor}:${price}'