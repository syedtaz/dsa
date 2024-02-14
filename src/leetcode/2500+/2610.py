from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)

        def iter(counter: Counter[int]) -> list[int]:
            acc: list[int] = []
            stack: list[int] = []
            for k in counter.keys():
                acc.append(k)
                counter[k] -= 1
                if counter[k] == 0:
                    stack.append(k)

            for k in stack:
                counter.pop(k)

            return acc

        mat: list[list[int]] = []

        while len(c) > 0:
            mat.append(iter(c))
        return mat
