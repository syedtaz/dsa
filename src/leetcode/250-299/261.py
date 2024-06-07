from typing import List
from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        def construct(edges: List[List[int]]) -> dict[int, list[int]]:
            g: dict[int, list[int]] = defaultdict(list)

            for edge in edges:
                fr = edge[0]
                to = edge[1]
                g[fr].append(to)
                g[to].append(fr)

            return g

        graph = construct(edges)
        seen: set[int] = set()

        def dfs(node: int, parent: int):
            if node in seen:
                return True

            seen.add(node)
            for edge in graph[node]:
                if edge == parent:
                    continue
                if edge in seen:
                    return False
                result = dfs(edge, node)
                if not result:
                    return False

            return True

        return dfs(0, -1) and len(seen) == n


# s = Solution()
# print(s.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))
