######### required tests ####################################################
"""
1) Node can be successfully added to the graph
2) An edge can be successfully added to the graph
3) A collection of all nodes can be properly retrieved from the graph
4) All appropriate neighbors can be retrieved from the graph
5) Neighbors are returned with the weight between nodes included
6) The proper size is returned, representing the number of nodes in the graph
7) A graph with only one node and edge can be properly returned
8) An empty graph properly returns null
"""
#############################################################################

import pytest

from data_structures_and_algorithms.challenges.graph.graph import Graph, Node
##############################################################################
## test 1
def test_add_node(): ## test 1
    
    graph = Graph()

    expected = 'osama' 

    actual = graph.add_node('osama').value

    assert actual == expected

###############################################################################
############ TEST 2 ############
def test_add_edge_start():
    
    graph = Graph()

    start = Node('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)




def test_add_edge_end():
    
    graph = Graph()

    end = Node('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_edge_other_case():
    
    graph = Graph()

    end = graph.add_node('end')

    start = graph.add_node('start')

    graph.add_edge(start, end)

####################################################################
##### test 3 

def test_get_nodes():

    graph = Graph()

    meat = graph.add_node('meat')

    chicken = graph.add_node('chicken')

    tomato = Node('tomato')

    expected = 2

    actual = len(graph.get_nodes())
    
    assert actual == expected

#######################################################################
###### TEST 4 ###########


def test_get_neighbors():

    graph = Graph()

    meat = graph.add_node('meat')
    chicken = graph.add_node('chicken')

    graph.add_edge(meat, chicken)

    expected = [(chicken, 0)]
    actual = graph.get_neighbors(meat)

    assert actual == expected
####################################################################
####### test 6 ###############

def test_size():

    graph = Graph()

    graph.add_node('osama')

    expected = 1

    actual = graph.size()

    assert actual == expected
#####################################################################
######## test 5 #########

def test_neighbors_with_weight_between_nodes():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    mid = graph.add_node('middle')
    other = graph.add_node('other')

    graph.add_edge(start, end, 1)
    graph.add_edge(start, mid, 2)
    graph.add_edge(start, other, 3)

    assert graph.get_neighbors(start) == [(end, 1), (mid, 2), (other, 3)]

######################################################################
##### test 7 #####

def test_one_node_and_one_edge():
    graph = Graph()

    start = graph.add_node('start')
    graph.add_edge(start, start, 10)

    assert graph.size() == 1
    assert graph.get_neighbors(start) == [(start, 10)]

#####################################################################
######### test  8 ########## 

def test_size_empty(): ## return 0 if its empty graph

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected

##################################################################333