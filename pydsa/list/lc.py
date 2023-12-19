from typing import TypeVar, Callable, Optional
from list import List
import list

a = TypeVar('a')
b = TypeVar('b')
L = Optional[List[a]]

# 203: Given the head of a linked list and an integer val, remove all the nodes
# of the linked list that has Node.val == val, and return the new head.

def remove_el(lst: L[int], target: int) -> List[int]:
  g : Callable[[int, L[int]], L[int]] = lambda v, acc: acc if v == target else List(value = v, next = acc)
  return list.fold(lst = lst, f = g, acc = None) # type: ignore
