from typing import List
from itertools import product
from enum import Enum

point = tuple[int, int]


class UnionFind:
    parents: dict[point, point]
    rank: dict[point, int]

    def __init__(self, m: int, n: int) -> None:
        self.parents = {}
        self.rank = {}

        for i in range(m):
            for j in range(n):
                self.parents[(i, j)] = (i, j)
                self.rank[(i, j)] = 0

        return

    def find(self, x: point) -> point:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: point, y: point) -> None:
        xbar = self.find(x)
        ybar = self.find(y)

        if xbar == ybar:
            return None

        if self.rank[xbar] > self.rank[ybar]:
            self.parents[ybar] = xbar
        else:
            self.parents[xbar] = ybar
            if self.rank[xbar] == self.rank[ybar]:
                self.rank[ybar] += 1


class Sea(Enum):
    Pacific = 0
    Atlantic = 1


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def find_sources(sea: Sea) -> set[point]:
            m, n = len(heights), len(heights[0])
            uf = UnionFind(m=m, n=n)
            direction = [(0, -1), (-1, 0)] if sea == Sea.Pacific else [(0, 1), (1, 0)]

            for i, j in product(range(m), range(n)):
                value = heights[i][j]
                for dx, dy in direction:
                    x2, y2 = i + dx, j + dy
                    if (
                        0 <= x2 <= m - 1
                        and 0 <= y2 <= n - 1
                        and heights[x2][y2] <= value
                    ):
                        uf.union((i, j), (x2, y2))

            targets: set[point] = set()
            acc: set[point] = set()

            for j in range(n):
                targets.add(uf.find((0, j) if sea == Sea.Pacific else (m - 1, j)))

            for i in range(m):
                targets.add(uf.find((i, 0) if sea == Sea.Pacific else (i, n - 1)))

            for i, j in product(range(m), range(n)):
                parent = uf.find((i, j))
                if parent in targets:
                    acc.add((i, j))

            return acc

        acc: list[list[int]] = []

        for a, b in find_sources(Sea.Pacific).intersection(find_sources(Sea.Atlantic)):
            acc.append([a, b])

        return acc


s = Solution()
print(
    s.pacificAtlantic(
        heights=[
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)
