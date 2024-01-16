from typing import List
from collections import defaultdict
from enum import Enum


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def construct(words: List[str]) -> tuple[dict[str, list[str]], set[str]]:
            graph: dict[str, set[str]] = defaultdict(set)
            seen: set[str] = set()

            for word in words:
                for idx, a in enumerate(word):
                    if a not in graph:
                        graph[a] = set()
                    for b in word[idx + 1 :]:
                        if a != b:
                          graph[a].add(b)
                          seen.add(a)
                          seen.add(b)

            return {k: list(v) for k, v in graph.items()}, seen

        graph, vertices = construct(words=words)
        print(graph)

        class Status(Enum):
            ACTIVE = 0
            NEW = 1
            FINISHED = 2

        status = {}

        def isAcyclicDFS(v: str) -> bool:
            status[v] = Status.ACTIVE
            for edge in graph[v]:
                if status[edge] == Status.ACTIVE:
                    return False
                elif status[edge] == Status.NEW:
                    if not isAcyclicDFS(edge):
                        return False

            status[v] = Status.FINISHED
            return True

        def isAcyclic(g: dict[str, list[str]]) -> bool:
            for v in vertices:
                status[v] = Status.NEW

            for u in vertices:
                if status[u] == Status.NEW:
                    if not isAcyclicDFS(u):
                        return False

            return True

        if not isAcyclic(graph):
            return "not doable"

        return "doable"


s = Solution()
print(s.alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"]))
