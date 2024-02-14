from functools import cache

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        @cache
        def f(x: frozenset[int]) -> list[list[int]]:
            if len(x) == 0:
                return []

            ans : list[list[int]] = []
            for num in x:
                next = f(frozenset(x.difference(set([num]))))
                if len(next) == 0:
                    ans.append([num])
                else:
                    for z in next:
                      ans.append([num] + z)
            return ans

        return f(frozenset(nums))

# s = Solution()
# print(s.permute(nums=[0,1]))