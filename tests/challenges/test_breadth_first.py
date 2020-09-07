from data_structures_and_algorithms.challenges.breadth_first.breadth_first import Node, BinaryTree, BinarySearchTree, breadth_first


#########  tests ##########

def test_empty_tree():
    '''If tree is empty  return None.'''
    tree = BinarySearchTree()
    actual = breadth_first(tree)
    expected = None
    assert expected == actual

def test_single_node():
    '''Test that binary tree with single item returns list with that single item.'''
    tree = BinaryTree()
    tree.add(15)
    actual = breadth_first(tree)
    expected = [15]
    assert expected == actual

def test_four_nodes():
    '''Test that binary tree with four nodes returns list with those four items.'''
    tree = BinaryTree()
    tree.add(11)
    tree.add(9)
    tree.add(15)
    tree.add(5)
    actual = breadth_first(tree)
    expected = [11, 9, 15, 5]
    assert expected == actual 


def test_many_nodes():
    '''Test that binary tree with 10 nodes returns list with those 10 items.'''
    tree = BinaryTree()
    tree.add(11)
    tree.add(9)
    tree.add(15)
    tree.add(5)
    tree.add(11)
    tree.add(9)
    tree.add(15)
    tree.add(5)
    actual = breadth_first(tree)
    expected = [11, 9, 15, 5, 11, 9, 15, 5]
    assert expected == actual   