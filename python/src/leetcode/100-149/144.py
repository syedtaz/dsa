from nodedef import TreeNode
from typing import Optional, List

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        acc : list[int] = []
        stack : list[TreeNode | None] = [root]

        while len(stack) > 0:
            node = stack.pop()

            if node is None:
                continue

            acc.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return acc