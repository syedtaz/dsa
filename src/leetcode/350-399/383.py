from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cmag = Counter(magazine)

        for k in ransomNote:
            if k not in cmag or cmag[k] < 1:
                return False
            cmag[k] -= 1

        return True