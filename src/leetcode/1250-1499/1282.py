from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        map: dict[int, list[int]] = defaultdict(list)

        for idx, k in enumerate(groupSizes):
            map[k].append(idx)

        acc: list[list[int]] = []
        for k, v in map.items():
            for lst in [v[i : i + k] for i in range(0, len(v), k)]:
                acc.append(lst)

        return acc
