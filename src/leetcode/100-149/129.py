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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        acc: list[str] = []

        def dfs(node: TreeNode, prev: str) -> None:
            if node.left is None and node.right is None:
                acc.append(prev + str(node.val))
                return

            if node.left is not None:
                dfs(node.left, prev + str(node.val))
            if node.right is not None:
                dfs(node.right, prev + str(node.val))

            return

        dfs(root, "")
        return sum([int(x) for x in acc])
