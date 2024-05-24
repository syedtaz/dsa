from typing import Optional


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        def f(turtle: Optional[ListNode], hare: Optional[ListNode]) -> bool:
            if turtle == hare:
                return True

            if hare is None or hare.next is None:
                return False

            return f(turtle.next, hare.next.next)

        return f(head, head.next)
