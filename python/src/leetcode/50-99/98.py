from nodedef import TreeNode
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        acc: list[int] = []
        stack: list[TreeNode] = []
        curr: TreeNode | None = root

        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            acc.append(curr.val)
            curr = curr.right

        return all([a < b for a, b in zip(acc, acc[1:])])