from typing import List
from math import inf, isinf
import heapq

graph_t = dict[int, list[tuple[int, int]]]


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        def initSSSP(k: int) -> list[float]:
            dist = [inf] * n
            dist[k - 1] = 0
            return dist

        def construct(edges: list[list[int]]) -> graph_t:
            graph: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}

            for u, v, w in edges:
                graph[u - 1].append((v - 1, -w))

            return graph

        def djikstra(s: int, graph: graph_t) -> list[float]:
            dist = initSSSP(k=s)
            queue: list[tuple[float, int]] = []

            for i in range(n):
                queue.append((dist[i], i))
            heapq.heapify(queue)

            while len(queue) > 0:
                tdist, u = heapq.heappop(queue)

                if tdist != dist[u]:
                    continue

                for v, w in graph[u]:
                    if dist[v] > dist[u] - w:
                        dist[v] = dist[u] - w
                        heapq.heappush(queue, (dist[v], v))

            return dist

        dist = djikstra(s=k, graph=construct(edges=times))

        if any([isinf(x) for x in dist]):
            return -1

        return int(max(dist))