from typing import List
from collections import deque, defaultdict


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        if len(edges) == 0:
            return 0

        def construct(edges: List[List[int]]) -> dict[int, List[int]]:
            g: defaultdict[int, list[int]] = defaultdict(list)

            for edge in edges:
                assert len(edge) == 2
                fr, to = edge[0], edge[1]
                g[fr].append(to)
                g[to].append(fr)

            return g

        def bfs(source: int, graph: dict[int, List[int]]) -> tuple[int, int]:
            queue : deque[tuple[int, int]] = deque([(0, source)])
            seen : set[int] = set()
            maxdist = 0
            maxv = source

            while len(queue) > 0:
                dist, v = queue.popleft()
                if v not in seen:
                    seen.add(v)
                    if dist > maxdist:
                        maxdist = dist
                        maxv = v
                    for edge in graph[v]:
                        queue.append((dist + 1, edge))

            return maxv, maxdist

        graph = construct(edges=edges)
        first, _ = bfs(source = 0, graph = graph)
        _, sdistance = bfs(source = first, graph = graph)
        return sdistance

s = Solution()
print(s.treeDiameter([[0,1],[0,2]]))
print(s.treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))