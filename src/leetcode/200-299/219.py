from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen : set[int] = set()

        for i in range(k):
            seen.add(nums[i])