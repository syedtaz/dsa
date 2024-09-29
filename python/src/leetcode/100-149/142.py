from nodedef import ListNode

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle = head
        hare = head

        while hare is not None and hare.next is not None:
            hare = hare.next.next
            turtle = turtle.next  # type: ignore

            if hare == turtle:
                break

        if hare is None or hare.next is None:
            return None

        hare = head

        while turtle != hare:
            hare = hare.next
            turtle = turtle.next

        return turtle