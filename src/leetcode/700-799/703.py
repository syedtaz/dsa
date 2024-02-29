from typing import List
import heapq

class KthLargest:
    heap : list[int]
    k : int

    def __init__(self, k: int, nums: List[int]) -> None:

        self.heap = [x for x in nums]
        heapq.heapify(self.heap)
        self.k = k

        while len(self.heap) > k:
            _ = heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]