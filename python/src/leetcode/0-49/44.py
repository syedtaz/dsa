from itertools import groupby


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        groups = [
            "".join(list(y)) for _, y in groupby(p, key=lambda x: x == "*" or x == "?")
        ][::-1]
        print(groups)

        i = 0

        while i < len(s) and len(groups) > 0:
            pat = groups.pop()
            j = 0

            while j != len(pat):
                match pat[j]:
                    case "?":
                        i, j = i + 1, j + 1
                    case "*":
                        if len(groups) == 0:
                            return True

        # def f(i: int, j: int) -> bool:
        #     if i >= n and j >= m:
        #         return True

        #     # Last pattern is "*"
        #     if j < m and p[j] == '*':
        #         if j == m - 1:
        #           return True

        #         nextpat = p[j + 1]

        #         while i < n and s[i] != nextpat:
        #             i += 1

        #         return f(i + 1, j + 2)

        #     if (i >= n) or (j >= m):
        #         return False

        #     if p[j] == "?":
        #         return f(i + 1, j + 1)

        #     if p[j] == s[i]:
        #         return f(i + 1, j + 1)

        #     return False

        return False


s = Solution()
print(s.isMatch("abcabczzzde", "*abc???de*"))
