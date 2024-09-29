from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        x = Counter(s)

        for v in x.values():
            if v > (len(s) // 2 if len(s) % 2 == 0 else (len(s) // 2) + 1):
                return ""

        queue: list[tuple[int, str]] = [(-v, k) for k, v in x.items()]
        heapq.heapify(queue)
        acc: str = ""
        prev: str = queue[-1][1]

        while len(queue) > 0:
            count, key = heapq.heappop(queue)

            if key == prev:
                return ""

            if count > 1:
                queue.append((count - 1, key))

            acc += key
            prev = key

        return acc
