from typing import List
from functools import cache


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @cache
        def f(i: int) -> list[str]:
            if i == 0:
                return [""]

            res: list[str] = []
            for l, r in zip(range(i), range(i - 1, -1, -1)):
                for cl in f(l):
                    for rl in f(r):
                        res.append("(" + cl + ")" + rl)

            return res

        return f(n)


# s = Solution()
# print(s.generateParenthesis(2))
