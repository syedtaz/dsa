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

        S = ListNode(-101, head)
        node: Optional[ListNode] = head
        prev = S

        def skip(node: ListNode) -> ListNode:
            return (
                node
                if node.next is None or node.val != node.next.val
                else skip(node.next)
            )

        def traverse(node: Optional[ListNode], prev: ListNode) -> None:
            if node is None:
                return

            if node.next is not None and node.val == node.next.val:
                n = skip(node)
                prev.next = n.next
                return traverse(n, prev)

            return traverse(node.next, prev)

        traverse(node, prev)
        return S.next
