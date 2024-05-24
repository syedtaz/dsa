from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def f(left: ListNode, right: Optional[ListNode]) -> ListNode:
            return (
                left
                if right is None
                else (left.next if right.next is None else f(left.next, right.next))
            )

        return f(head, head.next)
