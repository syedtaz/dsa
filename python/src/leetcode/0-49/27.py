from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1

        while True:
            if i > j:
                return i

            match nums[i] == val, nums[j] == val:
                case True, False:
                    nums[i] = nums[j]
                    i, j = i + 1, j - 1
                case True, True:
                    i, j = i, j - 1
                case _:
                    i, j = i + 1, j

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:

        i, j = 0, len(nums) - 1

        while True:
            if i > j:
                return i

            if nums[i] != val:
                i = i + 1
                continue

            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

            j = j - 1