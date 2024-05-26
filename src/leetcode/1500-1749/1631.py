from typing import List
from math import inf
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        dist = [[inf] * cols for _ in range(rows)]
        dist[0][0] = 0

        visited = [[False] * cols for _ in range(rows)]
        queue: list[tuple[float, tuple[int, int]]] = [(0, (0, 0))]

        while len(queue) > 0:
            _, (x, y) = heapq.heappop(queue)
            visited[x][y] = True

            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                a, b = x + dx, y + dy

                if 0 <= a < rows and 0 <= b < cols and (not visited[a][b]):
                    w = abs(heights[x][y] - heights[a][b])
                    diff = max(dist[x][y], w)

                    if dist[a][b] > diff:
                        dist[a][b] = diff
                        heapq.heappush(queue, (diff, (a, b)))

        return int(dist[rows - 1][cols - 1])
