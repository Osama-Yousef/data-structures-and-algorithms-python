class Node:
    '''this Class is for Node instanceeeee'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    '''this STack is implementing the (Stack data structure ) with common methods used with it'''
    top = None

    def __init__(self, top=None):
        ''' creates an empty Stack when instantiated.   '''
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
        try:
            return self.top.data
        except AttributeError as e:
            return "Stack is empty"

        ''' OR '''
        # if not self.is_empty():
        #     return self.top.data

        # return None
        

    def is_empty(self):
        '''Method, takes no argument, and returns a boolean when it checks whether Stack is empty or not'''
        if self.top == None:
            return True

        return False

class Queue:
    '''this class implementing (Queue data structure ) with common methods used with it'''
    def __init__(self, front=None, rear=None):
        '''   It creates an empty Queue when instantiated.'''
        self.front = front
        self.rear = rear

    def peek(self):
        '''Method, returns val of node located at front of queue, without  removing it'''

        try:
            return self.front.data
        except AttributeError as e:
            return "Queue is empty"

        ''' OR '''

        # if not self.is_empty():
        #     return self.front.data

        # return None

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
        '''Method, checks if queue is empty or not so it will return a boolean'''

        if self.front == None:
            return True

        return False
