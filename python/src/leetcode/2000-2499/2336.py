from sortedcontainers import SortedSet # type: ignore

class SmallestInfiniteSet:
    state : SortedSet

    def __init__(self) -> None:
        self.state = SortedSet(list(range(1,1001)))

    def popSmallest(self) -> int:
        return self.state.pop(0)

    def addBack(self, num: int) -> None:
        self.state.add(num)
