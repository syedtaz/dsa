from typing import List

class FirstUnique:
    __slots__ = ("uniq", "dup")
    uniq: dict[int, None]
    dup: set[int]

    def __init__(self, nums: List[int]):
        self.uniq = {}
        self.dup = set()

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return next(x for x in self.uniq) if self.uniq else -1

    def add(self, value: int) -> None:
        if value in self.uniq:
            del self.uniq[value]
            self.dup.add(value)
            return

        if value not in self.dup:
          self.uniq[value] = None
