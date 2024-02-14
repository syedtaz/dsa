from typing import List
from functools import cache


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid) - 1, len(grid[0]) - 1

        @cache
        def f(i: int, j: int) -> int:
            if i == m and j == n:
                return grid[i][j]

            if i == m:
                return grid[i][j] + f(i, j + 1)

            if j == n:
                return grid[i][j] + f(i + 1, j)

            right = grid[i][j] + f(i + 1, j)
            down = grid[i][j] + f(i, j + 1)
            return min(right, down)

        return f(0, 0)