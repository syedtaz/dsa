from nodedef import *

from typing import List
from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        queue : deque[tuple[int, TreeNode]] = deque([(0, root)])
        acc: list[list[int]] = []
        current_level = 0
        current : list[int] = []

        while len(queue) > 0:
            level, node = queue.popleft()

            if level > current_level:
                acc.append(current)
                current = []
                current_level = level

            current.append(node.val)

            if node.left is not None:
                queue.append((level + 1, node.left))

            if node.right is not None:
                queue.append((level + 1, node.right))

        acc.append(current)
        return acc[::-1]
