from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def f(x: int) -> bool:
            return sum([(a + x - 1) // x for a in nums]) <= threshold

        i, j = 1, max(nums)

        while i <= j:
            m = i + (j - i) // 2
            if f(m):
                j = m - 1
            else:
                i = m + 1

        return i
