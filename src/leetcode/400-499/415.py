class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_s = [int(x) for x in num1]
        num2_s = [int(x) for x in num2]

        longer = num1_s if len(num1_s) >= len(num2_s) else num2_s
        shorter = num2_s if longer == num1_s else num1_s
        power = acc = carry = 0

        while shorter:
            a, b = shorter.pop(), longer.pop()
            total = a + b + carry

            if total > 9:
                carry = total // 10
                total = total % 10

            acc += total * (10 ** power)
            power += 1

