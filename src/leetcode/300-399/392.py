class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True

        def f(i: int, j: int) -> bool:
            if i == len(s) and j <= len(t):
                return True

            if i <= len(s) - 1 and j == len(t):
                return False

            return f(i + 1, j + 1) if s[i] == t[j] else f(i, j + 1)

        return f(0, 0)