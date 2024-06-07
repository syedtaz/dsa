from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtbl : dict[int, int] = {}
        for i, num in enumerate(nums):
            if (j := hashtbl.get(target - num)) is not None:
                return [i, j]
            hashtbl[num] = i
        assert False