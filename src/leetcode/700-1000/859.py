from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        cs, cg = Counter(s), Counter(goal)
        if cs != cg:
            return False

        diff = sum([1 if a != b else 0 for a, b in zip(s, goal)])

        if diff == 0:
            return any([v >= 2 for v in cs.values()])

        return diff == 2 or diff == 1