from typing import List


class UnionFind:
    parents: list[int]
    ranks: list[int]

    def __init__(self, grid: list[list[int]]) -> None:
        self.make_set(grid)

    def make_set(self, grid: list[list[int]]) -> None:
        m, n = len(grid), len(grid[0])
        self.parents = [-1] * (m * n)
        self.ranks = [-1] * (m * n)

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:
                    continue

                idx = i * n + j
                self.parents[idx] = idx
                self.ranks[idx] = 0

    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        xbar = self.find(x)
        ybar = self.find(y)

        if xbar == ybar:
            return

        if self.ranks[xbar] > self.ranks[ybar]:
            self.parents[ybar] = xbar
        else:
            self.parents[xbar] = ybar
            if self.ranks[xbar] == self.ranks[ybar]:
                self.ranks[ybar] += 1


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        graph = UnionFind(grid)
        m, n = len(grid), len(grid[0])

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:
                    continue

                if i < m - 1 and grid[i + 1][j] == 1:
                    graph.union(i * n + j, (i + 1) * n + j)

                if j < n - 1 and grid[i][j + 1] == 1:
                    graph.union(i * n + j, i * n + (j + 1))

        for i in range(m):
            for j in range(n):
                _ = graph.find(i * n + j)

        rm: set[int] = set()
        for j in range(n):
            fst, lst = graph.find(j), graph.find((m - 1) * n + j)
            if fst > 0:
                rm.add(fst)
            if lst > 0:
                rm.add(lst)

        for i in range(m):
            fst, lst = graph.find(i * n), graph.find(i * n + (n - 1))
            if fst > 0:
                rm.add(fst)
            if lst > 0:
                rm.add(lst)

        return len([x for x in graph.parents if x > 0 and x not in rm])
