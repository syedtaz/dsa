from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen : set[int] = set(nums)
        acc : int = 0

        def streak(number: int) -> int:
            acc = 1

            while number + 1 in seen:
                number, acc = number + 1, acc + 1

            return acc

        for num in seen:
            # Beginning of the sequence
            if num - 1 not in seen:
                acc = max(acc, streak(number=num))

        return acc