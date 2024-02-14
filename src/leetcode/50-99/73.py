from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int | None]]) -> None:
        m, n = len(matrix), len(matrix[0])

        def set() -> None:
            for i, j in ((i, j) for i in range(m) for j in range(n)):
                if matrix[i][j] is None:
                    matrix[i][j] = 0

        def replace(i: int, j: int):
            matrix[i][j] = None

            for k in range(m):
                if matrix[k][j] is not None and matrix[k][j] == 0:
                    replace(k, j)
                    break
                else:
                    matrix[k][j] = None

            for k in range(n):
                if matrix[i][k] is not None and matrix[i][k] == 0:
                    replace(i, k)
                    break
                else:
                    matrix[i][k] = None

        def f(i: int) -> None:
            if i >= m or i >= n:
                return

            for j in range(m):
                if matrix[j][i] is not None and matrix[j][i] == 0:
                    replace(j, i)

            for j in range(n):
                if matrix[i][j] is not None and matrix[i][j] == 0:
                    replace(i, j)

            return f(i + 1)

        f(0)
        set()
        return