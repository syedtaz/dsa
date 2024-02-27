from typing import List

class AugmentedString(str):
    def __lt__(self, other: str) -> bool:
        return self + other > other + self



class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        x = "".join(sorted([str(x) for x in nums], key=AugmentedString))
        return '0' if x[0] == '0' else x