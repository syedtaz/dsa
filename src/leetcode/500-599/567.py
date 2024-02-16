from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        h = hash(frozenset(Counter(s1).items()))

        for i, j in zip(range(len(s2)), range(len(s2)+l)):
            if hash(frozenset(Counter(s2[i:j]).items())) == h:
                return True

        return False
