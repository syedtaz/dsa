from typing import List
from functools import cache

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:

        @cache
        def f(i: int, m: int) -> int:
            if m <= 0:
                return 0
            limit = len(nums) - i - m + 1
            if limit <= 0:
                return 0

            if limit == 1:
                return nums[i]

            acc = None
            sign = (-1) ** (m + 1)
            for j in range(max(0, limit)):
                cur = sum(nums[i:i+j]) + f(j, m - 1)
                if sign > 0:
                  acc = max(cur, acc) if acc is not None else cur
                else:
                  acc = min(cur, acc) if acc is not None else cur

            return 0 if acc is None else acc

        return f(0, k)

s = Solution()
print(s.maximumStrength([-99, 85],1))