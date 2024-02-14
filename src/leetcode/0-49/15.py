from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        hashtbl : dict[int, set[int]] = defaultdict(set)

        def twoSum(i: int, target: int) -> list[tuple[int, int]]:
            acc : list[tuple[int, int]] = []

            for idx, num in enumerate(nums[i:]):

                if num not in hashtbl:
                    hashtbl[num] = set([idx])
                elif idx not in hashtbl[num]:
                    hashtbl[num].add(idx)

                t = target - num
                if t != num and t in hashtbl:
                    for item in hashtbl[t]:
                      acc.append((idx, item))

            return acc

        ans : set[tuple[int, int, int]] = set()

        for i, j in zip(range(len(nums)), range(1, len(nums))):
            res = twoSum(j, -nums[i])

            for (a, b) in res:
                if a == i or b == i:
                    continue

                x = sorted([i, a, b])
                ans.add((x[0], x[1], x[2]))

        return [list(x) for x in ans]

s = Solution()
print(s.threeSum(nums = [-1,0,1,2,-1,-4]))