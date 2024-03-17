from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        acc = 0
        decr = 0

        while k > 0:
            value = happiness.pop()
            acc += max(value - decr, 0)
            decr += 1
            k -= 1

        return acc