from typing import List

class NeighborSum:
    memo: dict[int, tuple[int, int]]

    def __init__(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        memo: dict[int, tuple[int, int]] = {}

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                adj = 0
                # Adjacent
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + dx < m and 0 <= j + dy < n:
                        adj += grid[i + dx][j + dy]

                diag = 0
                for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    if 0 <= i + dx < m and 0 <= j + dy < n:
                        diag += grid[i + dx][j + dy]

                memo[val] = (adj, diag)

        self.memo = memo

    def adjacentSum(self, value: int) -> int:
        return self.memo[value][0]

    def diagonalSum(self, value: int) -> int:
        return self.memo[value][1]