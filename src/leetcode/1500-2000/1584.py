from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        class DisjointSet:
            parents: dict[tuple[int, int], tuple[int, int]]
            ranks: dict[tuple[int, int], int]

            def __init__(self):
                self.parents = {}
                self.ranks = {}

            def make_set(self, x: tuple[int, int]) -> None:
                self.parents[x] = x
                self.ranks[x] = 0

            def find(self, x: tuple[int, int]) -> tuple[int, int]:
                if x != self.parents[x]:
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

            def union(self, x: tuple[int, int], y: tuple[int, int]) -> None:
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

        pts = [(x[0], x[1]) for x in points]

        edges: list[tuple[tuple[int, int], tuple[int, int], int]] = []
        for idx, (xa, ya) in enumerate(pts):
            for xb, yb in pts[idx + 1 :]:
                edges.append(((xa, ya), (xb, yb), abs(xa - xb) + abs(ya - yb)))
        edges.sort(key=lambda x: x[2])

        dset = DisjointSet()
        for pt in pts:
            dset.make_set(pt)

        f: list[int] = []
        for u, v, w in edges:
            if len(f) == len(points) - 1:
                break
            if dset.find(u) != dset.find(v):
                dset.union(u, v)
                f.append(w)

        return sum(f)


s = Solution()
print(s.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
