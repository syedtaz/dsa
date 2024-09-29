from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        def f(i: int, acc: int) -> int:
            # print(f"{i}, {acc}")
            if i == len(nums) - 1:
                return acc

            M = [i + nums[j] for j in range(nums[i] + 1) if i + j < len(nums)]
            # print(M)
            m = max(M)
            return f(m, acc + 1) if m < len(nums) - 1 else f(len(nums) - 1, acc + 1)

        return f(0, 0)


# s = Solution()
# print(s.jump([1,1,2,1,1]))
