from typing import List, Generator
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        parents: dict[str, str] = {}
        ranks: dict[str, int] = {}

        def make_set(x: str) -> None:
            assert x not in parents and x not in ranks
            parents[x] = x
            ranks[x] = 0

        def find(x: str) -> str:
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x: str, y: str) -> None:
            xbar = find(x)
            ybar = find(y)

            if xbar == ybar:
                return None

            if ranks[xbar] > ranks[ybar]:
                parents[ybar] = xbar
            else:
                parents[xbar] = ybar
                if ranks[xbar] == ranks[ybar]:
                    ranks[ybar] += 1

        nodes: set[str] = set()

        def construct(
            equations: List[List[str]], values: List[float]
        ) -> dict[str, list[tuple[str, float]]]:
            graph: dict[str, list[tuple[str, float]]] = defaultdict(list)

            for eq, v in zip(equations, values):
                left = eq[0]
                right = eq[1]

                graph[left].append((right, v))
                graph[right].append((left, 1 / v))

                nodes.add(left)
                nodes.add(right)

            return graph

        # Create graph and disjoint set.

        g = construct(equations=equations, values=values)

        for node in nodes:
            make_set(node)

        for vertex, edges in g.items():
            for edge, _ in edges:
                union(vertex, edge)

        for node in nodes:
            _ = find(node)

        # Answer queries.

        def dfs(node: str, seen: set[str], mult: float) -> Generator[tuple[str, float], None, None]:
            if node in seen:
                return

            seen.add(node)
            for edge, val in g[node]:
                yield (edge, mult * val)
                yield from dfs(edge, seen, mult * val)

        def search(source: str, target: str) -> float:
            seen : set[str] = set()
            for val, mult in dfs(node=source, seen=seen, mult=1.0):
                if val == target:
                    return mult
            raise Exception


        def answer(query: List[str]) -> float:
            assert len(query) == 2

            left = query[0]
            right = query[1]

            # Not in same component
            if (left not in parents) or (right not in parents) or (parents[left] != parents[right]):
                return -1.0

            return search(left, right)

        return list(map(lambda x: answer(x), queries))


# s = Solution()
# print(s.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
