from typing import List
from math import inf


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        distances = [inf] * n
        distances[src] = 0

        for _ in range(k + 1):
            ndistances = [x for x in distances]
            for edge in flights:
                u, v, w = edge[0], edge[1], edge[2]
                if distances[u] != inf and ndistances[v] > distances[u] + w:
                    ndistances[v] = distances[u] + w
            distances = ndistances

        return int(distances[dst]) if distances[dst] != inf else -1
