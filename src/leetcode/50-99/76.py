from collections import Counter

type pair = tuple[int, int]

def fmap(bound: pair | None, cand: pair) -> pair:
    if bound is None:
        return cand

    l, r = bound
    a, b = cand
    return cand if b - a < r - l else bound

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        state = Counter(t)
        acc : tuple[int, int] | None = None
        i = 0
        remaining = len(t)

        for j, ch in enumerate(s):

            if ch in state:
                state[ch] -= 1
                if state[ch] <= 0:
                    remaining -= 1

            while remaining == 0:
                acc = fmap(acc, (i, j))
                rm_ch = s[i]

                if rm_ch in state:
                    state[rm_ch] += 1
                    if state[rm_ch] > 0:
                        remaining += 1

                i += 1

        if acc is None:
            return ""

        l, r = acc
        return s[l:r]

