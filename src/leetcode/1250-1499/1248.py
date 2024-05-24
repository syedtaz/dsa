from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(c: int) -> int:
            i, acc = 0, 0

            for j, num in enumerate(nums):
                c -= num % 2

                while c < 0:
                    c += nums[i] % 2
                    i += 1

                acc += j - i

            return acc

        return at_most(k) - at_most(k - 1)
