from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates.pop()
        x2, y2 = coordinates.pop()
        delx, dely = x2 - x1, y2 - y1

        if delx == 0:
            return all([lst[1] == y1 for lst in coordinates])

        m = dely / delx
        b = y1 - (m * x1)

        return all([(m * lst[0] + b == lst[1]) for lst in coordinates])
