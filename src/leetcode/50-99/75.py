from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def sort(idx: int, low: int, high: int) -> None:
            if idx > high:
                return

            match nums[idx]:
                case 0:
                    nums[idx], nums[low] = nums[low], nums[idx]
                    return sort(idx + 1, low + 1, high)
                case 1:
                    return sort(idx + 1, low, high)
                case 2:
                    nums[idx], nums[high] = nums[high], nums[idx]
                    return sort(idx, low, high - 1)
                case _:
                    assert False

        sort(0, 0, len(nums) - 1)
        return None