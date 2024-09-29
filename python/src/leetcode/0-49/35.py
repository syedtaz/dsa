from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def f(i: int, j: int) -> int:
            if i > j:
                return j
            mid = i + ((j - i) // 2)
            v = nums[mid]
            if v == target:
                return mid
            if v > target:
                return f(i, mid - 1)
            else:
                return f(mid + 1, j)

        return f(0, len(nums) - 1)
