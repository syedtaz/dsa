from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort()
        count = 0

        while total > 0:
            total -= capacity.pop()
            count += 1

        return count