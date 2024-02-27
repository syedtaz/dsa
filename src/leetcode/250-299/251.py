from typing import List


class Vector2D:
    i: int
    j: int
    vec: list[list[int]]

    def __init__(self, vec: List[List[int]]) -> None:
        self.i, self.j, self.vec = 0, 0, vec

    def _set_next(self) -> None:
        while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
            self.j = 0
            self.i += 1

    def next(self) -> int:
        x = self.vec[self.i][self.j]
        self.j += 1
        self._set_next()
        return x

    def hasNext(self) -> bool:
        self._set_next()
        if self.i >= len(self.vec):
            return False
        return True
