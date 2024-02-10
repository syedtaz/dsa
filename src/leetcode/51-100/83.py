from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int, next: Optional["ListNode"]) -> None:
        self.val = val
        self.next = next


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
