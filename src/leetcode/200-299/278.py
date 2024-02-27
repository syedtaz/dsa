def isBadVersion(version: int) -> bool:
    return version > 0


class Solution:
    def firstBadVersion(self, n: int) -> int:

        def binary_search(i: int, j: int) -> int:
            if i > j:
                return i

            mid = i + (j - i) // 2
            result = isBadVersion(mid)

            return binary_search(i, mid - 1) if result else binary_search(mid + 1, j)

        return binary_search(1, n)
