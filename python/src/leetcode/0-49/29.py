class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def f(r: int, b: int) -> int:
            q = 0
            while r >= 0:
                r, q = r - b, q + 1
            return q

        if divisor < 0:
            return -f(dividend, abs(divisor))

        if dividend < 0:
            ans = f(abs(dividend), divisor)


s = Solution()
print(s.divide(9, 3))
