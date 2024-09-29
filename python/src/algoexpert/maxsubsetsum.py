from functools import lru_cache


def maxSubsetSumNoAdjacent(array: list[int]) -> int:
    n = len(array)
    if n == 0:
        return 0

    @lru_cache
    def recurrence(i: int) -> int:
        if i >= n:
            return 0

        v = array[i]
        yes = v + recurrence(i + 2)
        no = recurrence(i + 1)
        return max(yes, no)

    return recurrence(0)
