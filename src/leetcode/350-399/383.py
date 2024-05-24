from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note, mag = Counter(ransomNote), Counter(magazine)

        for k, v in note.items():
            if k not in mag:
                return False
            mag[k] -= v
            if mag[k] < 0:
                return False

        return True
