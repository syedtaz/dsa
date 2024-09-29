from typing import List
from collections import deque

index = tuple[int, int]


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def find_gates(graph: list[list[int]]) -> list[index]:
            acc: list[index] = []

            for i, row in enumerate(graph):
                for j, val in enumerate(row):
                    if val == 0:
                        acc.append((i, j))

            return acc

        queue: deque[index] = deque(find_gates(rooms))
        m, n = len(rooms), len(rooms[0])

        while len(queue) > 0:
            (i, j) = queue.popleft()

            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni <= m - 1
                    and 0 <= nj <= n - 1
                    and rooms[ni][nj] == 2147483647
                ):
                    queue.append((ni, nj))
                    rooms[ni][nj] = rooms[i][j] + 1

        return
