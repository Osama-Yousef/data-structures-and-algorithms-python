from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import psueodoQueue
import pytest

q = psueodoQueue()

def test_enqueue():
    q.enqueue('apple')
    q.enqueue('banana')
    actual = q.stack.peek()
    assert actual == 'banana'

def test_dequeue():
    q.enqueue('apple')
    q.enqueue('banana')
    actual = q.dequeue()
    assert actual == 'apple'



def test_dequeue_2():
  q = psueodoQueue()

  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  popped = []
  for _ in range(3):
    popped.append(q.dequeue())
  
  assert popped == [1, 2, 3]