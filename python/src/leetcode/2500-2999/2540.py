from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        common = None

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common = nums1[i] if common is None else min(common, nums1[i])

            if nums1[i] >= nums2[j]:
                i = i + 1
                continue

            j = j + 1

        return -1 if common is None else common
