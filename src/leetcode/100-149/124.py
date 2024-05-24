from typing import Optional
from math import inf


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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        acc = -inf

        def traverse(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)

            nonlocal acc
            acc = max(acc, left + right + node.val)

            return max(left + node.val, right + node.val)

        traverse(root)
        return int(acc)
