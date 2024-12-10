class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def add(a: str, b: str, carr: int) -> tuple[int, int]:
            s = int(a) + int(b) + carr
            return (s // 10, s % 10)

