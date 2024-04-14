from collections import defaultdict
import heapq

class Leaderboard:
    state: dict[int, int]

    def __init__(self) -> None:
        self.state = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.state[playerId] += score

    def top(self, K: int) -> int:
        heap : list[int] = []

        for val in self.state.values():
            heapq.heappush(heap, val)
            if len(heap) > K:
                _ = heapq.heappop(heap)

        return sum(heap)

    def reset(self, playerId: int) -> None:
        _ = self.state.pop(playerId)
