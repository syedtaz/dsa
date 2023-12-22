from typing import Optional, Callable, TypeVar

# Mutable binary search trees.

class BST():
  value: int
  left: 'Optional[BST]'
  right: 'Optional[BST]'

  def __init__(self, value: int, left: "Optional[BST]", right:" Optional[BST]"):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self) -> str:
    return f"Node(value={self.value}, left={str(self.left)}, right={str(self.right)})"

t = Optional[BST]
a = TypeVar('a')
b = TypeVar('b')

def fold(node: t, f: Callable[[int, b, b], b], acc: b) -> b:
  return acc if node is None else f(node.value, fold(node.left, f, acc), fold(node.right, f, acc))

def search(node: t, v: int) -> t:
  if node is None:
    return None

  if node.value == v:
    return node

  return search(node.left, v) if v < node.value else search(node.right, v)

def search_wparent(node: t, parent: t, v: int) -> tuple[t, t]:
  if node is None:
    return None, None

  if node.value == v:
    return node, parent

  return search_wparent(node.left, node, v) if v < node.value \
    else search_wparent(node.right, node, v)

def minimum(root: t, acc: int | None = None) -> int | None:
  return acc if root is None else minimum(root.left, acc = root.value)

def insert(node: BST, v: int) -> None:
  match (v < node.value, node.left, node.right):
    case (True, None, _):
      node.left = BST(value = v, left = None, right = None)
      return None
    case (True, left, _):
      return insert(left, v) # type: ignore
    case (False, _, None):
      node.right = BST(value = v, left = None, right = None)
      return None
    case (False, _, right):
      return insert(right, v)

def successor(n: BST) -> BST:
    return n if n.left is None else successor(n.left)

def swap(n : BST, p: BST, v: t) -> None:
  if n == p.left:
    p.left = v
  else:
    p.right = v
  del n

def delete(root: BST, v: int) -> None:
  node, parent = search_wparent(root, None, v)

  if node is None:
    return None

  assert parent is not None
  match (node.left, node.right):
    case (None, None):
      swap(node, parent, None)
    case (child, None) | (None, child):
      swap(node, parent, child)
    case (_childl, childr):
      succ = successor(childr)
      temp = succ.value
      delete(node, temp)
      node.value = temp

  return None