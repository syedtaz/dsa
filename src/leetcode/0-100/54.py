from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def f(row: int, col: int, rows: int, cols: int, acc: list[int]) -> list[int]:
            if col <= cols:
                return f(row, col + 1, rows, cols, acc + [matrix[]])
