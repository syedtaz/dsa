import random
from sys import maxsize
from typing import Callable


class UniversalHash:
    M = 20
    f: Callable[[int], int]

    def __init__(self) -> None:

        chain = [self._generate() for _ in range(5)]

        def h(x: int) -> int:
            acc = x
            for f in chain:
                acc = f(acc)
            return acc

        self.f = h

    def _generate(self) -> Callable[[int], int]:
        a = random.randint(1, maxsize)
        a = a + 1 if a % 2 != 1 else a
        return lambda x: ((x * a) % maxsize) >> (64 - 20)


class MyHashMap:
    hashfunc: UniversalHash
    bins: list[list[tuple[int, int]]]

    def __init__(self) -> None:
        self.hashfunc = UniversalHash()
        self.bins = [[(-1, -1)]] * 1048576

    def put(self, key: int, value: int) -> None:
        idx = self.hashfunc.f(key) - 1

        if self.bins[idx][0] == (-1, -1):
            self.bins[idx] = [(key, value)]
            return

        for i, (k, _) in enumerate(self.bins[idx]):
            if k == key:
                self.bins[idx][i] = (k, value)
                return

        self.bins[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self.hashfunc.f(key) - 1

        for k, v in self.bins[idx]:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        idx = self.hashfunc.f(key) - 1
        candidate = None

        for i, (k, _) in enumerate(self.bins[idx]):
            if k == key:
                candidate = i

        if candidate is not None:
            self.bins[idx].pop(candidate)

        if len(self.bins[idx]) == 0:
            self.bins[idx].append((-1, -1))

