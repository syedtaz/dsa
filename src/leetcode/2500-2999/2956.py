from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = set(nums1), set(nums2)
        acc1, acc2 = 0, 0
        for v in nums1:
            if v in c2:
                acc1 += 1

        for v in nums2:
            if v in c1:
                acc2 += 1

        return [acc1, acc2]
