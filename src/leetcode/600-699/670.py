class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        hashtbl = {x: i for i, x in enumerate(nums)}

        for i, x in enumerate(nums):
            for j in range(9, x, -1):
                if hashtbl.get(j, -1) > i:
                    nums[i], nums[hashtbl[j]] = nums[hashtbl[j]], nums[i]
                    return int("".join([str(x) for x in nums]))
        return num
