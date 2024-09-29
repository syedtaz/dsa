from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda x: x[0])
        return all([a <= b for ([_, a], [b, _]) in zip(intervals, intervals[1:])])
