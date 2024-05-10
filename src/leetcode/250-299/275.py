from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        lo, hi = 0, len(citations) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            remaining = len(citations) - mid

            if citations[mid] == remaining:
                return citations[mid]
            elif citations[mid] < remaining:
                lo = mid + 1
            else:
                hi = mid - 1

        return len(citations) - lo
