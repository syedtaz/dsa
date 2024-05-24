from typing import List


class UnionFind:
    ranks: list[int]
    parents: list[int]

    def __init__(self, grid: list[list[str]]) -> None:
        self.make_set(grid)

    def make_set(self, grid: list[list[str]]) -> None:
        m, n = len(grid), len(grid[0])
        self.ranks = [-1] * (m * n)
        self.parents = [-1] * (m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue

                self.parents[i * n + j] = i * n + j
                self.ranks[i * n + j] = 0

    def find(self, x: int) -> int:
        if self.parents[x] != x:
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
    def numIslands(self, grid: List[List[str]]) -> int:
        graph = UnionFind(grid)
        m, n = len(grid), len(grid[0])

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "0":
                    continue

                if i < m - 1 and grid[i + 1][j] == "1":
                    graph.union(i * n + j, (i + 1) * n + j)

                if j < n - 1 and grid[i][j + 1] == "1":
                    graph.union(i * n + j, i * n + (j + 1))

        for i in range(m):
            for j in range(n):
                graph.find(i * n + j)

        return len(set([x for x in graph.parents if x != -1]))
