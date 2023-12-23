from typing import Optional, Callable

class TreeNode:
    val : int
    left : 'Optional[TreeNode]'
    right : 'Optional[TreeNode]'

    def __init__(self, val: int =0, left: 'Optional[TreeNode]' =None, right: 'Optional[TreeNode]' =None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    T = Optional[TreeNode]
    F = Callable[[int, int, int], int]

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def fold(node: Solution.T, f : Solution.F, acc: int) -> int:
          return acc if node is None else f(node.val, fold(node.left, f, acc), fold(node.right, f, acc))

        f : Solution.F = lambda v, l, r: v + l + r if low <= v <= high else l + r
        return fold(root, f, 0)