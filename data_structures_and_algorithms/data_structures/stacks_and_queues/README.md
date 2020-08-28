# Stacks and Queues
* A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

* Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends. One end is always used to insert data (enqueue) and the other is used to remove data (dequeue).

## Challenge

* Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

* Create a Stack class that has a top property. It creates an empty Stack when instantiated. This object should be aware of a default empty value assigned to top when the stack is created.

* Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.

* Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.

* Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
------------------------------------------------------------------
* Create a Queue class that has a front property. It creates an empty Queue when instantiated. This object should be aware of a default empty value assigned to front when the queue is created.

* Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.

* Define a method called dequeue that does not take any argument, removes the node from the ftront of the queue, and returns the node’s value.

* Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.


## Approach & Efficiency


* I implemented both data structures ( stack && queue) using a basic node class with a next and a value set to none 

* For the stack, I created a class '''Stack()''' and initialized it with self and top  properties then do the other methods in the class

* For the queue, I created a class '''Queue()''' and initialized it with self and front and rear  properties ten i do the other methods in this class

## API

### My stack class has 4 methods:

* `pop()` Since stacks use a last in first out approach, this method removes the item on top of the stack by setting its pointer to self.top.next. I also store a reference to the value to be popped in a temp variable, so that it can be returned

* `push()` This method pushes a new node onto the stack by setting the current top node as the incoming node's next, then setting the new node as self.top This method takes in a single value as its only parameter

* `peek()` This method returns the value at the top of the stack, if it exists

* `is_empty()` Checks if self.top exists and returns a boolean

---------------------------------------------------------------------------------------------------

### My Queue class has 4 similar methods:

* `is_empty()` Checks if self.front exists and returns a boolean

* `enqueue()` Appends a node to the end of the queue by pointing the current rear (if it exists) to the new node, and assigning self.rear to the new node. If the queue is empty, we assign the new_node to both the front and the rear.

* `dequeue()` removes a node from the front of the queue, if the queue is empty, we print a message and return the empty queue To remove the first node, we first store a reference to it in a temp variable We then reassign self.front to be the next item in the queue The return is a string of the value of the temp variable




















