from typing import List
from functools import cache
from collections import defaultdict
from sys import maxsize

class WordDistance:
    map: dict[str, list[int]]

    def __init__(self, wordsDict: List[str]) -> None:
        self.map = defaultdict(list)

        for idx, word in enumerate(wordsDict):
            self.map[word].append(idx)

        for word in self.map:
            self.map[word].sort()

    @cache
    def shortest(self, word1: str, word2: str) -> int:
        a, i = self.map[word1], 0
        b, j = self.map[word2], 0
        acc = maxsize

        while True:
            diff = abs(a[i] - b[j])
            acc = min(acc, diff)

            if i == len(a) - 1 and j == len(b) - 1:
                return acc

            if i <= j and i != len(a) - 1:
                i = i + 1
                continue

            if j != len(b) - 1:
                j = j + 1