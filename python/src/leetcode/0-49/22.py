from typing import List
from functools import cache

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        @cache
        def f(x: int) -> list[str]:
            if x == 0:
                return [""]

            res : list[str] = []
            for (l, r) in zip(range(x), range(x - 1, -1, -1)):
                for cl in f(l):
                    for rl in f(r):
                        res.append(f"({cl}){rl}")

            return res

        return f(n)
