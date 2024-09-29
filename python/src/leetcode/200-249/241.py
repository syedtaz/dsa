from typing import List, Callable
from operator import add, mul, sub


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def fsplit(expr: str) -> tuple[int, Callable[[int, int], int]]:
            for idx, char in enumerate(expr):
                match char:
                    case "-":
                        return idx, sub
                    case "*":
                        return idx, mul
                    case "+":
                        return idx, add
                    case _:
                        continue

            assert False

        def f(expr: str) -> list[int]:
            if expr.isdigit():
                return [int(expr)]

            idx, op = fsplit(expr)
            left = f(expr[:idx])
            right = f(expr[idx + 1 :])

            res: list[int] = []
            for i in left:
                for j in right:
                    res.append(op(i, j))

            return res


s = Solution()
print(s.diffWaysToCompute("1-1+2"))
