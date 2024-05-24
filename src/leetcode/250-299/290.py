class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        mapping: dict[str, str] = {}
        revmapping: dict[str, str] = {}

        for a, b in zip(pattern, words):
            if (a in mapping and mapping[a] != b) or (
                b in revmapping and revmapping[b] != a
            ):
                return False
            mapping[a] = b
            revmapping[b] = a

        return True
