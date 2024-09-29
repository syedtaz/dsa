from typing import List

Point = tuple[int, int]


class UnionFind:
    parents: dict[Point, Point]
    ranks: dict[Point, int]

    def __init__(self, points: list[Point]) -> None:
        self.parents = {p: p for p in points}
        self.ranks = {p: 0 for p in points}

    def find(self, x: Point) -> Point:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: Point, y: Point) -> None:
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
    def countBattleships(self, board: List[List[str]]) -> int:
        points: list[Point] = []
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == "X":
                    points.append((i, j))

        uf = UnionFind(points)
        m, n = len(board), len(board[0])

        for x, y in points:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][y + dy] == 'X':
                    uf.union((x, y), (x + dx, y + dy))

        # Force path compression
        for p in points:
            _ = uf.find(p)

        return len(set(uf.parents.values()))
