class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        acc = 0

        while target > startValue:
            acc += 1
            if target % 2 == 0:
                target //= 2
            else:
                target += 1

        return acc + startValue - target
