from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map, length, acc = {0: -1}, 0, 0

        for i, x in enumerate(nums):
            acc += 1 if x == 1 else -1
            length = max(length, i - map.setdefault(acc, i))

        return length