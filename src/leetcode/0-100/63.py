from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        moves : set[str] = set()

        def f(i: int, j: int, move: str) -> None:
            if i == m - 1 and j == n - 1:
                moves.add(move)
                return None

            if i < m - 1 and obstacleGrid[i + 1][j] != 1:
                f(i + 1, j, move + '1')

            if j < n - 1 and obstacleGrid[i][j + 1] != 1:
                f(i, j + 1, move + '0')

            return None

        f(0, 0, "")
        return len(moves)