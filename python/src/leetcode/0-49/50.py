class Solution:
    def myPow(self, x: float, n: int) -> float:
        def f(acc: float, v: float, k: int) -> float:
            if k == 0:
                return acc
            return (
                f(acc, v * v, k // 2) if k % 2 == 0 else f(acc * v, v * v, (k - 1) // 2)
            )

        return f(1.0, x, n) if n >= 0 else 1 / f(1.0, x, abs(n))
