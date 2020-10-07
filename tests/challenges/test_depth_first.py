import pytest
from data_structures_and_algorithms.challenges.depth_first.depth_first import depth_first
from data_structures_and_algorithms.challenges.depth_first.graph import Graph, Node


def test_graph_with_no_vertices():
   
    graph = Graph()
    node = None

    expected = set({})
    actual = depth_first(graph, node)
    assert actual == expected


def test_graph_with_no_start_node():

    graph = Graph()
    graph.add_node('c')

    node = None

    expected = set({})
    actual = depth_first(graph, node)
    assert actual == expected


def test_only_islands():
   

    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    c = graph.add_node('c')

    node = c

    expected = {c,}
    actual = depth_first(graph, node)
    assert actual == expected


def test_with_edges():
    

    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')

    graph.add_edge(a, b)
    graph.add_edge(a, d)

    graph.add_edge(b, a)
    graph.add_edge(b, c)
    graph.add_edge(b, d)

    graph.add_edge(c, b)
    graph.add_edge(c, h)

    graph.add_edge(d, a)
    graph.add_edge(d, b)
    graph.add_edge(d, e)
    graph.add_edge(d, f)
    graph.add_edge(d, g)

    graph.add_edge(e, d)

    graph.add_edge(f, d)
    graph.add_edge(f, g)

    graph.add_edge(g, d)
    graph.add_edge(g, f)

    graph.add_edge(h, c)

    expected = {a, b, c, h, d, e, f, g}
    actual = depth_first(graph, a)

    assert actual == expected