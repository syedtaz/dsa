from typing import List
from functools import cache


class Solution:
    def countBits(self, n: int) -> List[int]:
        @cache
        def recurrence(i: int) -> int:
            if i <= 1:
                return i

            return recurrence(i // 2) + (1 if i % 2 == 1 else 0)

        return [recurrence(i) for i in range(0, n + 1)]
