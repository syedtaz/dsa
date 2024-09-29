from nodedef import ListNode
from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = ListNode(0, None)
        head = sentinel

        while list1 or list2:
            if list1 is None:
                head.next = list2
                break

            if list2 is None:
                head.next = list1
                break

            assert list1 is not None and list2 is not None

            if list1.val <= list2.val:
                temp = list1.next
                list1.next = None
                head.next = list1
                head = head.next
                list1 = temp
            else:
                temp = list2.next
                list2.next = None
                head.next = list2
                head = head.next
                list2 = temp

        return sentinel.next
