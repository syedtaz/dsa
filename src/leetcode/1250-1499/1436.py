from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph: dict[str, str] = {source: dest for [source, dest] in paths}
        node = paths[0][0]

        while node in graph:
            node = graph[node]

        return node