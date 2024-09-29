from typing import Generator


class State:
    a: int
    b: int
    c: int
    i: int
    nexti: int

    def __init__(self) -> None:
        self.a, self.b, self.c = 2, 3, 5
        self.nexti = 1
        self.i = 1

    def _update(self) -> None:
        match min(self.a, self.b, self.c):
            case self.a:
                self.nexti = self.a
                self.a *= 2
            case self.b:
                self.nexti = self.b
                self.b *= 3
            case self.c:
                self.nexti = self.c
                self.c += 5
            case _:
                assert False

    def __iter__(self) -> Generator[int, None, None]:
        cur = self.nexti
        self._update()
        while self.nexti == cur:
            self._update()
        self.i += 1

        yield cur


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        iterator = State()
        retval = None

        for _ in range(n):
            retval = next(iterator.__iter__())

        assert retval is not None
        return retval
