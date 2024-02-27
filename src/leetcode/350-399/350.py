from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        def f(i: int, j: int, acc: list[int]) -> list[int]:
            if i >= len(nums1) or j >= len(nums2):
                return acc

            if nums1[i] == nums2[j]:
                return f(i + 1, j + 1, acc + [nums1[i]])

            return f(i, j + 1, acc) if nums1[i] > nums2[j] else f(i + 1, j, acc)

        return f(0, 0, [])