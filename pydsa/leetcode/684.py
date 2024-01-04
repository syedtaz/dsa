from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents : dict[int, int] = {}
        ranks : dict[int, int] = {}

        def make_set(x: int) -> None:
            if x not in parents:
              parents[x] = x
              ranks[x] = 0

        def find(x: int) -> int:
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x: int, y: int) -> bool:
            X, Y = find(x), find(y)

            if X == Y:
                return False

            if ranks[X] > ranks[Y]:
                parents[Y] = X
            else:
                parents[X] = Y
                if ranks[X] == ranks[Y]:
                    ranks[Y] += 1

            return True

        for edge in edges:
            l, r = edge[0], edge[1]
            make_set(l)
            make_set(r)

        for edge in edges:
            l, r = edge[0], edge[1]
            if not union(l, r):
                return edge

        return []

# s = Solution()
# print(s.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))