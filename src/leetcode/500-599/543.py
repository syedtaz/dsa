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


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depth(node: Optional[TreeNode], acc: int) -> int:
            return acc if node is None else 1 + max(depth(node.left, acc), depth(node.right, acc))



        def diameter(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            through = depth(node.left, 0) + depth(node.right, 0)
            left = diameter(node.left)
            right = diameter(node.right)

            return max(through, left, right)

        return diameter(root)