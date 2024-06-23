from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        return sorted(counts, key = lambda x: (-counts[x], x))[:k]
