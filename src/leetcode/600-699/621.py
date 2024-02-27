import heapq
from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        temp = [(k, v) for k, v in Counter(tasks).items()]
        queue = [(idx, k, v) for idx, (k, v) in enumerate(temp)]
        heapq.heapify(queue)
        time = 0

        while len(queue) > 0:
            next, key, count = heapq.heappop(queue)
            if time <= next:
              time = next + 1
            if count > 1:
                heapq.heappush(queue, (time + n, key, count - 1)) # type: ignore

        return time

# s = Solution()
# print(s.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))