from typing import List
from functools import cache


class Solution:
    @cache
    def pascal(self, i: int) -> list[int]:
        if i == 0:
            return [1]
        if i == 1:
            return [1, 1]

        prev = self.pascal(i - 1)
        return [1] + [a + b for (a, b) in zip(prev, prev[1:])] + [1]

    def getRow(self, rowIndex: int) -> List[int]:
        return self.pascal(rowIndex)
