# Definition for a Node.
from typing import Optional


class Node:
    val: int
    next: Optional["Node"]

    def __init__(self, val: int = None, next=None) -> None:  # type: ignore
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        if head is None:
            v = Node(val=insertVal, next=None)
            v.next = v
            return v

        if head.next is None and head.val >= insertVal:
            return Node(val=insertVal, next=head)

        if head.next is None and head.val < insertVal:
            head.next = Node(val=insertVal, next=head)
            return head

        def f(i: Node, j: Node) -> Node:
            print(f"{i.val} and {j.val}")
            if i.val > j.val and (insertVal >= i.val or insertVal <= j.val):
                i.next = Node(val=insertVal, next=j)
                return head

            if i.val <= insertVal <= j.val:
                i.next = Node(val=insertVal, next=j)
                return head

            assert i.next is not None and j.next is not None
            return f(i.next, j.next)

        assert head is not None and head.next is not None
        return f(head, head.next)
