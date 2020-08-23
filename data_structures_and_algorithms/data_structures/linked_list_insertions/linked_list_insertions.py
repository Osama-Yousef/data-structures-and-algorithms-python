class Node:
    """class for storing a singly linked node"""
    def __init__(self, data, next = None):
        """Arguments passed  constructor """
        self.data = data
        self.next = next

    
class LinkedList:

    def __init__(self, value = None):
        """Create empty linked list"""
        self.head = value
        self.size = 0

    def __len__(self):
        """Returns the number of elements in the list"""
        return self.size

    def is_empty(self):
        """Returns True if list is empty , return false if the list have elements inside it"""
        return self.size == 0

    

    def __str__(self):
        """Returns all values in list as a string"""
        current = self.head
        result = ''
        while current:
            result += f'{{ {current.data} }} -> '
            current = current.next
        result += f'NULL'
        return result

    def insert(self, data):
        """PUSH a new node with that value to the head of the list with an O(1) time performance"""
        current = self.head
        self.head = Node(data, current)
        self.size += 1

    def includes(self, data):
        """Returns True if value exists on the stack"""
        current = self.head
        while current:
            if current.data == data:
                return True
            else:
                current = current.next

        return False

    def append(self, value):
        '''Adds a new node to the end of the list'''
        node = Node(value)
        current = self.head
        if not self.head:
            self.head = node
            return 
        while current:
            if current.next == None:
                current.next = node
                return
            else:
                current = current.next
            
    def insert_before(self, value, new_val):
        '''Add a new node with  newVal before the first value node'''
        node = Node(new_val)
        current = self.head
        while current:
            if current.data == value:
                node.next = current
                self.head = node
                return
            if current.next:
                if current.next.data == value:
                    node.next = current.next
                    current.next = node
                    return
                current = current.next
        raise ValueError(f'{value} not found')
    
    def insert_after(self, value, new_val):
        '''Add a new node with newVal after the first value node'''
        node = Node(new_val)
        current = self.head
        while current:
            if current.data == value:
                node.next = current.next
                current.next = node
                return
            current = current.next
        raise ValueError(f'{value} not found')