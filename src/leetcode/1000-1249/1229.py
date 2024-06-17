from typing import List


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        i, j = 0, 0

        while i < len(slots1) and j < len(slots2):
            [s1, e1] = slots1[i]
            [s2, e2] = slots2[j]

            s, e = max(s1, s2), min(e1, e2)

            if e - s >= duration:
                return [s, s + duration]

            if e1 < e2:
                i += 1
            else:
                j += 1

        return []