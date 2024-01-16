from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def f(i: int, j: int) -> int:


