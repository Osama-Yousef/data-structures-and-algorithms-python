from data_structures_and_algorithms.challenges.tree_intersection.stacks_and_queues import Queue

class Node:
    def __init__(self, data=None, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

class BinaryTree:
    def __init__(self, data=None):
        if data:
            data = Node(data)
        self.root = data

    @staticmethod
    def breadth_first(tree, node=None, array=None):
        '''Returns all values of tree in order using breadth first approach'''

        q = Queue()

        if not array:
            array = []

        if tree.root:
            q.enqueue(tree.root)

        while q.peek():

            front_node = q.dequeue()

            array.append(front_node.data)

            if front_node.left:
                q.enqueue(front_node.left)

            if front_node.right:
                q.enqueue(front_node.right)

        return array

    def post_order(self, node=None, result=[]):
        '''Return an array from tree in post-order order'''
        
        node = node or self.root

        if node.left:
            self.post_order(node.left, result)

        if node.right:
            self.post_order(node.right, result)

        result.append(node.data)

        return result

    def pre_order(self, node=None, result=[]):
        '''Return an array from tree in pre-order order'''
        
        node = node or self.root
        result.append(node.data)

        if node.left:
            self.pre_order(node.left, result)

        if node.right:
            self.pre_order(node.right, result)

        return result

    def in_order(self, node=None, result=[]):
        '''Return an array from tree in in_order order.'''
        
        node = node or self.root
        
        if node.left:
            self.in_order(node.left, result)

        result.append(node.data)

        if node.right:
            self.in_order(node.right, result)

        return result

class BinarySearchTree(BinaryTree):
    '''Create a Binary Search Tree by importing a Binary Tree'''
    def __init__(self, data=None):
        super().__init__(data)

    def add(self, data):
        '''Adds new node to BST'''

        node = Node(data)

        if not self.root:
            self.root = node

            return

        current = self.root

        while True:
            if node.data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = node

                    return

            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node

                    return

    def contains(self, data):
        ''' Return Boolean indicating existence (but not location) of value on tree '''

        if not self.root:
            return False

        current = self.root

        while True:
            if data == current.data:
                
                return True

            # Looking for something less than data (value)
            if data < current.data:
                if current.left:
                    current = current.left
                else:

                    return False

            # Looking for something greater than data (value)
            else:
                if current.right:
                    current = current.right
                else:

                    return False