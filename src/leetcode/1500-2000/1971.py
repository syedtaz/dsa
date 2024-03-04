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

    def merge(self, x: int, y: int) -> None:
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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        uf = UnionFind(n)

        for edge in edges:
            uf.merge(edge[0], edge[1])

        return uf.parents[source] == uf.parents[destination]