from typing import List, Callable

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms : int = 1
        end : int = intervals[0][1]

        for interval in intervals[1:]:







