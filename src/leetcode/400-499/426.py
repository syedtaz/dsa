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

        def fold(node: "Optional[Node]", acc: list["Node"]) -> list["Node"]:
            if node is None:
                return acc

            return fold(node.left, acc) + [node] + fold(node.right, acc)

        result = fold(root, [])
        head, tail = result[0], result[-1]

        for (l, r) in zip(result, result[1:]):
            l.right = r
            r.left = l

        head.left = tail
        tail.right = head
        return head









