from nodedef import ListNode
from typing import Optional


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode | None) -> ListNode | None:
            curr, prev = node, None

            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        def monotonic(node: ListNode | None) -> ListNode | None:
            curr = node

            while curr is not None:
                while curr.next is not None and curr.next.val < curr.val:
                    curr.next = curr.next.next
                curr = curr.next

            return node

        return reverse(monotonic(reverse(head)))
