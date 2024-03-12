from typing import Optional

class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class TreeNode:
    val: int
    left: Optional["ListNode"]
    right: Optional["ListNode"]

    def __init__(
        self,
        val: int = 0,
        left: Optional["ListNode"] = None,
        right: Optional["ListNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

def middle(node: ListNode) -> ListNode:
    turtle = node
    hare = node.next

    while hare is not None:
        turtle = turtle.next # type: ignore
        hare = hare.next.next # type: ignore

    assert turtle is not None
    return turtle

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def convert(node: ListNode)

