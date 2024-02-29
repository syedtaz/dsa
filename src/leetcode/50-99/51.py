from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def convert(positions: list[int]) -> list[str]:
            acc: list[str] = []

            for pos in positions:
                acc.append("".join(["." if i != pos else "Q" for i in range(n)]))

            return acc

        def f(state: list[int], idx: int) -> list[list[str]]:
            if idx >= n:
                return [convert(state)]

            acc: list[list[str]] = []

            for j in range(n):
                legal = True

                for i in range(idx):
                    if (
                        state[i] == j
                        or state[i] == j + idx - i
                        or state[i] == j - idx + i
                    ):
                        legal = False

                if legal:
                    next = state + [j]
                    acc += f(next, idx + 1)

            return acc

        return f([], 0)