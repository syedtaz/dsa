from nodedef import ListNode
from typing import Optional


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        sentinel = ListNode(0, head)
        curr = sentinel

        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
                continue

            curr = curr.next

        return sentinel.next
