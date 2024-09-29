from typing import List
from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map: dict[frozenset[tuple[str, int]], list[str]] = defaultdict(list)

        for word in strs:
            map[frozenset([(k, v) for k, v in Counter(word).items()])].append(word)

        return [v for v in map.values()]
