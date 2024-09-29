from sortedcontainers import SortedList

interval = tuple[int, int]

class MyCalendar:
    intervals : SortedList

    def __init__(self) -> None:
        self.intervals = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.intervals.bisect_right((start, end))

        if (idx > 0 and self.intervals[idx - 1][1] > start):
            return False

        if (idx < len(self.intervals) and self.intervals[idx][0] < end):
            return False

        self.intervals.add((start, end))
        return True