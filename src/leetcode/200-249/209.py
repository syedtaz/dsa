from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def f(i: int, j: int, sum: int, length: int) -> int:
            if sum >= target:
                print(f"{sum} and i = {i} and j = {j} and length = {length}")
                return length

            if i < 0 and j >= len(nums) and sum < target:
                return 0

            prev = 0 if i < 0 else nums[i]
            next = 0 if j >= len(nums) else nums[j]
            return (
                f(i, j + 1, sum + next, length + 1)
                if next >= prev
                else f(i - 1, j, sum + prev, length + 1)
            )

        v = max(nums)
        idx = nums.index(v)
        return f(i=idx - 1, j=idx + 1, sum=v, length=1)


s = Solution()
print(s.minSubArrayLen(target=213, nums=[12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]))
