class Solution:
    def isHappy(self, n: int) -> bool:
        def f(x: int) -> int:
            acc, k = 0, x
            while k > 0:
                d = k % 10
                acc += d * d
                k //= 10
            return acc

        def cycle(turtle: int, hare: int) -> bool:
            return (
                True
                if hare == 1
                else (False if turtle == hare else cycle(f(turtle), f(f(hare))))
            )

        return cycle(n, f(n))
