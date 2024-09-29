from typing import List
from functools import cache


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def f(i: int) -> list[list[str]]:
            if i >= len(s):
                return []

            acc: list[list[str]] = []

            for j in range(i, len(s)):
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    ans = f(j + 1)

                    if len(ans) == 0:
                        acc.append([s[i : j + 1]])
                    else:
                        for x in ans:
                            acc.append([s[i : j + 1]] + x)

            return acc

        return f(0)