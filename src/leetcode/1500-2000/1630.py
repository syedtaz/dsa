from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:

        def is_sequence(i: int, j: int) -> bool:
            lst = sorted(nums[i:j + 1])
            if len(lst) <= 1:
                return True

            diff = lst[0] - lst[1]
            return all([j - i == diff for i, j in zip(lst, lst[1:])])

        return [is_sequence(i, j) for i, j in zip(l, r)]