from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import Node, BinaryTree, fizz_buzz_tree
import pytest

@pytest.fixture
def empty_tree():

    return BinaryTree()

@pytest.fixture
def fizzy_tree():
    ## preparing data
    tree = BinaryTree()
    tree.root = Node(3)
    tree.root.left = Node(5)
    tree.root.right = Node(7)
    tree.root.left.left = Node(15)

    return tree

def test_empty_tree(empty_tree):
    '''Test that running fizz_buzz_tree on an empty tree returns an empty tree'''

    expected = None
    actual = fizz_buzz_tree(empty_tree)
    assert expected == actual.root
        
def test_fizz_buzz_filled_tree(fizzy_tree):
    '''
    Tests old_tree node values become fizz, buzz, str(num), 
    and fizzbuzz in new_tree node values
    '''

    new_tree = fizz_buzz_tree(fizzy_tree)
    assert new_tree.root.val == 'Fizz'
    assert new_tree.root.left.val == 'Buzz'
    assert new_tree.root.right.val == '7'
    assert new_tree.root.left.left.val == 'FizzBuzz'