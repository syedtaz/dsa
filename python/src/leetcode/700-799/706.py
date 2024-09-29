from typing import Callable
from random import randint
from enum import Enum


def hashf(a: int, x: int, m: int) -> int:
    return ((a * x) >> (32 - m)) & 0xFFFFFFFF

def define_hashf(m: int) -> Callable[[int], int]:
    a = randint(1, m)

    while a % 2 != 1:
        a = randint(1, m)

    return lambda x: hashf(a, x, m)

class Result(Enum):
    present = 0
    absent = 1
    full = 2


def search(
    x: int, m: int, bins: list[int], hfunc: Callable[[int], int]
) -> tuple[Result, int]:
    for i in range(m):
        idx = hfunc(x) ^ i
        if bins[idx] == x:
            return (Result.present, idx)
        elif bins[idx] == -1:
            return (Result.absent, -1)

    return (Result.full, -1)


class MyHashMap:
    bins: list[tuple[int, int]]
    m: int
    f: Callable[[int], int]

    def __init__(self) -> None:
        self.m = 10
        self.bins = [(-1, -1) for _ in range(2 ** self.m)]
        self.f = define_hashf(self.m)

    def _search(self, key: int) -> tuple[Result, int, int]:

        for i in range(self.m):
            idx = self.f(key) ^ i
            k_prime, v_prime = self.bins[idx]
            if k_prime == key:
                return (Result.present, idx, v_prime)
            elif k_prime == -1:
                return (Result.absent, idx, -1)

        return (Result.full, 0, -1)


    def put(self, key: int, value: int) -> None:
        match self._search(key):
            case (Result.absent, i, _) | (Result.present, i, _):
                self.bins[i] = (key, value)
                return
            case (Result.full, _, _):




    def get(self, key: int) -> int:
        match self._search(key):
            case (Result.absent, _, _) | (Result.full, _, _):
                return -1
            case (Result.present, _, v):
                return v


    def remove(self, key: int) -> None: