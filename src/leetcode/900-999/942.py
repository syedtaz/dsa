from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        acc : list[int] = []
        low, high = 0, len(s)

        for x in s:
            if x == 'I':
                acc.append(low)
                low += 1
            else:
                acc.append(high)
                high -= 1

        acc.append(low)
        return acc