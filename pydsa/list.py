from typing import TypeVar, Tuple, Any, Optional
from dataclasses import dataclass

a = TypeVar('a')

# Singly linked list.
@dataclass
class List[a]():
  value: a
  next: 'List[a] | None'

# Finds the node containing a value if it exists.
def search(lst : List[a] | None, k: a) -> List[a] | None:
  return None if lst is None else search(lst.next, k)

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

# 10.2.5 O(n) reverse with O(1) space for singly linked list.
# Pretty much the same as tail recursive reverse later in Skiena.
def reverse_const(lst: List[a] | None) -> List[a] | None:
  acc = None
  cur = lst
  while cur is not None:
    acc = List(value = cur.value, next = acc)
    cur = cur.next

  return acc

# Skiena

# 3.1

def valid_parentheses(input: str) -> bool:
  stack : Stack[str] = Stack()

  for char in input:
    match char:
      case '(':
        stack.push('(')
      case ')':
        if stack.pop() is None:
          return False
      case _:
        raise Exception

  return True

# 3.3 Give an algorithm to reverse the direction of a given singly linked list.
# In other words, after the reversal all pointers should now point backwards.
# Your algorithm should take linear time.

def reverse(input: List[a]) -> List[a]:

  def aux(input: List[a] | None, acc: List[a]) -> List[a]:
    return acc if input is None else aux(input.next, List(value = input.value, next = acc))

  return aux(input, None) # type: ignore

# 3.4 Design a stack S that supports S.push(x), S.pop(), and S.findmin(),
# which returns the minimum element of S. All operations should run in constant
# time.

class MinStack():
  stack: List[Tuple[int, int]] | None

  def __init__(self):
    self.stack = None

  def push(self, v: int) -> None:
    if self.stack is None:
      self.stack = List(value = (v, v), next = None)
    else:
      _, cur = self.stack.value
      self.stack = List(value = (v, min(cur, v)), next = self.stack)

  def pop(self) -> int | None:
    if self.stack is None:
      return None

    v, _ = self.stack.value
    self.stack = self.stack.next
    return v

  def find_min(self) -> int | None:
    if self.stack is None:
      return None

    _, minimum = self.stack.value
    return minimum

# 3.7 Work out the details of supporting constant-time deletion from a singly
# linked list as per the footnote from page 79, ideally to an actual implementation.
# Support the other operations as efficiently as possible.

# TODO! NOT CORRECT ADD SENTINEL
def const_delete(lst: List[Any] | None) -> None:
  if lst is None or lst.next is None:
    return

  lst.value = lst.next.value
  lst.next = lst.next.next
  return