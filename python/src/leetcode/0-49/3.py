class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, acc = 0, 0
        seen: dict[str, int] = {}

        for idx, ch in enumerate(s):
            if ch in seen and seen[ch] >= i:
                i = seen[ch] + 1

            acc = max(acc, idx - i + 1)
            seen[ch] = idx

        return acc
