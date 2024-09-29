from typing import Optional, List


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return [0.0]

        queue: deque[tuple[int, TreeNode]] = deque([(0, root)])
        acc: list[float] = []
        cur_level: int = 0
        cur_value: int = 0
        cur_n: int = 0

        while len(queue) > 0:
            level, node = queue.popleft()

            if level != cur_level:
                acc.append(cur_value / cur_n)
                cur_value, cur_n, cur_level = 0, 0, level

            cur_value += node.val
            cur_n += 1

            if node.left is not None:
                queue.append((level + 1, node.left))

            if node.right is not None:
                queue.append((level + 1, node.right))

        acc.append(cur_value / cur_n)

        return acc
