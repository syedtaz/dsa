from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        acc : list[list[int]] = []

        def f(choices: list[int], r: int) -> None:
            if r == n:

