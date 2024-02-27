from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        temp = [a - b for (a, b) in zip(gas, cost)]

        if sum(temp) < 0:
            return -1

        cand, cur = 0, 0

        for i in range(len(temp)):
            cur += temp[i]
            if cur < 0:
                cur = 0
                cand = i + 1

        return cand
