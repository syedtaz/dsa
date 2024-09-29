from functools import cache


def numberOfWaysToMakeChange(n: int, denoms: list[int]) -> int:
    @cache
    def f(n: int, i: int) -> int:
        if i == 0:
            return 0
        elif n == 0:
            return 1
        elif denoms[i - 1] > n:
            return f(n, i - 1)
        else:
            return f(n, i - 1) + f(n - denoms[i - 1], i)

    return f(n, len(denoms))
