from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        pref = 0
        prefix = [pref := pref + x for x in nums]
        counts : dict[int, int] = defaultdict(int)

        acc = 0
        for x in prefix:
            counts[x] += 1
            if x == goal:
                acc += 1
            if x - goal in counts:
                acc += counts[x - goal]

        return acc

# s = Solution()
# print(s.numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))