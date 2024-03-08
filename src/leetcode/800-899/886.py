from typing import List
from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        def construct_graph(edges: list[list[int]]) -> dict[int, list[int]]:
            graph : dict[int, list[int]] = defaultdict(list)

            for edge in edges:
                u, v = edge[0], edge[1]
                graph[u].append(v)
                graph[v].append(u)

            return graph

        def two_color(graph: dict[int, list[int]]) -> dict[int, bool]:

            not_seen = set(graph.keys())
            queue: deque[tuple[bool, int]] = deque([(True, not_seen.pop())])
            coloring: dict[int, bool] = {}

            while len(queue) > 0:
                color, node = queue.popleft()
                coloring[node] = color

                for neighbor in graph[node]:
                    if neighbor in not_seen:
                        not_seen.remove(neighbor)
                        queue.append((not color, neighbor))

                if len(queue) == 0 and len(not_seen) > 0:
                    queue.append((not color, not_seen.pop()))

            return coloring

        def check_two_coloring(graph: dict[int, list[int]], coloring: dict[int, bool]) -> bool:

            for u, vs in graph.items():
                color = coloring[u]

                for v in vs:
                    if coloring[v] == color:
                        return False

            return True

        graph = construct_graph(dislikes)
        if len(graph.keys()) <= 1:
            return True

        coloring = two_color(graph)
        return check_two_coloring(graph, coloring)




