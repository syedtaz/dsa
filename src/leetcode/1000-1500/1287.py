from typing import List
from random import choice

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        def quickselect(i: int, j: int, k: int) -> int:
            if i == j:
                return arr[i]

            pivot = choice(arr[i:j])
            l, h, eq = 0, 0, 0

            for el in arr[i:j]:
                if el < pivot:
                    l += 1
                elif el > pivot:
                    h += 1
                else:
                    eq += 1

            if k < l:
                return quickselect(i, arr[i:j].index(pivot), k)
            elif k < l + eq:
                return pivot
            else:
                return quickselect(j, arr[j-1:i-1:-1].index(pivot) + 1, k - l - eq)