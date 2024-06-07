from nodedef import TreeNode

# =================
from typing import Optional
from functools import cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def f(node: TreeNode | None) -> int:
            if node is None:
                return 0

            if node.left is None and node.right is None:
                return node.val

            no = f(node.left) + f(node.right)

            yes = node.val

            if node.left is not None:
                yes += f(node.left.right) + f(node.left.left)

            if node.right is not None:
                yes += f(node.right.left) + f(node.right.right)

            return max(yes, no)

        return f(root)