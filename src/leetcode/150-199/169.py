from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ch, count = nums[0], 1

        for n in nums[1:]:
            if count == 0:
                ch = n
            count += 1 if ch == n else -1

        return ch
