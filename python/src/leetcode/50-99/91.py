from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        maps: set[str] = {str(x) for x in range(1, 27)}
        nums: list[str] = list(s)

        @cache
        def f(i: int) -> int:
            if i == len(nums):
                return 1

            if nums[i] == "0":
                return 0

            if i == len(nums) - 1:
                return 1

            acc = f(i + 1)

            if "".join(nums[i : i + 2]) in maps:
                acc += f(i + 2)

            return acc

        return f(0)
