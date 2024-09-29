class Solution:
    def balancedStringSplit(self, s: str) -> int:
        acc, count = 0, 0

        for i in range(len(s)):
            count += 1 if s[i] == "R" else -1
            if count == 0:
                acc += 1

        return acc
