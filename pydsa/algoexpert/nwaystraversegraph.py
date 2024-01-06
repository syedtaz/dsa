from functools import lru_cache

def numberOfWaysToTraverseGraph(width, height):
    @lru_cache
    def f(i, j):
        if i == width and j == height:
            return 1
        elif i == width:
            return f(i, j + 1)
        elif j == height:
            return f(i + 1, j)
        else:
            return f(i + 1, j) + f(i, j + 1)

    return f(1, 1)
