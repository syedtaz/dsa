from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        stack: list[tuple[ListNode, int]] = []
        sum = 0

        while cur is not None:

            if len(stack) > 0 and stack[-1][1] + cur.val == 0:

                value = cur.val

                while stack[-1][1] + value != 0:
                  x, s = stack.pop()
                  sum = s
                  value -= x.val
                continue

            sum += cur.val
            stack.append((cur, sum))
            cur = cur.next

        if len(stack) == 0:
            return None

        acc, _ = stack.pop()
        acc.next = None

        while len(stack) > 0:
            v, _ = stack.pop()
            v.next = acc
            acc = v

        return acc