class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1

        while True:
            if i > j:
                return 0

            if i == j:
                return 1

            if s[i] != s[j]:
                return j - i + 1

            character = s[i]

            while i < len(s) and s[i] == character:
                i += 1

            while j > 0 and s[j] == character:
                j -= 1
