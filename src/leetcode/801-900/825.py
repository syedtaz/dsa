from typing import List
from itertools import groupby

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        lst = [(k, len(list(v))) for k, v in groupby(ages)]
        lst.sort(reverse=True)
        req = 0
        print(lst)

        for idx, (older, c1) in enumerate(lst):
            for (younger, c2) in ages[idx+1:]:
                if younger <= (0.5 * older) + 7 or (older > 100 and younger < 100):
                    break
                req += c2 if older != younger else c1

        return req