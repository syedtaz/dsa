from nodedef import *

from typing import Optional


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def fold(
            node: Optional[TreeNode],
            acc: int,
            gp: Optional[int],
            parent: Optional[int],
        ) -> int:
            if node is None:
                return acc

            to_add = node.val if gp is not None and gp % 2 == 0 else 0

            return (
                fold(node.left, acc, parent, node.val)
                + to_add
                + fold(node.right, acc, parent, node.val)
            )

        return fold(root, 0, None, None)
