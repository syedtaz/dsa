from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        A = jobDifficulty

        memo = [[-1 for _ in range(len(A))] for _ in range(d)]
        memo[d-1] = A

        for i in range(d-1,-1,-1):
            cur = memo[i]
            print(cur)

        return 0


        # @cache
        # def f(i: int, j: int) -> int:
        #     if i >= len(jobDifficulty) and j <= 0:
        #         return 0

        #     if i >= len(jobDifficulty) and j > 0:
        #         return -1

        #     acc = 0
        #     maximums = [acc := max(acc, x) for x in jobDifficulty[i:]]
        #     results : list[int] = []

        #     for k, v in enumerate(maximums):
        #         res = f(i + 1 + k, j - 1)
        #         if res != -1:
        #             results.append(res + v)

        #     return min(results) if len(results) > 0 else -1

        # return f(0, d)

s = Solution()
print(s.minDifficulty(jobDifficulty=[1,1,1], d = 3))