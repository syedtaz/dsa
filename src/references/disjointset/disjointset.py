parents: dict[int, int] = {}
ranks: dict[int, int] = {}


def make_set(x: int) -> None:
    assert x not in parents and x not in ranks
    parents[x] = x
    ranks[x] = 0


def find(x: int) -> int:
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    xbar = find(x)
    ybar = find(y)

    if ranks[xbar] > ranks[ybar]:
        parents[ybar] = xbar
    else:
        parents[xbar] = ybar
        if ranks[xbar] == ranks[ybar]:
            ranks[ybar] += 1
