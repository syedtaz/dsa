class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def f(i: int, j: int, k: int) -> bool:
            print(f"{i} and {j} and {k}")
            if (i >= len(s1) or j >= len(s2)) and k < len(s3):
                return False

            if k >= len(s3):
                return True

            if i <= len(s1) - 1 and s3[k] == s1[i]:
                return f(i + 1, j, k + 1)

            if j <= len(s2) - 1 and s3[k] == s2[j]:
                return f(i, j + 1, k + 1)

            return False

        return f(0, 0, 0)
