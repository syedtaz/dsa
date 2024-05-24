from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        i = 0
        j = 1

        while i < j and j <= len(nums) - 1:
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1
            elif nums[i] == 0 and nums[j] == 0:
                j = j + 1
            elif nums[i] != 0 and nums[j] != 0:
                i, j = i + 1, j + 1
            else:
                i, j = i + 1, j + 1
        return None
