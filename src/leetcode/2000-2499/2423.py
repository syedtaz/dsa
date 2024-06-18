from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counts = Counter(Counter(word).values())
        if len(counts) == 1:
            key, val = counts.popitem()
            return key == 1 or val == 1

        if len(counts) == 2:
            k1 = min(counts)
            k2 = max(counts)
            return (k1 == 1 and counts[k1] == 1) or (k1 + 1 == k2 and counts[k2] == 1)

        return False