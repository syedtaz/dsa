from typing import List
from collections import deque, defaultdict
from enum import Enum

graph_t = dict[str, set[str]]


class Status(Enum):
    Finished = 0
    Active = 1
    New = 2


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def construct(words: list[str]) -> graph_t:
            queue: deque[tuple[int, list[str]]] = deque(
                [(0, list(x)[::-1]) for x in words]
            )
            graph: graph_t = defaultdict(set)
            current_level = 0
            wavefront: list[str] = []

            while len(queue) > 0:
                level, word = queue.popleft()

                if len(word) == 0:
                    continue

                if current_level != level:
                    current_level = level
                    wavefront.clear()

                char = word.pop()

                for prev in wavefront:
                    if prev != char:
                        graph[prev].add(char)

                wavefront.append(char)
                queue.append((level + 1, word))

            return graph

        def dfs(
            v: str,
            graph: graph_t,
            clock: int,
            order: list[str],
            status: dict[str, Status],
        ) -> int:
            status[v] = Status.Active

            for w in graph[v]:
                if status[w] == Status.New:
                    clock = dfs(w, graph, clock, order, status)
                elif status[w] == Status.Active:
                    print(f"Exception: {v} -> {w}")
                    raise Exception

            status[v] = Status.Finished
            order[clock] = v
            clock = clock - 1
            return clock

        def topsort(graph: graph_t) -> list[str]:
            status: dict[str, Status] = {vertex: Status.New for vertex in graph.keys()}
            clock = len(status)
            order = ["" for _ in range(len(status))]

            for v, stat in status.items():
                if stat == Status.New:
                    try:
                        clock = dfs(v, graph, clock, order, status)
                    except Exception:
                        return []

            return order

        return "".join(topsort(construct(words)))


s = Solution()
print(s.alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"]))
