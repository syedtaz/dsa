from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        acc, i, curr = 0, 0, 0

        for j, num in enumerate(nums):
            curr += num - nums[i]

            while curr > k:
                curr -= num - nums[i]
                i += 1

            acc = max(acc, j - i + 1)

        return acc
