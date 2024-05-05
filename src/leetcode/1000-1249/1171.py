from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        d = {0: dummy}
        prefix_sum = 0

        while head:
            prefix_sum += head.val
            node = d.get(prefix_sum)

            if node:
                curr, _sum = node, prefix_sum

                while curr.next is not head:
                    curr = curr.next
                    _sum += curr.val
                    d.pop(_sum)

                node.next = head.next
            else:
                d[prefix_sum] = head
            head = head.next
        return dummy.next