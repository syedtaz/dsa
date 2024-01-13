from typing import TypeVar, Any, Optional, Callable
from dataclasses import dataclass

a = TypeVar('a')
b = TypeVar('b')

# Singly linked list.
@dataclass
class List[a]():
  value: a
  next: 'List[a] | None'

L = Optional[List[a]]

def fold(lst: List[a] | None, f: Callable[[a, b], b], acc: b) -> b:
  return acc if lst is None else fold(lst = lst.next, f = f, acc = f(lst.value, acc))

def map_aux(lst: List[a] | None, f: Callable[[a], b], acc: List[b] | None) -> List[b] | None:
  return acc if lst is None else map_aux(lst = lst.next, f = f, acc = List(value = f(lst.value), next = acc))

def mapi_aux(lst: List[a] | None, f: Callable[[a, int], b], idx: int, acc: List[b] | None) -> List[b] | None:
  return acc if lst is None else mapi_aux(lst = lst.next, f = f, idx = idx + 1, acc = List(value = f(lst.value, idx), next = acc))

def map(lst: List[a] | None, f: Callable[[a], b]) -> List[b] | None:
  return map_aux(lst, f, None)

def mapi(lst: List[a] | None, f: Callable[[a, int], b]) -> List[b] | None:
  return mapi_aux(lst, f, 0, None)

def filter_aux(lst: List[a] | None, f: Callable[[a], bool], acc: List[a] | None) -> List[a] | None:
  if lst is None:
    return acc
  return filter_aux(lst.next, f, List(value = lst.value, next = acc)) if f(lst.value) else filter_aux(lst.next, f, acc)

def filteri_aux(lst: List[a] | None, f: Callable[[a, int], bool], idx: int, acc: List[a] | None) -> List[a] | None:
  return acc if lst is None else (filteri_aux(
    lst = lst.next, f = f, idx = idx + 1, acc = List(value = lst.value, next = acc))
    if f(lst.value, idx)
    else filteri_aux(lst = lst.next, f = f,idx = idx + 1, acc = acc))

def filter(lst: List[a] | None, f: Callable[[a], bool]) -> List[a] | None:
  return filter_aux(lst, f, None)

def filteri(lst: L[a], f: Callable[[a, int], bool]) -> L[a]:
  return filteri_aux(lst = lst, f = f, idx = 0, acc = None)

def length(lst: L[Any]) -> int:
  return fold(lst = lst, f = lambda _, acc: acc + 1, acc = 0)

def append_aux(left: L[a], right: L[a], acc: L[a]) -> L[a]:
  match left, right:
    case None, None:
      return acc
    case None, b:
      assert b is not None
      return append_aux(left = None, right = b.next, acc = List(value = b.value, next = acc))
    case a, None:
      assert a is not None
      return append_aux(left = a.next, right = None, acc = List(value = a.value, next = acc))
    case a, b:
      assert a is not None
      return append_aux(left = a.next, right = b, acc = List(value = a.value, next = acc))

def append(left: L[a], right: L[a]) -> L[a]:
  return append_aux(left = left, right = right, acc = None)

def reverse(lst: L[a]) -> L[a]:
  return fold(lst, lambda v, acc: List[a](value = v, next = acc), None)

# Finds the node containing a value if it exists.
def search(lst : List[a] | None, k: a) -> List[a] | None:
  return None if lst is None else search(lst.next, k)


