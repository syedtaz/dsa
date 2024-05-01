from typing import List
from collections import defaultdict
from heapq import heappop, heappush

graph_t = dict[int, list[tuple[int, float]]]


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:

        def construct(edges: list[list[int]], weights: list[float]) -> graph_t:

            graph: graph_t = defaultdict(list)

            for [a, b], w in zip(edges, weights):
                graph[a].append((b, w))
                graph[b].append((a, w))

            return graph

        def dijkstra(source: int, graph: graph_t) -> list[float]:

            # Init SSSP
            dist: list[float] = [0.0 for _ in range(n)]
            dist[source] = 1

            visited: list[bool] = [False for _ in range(n)]
            queue: list[tuple[float, int]] = [(-1.0, source)]

            while len(queue) > 0:
                _, node = heappop(queue)
                visited[node] = True

                for neighbor, w in graph[node]:
                    if visited[neighbor]:
                        continue

                    tentative_dist = dist[node] * w

                    if dist[neighbor] < tentative_dist:
                        dist[neighbor] = tentative_dist
                        heappush(queue, (-tentative_dist, neighbor))

            return dist

        g = construct(edges, succProb)

        return dijkstra(start_node, g)[end_node]
