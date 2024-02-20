from typing import List
from math import inf

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current, cur_max = 0, -inf

        for num in nums:
            current += num
            cur_max = max(current, cur_max)

            if current < 0:
                current = 0

        return int(cur_max)