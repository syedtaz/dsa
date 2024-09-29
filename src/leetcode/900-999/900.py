from typing import List

class RLEIterator:
    val: int | None
    count: int | None
    lst: list[int]
    pos: int

    def __init__(self, encoding: List[int]) -> None:
        if len(encoding) == 0:
            self.val, self.count, self.lst, self.pos = None, None, [], 0
            return

        self.pos = 0
        self.lst = encoding
        self._find_next()

    def _find_next(self) -> None:
        if self.pos >= len(self.lst):
            self.val = None
            self.count = None
            return

        count = self.lst[self.pos]
        val = self.lst[self.pos + 1]
        self.pos += 2

        if count == 0:
            self._find_next()
            return

        self.count = count
        self.val = val

    def next(self, n: int) -> int:

        while n > 0:

          if self.val is None:
              return -1

          assert self.count is not None and self.val is not None
          temp = self.val
          reduction = min(n, self.count)
          self.count -= reduction

          if self.count <= 0:
              self._find_next()

          n -= reduction

        return temp
