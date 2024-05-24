from functools import cache
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @cache
        def f(i: int, j: int) -> int:
            if i == m:
                return 0

            choices = [f(i + 1, j)]

            if 1 <= j:
                choices.append(f(i + 1, j - 1))

            if j < n - 1:
                choices.append(f(i + 1, j + 1))

            return matrix[i][j] + min(choices)

        return min([f(0, i) for i in range(n)])
