# 3.11 Design a dictionary data structure in which search, insertion, and
# deletion can all be processed in O(1) time in the worst case. You may assume
# the set elements are integers drawn from a finite set 1, 2, .., n, and
# initialization can take O(n) time.
import pydsa.bst.bst as bst

# from pydsa.bst.bst import BST
from typing import Callable


class ConstDict:
    store: list[bool]

    def __init__(self, n: int):
        self.store = [False] * n

    def __str__(self) -> str:
        return str(self.store)

    def search(self, k: int) -> int | None:
        return k if self.store[k] else None

    def insert(self, k: int) -> None:
        self.store[k] = True

    def delete(self, k: int) -> None:
        self.store[k] = False


# 3.12 The maximum depth of a binary tree is the number of nodes on the path
# from the root down to the most distant leaf node. Give an O(n) algorithm
# to find the maximum depth of a binary tree with n nodes.


def depth(tree: bst.t) -> int:
    height: Callable[[int, int, int], int] = lambda _, l, r: 1 + max(l, r)
    return bst.fold(tree, height, 0)


# 3.13 Two elements of a binary search tree have been swapped by mistake. Give an
# O(n) algorithm to identify these two elements so they can be swapped back.


def fswap(tree: bst.t) -> tuple[int, int]:
    inorder: Callable[[int, list[int], list[int]], list[int]] = (
        lambda v, l, r: l + [v] + r
    )
    lst = bst.fold(tree, inorder, [])
    x, y = None, None

    for left, right in zip(lst, lst[1:]):
        if left > right:
            y = right
            if x is None:
                x = left
            else:
                break

    assert x is not None and y is not None
    return (x, y)
