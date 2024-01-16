import math

class MyHashSet:
    t : list[int | None]
    size : int

    def __init__(self):
        self.size = 2
        self.t = [None] * self.size

    def hash(self, v: int) -> int:
        return v % self.size

    def rebalance(self) -> None:
        self.size = 2 ** (int(math.log2(self.size)) + 1)
        new_t = [None] * self.size

        for v in filter(lambda x: x is not None, self.t):
            new_t[self.hash(v)] = v # type: ignore

        self.t = new_t
        return None

    def search(self, idx: int, v: int) -> tuple[bool, int]:
        cur = idx

        while cur < self.size and self.t[cur] != v:
            cur += 1

        return (False, cur) if (cur > self.size or self.t[cur] != v) else (True, cur)

    def add(self, key: int) -> None:
        idx = self.hash(key)
        if self.t[idx] is None:
            self.t[idx] = key
            return

        cur = idx
        while  and self.t[cur] is not None:
            cur += 1

        if cur == self.size:
            self.rebalance()
            self.add(key)
        else:
            self.t[cur] = key
            return


    def remove(self, key: int) -> None:
        idx = self.hash(key)
        if self.t[idx] is None:
            return None

        found, nidx = self.search(idx, key)
        if not found:
            return None

        self.t[nidx] = None
        return None


    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        if self.t[idx] is None:
            return False
        v, _ = self.search(idx, key)
        return v