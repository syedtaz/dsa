from typing import List
from functools import cache


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def modify(x: int, idx: int) -> int:
            return x | (1 << idx)

        def check(x: int, idx: int) -> int:
            return (x >> idx) & 1

        def convert(x: int) -> tuple[int, ...]:
            temp = [candidates[i] for i in range(len(candidates)) if check(x, i)]
            temp.sort()
            return tuple(temp)

        @cache
        def f(choices: int, k: int) -> list[tuple[int, ...]]:
            if k == 0:
                return [convert(choices)]

            acc: list[tuple[int, ...]] = []
            for idx in range(len(candidates)):
                if not check(choices, idx) and candidates[idx] <= k:
                    acc += f(modify(choices, idx), k - candidates[idx])

            return [x for x in set(acc)]

        return [list(x) for x in f(0, target)]
