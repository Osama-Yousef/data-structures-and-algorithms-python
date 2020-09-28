from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import tree_intersection
from data_structures_and_algorithms.challenges.tree_intersection.tree import BinaryTree, BinarySearchTree
import pytest

@pytest.fixture
def tree_a():
    tree = BinarySearchTree(88)
    tree.add(66)
    tree.add(60)
    tree.add(55)
    tree.add(50)
    tree.add(40)

    return tree

@pytest.fixture
def tree_b():
    tree = BinarySearchTree(1000)
    tree.add(900)
    tree.add(850)
    tree.add(800)
    tree.add(50)
    tree.add(40)

    return tree

def test_null_tree():
    ''' Returns empty set if either tree is null (empty) '''
    tree_a, tree_b = BinaryTree(), BinaryTree()
    actual = tree_intersection(tree_a, tree_b)
    expected = set()
    assert actual == expected

def test_intersection(tree_a, tree_b):
    ''' Test that given two BTs only elements found in both sets are returned. '''
    assert tree_intersection(tree_a, tree_b) == {50,40}




################### test other two trees #############



@pytest.fixture
def tree_c():
    tree = BinarySearchTree(150)
    tree.add(100)
    tree.add(250)
    tree.add(75)
    tree.add(160)
    tree.add(200)
    tree.add(350)
    tree.add(125)
    tree.add(175)
    tree.add(300)
    tree.add(500)
    


    return tree

@pytest.fixture
def tree_d():
    tree = BinarySearchTree(42)
    tree.add(100)
    tree.add(600)
    tree.add(15)
    tree.add(160)
    tree.add(200)
    tree.add(350)
    tree.add(125)
    tree.add(175)
    tree.add(4)
    tree.add(500)
    

    return tree

def test_null_tree():
    ''' Returns empty set if either tree is null (empty) '''
    tree_c, tree_d = BinaryTree(), BinaryTree()
    actual = tree_intersection(tree_c, tree_d)
    expected = set()
    assert actual == expected

def test_intersection(tree_c, tree_d):
    ''' Test that given two BTs only elements found in both sets are returned. '''
    assert tree_intersection(tree_c, tree_d) == {100,160,125,175,200,350,500}





















