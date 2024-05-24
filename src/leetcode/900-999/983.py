from typing import List
from functools import cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def next(i: int, k: int) -> int:
            while i <= len(days) - 1 and days[i] < k:
                i = i + 1
            return i

        @cache
        def recurrence(i: int) -> int:
            if i >= len(days):
                return 0

            one = costs[0] + recurrence(next(i, days[i] + 1))
            seven = costs[1] + recurrence(next(i, days[i] + 7))
            thirty = costs[2] + recurrence(next(i, days[i] + 30))
            return min(one, seven, thirty)

        return recurrence(0)
