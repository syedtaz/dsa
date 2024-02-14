# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue: deque[tuple[int, TreeNode]] = deque([(0, root)])
        level = 0
        acc: list[list[int]] = []
        cur: list[int] = []

        while len(queue) > 0:
            clevel, node = queue.popleft()
            if clevel != level:
                acc.append(cur)
                cur = []
                level = clevel

            cur.append(node.val)
            if node.left is not None:
                queue.append((clevel + 1, node.left))
            if node.right is not None:
                queue.append((clevel + 1, node.right))

        if len(cur) > 0:
            acc.append(cur)

        return acc
