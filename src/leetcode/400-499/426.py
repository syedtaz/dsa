from typing import Optional


class Node:
    val: int
    left: Optional["Node"]
    right: Optional["Node"]

    def __init__(
        self, val: int, left: Optional["Node"] = None, right: Optional["Node"] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":

        current : Optional[Node] = root
        stack : list[Node] = []
        head : Optional[Node] = None

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
                continue

            if len(stack) > 0:
                current = stack.pop()
                if head is not None:
                    head.right = current
                    current.left = next
                else:









