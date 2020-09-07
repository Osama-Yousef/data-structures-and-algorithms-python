from collections import deque


class BinaryTree:
    """Simple BinaryTree with enough functionality for breadth first adding"""

    def __init__(self):
        self.root = None

    def add(self, value):

        node = Node(value)

        if not self.root:
            self.root = node
            return

        q = Queue()

        q.enqueue(self.root)

        while not q.is_empty():

            current = q.dequeue()

            if current.left:
                q.enqueue(current.left)
            else:
                current.left = node
                break

            if current.right:
                q.enqueue(current.right)
            else:
                current.right = node
                break

class BinarySearchTree():
    """BinarySearchTree with enough functionality for breadth first adding"""
    def __init__(self, value=None):
        self.root = value

    def add(self, value, current=None):
        pass

class Node:
    """ Tree Node"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right

class Queue:
    """Implementation of Queue that compose built in deque class"""

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def peek(self):
        return self.dq[-1]

    def is_empty(self):
        return len(self.dq) == 0 

def breadth_first(tree):
    """
    Breadth first traversal that takes in binary tree, 
    traverses the tree using breadth first method and finally
    returns a list of the values in order    
    """

    if not tree.root:
        return None

    q = Queue()
    lst = []

    q.enqueue(tree.root)

    while not q.is_empty():
        node = q.dequeue()
        lst.append(node.value)

        if node.left:
            q.enqueue(node.left)

        if node.right:
            q.enqueue(node.right)

    return lst