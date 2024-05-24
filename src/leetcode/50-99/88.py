from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        def f(i: int, j: int, k: int) -> None:
            if k < 0:
                return

            if j >= 0 and nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                return f(i - 1, j - 1, k)

            nums1[i] = nums2[k]
            return f(i - 1, j, k - 1)

        return f(m + n - 1, m - 1, n - 1)
