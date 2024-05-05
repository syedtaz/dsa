import heapq
from math import sqrt

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def moves(a: int, b: int) -> list[tuple[int, int]]:
            return [
                (a + 2, b + 1),
                (a + 2, b - 1),
                (a - 2, b + 1),
                (a + 2, b - 1),
                (a + 1, b + 2),
                (a + 1, b - 2),
                (a - 1, b + 2),
                (a - 1, b - 2),
            ]

        def distance(a: int, b: int) -> float:
            return sqrt((x - a) ** 2 + (y - b) ** 2)

        queue : list[tuple[float, int, int, int]] = [(distance(0, 0), 0, 0, 0)]
        seen : set[tuple[int, int]] = set()

        while len(queue) > 0:
            _, level, a, b = heapq.heappop(queue)
            if a == x and b == y:
                return level

            for move in moves(a, b):
                if move not in seen:
                    nx, ny = move
                    heapq.heappush(queue, ((distance(nx, ny), level + 1, nx, ny)))

            seen.add((a, b))

        raise Exception
