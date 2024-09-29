from typing import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins: dict[int, int] = defaultdict(int)
        losses: dict[int, int] = defaultdict(int)

        for [w, l] in matches:
            wins[w] += 1
            losses[l] += 1

        winners = sorted([k for k in wins.keys() if k not in losses])
        losers = sorted([k for k, v in losses.items() if v == 1])
        return [winners, losers]
