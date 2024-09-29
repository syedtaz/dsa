class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        m = num // 2

        while m * m > num:
            m = (m * m + num) // (2 * m)

        return m * m - num == 0