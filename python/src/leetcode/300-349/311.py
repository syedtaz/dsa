from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

        for i, row in enumerate(mat1):
            for j, val in enumerate(row):
                if val == 0:
                    continue

                acc = 0

                for row2 in mat2:
                    acc += val * row2[j]

                result[i][j] = acc

        return result
