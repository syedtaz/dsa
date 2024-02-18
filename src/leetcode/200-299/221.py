from typing import List
from functools import cache

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def f(idx: int, size: int) -> int:
            if size <= 0:
                return 0

