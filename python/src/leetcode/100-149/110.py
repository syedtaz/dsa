from nodedef import TreeNode
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(node: Optional[TreeNode]) -> tuple[bool, int]:
            if node is None:
                return True, -1

            left_balanced, left_height = f(node.left)
            right_balanced, right_height = f(node.right)

            if not left_balanced or not right_balanced:
                return False, 0

            return abs(left_height - right_height) < 2, 1 + max(
                left_height, right_height
            )

        result, _ = f(root)
        return result
