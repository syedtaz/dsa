from typing import List
from math import inf


class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        dist = [inf for _ in range(n)]
        dist[0] = 0.0

        for _ in range(n - 1):
            for edge in edges:
                u, v = edge[0], edge[1]
                if dist[v] > dist[u] + 1:
                    dist[v] = dist[u] + 1

        return dist
