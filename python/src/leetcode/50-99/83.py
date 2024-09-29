from typing import Optional
from nodedef import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        def f(node: Optional[ListNode], prev: ListNode) -> None:
            if node is None:
                return

            if node.val == prev.val:
                prev.next = node.next
                return f(node.next, prev)

            return f(node.next, node)

        f(head.next, head)
        return head

class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        pred = head
        succ = head.next

        while succ is not None:
            if pred.val == succ.val:
                pred.next = succ.next
                succ = succ.next
                continue

            pred = succ
            succ = succ.next

        return head