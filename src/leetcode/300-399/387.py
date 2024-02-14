class Solution:
    def firstUniqChar(self, s: str) -> int:
        positions : list[int | None] = [None] * 26

        for idx, ch in enumerate(s):
            i = ord(ch) % 26
            if positions[i] is None:
                positions[i] = idx + 1
                continue

            if positions[i] > 0: # type: ignore
                positions[i] *= -1 # type: ignore

        cands = [x for x in positions if x is not None and x > 0]
        return -1 if len(cands) == 0 else min(cands) - 1