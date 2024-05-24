from nodedef import *
from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue: deque[tuple[int, TreeNode]] = deque([(1, root)])
        max_sum, min_level = root.val, 1
        cur_sum, cur_level = root.val, 1

        def flush() -> None:
            nonlocal max_sum, min_level
            if cur_sum > max_sum:
                max_sum = cur_sum
                min_level = cur_level

        while len(queue) > 0:
            level, node = queue.popleft()

            if level > cur_level:
                flush()
                cur_level, cur_sum = level, 0

            cur_sum += node.val

            if node.left is not None:
                queue.append((level + 1, node.left))

            if node.right is not None:
                queue.append((level + 1, node.right))

        flush()
        return min_level
