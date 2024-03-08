from typing import List
from collections import Counter


class UnionFind:
    parents: list[int]
    ranks: list[int]
    counts: list[int]

    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]
        self.counts = [1 for _ in range(n)]

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        xbar = self.find(x)
        ybar = self.find(y)

        if xbar == ybar:
            return None

        self.counts[xbar] = self.counts[ybar] = self.counts[xbar] + self.counts[ybar]

        if self.ranks[xbar] > self.ranks[ybar]:
            self.parents[ybar] = xbar
        else:
            self.parents[xbar] = ybar
            if self.ranks[xbar] == self.ranks[ybar]:
                self.ranks[ybar] += 1

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n=n)
        counter : Counter[int] = Counter()

        for edge in edges:
            u, v = edge[0], edge[1]
            uf.union(u, v)
            counter[u], counter[v] = counter[u] + 1, counter[v] + 1

        for i in range(n):
            _ = uf.find(i)

        groups = set([i for i in uf.parents])

        for i in range(n):
            if uf.counts[uf.find(i)] != counter[i] + 1:
                groups.discard(i)

        return len(groups)






