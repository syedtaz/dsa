# Definition for singly-linked list.
from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(
        self,
        val: int = 0,
        next: Optional["ListNode"] = None,
    ) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def f(node: Optional[ListNode], acc: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return acc

            return f(node.next, ListNode(node.val, acc))

        return f(head, None)
