from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def f(i: int, j: int, acc: list[tuple[int, int]]) -> list[str]:
            if i >= len(nums):
                return [f"{nums[a]}->{nums[b]}" if a != b else f"{nums[a]}" for a, b in acc]

            if j >= len(nums):
                return f(j, j + 1, acc + [(i, j - 1)])

            if nums[j - 1] + 1 == nums[j]:
                return f(i, j + 1, acc)
            else:
                return f(j, j + 1, acc + [(i, j - 1)])

        return f(0, 1, [])


# s = Solution()
# print(s.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
