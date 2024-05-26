from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) <= 1:
            return [idx for idx in range(len(heights))]

        pref = heights[-1]
        for idx in reversed(range(len(heights))):
            pref = max(pref, heights[idx])
            heights[idx] = pref

        return [
            idx for idx, (l, r) in enumerate(zip(heights, heights[1:])) if l > r
        ] + [len(heights) - 1]
