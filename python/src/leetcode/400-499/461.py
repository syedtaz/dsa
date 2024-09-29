class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        acc = 1 if z else 0

        while z := z & (z - 1):
            acc += 1

        return acc
