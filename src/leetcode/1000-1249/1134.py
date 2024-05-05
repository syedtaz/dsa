from typing import List
from math import inf
import heapq


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:

        weights = [[inf] * n] * n
        for u, v, w in edges:
            weights[u][v] = weights[v][u] = w

        def djikstra(u: int) -> int:
            dist: list[float] = [inf] * n
            dist[u] = 0

            pqueue: list[tuple[float, int]] = []

            for v in range(n):
                if u != v:
                    pqueue.append((-weights[u][v], v))

            heapq.heapify(pqueue)

            while len(pqueue) > 0:
                d, v = heapq.heappop(pqueue)

                if -d != dist[v]:
                    continue

                for x in range(n):

                    if dist[v] > dist[v] + (-d):






# s = Solution()
# print(
#     s.findTheCity(
#         n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4
#     )
# )
