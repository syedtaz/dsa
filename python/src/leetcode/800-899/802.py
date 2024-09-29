from typing import List
from enum import Enum


class State(Enum):
    New = 0
    Active = 1
    Finished = 2


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        lst = [False for _ in range(len(graph))]
        status = [State.New for _ in range(len(graph))]

        def dfs(source: int) -> bool:
            status[source] = State.Active

            for edge in graph[source]:
                if status[edge] == State.Active:
                    lst[source] = False
                    return False
                elif status[edge] == State.New:
                    if not dfs(edge):
                        lst[source] = False
                        return False

            status[source] = State.Finished
            lst[source] = True
            return True

        for i in range(len(graph)):
            if status[i] == State.New:
                dfs(i)

        return [i for i in range(len(graph)) if lst[i]]
