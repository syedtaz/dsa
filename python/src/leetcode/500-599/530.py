from typing import Optional
import sys


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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def fold(node: Optional[TreeNode], acc: list[int]) -> list[int]:
            return (
                acc
                if node is None
                else fold(node.left, acc) + [node.val] + fold(node.right, acc)
            )

        result = fold(root, [])
        acc = sys.maxsize
        for x, y in zip(result, result[1:]):
            acc = min(acc, y - x)
        return acc
