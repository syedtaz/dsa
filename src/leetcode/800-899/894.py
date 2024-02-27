from typing import Optional, List
from functools import cache


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self, val: int, left: Optional["TreeNode"], right: Optional["TreeNode"]
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"({self.val}, ({self.left.__repr__()}), ({self.right.__repr__()}))"

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        @cache
        def f(k: int) -> list[Optional[TreeNode]]:
            if k % 2 == 0:
                return []

            if k == 1:
                return [TreeNode(0, None, None)]

            acc : list[Optional[TreeNode]] = []
            for i in range(1, k):
                acc += f(i)
                acc += f(k - i)

            return acc

        return f(n)

s = Solution()
x = s.allPossibleFBT(7)
print(len(x))