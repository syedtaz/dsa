from typing import List
from collections import Counter
from string import punctuation


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.translate(str.maketrans(punctuation, " " * len(punctuation)))
        ban = set([x.lower() for x in banned])
        counts = Counter([x.lower() for x in words.split() if x.lower() not in ban])
        return counts.most_common(1)[0][0]