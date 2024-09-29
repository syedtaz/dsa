class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                memo[i][j] = (
                    max(memo[i + 1][j], memo[i][j + 1])
                    if text1[i] != text2[j]
                    else 1 + memo[i + 1][j + 1]
                )

        return memo[0][0]
