from typing import List
from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words: set[str] = set(wordDict)

        @cache
        def f(i: int) -> bool:
            if i >= len(s):
                return True

            acc: list[bool] = []
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words:
                    acc.append(True & f(j))

            return any(acc)

        return f(0)
