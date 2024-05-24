from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        acc = 0
        pref = [acc := max(acc, x) for x in height]

        acc = 0
        suff = [acc := max(acc, x) for x in reversed(height)][::-1]

        vals = [min(p, s) - h for p, s, h in zip(pref, suff, height)]

        return sum(vals)
