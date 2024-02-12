class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for ch in s:
            length += length * (int(ch) - 1) if ch.isdigit() else 1

        for ch in reversed(s):
            k %= length
            if k == 0 and ch.isalpha():
                return ch

            length = length // int(ch) if ch.isdigit() else length - 1