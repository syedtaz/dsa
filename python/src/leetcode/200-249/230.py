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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def fold(node: Optional[TreeNode], acc: list[int]) -> list[int]:
            return (
                acc
                if node is None
                else fold(node.left, acc) + [node.val] + fold(node.right, acc)
            )

        return fold(root, [])[k - 1]
