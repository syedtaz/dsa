from typing import TypeVar, Optional, Any
from dataclasses import dataclass
from list import List
import list

a = TypeVar('a')

@dataclass
class DList[a]():
  left: Optional[List[a]]
  right: Optional[List[a]]

def empty() -> DList[Any]:
  return DList(left = None, right = None)

def is_empty(queue: DList[Any]) -> bool:
  return queue.left is None

# Maintains invariant that left list is only empty when the queue is empty.
def checkf(queue: DList[a]) -> DList[a]:
  match queue.left, queue.right:
    case None, x:
      return DList[a](left = list.reverse(x), right=None)
    case _:
      return queue

def head(queue: DList[a]) -> a | None:
  return None if queue.left is None else queue.left.value

def tail(queue: DList[a]) -> DList[a] | None:
  return None if queue.left is None else checkf(DList[a](left = queue.left.next, right=queue.right))

def snoc(queue: DList[a], v: a) -> DList[a]:
  return checkf(DList[a](left = queue.left, right=List[a](value = v, next = queue.right)))