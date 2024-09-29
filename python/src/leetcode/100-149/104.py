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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def fold(node: Optional[TreeNode], acc: int) -> int:
            return (
                acc
                if node is None
                else max(fold(node.left, acc), fold(node.right, acc)) + 1
            )

        return fold(root, 0)
