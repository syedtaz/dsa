from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        i = 0
        while True:
            if i == nums[i]:
                break
            j = nums[i]
            nums[i] = i
            i = j

        return i