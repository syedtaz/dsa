from typing import List
from random import choice


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def swap(i: int, j: int) -> None:
            nums[i], nums[j] = nums[j], nums[i]
            return None

        def partition(left: int, right: int, pivot: int) -> int:
            swap(pivot, right)
            l = -1

            for i in range(0, right - 1):
                if nums[i] < nums[right]:
                    l += 1
                    swap(l, i)

            swap(right, l + 1)
            return l + 1

        def quickselect(left: int, right: int, target: int) -> int:
            if left == right:
                return nums[left]

            pivot = partition(left, right, choice(range(left, right + 1)))
            if target < pivot:
                return quickselect(left, pivot - 1, target)
            elif target > pivot:
                return quickselect(pivot + 1, right, target - pivot)
            else:
                return nums[pivot]

        print(nums)
        v = quickselect(0, len(nums) - 1, k)
        print(nums)
        return v


s = Solution()
print(s.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=4))
