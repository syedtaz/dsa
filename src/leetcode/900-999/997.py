from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = [0 for _ in range(n)]

        for fr, to in trust:
            degrees[to - 1] += 1
            degrees[fr - 1] -= 1

        for i, deg in enumerate(degrees):
            if deg == n - 1:
                return i + 1
        return -1
