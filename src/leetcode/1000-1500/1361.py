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

        if xbar == ybar or ybar != y:
            raise RuntimeError

        if self.ranks[xbar] >= self.ranks[ybar]:
            self.parents[ybar] = xbar
        else:
            self.parents[xbar] = ybar
            if self.ranks[xbar] == self.ranks[ybar]:
                self.ranks[ybar] += 1


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:

        uf = UnionFind(n)

        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            for x in [l, r]:
                if x != -1:
                    try:
                        uf.merge(i, x)
                    except RuntimeError:
                        return False

        return len([i for i in range(n) if uf.find(i) == i]) == 1