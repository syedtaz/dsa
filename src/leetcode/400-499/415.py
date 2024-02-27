class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        def f(i: int, acc: int) -> int:
            if i >= len(num1) and i >= len(num2):
                return acc

            if i >= len(num1):
                return acc + int(num2[:len(num2) - i]) * (10 ** i)

            if i >= len(num2):
                return acc + int(num1[:len(num1) - i]) * (10 ** i)

            return f(i + 1, acc + )