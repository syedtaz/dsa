from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        acc : list[int] = []
        for a, b in zip(nums, nums[n:]):
            acc.append(a)
            acc.append(b)
        return acc
