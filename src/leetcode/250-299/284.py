from typing import Iterable

class PeekingIterator:
    el: int | None
    it: Iterable[int]

    def __init__(self, iterator: Iterable[int]) -> None:
        self.it = iterator
        self.el = self.it.next() # type: ignore


    def peek(self) -> int | None:
        return self.el


    def next(self) -> int | None:
        if self.el is None:
            return None

        temp = self.el
        self.el = self.it.next() # type: ignore
        if self.el <= -1000:
            self.el = None
        return temp


    def hasNext(self) -> bool:
        return self.el is not None