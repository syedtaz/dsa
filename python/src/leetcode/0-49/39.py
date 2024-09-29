from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        A: list[list[int]] = []

        def f(i: int, acc: list[int]) -> None:
            if i == 0:
                A.append(acc)  # type: ignore
                return

            for cand in filter(lambda x: i - x >= 0, candidates):
                _ = f(i - cand, acc + [cand])

            return

        f(target, [])
        return [list(x) for x in A]
