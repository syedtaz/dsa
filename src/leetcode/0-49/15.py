from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results: list[list[int]] = []

        def skip(i: int, j: int) -> int:
            while nums[i] == nums[i - 1] and i < j:
                i += 1
            return i

        def two_sum(i: int, j: int, target: int) -> None:

            while i < j:

                s = nums[i] + nums[j]
                diff = s - target
                if diff > 0:
                    j = j - 1
                elif diff < 0:
                    i = i + 1
                else:
                    nonlocal results
                    results.append([-target, nums[i], nums[j]])
                    i = skip(i + 1, j)

        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue

            two_sum(idx + 1, len(nums) - 1, -num)

        return results
