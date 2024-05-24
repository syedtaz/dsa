from typing import List

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:

#         def f(i: int, j: int) -> int:
#             if i > j:
#                 return i

#             if nums[i] == val and nums[j] != val:
#                 nums[i] = nums[j]
#                 return f(i + 1, j - 1)
#             elif nums[i] == val and nums[j] == val:
#                 return f(i, j - 1)
#             else:
#                 return f(i + 1, j)

#         return f(0, len(nums) - 1)


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
