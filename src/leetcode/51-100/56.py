from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack : list[list[int]] = []

        for interval in intervals:
            x, y = interval[0], interval[1]
            if len(stack) == 0:
                stack.append([x, y])
            else:
                topx : int = stack[-1][0]
                topy : int = stack[-1][1]
                if x <= topy:
                    left = x if x < topx else topx
                    right = y if y > topy else topy
                    _ = stack.pop()
                    stack.append([left, right])
                else:
                    stack.append([x, y])

        return stack