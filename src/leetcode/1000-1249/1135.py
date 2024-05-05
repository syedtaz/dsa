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

  def union(self, x: int, y: int) -> None:
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
  def minimumCost(self, n: int, connections: List[List[int]]) -> int:

    # Initialize
    uf = UnionFind(n=n)
    connections.sort(key=lambda x: x[2])
    weight = 0

    for conn in connections:
      u, v, w = conn[0] - 1, conn[1] - 1, conn[2]
      print(f"{u} and {v}")

      if uf.find(u) != uf.find(v):
        uf.union(u, v)
        weight += w

    # Force path compression
    for i in range(n):
      _ = uf.find(i)

    # Check if there are more than 1 component
    if len(set([i for i in uf.parents])) > 1:
      return -1

    return weight