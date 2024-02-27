from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()

        i, j, flip = 0, len(nums) - 1, True

        while i <= j:
            if flip:
                i, flip = i + 1, not flip
                continue

            nums[i], nums[j] = nums[j], nums[i]
            i, j, flip = i + 1, j - 1, not flip

        print(nums)

s = Solution()
s.wiggleSort(nums = [3,5,2,1,6,4])
# 6 >= 2 <= 5 >= 4 <= 3 >= 1