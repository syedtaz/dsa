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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def f(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None

            node.left, node.right = f(node.right), f(node.left)
            return node

        return f(root)