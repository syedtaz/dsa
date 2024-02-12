from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def f(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 0

            if word1[i - 1] == word2[j - 1]:
                return 1 + f(i - 1, j - 1)

            a = f(i - 1, j)
            b = f(i, j - 1)
            return max(a, b)

        return len(word1) + len(word2) - (2 * f(len(word1) - 1, len(word2) - 1))
