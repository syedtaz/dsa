from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        minus = [x for x in nums if x < 0]
        plus =  [x for x in nums if x > 0]
        acc : list[int] = []

        for (a, b) in zip(plus, minus):
            acc.append(a)
            acc.append(b)

        return acc