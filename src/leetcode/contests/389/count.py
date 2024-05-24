class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        seen = 0

        for char in s:
            if char == c:
                seen += 1

        return seen + (seen * (seen - 1)) // 2
