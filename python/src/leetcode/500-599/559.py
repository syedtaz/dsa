from typing import Optional, List


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ) -> None:
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:

        if root is None:
            return 0

        acc = 1
        stack = [(root, 1)]

        while stack:
            node, h = stack.pop()
            acc = max(h, acc)

            if node.children is None:
                continue

            for child in node.children:
                stack.append((child, h + 1))

        return acc
