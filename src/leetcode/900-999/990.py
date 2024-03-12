from typing import List


class UnionFind:
    parents: dict[str, str]
    ranks: dict[str, int]

    def __init__(self, strings: set[str]) -> None:
        self.parents = {s: s for s in strings}
        self.ranks = {s: 0 for s in strings}

    def find(self, x: str) -> str:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: str, y: str) -> None:
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
    def equationsPossible(self, equations: List[str]) -> bool:

        def parse(x: str) -> tuple[str, str, bool]:
            return x[0], x[-1], x[1] == "="

        symbols: set[str] = set()

        for eq in equations:
            symbols.add(eq[0])
            symbols.add(eq[-1])

        uf = UnionFind(strings=symbols)
