from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        acc = set(mat[0])

        for row in mat[1:]:
            acc = acc.intersection(set(row))

        return min(acc) if len(acc) > 0 else -1
