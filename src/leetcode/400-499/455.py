from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i, j, acc = len(g) - 1, len(s) - 1, 0

        while True:
            if j < 0 or i < 0:
                return acc

            cookie, child = s[j], g[i]

            if cookie >= child:
                i, j, acc = i - 1, j - 1, acc + 1
                continue

            i = i - 1