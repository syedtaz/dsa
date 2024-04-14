from nodedef import *
from typing import List


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def fold(node: Optional[TreeNode], acc: list[int]) -> list[int]:
            return (
                acc
                if node is None
                else fold(node.left, acc) + fold(node.right, acc) + [node.val]
            )

        return fold(root, [])
