# Definition for singly-linked list.
from nodedef import *

from typing import Optional


def middle(turtle: ListNode, hare: Optional[ListNode]) -> ListNode:
    return (
        turtle
        if hare is None or hare.next is None
        else middle(turtle.next, hare.next.next)  # type: ignore
    )


def reverse(node: Optional[ListNode], acc: Optional[ListNode]) -> ListNode:
    if node is None:
        return acc  # type: ignore

    temp = node.next
    node.next = acc
    return reverse(temp, node)


def merge(left: Optional[ListNode], right: Optional[ListNode]) -> None:
    if right.next is None:
        return

    left.next, temp = right, left.next
    right.next, temp2 = temp, right.next
    return merge(temp, temp2)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        return merge(head, reverse(middle(head, head), None))
