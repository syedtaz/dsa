from typing import List
from collections import deque

index = tuple[int, int]


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def initialize(graph: list[list[int]]) -> tuple[int, deque[tuple[int, index]]]:
            queue: list[tuple[int, index]] = []
            count = 0

            for i, row in enumerate(graph):
                for j, val in enumerate(row):
                    if val == 1:
                        count += 1
                    elif val == 2:
                        queue.append((0, (i, j)))

            return count, deque(queue)

        count, queue = initialize(graph=grid)

        if count == 0:
            return 0

        minute = 0
        m, n = len(grid), len(grid[0])

        while len(queue) > 0 and count != 0:
            level, (i, j) = queue.popleft()

            if grid[i][j] != 2:
                grid[i][j] = 2
                count -= 1

            minute = max(level, minute)

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni <= m - 1 and 0 <= nj <= n - 1 and grid[ni][nj] == 1:
                    queue.append((level + 1, (ni, nj)))

        return minute if count <= 0 else -1