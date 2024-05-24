from typing import List

point = tuple[int, int]


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def construct(grid: list[list[int]]) -> tuple[point, point, set[point]]:
            start = None
            end = None
            points: set[point] = set()

            for i, row in enumerate(grid):
                for j, value in enumerate(row):
                    match value:
                        case 0:
                            points.add((i, j))
                        case 1:
                            start = (i, j)
                        case 2:
                            end = (i, j)
                        case _:
                            continue

            assert start is not None and end is not None
            return (start, end, points)

        start, end, points = construct(grid)

        def search(
            position: point, end: point, seen: set[point], points: set[point]
        ) -> int:
            if position == end and len(seen) == len(points) - 1:
                return 1

            seen.add(position)
