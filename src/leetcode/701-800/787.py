from typing import List
from collections import defaultdict
from math import inf


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        def construct(edges: list[list[int]]) -> dict[int, list[tuple[int, int]]]:
            g: dict[int, list[tuple[int, int]]] = defaultdict(list)

            for edge in edges:
                u, v, w = edge[0], edge[1], edge[2]
                g[u].append((v, w))

            return g

        return 0  # TODO!
