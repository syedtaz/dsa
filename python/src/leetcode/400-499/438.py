from typing import List
from collections import Counter, deque


class Window:
    letters: deque[str]
    state: Counter[str]
    cap: int

    def __init__(self, target: str) -> None:
        self.state = Counter(target)
        self.letters = deque()
        self.cap = len(target)

    def feed(self, letter: str) -> bool:
        if letter in self.state:
            self.state[letter] -= 1

        if len(self.letters) == self.cap:
            last = self.letters.popleft()

            if last in self.state:
                self.state[last] += 1

        self.letters.append(letter)
        return all([v == 0 for v in self.state.values()])


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        acc: list[int] = []
        window = Window(p)

        for idx, ch in enumerate(s):
            if window.feed(ch):
                acc.append(idx - len(p) + 1)

        return acc
