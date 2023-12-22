from pydsa.bst.bst import BST
import pydsa.bst.bst as bst
from typing import Callable

# 12.1-4 Give recursive algorithms that perform preorder and postorder tree walks in
# time on a tree of nodes.

foldt = Callable[[int, list[int], list[int]], list[int]]
foldint = Callable[[int, int, int], int]

def postorder(tree: bst.t) -> list[int]:
  f : foldt = lambda v, l, r: l + r + [v]
  return bst.fold(tree, f, [])

def preorder(tree: bst.t) -> list[int]:
  f : foldt = lambda v, l, r: [v] + l + r
  return bst.fold(tree, f, [])

# 12.1-3 Give a nonrecursive algorithm that performs an inorder tree walk.
# (Hint: An easy solution uses a stack as an auxiliary data structure. A more
# complicated, but elegant, solution uses no stack but assumes that you can
# test two pointers for equality.)

def stackless_inorder(tree: bst.t) -> list[int]:
  cur = tree
  acc : list[int] = []

  while cur is not None:
    if cur.left is None:
      acc.append(cur.value)
      cur = cur.right
    else:
      x = cur.left
      while x.right is not None and x.right != cur:
        x = x.right
      if x.right == cur:
        x.right = None
        acc.append(cur.value)
        cur = cur.right
      else:
        x.right = cur
        cur = cur.left

  return acc

# 12.2-2. Write recursive versions of TREE-MINIMUM and TREE-MAXIMUM.
def minimum(tree: BST) -> int:
  def min_aux(tree: bst.t, acc: int) -> int:
    return acc if tree is None else min_aux(tree.left, tree.value)
  return min_aux(tree, tree.value)

def maximum(tree: BST) -> int:
  def max_aux(tree: bst.t, acc: int) -> int:
    return acc if tree is None else max_aux(tree.right, tree.value)
  return max_aux(tree, tree.value)

# 12.2-3 Write the TREE-PREDECESSOR procedure