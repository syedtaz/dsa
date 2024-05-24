class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mapping = {k: idx for idx, k in enumerate(keyboard)}
        current = keyboard[0]
        cost = 0
        for k in word:
            cost += abs(mapping[k] - mapping[current])
            current = k

        return cost
