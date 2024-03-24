from nodedef import *

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        def f(l: Optional[ListNode], r: Optional[ListNode], i: int, acc: Optional[ListNode]) -> Optional[ListNode]:

            if a <= i <= b and r is not None:
                temp, r.next = r.next, acc
                return f(l, temp, i, r)

            if a <= i <= b and r is None:
                return f(l.next, r, i + 1, acc) if l is not None else acc

            if l is None:
                return acc

            temp, l.next = l.next, acc
            return f(temp, r, i + 1, l)

        def reverse(node: Optional[ListNode], acc: Optional[ListNode]) -> ListNode:
            if node is None:
                return acc

            temp = node.next
            node.next = acc
            return reverse(temp, node)

        return reverse(f(list1, list2, 0, None), None)