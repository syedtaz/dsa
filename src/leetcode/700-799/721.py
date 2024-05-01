from typing import List
from collections import defaultdict

pair = tuple[str, str]


class UnionFind:
    parents: dict[pair, pair]
    ranks: dict[pair, int]

    def __init__(self, n: list[pair]) -> None:
        self.parents = {p: p for p in n}
        self.ranks = {p: 0 for p in n}

    def find(self, x: pair) -> pair:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: pair, y: pair) -> None:
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accs: list[list[pair]] = []

        for acc in accounts:
            name = acc[0]
            result = [(name, x) for x in acc[1:]]
            accs.append(result)

        flattened = [item for acc in accs for item in acc]
        uf = UnionFind(flattened)

        for acc in accs:
            if len(acc) <= 1:
                continue

            for a, b in zip(acc, acc[1:]):
                uf.union(a, b)

        rev_parents: dict[pair, list[pair]] = defaultdict(list)

        for item in flattened:
            rev_parents[uf.find(item)].append(item)

        final: list[list[str]] = []

        for vs in rev_parents.values():
            name = vs[0][0]
            results = sorted(set([x for _, x in vs]))
            final.append([name] + results)

        return final
