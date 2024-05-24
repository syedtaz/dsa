# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


from functools import cache


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        @cache
        def depth(node: Optional[TreeNode]) -> int:
            return 0 if node is None else 1 + max(depth(node.left), depth(node.right))

        def diameter(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            through = left + right

            return max(left, right, through)

        return diameter(root)
