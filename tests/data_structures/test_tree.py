from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree, Node, BinarySearchTree
import pytest

#################### prepare the data #########################

@pytest.fixture
def tree():
    tree = BinaryTree(88)
    tree.root.left = Node(42)
    tree.root.right = Node(22)
    tree.root.left.left = Node(99)
    tree.root.right.left = Node(1)

    return tree

@pytest.fixture
def bst():
    bst = BinarySearchTree(1001)
    bst.root.left = Node(42)
    bst.root.right = Node(10001)
    bst.root.left.left = Node(41)
    bst.root.right.left = Node(9999)

    return bst
##############################################################    
                   ### Required Tests ###
############################################################

# 1) Can successfully instantiate an empty tree
# 2) Can successfully instantiate a tree with a single root node
# 3) Can successfully add a left child and right child to a single root node
# 4) Can successfully return a collection from a preorder traversal
# 5) Can successfully return a collection from an inorder traversal
# 6) Can successfully return a collection from a postorder traversal


#############################################################



def test_success_instantiate_an_empty_tree():  ## 1
    ''' Can successfully instantiate an empty tree '''

    tree = BinaryTree()
    assert tree.root == None

def test_success_instantiate_tree_with_root_node(): ## 2
    ''' Can successfully instantiate a tree with a single root node '''

    tree = BinaryTree(88)
    assert tree.root.data == 88

def test_success_left_right_child(): ## 3
    ''' Can successfully add a left child and right child to a single root node '''

    tree = BinaryTree(88)
    tree.root.left = Node(42)
    tree.root.right = Node(22)

    assert tree.root.left.data == 42
    assert tree.root.right.data == 22

def test_success_return_collection_pre_order(tree): ## 4
    ''' Can successfully return a collection from a pre_order traversal '''
    
    result = tree.pre_order()
    assert result == [88, 42, 99, 22, 1] 

def test_success_return_collection_post_order(tree): ## 5
    ''' Can successfully return a collection from an post_order traversal '''

    result = tree.post_order()
    assert result == [99, 42, 1, 22, 88]

def test_success_return_collection_in_order(tree): ## 6
    ''' Can successfully return a collection from an inorder traversal '''

    result = tree.in_order()
    assert result == [99, 42, 88, 1, 22]


################### Additional Tests ##################


def test_success_add_node_to_bst(bst):
    ''' Test for successful addition of node to Binary Search Tree '''

    bst.add(1000)
    bst.add(10_000)
    assert bst.root.left.right.data == 1000
    assert bst.root.right.left.right.data == 10_000

def test_success_bst_contains_value(bst):
    ''' Test for successful traversal of Binary Search Tree to find existance of data '''

    bst.add(1000)
    bst.add(10_000)
    bst.add(-1)
    assert bst.contains(1000) == True
    assert bst.contains(10_000) == True
    assert bst.contains(-5) == False
    assert bst.contains(-1) == True
    assert bst.contains(99) == False 