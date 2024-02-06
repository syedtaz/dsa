from typing import List
from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        left = set([k for k, v in Counter(words1).items() if v == 1])
        right = set([k for k, v in Counter(words2).items() if v == 1])

        return len(left.intersection(right))