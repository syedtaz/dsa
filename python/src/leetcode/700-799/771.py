class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashset: set[str] = set(list(jewels))
        count = 0

        for k in stones:
            if k in hashset:
                count += 1

        return count
