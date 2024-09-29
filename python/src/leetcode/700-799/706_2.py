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
