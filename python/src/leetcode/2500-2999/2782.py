class CategoryHandler:
    def haveSameCategory(self, a: int, b: int) -> bool:
        return True


from typing import Optional


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

        # Same component
        if xbar == ybar:
            return None

        if self.ranks[xbar] > self.ranks[ybar]:
            self.parents[ybar] = xbar
        else:
            self.parents[xbar] = ybar
            if self.ranks[xbar] == self.ranks[ybar]:
                self.ranks[ybar] += 1


class Solution:
    def numberOfCategories(
        self, n: int, categoryHandler: Optional["CategoryHandler"]
    ) -> int:
        uf = UnionFind(n=n)
        assert categoryHandler is not None

        for a in range(n):
            for b in range(n):
                if a != b and categoryHandler.haveSameCategory(a, b):
                    uf.union(a, b)

        # Force path compression
        for i in range(n):
            _ = uf.find(i)

        return len(set(uf.parents))
