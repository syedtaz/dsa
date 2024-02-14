from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def set(x: int, idx: int) -> int:
            return x | (1 << idx)

        def check(x: int, idx: int) -> int:
            return (x >> idx) & 1

        def f()

