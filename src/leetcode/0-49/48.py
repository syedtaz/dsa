from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        def transpose(k: int) -> None:
            if k == N:
                return None
            for i in range(k, N):
                a, b = matrix[k][i], matrix[i][k]
                matrix[k][i] = b
                matrix[i][k] = a

            transpose(k + 1)
            return None

        def flip() -> None:
            for k in range(N):
                i, j = 0, N - 1
                while i < j:
                    matrix[k][i], matrix[k][j] =  matrix[k][j], matrix[k][i]
                    i, j = i + 1, j - 1
            return None


        transpose(0)
        flip()
        return
