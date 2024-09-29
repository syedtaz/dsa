from nodedef import *

from typing import List
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue: deque[tuple[int, bool, TreeNode]] = deque([(0, True, root)])
        acc: list[list[int]] = []
        cur: deque[int] = deque([])
        clevel: int = 0

        while len(queue) > 0:
            level, l2r, node = queue.popleft()

            if level > clevel:
                acc.append([x for x in cur])
                cur = deque([])
                clevel = level

            _ = cur.append(node.val) if l2r else cur.appendleft(node.val)

            if node.left is not None:
                queue.append((level + 1, not l2r, node.left))

            if node.right is not None:
                queue.append((level + 1, not l2r, node.right))

        acc.append([x for x in cur])
        return acc
