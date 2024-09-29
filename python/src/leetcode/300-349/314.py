from typing import Optional, List
from collections import defaultdict, deque


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


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levels: dict[int, list[int]] = defaultdict(list)
        queue: deque[tuple[int, TreeNode]] = deque([(0, root)])

        while len(queue) > 0:
            level, node = queue.popleft()
            levels[level].append(node.val)

            if node.left is not None:
                queue.append((level - 1, node.left))
            if node.right is not None:
                queue.append((level + 1, node.right))

        acc: list[list[int]] = []
        for key in sorted(levels.keys()):
            acc.append(levels[key])
        return acc
