from typing import List
from collections import defaultdict, deque

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        def construct(pid: list[int], ppid: list[int]) -> dict[int, list[int]]:
            g: dict[int, list[int]] = defaultdict(list)

            for idx, x in enumerate(ppid):
                g[x].append(pid[idx])

            return g

        graph = construct(pid, ppid)
        acc : list[int] = []
        queue : deque[int] = deque([kill])

        while len(queue) > 0:
            node = queue.popleft()

            for child in graph[node]:
                queue.append(child)

            acc.append(node)

        return acc