from typing import List
from bisect import bisect_left
from functools import cache


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit)), key=lambda x: x[0])

        @cache
        def f(i: int) -> int:
            if i >= len(jobs):
                return 0

            _, end, prof = jobs[i]
            nexti = bisect_left(jobs, end, lo=i, key=lambda x: x[0])
            return max(f(i + 1), prof + f(nexti))

        return f(0)