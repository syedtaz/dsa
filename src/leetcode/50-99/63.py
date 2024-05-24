from typing import List
from functools import cache

point = tuple[int, int]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def search(positition: point) -> int:
            x, y = positition

            if obstacleGrid[x][y] == 1:
                return 0

            if positition == (m - 1, n - 1):
                return 1

            right = search((x + 1, y)) if (0 <= x + 1 < m) else 0
            down = search((x, y + 1)) if (0 <= y + 1 < n) else 0

            return right + down

        return search((0, 0))
