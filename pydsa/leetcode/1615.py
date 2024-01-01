from typing import List
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        def construct(edges: List[List[int]]) -> dict[int, set[int]]:
            g: dict[int, set[int]] = defaultdict(set)

            for edge in edges:
                l, r = edge[0], edge[1]
                g[l].add(r)
                g[r].add(l)

            return g

        graph = construct(edges=roads)
        m = 0

        for i in range(n):
          for j in range(n):
              if i == j:
                  continue

              e1 = len([x for x in graph[i] if x != j])
              e2 = len(graph[j])
              size = e1 + e2
              m = max(m, size)

        return m


# s = Solution()
# s.maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])
