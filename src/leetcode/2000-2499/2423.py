from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter: dict[str, int] = Counter(word)
        vs = sorted(set(counter.values()))

        if len(vs) != 2:
            return False

        keys = [k for k, v in counter.items() if v == vs[0]]
        if len(keys) > 1:
            return False

        return True
