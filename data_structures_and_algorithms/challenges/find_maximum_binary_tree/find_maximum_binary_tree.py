class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, data=None):
        if data:
            data = Node(data)
        self.root = data

    

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

    def find_maximum_value_iterative(self,node=None,result=[]):
        ''' return the maximum value stored in the binary tree'''
        
        max_val = 0

        if not self.root:
            return max_val

        result = []
        result.append(self.root)

        while result:
            current_node = result.pop(0)

            if current_node.data > max_val:
                max_val = current_node.data

            if current_node.left:
                result.append(current_node.left)

            if current_node.right:
                result.append(current_node.right)

        return max_val

class BinarySearchTree(BinaryTree):
    

    def add(self, data): ## adds a new node with that value in the correct location in the binary search tree.
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

    def contains(self, data): ## returns a boolean indicating whether or not the value is in the tree at least once 
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