from typing import List


class Solution:
    # Sorting
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any([a == b for a, b in zip(nums, nums[1:])])

    # Hashing
    def containsDuplicate2(self, nums: List[int]) -> bool:
        seen : set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False