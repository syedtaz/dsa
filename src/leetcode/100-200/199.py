# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(
        self, val: int, left: Optional["TreeNode"], right: Optional["TreeNode"]
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        queue : deque[tuple[TreeNode, int]] = deque([(root, 0)])
        acc : list[int] = []
        cand_level, cand = 0, root

        while len(queue) > 0:
            node, level = queue.popleft()

            if level > cand_level:
                acc.append(cand.val)
                cand_level = level
                cand = node
            else:
                cand = node

            if node.left is not None:
                queue.append((node.left, level + 1))

            if node.right is not None:
                queue.append((node.right, level + 1))

        return acc


