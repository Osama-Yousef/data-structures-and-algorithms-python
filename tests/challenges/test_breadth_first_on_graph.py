from data_structures_and_algorithms.challenges.breadth_first_on_graph.breadth_first_on_graph import Graph,Node
import pytest

def test_one_node_and_one_edge():
    graph = Graph()

    start = graph.add_node('start')
    graph.add_edge(start, start, 10)

    assert graph.size() == 1
    assert graph.get_neighbors(start) == [(start, 10)]


def test_add_edge_start():
    
    graph = Graph()

    start = Node('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_node(): 
    
    graph = Graph()

    expected = 'osama' 

    actual = graph.add_node('osama').value

    assert actual == expected