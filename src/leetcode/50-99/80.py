from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        def f(i: int, j: int) -> int:
            if j >= len(nums):
                return i

            if nums[i] == nums[j] and nums[i + 1] == nums[j]:
                return f(i, j + 1)

            nums[i + 1] = nums[j]
            return f(i + 1, j + 1)

        return f(0, 0)

s = Solution()
print(s.removeDuplicates(nums = [1,1,1,2,2,3]))