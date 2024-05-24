graph = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]


def knows(a: int, b: int) -> bool:
    return graph[a][b] == 1


class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0

        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        for j in range(n):
            if j == candidate:
                continue
            if knows(candidate, j) or not knows(j, candidate):
                return -1

        return candidate
