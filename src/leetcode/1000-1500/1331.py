from typing import List
from itertools import groupby

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        f = {x : idx + 1 for idx, (x, _) in enumerate(groupby(sorted(arr)))}
        return [f[x] for x in arr]