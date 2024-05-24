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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def fold(node: TreeNode, acc: int) -> bool:
            if node.left is None and node.right is None:
                return acc + node.val == targetSum

            left = fold(node.left, acc + node.val) if node.left is not None else False
            right = (
                fold(node.right, acc + node.val) if node.right is not None else False
            )

            return left or right

        return fold(root, 0)
