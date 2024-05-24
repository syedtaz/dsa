from typing import List
from collections import defaultdict

point = tuple[int, int]


class UnionFind:
    parents: dict[point, point]
    ranks: dict[point, int]

    def __init__(self, points: set[point]) -> None:
        self.parents = {point: point for point in points}
        self.ranks = {point: 0 for point in points}

    def find(self, x: point) -> point:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: point, y: point) -> None:
        xbar = self.find(x)
        ybar = self.find(y)

        # Component exists
        if xbar == ybar:
            return None

        if self.ranks[xbar] > self.ranks[ybar]:
            self.parents[ybar] = xbar
        else:
            self.parents[xbar] = ybar
            if self.ranks[ybar] == self.ranks[xbar]:
                self.ranks[ybar] += 1


def generate_offsets(uf: UnionFind) -> int:
    components: dict[point, list[point]] = defaultdict(list)

    for k, v in uf.parents.items():
        components[v].append(k)

    for k, v in components.items():
        if len(v) == 1:
            components[k] = [(0, 0)]
            continue

        component = v
        component.sort()

        x, y = component[0]

        for idx, other in enumerate(component[1:]):
            a, b = other
            component[idx + 1] = (x - a, y - b)

        component[0] = (0, 0)
        components[k] = component

    return len(set([tuple(x) for x in components.values()]))


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        points: set[tuple[int, int]] = set()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    points.add((i, j))

        uf = UnionFind(points)

        for point in points:
            x, y = point
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx <= m - 1 and 0 <= y + dy <= n - 1:
                    neighbor = (x + dx, y + dy)
                    if neighbor in points:
                        uf.union(point, neighbor)

        for p in uf.parents:
            _ = uf.find(p)

        return generate_offsets(uf)
