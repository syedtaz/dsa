from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odds = 0
        evens = 0
        even = True

        while n:
            if n & 1:
                if even:
                    evens += 1
                else:
                    odds += 1
            n = n >> 1
            even = not even

        return [evens, odds]