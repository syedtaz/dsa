from nodedef import ListNode

from typing import Optional

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        curr = head
        acc : ListNode | None = None

        def find(node: ListNode | None, target: int) -> ListNode:


        while curr is not None:

            node = acc

            while node is not None and node.val < curr.val:
                node = node.next




            curr = curr.next