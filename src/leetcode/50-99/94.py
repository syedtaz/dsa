from nodedef import *
from typing import List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def fold(node: Optional[TreeNode], acc: list[int]) -> list[int]:
            if node is None:
                return acc
            return fold(node.left, acc) + [node.val] + fold(node.right, acc)

        return fold(root, [])