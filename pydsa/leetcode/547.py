from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents: dict[int, int] = {}
        ranks: dict[int, int] = {}

        def make_set(x: int) -> None:
            assert x not in parents and x not in ranks
            parents[x] = x
            ranks[x] = 0

        def find(x: int) -> int:
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x : int, y: int) -> None:
            x2 = find(x)
            y2 = find(y)

            if parents[x2] == parents[y2]:
                return

            if ranks[x2] > ranks[y2]:
                parents[y2] = x2
            else:
                parents[x2] = y2
                if ranks[x2] == ranks[y2]:
                    ranks[y2] += 1

        for i in range(len(isConnected)):
            make_set(i)

        n = len(isConnected)

        for i in range(0, n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        for i in range(0, n):
            _ = find(i)

        return len(set(parents.values()))

# s = Solution()
# print(s.findCircleNum(isConnected=[[1,0,0,1],
#                                    [0,1,1,0],
#                                    [0,1,1,1],
#                                    [1,0,1,1]]))