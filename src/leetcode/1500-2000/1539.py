from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def search(i: int, j: int) -> int:
            if i > j:
                return i + k

            mid = i + (j - i) // 2

            return search(mid + 1, j) if arr[mid] - mid - 1 < k else search(i, mid - 1)

        return search(0, len(arr) - 1)
