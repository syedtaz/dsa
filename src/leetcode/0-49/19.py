# Definition for singly-linked list.
from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return None

        cur = head
        prev = head

        for _ in range(n):
            cur = cur.next

        while cur is not None and cur.next is not None:
            cur, prev = cur.next, prev.next

        prev.next = prev.next.next

        return head
