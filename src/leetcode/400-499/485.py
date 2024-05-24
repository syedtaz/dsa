from typing import List
from itertools import groupby


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(
            [len(list(counts)) for group, counts in groupby(nums) if group == 1],
            default=0,
        )


s = Solution()
print(s.findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))
