class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        output, count = ["0" for _ in s], sum([1 if x == "1" else 0 for x in s]) - 1
        output[-1] = "1"
        i = 0

        while count > 0:
            output[i], count, i = "1", count - 1, i + 1

        return "".join(output)
