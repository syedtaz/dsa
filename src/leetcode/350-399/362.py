from collections import deque


class HitCounter:
    state: deque[int]

    def __init__(self):
        self.state = deque([])

    def hit(self, timestamp: int) -> None:
        self.state.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while len(self.state) > 0 and self.state[0] <= timestamp - 300:
            _ = self.state.popleft()

        return len(self.state)