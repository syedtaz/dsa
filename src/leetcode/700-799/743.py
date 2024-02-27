from typing import List
from collections import defaultdict
from math import inf
import heapq

edge_t = tuple[int, int]
graph_t = dict[int, list[edge_t]]


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        def construct(edges: list[list[int]]) -> graph_t:
            graph: dict[int, list[edge_t]] = defaultdict(list)

            for edge in edges:
                u, v, w = edge[0], edge[1], edge[2]
                graph[u].append((v, w))

            for i in graph.keys():
                graph[i].sort(key=lambda x: x[1])

            return graph

        graph = construct(times)
        dist = {i: inf for i in range(1, n + 1)}
        dist[k] = 0

        queue = [(0, k)]

        while len(queue) > 0:



