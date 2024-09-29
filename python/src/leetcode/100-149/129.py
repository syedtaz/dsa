from nodedef import TreeNode
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def fold(node: TreeNode | None, acc: int) -> int:
            if node is None:
                return 0

            result = acc * 10 + node.val
            if node.left is None and node.right is None:
                return result

            return fold(node.left, result) + fold(node.right, result)

        return fold(root, 0)
