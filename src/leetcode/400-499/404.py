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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        def fold(node: TreeNode, acc: int) -> int:

            right = fold(node.right, acc) if node.right is not None else 0
            if node.left is not None and leaf(node.left):
                left = acc + node.left.val
            elif node.left is not None:
                left = fold(node.left, acc)
            else:
                left = 0

            return right + left

        return fold(root, 0) if root is not None else 0
