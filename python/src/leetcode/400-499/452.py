from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i = 0
        acc = 0

        while i < len(points):
            start, end = points[i]
            j = i + 1

            while j < len(points):
                if points[j][0] > end:
                    break

                nstart, nend = points[j]
                start, end = max(start, nstart), min(end, nend)
                j = j + 1

            acc += 1
            i = j

        return acc
