from nodedef import *

node = Optional[ListNode]


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def merge(left: node, right: node, acc: node) -> tuple[node, node]:
            if left is None and right is None:
                return acc, None

            if left is None:
                return acc, right

            if right is None:
                return acc, left

            if left.val <= right.val:
                temp = left.next
                left.next = acc
                return merge(temp, right, left)
            else:
                temp = right.next
                right.next = acc
                return merge(left, temp, right)

        def reverse(n: node, acc: node) -> node:
            if n is None:
                return acc
            temp = n.next
            n.next = reverse(temp, acc)
            return n

        a, leftover = merge(list1, list2, None)
        a = reverse(a, None)

        if leftover is None:
            return a
