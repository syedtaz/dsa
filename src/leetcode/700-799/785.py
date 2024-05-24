from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen: set[int] = set()
        total: set[int] = set(range(len(graph)))
        colors: dict[int, bool] = {}

        def bfs(source: int) -> None:
            queue: deque[tuple[int, bool]] = deque([(source, True)])

            while len(queue) > 0:
                v, color = queue.popleft()
                seen.add(v)

                if v not in colors:
                    colors[v] = color

                for edge in graph[v]:
                    if edge not in seen:
                        queue.append((edge, not color))

        def bfsAll() -> None:
            diff = total.difference(seen)

            while len(diff) > 0:
                source = next(iter(diff))
                bfs(source)
                diff = total.difference(seen)

        bfsAll()

        for u, edges in enumerate(graph):
            c = colors[u]
            for v in edges:
                if c == colors[v]:
                    return False

        return True


# s = Solution()
# print(s.isBipartite(graph=[[1,2,3],[0,2],[0,1,3],[0,2]]))
