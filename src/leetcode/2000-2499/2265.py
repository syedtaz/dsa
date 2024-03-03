from typing import Optional

class TreeNode:
    val : int
    left : Optional["TreeNode"]
    right : Optional["TreeNode"]

    def __init__(self, val : int, left : Optional["TreeNode"], right : Optional["TreeNode"]) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def traverse(node: TreeNode) -> int:
            if node.left is None and node.right is None:
                return node.val

            if node.left is None:
                return node.val +