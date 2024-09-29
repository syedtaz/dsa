from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        A: list[list[int]] = []

        def f(idx: int, count: int, acc: list[int]) -> None:
            if count == 0:
                A.append(acc)
                return

            for i in range(idx + 1, n + 1):
                _ = f(i, count - 1, acc + [i])

            return

        return A
