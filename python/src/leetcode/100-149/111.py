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


from sys import maxsize


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def fold(node: TreeNode, acc: int) -> int:
            if node.left is None and node.right is None:
                return acc + 1

            left = fold(node.left, acc + 1) if node.left is not None else maxsize
            right = fold(node.right, acc + 1) if node.right is not None else maxsize
            return min(left, right)

        return fold(root, 0)
