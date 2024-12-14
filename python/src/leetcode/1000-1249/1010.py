from typing import List
from collections import Counter, defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashtbl = Counter([x % 60 for x in time])
        acc = 0

        seen: dict[int, set[int]] = defaultdict(set)

        for k, v in hashtbl.items():
            if (k2 := (60 - k) % 60) in hashtbl and k2 not in seen[k]:
                if k2 != k:
                    acc += v * hashtbl[k2]
                    seen[k].add(k2)
                    seen[k2].add(k)
                else:
                    acc += (v * (v - 1)) // 2
                    seen[k].add(k)

        return acc