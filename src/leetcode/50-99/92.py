from nodedef import *

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def reverse_until(start: Optional[ListNode], j: int) -> None:
            prev = None
            cur = start
            i = 0

            while i != j:
                temp = cur.next
                cur.next = prev
                cur = temp
                prev = cur

        reverse_until(head, left)
        return head