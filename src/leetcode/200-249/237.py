# Definition for singly-linked list.
from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        temp = node.next
        node.val = node.next.val
        node.next = node.next.next
        del temp
