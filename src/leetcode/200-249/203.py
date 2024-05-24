from nodedef import *


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def remove(start: Optional[ListNode]) -> Optional[ListNode]:
            node, acc = start, None
            while True:
                if node is None:
                    return acc

                if node.val == val:
                    node = node.next
                    continue

                temp = node.next
                node.next = acc
                node, acc = temp, node
                continue

        def reverse(start: Optional[ListNode]) -> Optional[ListNode]:
            node, acc = start, None
            while True:
                if node is None:
                    return acc

                temp = node.next
                node.next = acc
                node, acc = temp, node

        return reverse(remove(head))
