from typing import List
from functools import cache


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g: dict[int, list[int]] = {u: vs for u, vs in enumerate(graph)}

        @cache
        def f(source: int, sink: int) -> list[list[int]]:
            if source == sink:
                return [[sink]]

            paths: list[list[int]] = []
            for edge in g[source]:
                for path in f(edge, sink):
                    if len(path) > 0 and path[-1] == sink:
                        paths.append([source] + path)

            return paths

        return f(0, len(graph) - 1)


# s = Solution()
# print(s.allPathsSourceTarget(graph=[[4,3,1],[3,2,4],[3],[4],[]]))
