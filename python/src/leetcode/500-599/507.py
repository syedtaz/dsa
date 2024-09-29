from math import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        bound = int(sqrt(num))
        acc = 1

        for i in range(2, bound + 1):
            if num % i == 0:
                acc += i
                acc += num // i
                if acc > num:
                    return False

        return acc == num
