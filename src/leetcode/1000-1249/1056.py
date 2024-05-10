class Solution:
    def confusingNumber(self, n: int) -> bool:
        repr = str(n)
        acc = ['' for _ in range(len(repr))]
        mapping = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

        for i, v in enumerate(repr):
            if v in {"2", "3", "4", "5", "7"}:
                return False
            acc[len(repr) - 1 - i] = mapping[v]

        return n != int("".join(acc))