from typing import List
from itertools import product


class UnionFind:
    parents: dict[str, str]
    rank: dict[str, int]

    def __init__(self, strings: list[str]) -> None:
        self.parents = {s: s for s in strings}
        self.ranks = {s: 0 for s in strings}

    def find(self, x: str) -> str:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def get_set(self, x: str) -> list[str]:
        xbar = self.find(x)
        return [y for y in self.parents if self.parents[y] == xbar]

    def union(self, x: str, y: str) -> None:
        xbar = self.find(x)
        ybar = self.find(y)

        if xbar == ybar:
            return None

        if self.ranks[xbar] > self.ranks[ybar]:
            self.parents[ybar] = xbar
        else:
            self.parents[xbar] = ybar
            if self.ranks[xbar] == self.ranks[ybar]:
                self.ranks[ybar] += 1


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        def define_set(word_list: list[list[str]]) -> UnionFind:
            words: set[str] = set()

            for xs in word_list:
                words = words.union(set(xs))

            return UnionFind(list(words))

        uf = define_set(word_list=synonyms)

        for words in synonyms:
            for a, b in zip(words, words[1:]):
                uf.union(a, b)

        # Force path compression
        for i in uf.parents.keys():
            _ = uf.find(i)

        new_text = [
            [x] if x not in uf.parents else uf.get_set(x) for x in text.split(" ")
        ]
        acc: list[str] = new_text[0]
        for words in new_text[1:]:
            res: list[str] = []
            for a, b in product(acc, words):
                res.append(f"{a} {b}")
            acc = res

        acc.sort()
        return acc
