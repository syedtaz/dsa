from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        left, right = 0, len(nums) - 1

        while left < right:
            match nums[left] % 2 == 0, nums[right] % 2 == 1:
                case (True, True):
                    left, right = left + 1, right - 1
                case (False, False):
                    nums[left], nums[right] = nums[right], nums[left]
                    left, right = left + 1, right - 1
                case (True, False):
                    left = left + 1
                case (False, True):
                    right = right - 1
                case _:
                    assert False

        return nums
