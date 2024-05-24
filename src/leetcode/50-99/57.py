from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        acc: list[list[int]] = []
        added = False

        for interval in intervals:
            if added:
                acc.append(interval)

            if newInterval[0] <= interval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
            else:
                acc.append(newInterval)

            if newInterval[1] >= interval[0]:
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                acc.append(newInterval)
                acc.append(interval)

        return acc
