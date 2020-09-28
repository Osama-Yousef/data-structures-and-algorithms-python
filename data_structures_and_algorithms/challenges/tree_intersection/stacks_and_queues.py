class Node:
    '''Class for Node instance'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    '''Class STack implementing Stack data structure with common methods'''
    top = None

    def __init__(self, top=None):
        '''Initiate Stack'''
        self.top = top

    def push(self, val):
        '''Method, takes val as argument and adds new node with val to the top of the stack'''
        new_node = Node(val)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        '''Method, removes node from top of Stack, returns node's data'''
        if not self.is_empty():
            self.top = self.top.next_node
            temp = self.top
            return temp.data

        return None

    def peek(self):
        '''Method, returns val of node at top of stack, doesn't remove from stack'''
        if not self.is_empty():
            return self.top.data

        return None
        

    def is_empty(self):
        '''Method, checks whether Stack is empty'''
        if self.top == None:
            return True

        return False

class Queue:
    '''Class Queue implementing Queue data structure with common methods'''
    def __init__(self, front=None, rear=None):
        '''Initiates Queue class'''
        self.front = front
        self.rear = rear

    def peek(self):
        '''Method, returns val of node located at front of queue, w/o removing it'''
        if not self.is_empty():
            return self.front.data

        return None

    def dequeue(self):
        '''Method, removes node from front of queue, returns that node's data'''
        if not self.is_empty():
            self.front = self.front.next_node
            temp = self.front
            temp.next = None
            return temp.data

        return None

    def enqueue(self, data):
        '''Method, takes any value as argument and adds node with that value to back of queue'''
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node

    def is_empty(self):
        '''Method, checks if queue is empty'''

        if self.front == None:
            return True

        return False