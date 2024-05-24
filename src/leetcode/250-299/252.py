from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda x: x[0], reverse=True)

        init = intervals.pop()
        end = init[1]

        while len(intervals) > 0:
            next = intervals.pop()
            nstart, nend = next[0], next[1]

            if nstart < end:
                return False

            end = nend

        return True
