class Solution:
    def smallestNumber(self, pattern: str) -> str:
        acc = ""
        low, high = 1, len(pattern) + 1

        for x in pattern:
            if x == 'I':
                acc += str(low)
                low += 1
            else:
                acc += str(high)
                high -= 1

        return acc