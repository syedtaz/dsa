from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        def construct(edges: list[list[int]]) -> dict[int, list[int]]:
            g : dict[int, list[int]] = defaultdict(list)

            for edge in edges:
                u, v = edge[0], edge[1]
                g[u].append(v)
                g[v].append(u)

            return g

        graph = construct(edges=edges)
        start = max(graph.keys(), key=lambda x: len(graph[x]))
        queue = [start]
        sources = []

        while len(queue) > 0:


        return sources

s = Solution()
print(s.findMinHeightTrees(n = 6, edges=[[3,0],[3,1],[3,2],[3,4],[5,4]]))

