class Solution:
    def maxPower(self, s: str) -> int:
        acc = 0
        cur = 1

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                acc = max(acc, cur)
                cur = 0

            cur += 1

        acc = max(acc, cur)
        return acc