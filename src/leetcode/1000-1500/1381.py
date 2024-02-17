class CustomStack:
    n: int
    stack: list[int]
    incr: list[int]

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.incr = []


    def push(self, x: int) -> None:
        if self.n == len(self.stack):
            return

        self.stack.append(x)
        self.incr.append(0)
        return


    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1

        if len(self.incr) > 1:
            self.incr[-2] += self.incr[-1]

        return self.stack.pop() + self.incr.pop()


    def increment(self, k: int, val: int) -> None:
        if len(self.stack) > 0:
          self.incr[min(k, len(self.stack)) - 1] += val
