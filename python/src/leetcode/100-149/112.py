from nodedef import TreeNode
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def fold(node: TreeNode | None, acc: int) -> bool:
            if node is None:
                return False

            if node.left is None and node.right is None:
                return node.val == acc

            return fold(node.left, acc - node.val) or fold(node.right, acc - node.val)

        return fold(root, targetSum)