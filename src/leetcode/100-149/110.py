from nodedef import *


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(node: Optional[TreeNode]) -> tuple[bool, int]:
            if node is None:
                return True, -1

            l_balanced, l_height = f(node.left)
            if not l_balanced:
                return False, 0

            r_balanced, r_height = f(node.right)
            if not r_balanced:
                return False, 0

            return abs(l_height - r_height) < 2, 1 + max(l_height, r_height)

        result, _ = f(root)
        return result
