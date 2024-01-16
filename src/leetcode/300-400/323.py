from typing import List
from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def construct(edges: List[List[int]]) -> dict[int, list[int]]:
            g: dict[int, list[int]] = defaultdict(list)

            for edge in edges:
                fr = edge[0]
                to = edge[1]

                g[fr].append(to)
                g[to].append(fr)

            return g

        graph = construct(edges=edges)
        seen: set[int] = set()
        keys: set[int] = set([x for x in graph.keys()])
        count = 0

        def dfs(node: int, parent: int) -> None:
            if node in seen:
                return

            seen.add(node)
            for v in graph[node]:
                if v == parent:
                    continue

                if v in seen:
                    return

                dfs(v, node)

            return

        diff = keys
        source = 0
        while len(seen) != n:
            dfs(source, -1)
            count += 1
            diff = keys.difference(seen)
            if len(diff) > 0:
                source = diff.pop()

        return count


# s = Solution()
# print(f"The count is {s.countComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,4]])}")
