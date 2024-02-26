from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        choices : list[str] = []

        for num in nums:
            choices.append(str(num))

        choices.sort(reverse=True)
        return "".join(choices)