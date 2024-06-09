from heapq import heappush, heappop, heappushpop


class MedianFinder:
    top: list[int] # Min heap
    bottom: list[int] # Max heap

    def __init__(self) -> None:
        self.top, self.bottom = [], []


    def addNum(self, num: int) -> None:
        heappush(self.top, -1 * heappushpop(self.bottom, -1 * num))

        if len(self.bottom) < len(self.top):
            heappush(self.bottom, -1 * heappop(self.top))

    def findMedian(self) -> float:
        if len(self.bottom) > len(self.top):
            return self.bottom[0] * -1

        return  ((self.bottom[0] * -1) + (self.top[0])) / 2