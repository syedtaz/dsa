from collections import deque


class MovingAverage:
    queue: deque[int]
    size: int
    total: int

    def __init__(self, size: int) -> None:
        self.queue = deque([])
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            x = self.queue.popleft()
            self.total -= x

        self.queue.append(val)
        self.total += val
        return self.total / len(self.queue)
