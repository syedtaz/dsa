from list import List, a
from typing import Optional

# CLRS

# 10.2.1 Implement insert in O(1) time.
def insert(lst : List[a] | None, k: a) -> List[a]:
  return List(value = k, next = lst)

# 10.2.2 Implement a stack with a singly linked list.
class Stack[a]():
  stack: List[a] | None

  def __init__(self) -> None:
    self.stack = None

  def push(self, v: a) -> None:
    if self.stack is None:
      self.stack = List(value = v, next = None)
    else:
      self.stack = List(value = v, next = self.stack)

  def pop(self) -> a | None:
    if self.stack is None:
      return None

    v = self.stack.value
    self.stack = self.stack.next
    return v

# 10.2.3 Implement a queue with singly linked lists.
class Queue[a]():
  head: List[a] | None
  tail: List[a] | None

  def __init__(self):
    self.head = None

  def enqueue(self, v: a):
    if self.head is None:
      self.head = List[a](value = v, next = None)
      self.tail = self.head
    else:
      assert self.tail is not None
      self.tail.next = List[a](value = v, next = None)
      self.tail = self.tail.next

  def dequeue(self) -> Optional[a]:
    if self.head is None:
      return None

    t = self.head.value
    self.head = self.head.next
    return t

# 10.2.4 Disjoint set -- support union in O(1) time.

class CircularList[a]():
  lst: List[a] | None
  hd: List[a] | None

  def __init__(self, v: a) -> None:
    self.lst = List(value = v, next = None)
    self.hd = self.lst

  def insert(self, v: a) -> None:
    self.lst = List(value = v, next = self.lst)

  def union(self, b: 'CircularList[a]') -> None:
    hd_a = self.hd
    assert hd_a is not None

    hd_a.next = b.lst
    self.hd = b.hd

# 10.2.5 O(n) reverse with O(1) space for singly linked list.
# Pretty much the same as tail recursive reverse later in Skiena.
def reverse_const(lst: List[a] | None) -> List[a] | None:
  acc = None
  cur = lst
  while cur is not None:
    acc = List(value = cur.value, next = acc)
    cur = cur.next

  return acc
