from typing import List
from collections import defaultdict


class Solution:
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        restr = set(restricted)

        def construct(edges: List[List[int]]) -> defaultdict[int, list[int]]:
            g: dict[int, list[int]] = defaultdict(list)

            for edge in edges:
                l, r = edge[0], edge[1]
                if l in restr or r in restr:
                    continue

                g[l].append(r)
                g[r].append(l)

            return g

        graph = construct(edges=edges)

        seen: set[int] = set()

        def dfs(source: int) -> None:
            stack = [source]

            while len(stack) > 0:
                v = stack.pop()
                if v not in seen:
                    seen.add(v)
                    for edge in graph[v]:
                        stack.append(edge)

        dfs(0)
        return len(seen)
