class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def f(i: int, j: int, acc: int) -> int:
            if i >= len(text1) or j >= len(text2):
                return acc

            if text1[i] == text2[j]:
                yes = f(i + 1, j + 1, acc + 1)
                no = f(i + 2, j + 2, acc + 1)
                return max(yes, no)

            return f(i, j + 1, acc)

        return max([f(i, i, 0) for i in range(len(text1))])