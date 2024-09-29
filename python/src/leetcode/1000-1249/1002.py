from typing import List
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        acc = Counter(words[0])

        for word in words:
            acc &= Counter(word)

        result: list[str] = []

        for key, count in acc.items():
            result += [key] * count

        return result
