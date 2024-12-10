class Solution:
    def checkRecord(self, s: str) -> bool:

        for a, b, c in zip(s, s[1:], s[2:]):
            if a == b == c == "L":
                return False

        return sum([1 if c == "A" else 0 for c in s]) < 2