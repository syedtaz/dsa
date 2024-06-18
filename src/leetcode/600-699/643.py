from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        acc : int = 0

        for i in range(k):
            acc += nums[i]

        curr = acc

        for i in range(k, len(nums)):
            curr +=  nums[i] - nums[i - k]
            acc = max(acc, curr)

        return acc / k