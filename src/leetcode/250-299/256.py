from typing import List
from functools import cache


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        @cache
        def recurrence(i: int, prev: int) -> int:
            if i >= len(costs):
                return 0

            match prev:
                case 0:
                    return min(
                        costs[i][1] + recurrence(i + 1, 1),
                        costs[i][2] + recurrence(i + 1, 2),
                    )
                case 1:
                    return min(
                        costs[i][0] + recurrence(i + 1, 0),
                        costs[i][2] + recurrence(i + 1, 2),
                    )
                case 2:
                    return min(
                        costs[i][0] + recurrence(i + 1, 0),
                        costs[i][1] + recurrence(i + 1, 1),
                    )
                case _:
                    assert False

        return min(recurrence(0, 0), recurrence(0, 1), recurrence(0, 2))
