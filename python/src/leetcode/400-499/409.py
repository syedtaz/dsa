from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        evens = sum([v // 2 for _, v in counts.items() if v >= 2]) * 2
        odds = 1 if any([v % 2 == 1 for v in counts.values()]) else 0
        return evens + odds
