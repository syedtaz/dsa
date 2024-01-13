from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def f(i: int, j: int) -> int:
            match (i == m, j == n):
                case True, True:
                    return 1
                case False, False:
                    return f(i, j + 1) + f(i + 1, j)
                case True, False:
                    return f(i, j + 1)
                case False, True:
                    return f(i + 1, j)
                case _:
                    # refute
                    raise Exception

        return f(1, 1)
