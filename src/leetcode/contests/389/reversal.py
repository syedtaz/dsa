class Solution:
    def isSubstringPresent(self, s: str) -> bool:

        seen: set[str] = set()

        for (a, b) in zip(s, s[1:]):
            if a == b or f"{b}{a}" in seen:
                return True
            seen.add(f"{a}{b}")

        return False