class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        representation = str(n)

        def monotonic(number: str, idx: int) -> bool:
            return all(
                [int(i) <= int(j) for (i, j) in zip(number[idx:], number[idx + 1 :])]
            )
