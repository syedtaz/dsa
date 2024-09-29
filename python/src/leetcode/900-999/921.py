class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        i, lbraces, count = 0, 0, 0

        while True:
            if i >= len(s):
                return lbraces + count
            if s[i] == "(":
                i, lbraces = i + 1, lbraces + 1
                continue
            if lbraces > 0:
                i, lbraces = i + 1, lbraces - 1
            else:
                i, count = i + 1, count + 1
