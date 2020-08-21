""" class for storing a singly linked node"""

class Node():
        # Function to initialise the node object 
   ## Arguments passed to the class constructor expression"""

    def __init__(self, value):
        self.value = value  # assign value
        self.next = None  # Initialize next as null


class LinkedList():

    """Create empty linked list"""

    def __init__(self):
        self.head = None  # Initialize head as None 
        self.size = 0     # Initialize size as 0



    def __len__(self):
        """Returns the number of elements """
        return self.size

    def is_empty(self):
        """ this will return true if list is empty """
        return self.size == 0

    def __str__(self):
        """will Return a string which has all the  values in the list"""
        current = self.head
        output = ''

        if current is None:
            print("Empty List!!!")
            return False


        while current:
            output += f'{{ {current.value} }} -> '
            current = current.next
        output += f'NULL'
        return output

   ### inserting new node with the value at the beginning(to the head of list)

    def insert(self, value):


        # current_node = self.head
        # self.head = Node(data, current_node)
        self.size += 1

        new_node = Node(value)         # Create a new Node 

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # This Function checks if the value exist in the list 
    # will return true if exists ,return no if not exist
    def includes(self, value):

        current = self.head              # Initialize current to head 

        # loop till current not equal to None 
        if current != None: 
            
            while current.next != None: ## or we can say while current
                if current.value == value: 
                    return True # data found 
                else:
                    current = current.next
          
        return False # Data Not found 



# #### Code execution starts here 

# if __name__=="__main__":
#     fruits = LinkedList()      # Start with the empty list 

#     fruits.append('Apple')
#     fruits.append('Orange')
#     fruits.append('Banana')
#     print(fruits)
#     if fruits.search('Apple'): 
#         print("Yes") 
#     else: 
#         print("No")







