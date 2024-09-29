from typing import List
from collections import defaultdict
from enum import Enum


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def construct(edges: List[List[int]]) -> dict[int, list[int]]:
            g: dict[int, list[int]] = defaultdict(list)

            for edge in edges:
                to, fr = edge[0], edge[1]
                g[fr].append(to)

            return g

        graph = construct(edges=prerequisites)

        class Status(Enum):
            NEW = 0
            ACTIVE = 1
            FINISHED = 2

        class Cycle(Exception):
            pass

        def topsort(graph: dict[int, list[int]]) -> list[int]:
            status = {k: Status.NEW for k in range(numCourses)}
            clock = numCourses - 1
            S = [numCourses] * numCourses

            def dfs(v: int, cl: int) -> int:
                status[v] = Status.ACTIVE

                for edge in graph[v]:
                    if status[edge] == Status.NEW:
                        cl = dfs(edge, cl)
                    elif status[edge] == Status.ACTIVE:
                        raise Cycle

                status[v] = Status.FINISHED
                S[cl] = v
                cl -= 1
                return cl

            for v in range(numCourses):
                if status[v] == Status.NEW:
                    try:
                        clock = dfs(v, clock)
                    except Cycle:
                        return []

            return S

        return topsort(graph=graph)


# s = Solution()
# print(s.findOrder(numCourses = 1, prerequisites = []))
