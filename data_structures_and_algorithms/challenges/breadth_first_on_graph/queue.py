from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value) # O(1)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)