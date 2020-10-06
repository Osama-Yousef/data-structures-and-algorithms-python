from data_structures_and_algorithms.challenges.get_edge.graph import Graph
from data_structures_and_algorithms.challenges.get_edge.get_edge import get_edge
import pytest


def test_graph_empty():
    """
    Trip through empty test.
    """

    graph = Graph()
    cities = ['a', 'b', 'c']

    expected = 'False:$0'
    actual = get_edge(graph, cities)
    assert actual == expected


def test_cities_empty(graph):
    """
    the Trip with (no cities) -->>soo  no trips.
    """

    expected = 'False:$0'
    actual = get_edge(graph, [])
    assert actual == expected


def test_get_edge(graph):
    """
    Trip through graph could  happen test.
    """

    cities = ['a', 'b', 'c']

    expected = 'True:$249'
    actual = get_edge(graph, cities)
    assert actual == expected





@pytest.fixture
def graph():
   

    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')

    graph.add_edge(a, b, 150)
    graph.add_edge(a, c, 82)

    graph.add_edge(b, a, 150)
    graph.add_edge(b, c, 99)
    graph.add_edge(b, d, 42)

    graph.add_edge(c, a, 82)
    graph.add_edge(c, b, 99)
    graph.add_edge(c, d, 105)
    graph.add_edge(c, e, 37)
    graph.add_edge(c, f, 26)

    graph.add_edge(d, b, 42)
    graph.add_edge(d, c, 105)
    graph.add_edge(d, f, 73)

    graph.add_edge(e, c, 37)
    graph.add_edge(e, f, 250)

    graph.add_edge(f, c, 26)
    graph.add_edge(f, d, 73)
    graph.add_edge(f, e, 250)

    return graph