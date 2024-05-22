from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def at_most(c: int) -> int:

            counts : dict[int, int] = defaultdict(int)
            i, acc = 0, 0

            for j, ch in enumerate(nums):

                counts[ch] += 1

                while len(counts) > c:

                    counts[nums[i]] -= 1

                    if counts[nums[i]] == 0:
                        _ = counts.pop(nums[i])

                    i += 1

                acc += j - i + 1

            return acc

        return at_most(k) - at_most(k - 1)
