from nodedef import *
from typing import List, Optional
from functools import cache


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def f(numbers: frozenset[int]) -> list[TreeNode | None]:
            if len(numbers) == 0:
                return [None]

            acc: list[TreeNode | None] = []

            for number in numbers:
                pivot = number
                lesser: frozenset[int] = frozenset([x for x in numbers if x < pivot])
                greater: frozenset[int] = frozenset([x for x in numbers if x > pivot])

                for left in f(lesser):
                    for right in f(greater):
                        acc.append(TreeNode(val=pivot, left=left, right=right))

            return acc

        return f(frozenset([x for x in range(1, n + 1)]))
