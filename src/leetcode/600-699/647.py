class Solution:
    def countSubstrings(self, s: str) -> int:
        table = [[False] * len(s)] * len(s)
        count = 0
        for i in range(len(s)):
            table[i][i] = True
            count += 1

        for i in range(len(s) - 1):
            table[i][i + 1] = s[i] == s[i + 1]
            count += 1 if table[i][i + 1] else 0

        for length in range(3, len(s) + 1):
            for i in range(0, len(s) - length):
                for j in range(i + length - 1, len(s)):
                    table[i][j] = table[i + 1][j - 1] and s[i] == s[j]
                    count += 1 if table[i][j] else 0

        return count
