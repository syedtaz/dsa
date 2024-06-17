from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counts : dict[str, int] = defaultdict(int)
        bulls = cows = 0

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cows += 1 if counts[s] < 0 else 0
                cows += 1 if counts[g] > 0 else 0
                counts[s] += 1
                counts[g] -= 1

        return f"{bulls}A{cows}B"