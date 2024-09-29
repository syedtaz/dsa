from collections import deque


class RecentCounter:
    state: deque[int]

    def __init__(self) -> None:
        self.state = deque([])

    def _clear(self, t: int) -> int:
        target = t - 3000

        while len(self.state) > 0 and self.state[0] < target:
            _ = self.state.popleft()

        return len(self.state)

    def ping(self, t: int) -> int:
        self.state.append(t)
        return self._clear(t)
