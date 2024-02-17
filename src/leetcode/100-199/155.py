class MinStack:
    stack : list[tuple[int, int]]

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
            return None

        m, _ = self.stack[-1]
        self.stack.append((min(m, val), val))
        return


    def pop(self) -> None:
        _ = self.stack.pop()


    def top(self) -> int:
        _, v = self.stack[-1]
        return v


    def getMin(self) -> int:
        m, _ = self.stack[-1]
        return m