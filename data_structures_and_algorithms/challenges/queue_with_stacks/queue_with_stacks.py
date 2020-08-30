from data_structures_and_algorithms.challenges.queue_with_stacks.stacks_and_queues import Stack

class psueodoQueue:
    def __init__(self):
        self.stack = Stack()

    def dequeue(self):
        reverse_stack = Stack()

        while self.stack.top:
            reverse_stack.push(self.stack.pop())
        removed = reverse_stack.pop()

        while reverse_stack.top:
            self.enqueue(reverse_stack.pop())

        return removed

    def enqueue(self, data):
        self.stack.push(data)