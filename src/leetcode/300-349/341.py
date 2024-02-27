class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return True

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return 0

    def getList(self) -> list["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return [self]


class NestedIterator:
    stack: list[NestedInteger]

    def __init__(self, nestedList: list[NestedInteger]) -> None:
        self.stack = nestedList[::-1]

    def _unravel(self) -> None:
        if len(self.stack) == 0 or self.stack[-1].isInteger():
            return

        x = self.stack.pop()
        xs = x.getList()
        if len(xs) > 0:
            self.stack += xs[::-1]
        return self._unravel()

    def next(self) -> int:
        self._unravel()
        print(self.stack)
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self._unravel()
        return len(self.stack) > 0
