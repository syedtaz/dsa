from typing import List
from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def priority(x: int, y: int) -> float:
            return -sqrt(x ** 2 + y ** 2)

        pqueue = []
        heapq.heapify(pqueue)

        for point in points:
            x, y = point[0], point[1]
            p = priority(x, y)

            if len(pqueue) == k:
                _ = heapq.heappushpop(pqueue, (p, x, y))
            else:
                heapq.heappush(pqueue, (p, x, y))

        return [[x, y] for _, x, y in pqueue] # type: ignore