from dataclasses import dataclass
from typing import NamedTuple
from collections import OrderedDict

# Handwritten doubly linked list

book = NamedTuple('book', [('isbn', int), ('price', int)])

@dataclass
class Node[T]:
  value: T
  prev: 'Node[T] | None'
  next: 'Node[T] | None'

class List[T]:
  head : Node[T] | None
  tail : Node[T] | None
  _length: int

  def __init__(self) -> None:
    self.head, self.tail = None, None
    self._length = 0

  def __len__(self) -> int:
    return self._length

  def _addfirst(self, node: Node[T]) -> None:
    node.prev = node.next = None
    self.head = node
    self.tail = node
    self._length += 1
    return None

  def preprend(self, node: Node[T]) -> None:
    if len(self) == 0:
      return self._addfirst(node)

    assert self.head is not None
    node.next = self.head
    self.head.prev = node
    self.head = node
    self._length += 1
    return None

  def remove(self, node: Node[T]) -> Node[T]:
    if self.head == node:
      self.head = node.next

    if self.tail == node:
      self.tail = node.prev

    if node.prev is not None:
      node.prev.next = node.next

    if node.next is not None:
      node.next.prev = node.prev

    node.prev = node.next = None
    self._length -= 1
    return node

class ISBNCache:
  mapping: dict[int, Node[book]]
  lru: List[book]
  cap: int

  def __init__(self, cap: int = 20) -> None:
    self.lru = List()
    self.mapping = {}
    self.cap = cap

  def _touch(self, node: Node[book]) -> None:
    node = self.lru.remove(node)
    self.lru.preprend(node)

  def lookup(self, isbn: int) -> int:
    node = self.mapping.get(isbn)
    if node is None:
      return -1

    self._touch(node)
    return node.value.price

  def insert(self, isbn: int, price: int) -> None:

    if (retrieved := self.mapping.get(isbn)) is not None:
      self._touch(retrieved)
      return None

    node = Node(book(isbn, price), None, None)
    self.lru.preprend(node)
    self.mapping[isbn] = node

    if len(self.lru) >= self.cap:
      assert self.lru.tail is not None
      rm = self.lru.remove(self.lru.tail)
      self.mapping.pop(rm.value.isbn)

    return None

  def erase(self, isbn: int) -> bool:
    if (node := self.mapping.get(isbn)) is not None:
      self.lru.remove(node)
      self.mapping.pop(isbn)
      return True

    return False

# With ordered dict

class ISBNCacheOD:
  _mapping : OrderedDict[int, int]
  _cap : int

  def __init__(self, cap: int = 20) -> None:
    self._mapping = OrderedDict()
    self._cap = cap

  def insert(self, isbn: int, price: int) -> None:
    if isbn in self._mapping:
      self._mapping[isbn] = self._mapping.pop(isbn)
      return None

    if len(self._mapping) == self._cap:
      self._mapping.popitem(last=False)

    self._mapping[isbn] = price

  def lookup(self, isbn: int) -> int:
    if isbn not in self._mapping:
      return -1

    self._mapping[isbn] = self._mapping.pop(isbn)
    return self._mapping[isbn]

  def erase(self, isbn: int) -> bool:
    return self._mapping.pop(isbn, None) is not None