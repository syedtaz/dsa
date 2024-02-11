import heapq

class SeatManager:
    idx: int
    pqueue : list[int]

    def __init__(self, n: int):
        self.idx = 1
        self.pqueue = []

    def reserve(self) -> int:
        if len(self.pqueue) > 0:
            return heapq.heappop(self.pqueue)
        self.idx += 1
        return self.idx - 1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.pqueue, seatNumber)