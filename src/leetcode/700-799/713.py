from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        acc = 1
        prefs = [acc := acc * x for x in nums]
        print(prefs)
        return 0


s = Solution()
print(s.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
