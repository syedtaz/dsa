from typing import List
from itertools import product

point = tuple[int, int]


class UnionFind:
    parents: dict[point, point]
    ranks: dict[point, int]

    def __init__(self, n: int) -> None:
        self.parents = {(i, j): (i, j) for i, j in product(range(n), range(n))}
        self.ranks = {(i, j): 0 for i, j in product(range(n), range(n))}

    def find(self, x: point) -> point:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: point, y: point) -> None:
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
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        uf = UnionFind(n)
        points = sorted([(grid[i][j], i, j) for i, j in product(range(n), range(n))])
        acc = 0

        for height, x, y in points:
            acc = max(acc, height)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (
                    0 <= x + dx <= n - 1
                    and 0 <= y + dy <= n - 1
                    and grid[x + dx][y + dy] <= acc
                ):
                    uf.union((x, y), (x + dx, y + dy))

            if uf.find((0, 0)) == uf.find((n - 1, n - 1)):
                break

        return acc

s = Solution()
print(s.swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))