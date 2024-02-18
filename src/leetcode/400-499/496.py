from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        map: dict[int, int] = {}
        stack : list[int] = []

        for i in range(len(nums2)):
            el = nums2[i]

            while len(stack) > 0 and stack[-1] <= el:
                x = stack.pop()
                map[x] = el

            if len(stack) == 0 or stack[-1] >= el:
                stack.append(el)


        while len(stack) > 0:
            x = stack.pop()
            map[x] = -1

        return [map[x] for x in nums1]