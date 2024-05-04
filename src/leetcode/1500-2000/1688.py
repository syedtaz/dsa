class Solution:
    def numberOfMatches(self, n: int) -> int:
        acc = 0

        while n != 1:
            acc += n // 2
            n = n // 2 if n % 2 == 0 else (n // 2) + 1

        return acc

    # def numberOfMatches(self, n: int) -> int:
    #     return n - 1