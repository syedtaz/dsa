# Definition for singly-linked list.
from typing import Optional, List
import heapq

class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

class EqListNode(ListNode):

    def __lt__(self, other: 'EqListNode') -> bool:
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        queues : list[EqListNode] = [EqListNode(lst.val, lst.next) for lst in lists if lst is not None]
        heapq.heapify(queues)


        def merge() -> Optional[ListNode]:
            prev = None

            while True:
              if len(queues) == 0:
                  return prev

              v = heapq.heappop(queues)

              if v.next is not None:
                  heapq.heappush(queues, EqListNode(v.next.val, v.next.next))

              v.next = prev
              prev = v

        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = node

            while current is not None:
                next = current.next
                current.next = prev
                prev = current
                current = next

            return prev

        return reverse(merge())
