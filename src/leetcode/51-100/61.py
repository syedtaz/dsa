# Definition for singly-linked list.
from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int, next: Optional["ListNode"]) -> None:
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # 1 -> 2 -> 3 -> 4 -> 5
        # 5 -> 1 -> 2 -> 3 -> 4

        def length(node: Optional[ListNode], acc: int) -> int:
            return acc if node is None else length(node.next, acc + 1)

        if k == 0 or head is None:
            return head

        l = length(head, 0)
        k = k % l

        if k == 0 or k == l:
            return head

        left = head
        right = left

        for _ in range(k):
            right = right.next

        while right.next is not None:
            left, right = left.next, right.next

        nhead = left.next
        left.next = None
        right.next = head

        return nhead

