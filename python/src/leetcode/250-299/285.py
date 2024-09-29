from nodedef import TreeNode
from typing import Optional


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        candidate = None
        curr = root

        while curr is not None:
            if curr.val <= p.val:
                curr = curr.right
            else:
                candidate = curr
                curr = curr.left

        return candidate
