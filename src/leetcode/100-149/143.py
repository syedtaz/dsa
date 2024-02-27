# Definition for singly-linked list.
from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next.__repr__()}"


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None or head.next is None:
            return

        def length(node: Optional[ListNode], acc: int) -> int:
            return acc if node is None else length(node.next, acc + 1)

        def nth(node: Optional[ListNode], n: int) -> Optional[ListNode]:
            if node is None:
                return None

            return node if n == 0 else nth(node.next, n - 1)

        def reverse(node: Optional[ListNode]) -> None:
            if node is None or node.next is None:
                print(node)
                return None

            l = reverse(node.next)
            node.next.next = node
            node.next = None
            return l


s = Solution()
s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))
