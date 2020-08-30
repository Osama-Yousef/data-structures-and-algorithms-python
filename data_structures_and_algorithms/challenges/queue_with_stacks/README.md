# Queues with Stacks
* Make a queue data structure interface made with two stack data structure instances.

## Challenge
* Write queue interface methods enqueue and dequeue.
* you have access to two stacks the method enqueue should take in a value and essetially "shift()" the value onto the stack the method dequeue should take off and return the last value in the stack




## Approach & Efficiency
* To enqueue a value to the pseudo queue all values are popped into a second stack, the value is pushed to the top of the second stack and then all values are popped from the second stack back into the first stack. To dequeue a value from the pseudo queue the top of the first stack is popped off.


## API
* The Pseudo Queue instance methods are enqueue which takes a value to add to the front of the queue and dequeue which removes a value from the front of the queue.


## White Board 

* see it on this link : https://drive.google.com/file/d/1MsZWIInfq38NjoUCnlVTFFCXBSTSzna7/view?usp=sharing