import sys

type Game = list[int]


def disturbance(g: Game) -> int:
    return sum([1 if a == b else 0 for (a, b) in zip(g, g[1:])])


def solve(g: Game) -> int:
    left = 1
    right = len(g) - 2

    while left < right:
        if (g[left - 1] == g[left] or g[right] == g[right + 1]) and g[right] != g[left]:
            g[left], g[right] = g[right], g[left]

        left += 1
        right -= 1

    return disturbance(g)


count = int(sys.stdin.readline())
for _ in range(count):
    _ = sys.stdin.readline()
    res = solve([int(x) for x in sys.stdin.readline().strip().split()])
    print(res)
