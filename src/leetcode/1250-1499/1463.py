from typing import List
from functools import cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def moves(i: int, j: int) -> list[tuple[int, int]]:
            acc: list[tuple[int, int]] = []
            if i < m - 1:
                acc.append((i + 1, j))
            if j < n - 1:
                acc.append((i + 1, j + 1))
            if j > 0:
                acc.append((i + 1, j - 1))
            return acc

        @cache
        def f(robone: tuple[int, int], robtwo: tuple[int, int]) -> int:
            x1, y1 = robone
            x2, y2 = robtwo

            if x1 == m - 1 and x2 == m - 1:
                return 0

            moves_one, moves_two = moves(x1, y1), moves(x2, y2)

            acc: list[int] = []
            for m1 in moves_one:
                for m2 in moves_two:
                    mx1, my1 = m1
                    mx2, my2 = m2

                    if m1 == m2:
                        acc.append(grid[mx1][my1] + f(m1, m2))
                    else:
                        acc.append(grid[mx1][my1] + grid[mx2][my2] + f(m1, m2))
            return max(acc)

        return f((0, 0), (0, n - 1)) + grid[0][0] + grid[0][n - 1]