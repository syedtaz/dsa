from typing import List
from collections import defaultdict

Point = tuple[int, int]


def invert(tbl: dict[Point, Point]) -> list[list[Point]]:
    inverted: dict[Point, list[Point]] = defaultdict(list)

    for k, v in tbl.items():
        inverted[v].append(k)

    return [v for v in inverted.values()]


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
            return

        if self.ranks[xbar] > self.ranks[ybar]:
            self.parents[ybar] = xbar
        else:
            self.parents[xbar] = ybar
            if self.ranks[xbar] == self.ranks[ybar]:
                self.ranks[ybar] += 1


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        points: list[Point] = []
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == "O":
                    points.append((i, j))

        uf = UnionFind(points)
        m, n = len(board), len(board[0])

        # Create sets
        for i, j in points:
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + di < m and 0 <= j + dj < n and board[i + di][j + dj] == "O":
                    uf.union((i, j), (i + di, j + dj))

        # Force path compression.
        for p in points:
            _ = uf.find(p)

        sets = invert(uf.parents)

        for choices in sets:
            if all(
                [i != m - 1 and j != n - 1 and i != 0 and j != 0 for i, j in choices]
            ):
                for i, j in choices:
                    board[i][j] = "X"
