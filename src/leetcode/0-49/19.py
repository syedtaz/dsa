# Definition for singly-linked list.
from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def length(node: Optional[ListNode]) -> int:
            acc = 0

            while node is not None:
                node, acc = node.next, acc + 1

            return acc

        def advance(node: ListNode, k: int) -> ListNode:
            cur, nxt = node, node.next

            while nxt is not None and k > 1:
                cur, nxt, k = cur.next, nxt.next, k - 1

            return cur

        match (k := length(head) - n) <= 0:
            case True:
                return None if k < 0 else head.next
            case False:
                x = advance(head, k)
                x.next = x.next.next
                return head
