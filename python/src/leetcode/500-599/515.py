from nodedef import *
from typing import Optional, List
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue: deque[tuple[int, TreeNode]] = deque([(0, root)])
        current_level = 0
        current_max = root.val
        acc: list[int] = []

        while len(queue) > 0:
            level, node = queue.popleft()

            if level > current_level:
                acc.append(current_max)
                current_max = node.val
                current_level = level

            current_max = max(node.val, current_max)

            if node.left is not None:
                queue.append((level + 1, node.left))

            if node.right is not None:
                queue.append((level + 1, node.right))

        return acc + [current_max]
