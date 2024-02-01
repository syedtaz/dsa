from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat) - 1, len(mat[0]) - 1
        acc: list[int] = []

        def right(i: int, j: int) -> list[int]:
            if i == m and j == n:
                acc.append(mat[i][j])
                return acc

            if i < 0 and j <= n:
                return left(0, j)

            if j > n:
                return left(i + 2, n)

            acc.append(mat[i][j])
            return right(i - 1, j + 1)

        def left(i: int, j: int) -> list[int]:
            if i == m and j == n:
                acc.append(mat[i][j])
                return acc

            if j < 0 and i <= m:
                return right(i, j + 1)

            if i > m:
                return right(m, j + 2)

            acc.append(mat[i][j])
            return left(i + 1, j - 1)

        return right(0, 0)
