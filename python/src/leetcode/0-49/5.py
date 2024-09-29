from functools import cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        @cache
        def f(i: int, j: int) -> str:
            if i > j:
                return ""
            if i == j:
                return s[i]

            return s[i] + f(i + 1, j - 1) + s[j] if s[i] == s[j] else ""

        m = s[0]
        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s) - 1):
                m = max(m, f(i, j), key=len)

        return m


s = Solution()
print(s.longestPalindrome("aacabdkacaa"))
