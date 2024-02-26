from typing import Optional


class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def length(node: Optional[ListNode], acc: int) -> int:
            return acc if node is None else length(node.next, acc + 1)

        def iter(node: Optional[ListNode], n: int) -> Optional[ListNode]:
            return node if (n == 0 or node is None) else iter(node.next, n - 1)

        def build(
            node: Optional[ListNode], target: Optional[ListNode], acc: list[int]
        ) -> list[int]:
            if node is None or node == target:
                return acc

            return build(
                node.next,
                target,
                acc + [node.val] if target is not None else [node.val] + acc,
            )

        l = length(head, 0)
        l = l // 2 if l % 2 == 0 else l // 2 + 1
        right = iter(head, l)
        x = build(head, right, [])
        y = build(right, None, [])

        return x == y
