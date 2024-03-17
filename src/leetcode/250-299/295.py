from collections import defaultdict
from bisect import insort_left

class MedianFinder:
    hashtbl : dict[int, int]
    keys: list[int]
    length: int
    median: int
    acc: int

    def __init__(self) -> None:
        self.hashtbl = defaultdict(int)
        self.keys = []
        self.length = 0
        self.median = -1


    def addNum(self, num: int) -> None:
        if num not in self.hashtbl:
          self.hashtbl[num] += 1
          insort_left(self.keys, num)
        else:
          self.hashtbl[num] += 1

        self.length += 1

    def findMedian(self) -> float:

