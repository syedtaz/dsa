from list import List, a
from clrs import Stack
from typing import Tuple, Any

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

# 3.2 Give an algorithm that takes a string S consisting of opening and closing
# parentheses and finds the length of the longest balanced parentheses in S.

# def longest_parentheses(input: str) -> Stack[Tuple[int, str]]:
#   stack : Stack[Tuple[int, str]] = Stack()

#   for idx, char in enumerate(input):
#     match char:
#       case '(':
#         stack.push((idx, char))
#       case ')':
#         if stack.stack is not None and stack.stack.value[1] == '(':
#           _ = stack.pop()
#       case _:
#         raise Exception

#   return stack

# 3.3 Give an algorithm to reverse the direction of a given singly linked list.
# In other words, after the reversal all pointers should now point backwards.
# Your algorithm should take linear time.

def reverse(input: List[a] | None) -> List[a]:

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