class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def strip_zeros(number: str) -> str:
            while len(number) > 1 and number[0] == "0":
                number = number[1:]
            return number

        def equalize(lst: list[int], amount: int) -> None:
            for _ in range(amount):
                lst.append(0)

        a = [int(strip_zeros(x)) for x in version1.split(".")]
        b = [int(strip_zeros(x)) for x in version2.split(".")]

        if len(a) > len(b):
            equalize(b, len(a) - len(b))
        elif len(b) > len(a):
            equalize(a, len(b) - len(a))

        for left, right in zip(a, b):
            if left > right:
                return 1
            if right > left:
                return -1

        return 0
