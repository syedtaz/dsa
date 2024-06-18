from typing import List
import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        seen : set[int] = set()
        heap : list[int] = []

        for item in nums:
            if item in seen:
                continue

            seen.add(item)
            heapq.heappush(heap, item)

            if len(seen) > 3:
                rm = heapq.heappop(heap)
                seen.remove(rm)

        if len(seen) <= 2:
            return max(seen)

        return heapq.heappop(heap)