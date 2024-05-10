from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum([1 if v % 2 == 1 else 0 for v in Counter(s).values()]) <= 1
