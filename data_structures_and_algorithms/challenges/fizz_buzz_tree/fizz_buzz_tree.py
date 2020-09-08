class Node():
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        pass

    def in_order(self):
        pass

    def post_order(self):
        pass

    def contains(self):
        pass

    def is_empty(self):
        pass

def fizz_buzz_tree(tree):
    '''  which takes a k-ary tree as an argument 
    determine whether or not the value of each node is
     divisible by 3, 5 or both. Create a new tree with the same structure as the original'''
    new_tree = BinaryTree()
    new_node = Node()

    if tree.root == None:
        return new_tree
        
    old_node = tree.root   # root is ref to first node



    def visit_node(old_node, new_node):

        new_node.val = fizz_buzz(old_node.val)
        if old_node.left:
            new_node.left = Node()
            visit_node(old_node.left, new_node.left)

        if old_node.right:
            new_node.right = Node()
            visit_node(old_node.right, new_node.right)

    def fizz_buzz(old_value):

        result = ''
        if old_value % 3 == 0:
            result += 'Fizz'

        if old_value % 5 == 0:
            result += 'Buzz'

        return result or str(old_value)

    visit_node(old_node, new_node)

    new_tree.root = new_node

    return new_tree