from typing import List
from collections import Counter

index = tuple[int, int]


class DisjointSet:
    parents: dict[index, index]
    ranks: dict[index, int]

    def __init__(self, points: list[index]) -> None:
        self.parents = {}
        self.ranks = {}
        for idx in points:
            self.parents[idx] = idx
            self.ranks[idx] = 0

    def find(self, x: index) -> index:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: index, y: index) -> None:
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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def find_land(graph: list[list[int]]) -> list[index]:
            acc: list[index] = []

            for i, row in enumerate(graph):
                for j, val in enumerate(row):
                    if val == 1:
                        acc.append((i, j))
            return acc

        lands = find_land(grid)
        disjointset = DisjointSet(lands)
        diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for cur in lands:
            i, j = cur
            for di, dj in diffs:
                neighbor = (i + di, j + dj)
                if neighbor in disjointset.parents:
                    disjointset.union(cur, neighbor)

        for x in lands:
            _ = disjointset.find(x)

        candidate = Counter(disjointset.parents.values()).most_common(1)
        if len(candidate) == 0:
            return 0

        _, area = candidate[0]
        return area
