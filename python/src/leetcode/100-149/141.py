from typing import Optional
from nodedef import ListNode


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

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        turtle, hare = head, head.next

        while turtle != hare:
            if hare is None or hare.next is None:
                return False

            turtle, hare = turtle.next, hare.next.next # type: ignore

        return True