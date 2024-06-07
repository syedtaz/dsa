from functools import lru_cache


def levenshteinDistance(str1, str2):
    @lru_cache
    def f(i, j):
        if i == 0:
            return j
        elif j == 0:
            return i
        else:
            insert = 1 + f(i - 1, j)
            delete = 1 + f(i, j - 1)
            swap = (1 if str1[i - 1] != str2[j - 1] else 0) + f(i - 1, j - 1)
            return min(insert, delete, swap)

    return f(len(str1), len(str2))
