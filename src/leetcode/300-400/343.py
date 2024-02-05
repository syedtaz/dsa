# class Solution:
#     def integerBreak(self, n: int) -> int:

#         @cache
#         def f(k: int) -> int:
#             if k <= 3:
#                 return k

#             return max([i * f(k - i) for i in range(1, k + 1)])

#         return f(n) if n > 3 else n - 1


class Solution:
    def integerBreak(self, n: int) -> int:

        if n <= 3:
            return n - 1

        f: list[int] = [0, 1, 2, 3] + [0] * (n - 2)
        for k in range(4, n + 1):
            f[k] = max([i * f[k - i] for i in range(1, k + 1)])

        return f[n]
