# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self, val: int, left: Optional["TreeNode"], right: Optional["TreeNode"]
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def fold(node: TreeNode, acc: str) -> str:
            if node.left is None and node.right is not None:
                return str(node.val) + "()" + "(" + fold(node.right, acc) + ")"

            if node.left is not None and node.right is None:
                return str(node.val) + "(" + fold(node.left, acc) + ")"

            if node.left is not None and node.right is not None:
                return (
                    str(node.val)
                    + "("
                    + fold(node.left, acc)
                    + ")"
                    + "("
                    + fold(node.right, acc)
                    + ")"
                )

            return str(node.val)

        return fold(root, "") if root is not None else ""
