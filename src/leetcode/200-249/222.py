from nodedef import TreeNode

from typing import Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def find_height(root: TreeNode) -> int:

            curr = root
            acc = 0

            while curr is not None:
                curr = curr.left
                acc += 1

            return acc

        def find_bound(root: TreeNode) -> int:

