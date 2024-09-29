from typing import List


class UnionFind:
    parents: list[int]
    ranks: list[int]

    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        xbar = self.find(x)
        ybar = self.find(y)

        if xbar == ybar:
            return None

        if self.ranks[xbar] > self.ranks[ybar]:
            self.parents[ybar] = xbar
        else:
            self.parents[xbar] = ybar
            if self.ranks[xbar] == self.ranks[ybar]:
                self.ranks[ybar] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize
        uf = UnionFind(n=n)

        for [u, v] in edges:
            uf.union(u, v)

        # Force path compression.
        for i in range(n):
            _ = uf.find(i)

        return len(set(uf.parents))
