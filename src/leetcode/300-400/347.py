from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items = [(k, v) for k, v in Counter(nums).items()]

        def partition(i: int, j: int) -> int:
            pivot = nums[j]
            l = 0

            for i in range(0, j):
                if nums[i] <= pivot:
                    nums[i], nums[l] = nums[l], nums[i]
                    l = l + 1

            nums[l], nums[j] = nums[j], nums[l]
            return l

        def quickselect(i: int, j: int, k: int) -> int:
            pivot = partition(i, j)
            if

        x = partition(0, len(nums) - 1)
        print(nums)
        print(x)

        return []

s = Solution()
print(s.topKFrequent(nums = [2,2,3,1,1,3], k = 3))
