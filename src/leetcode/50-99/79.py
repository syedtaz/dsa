from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        if m * n < len(word):
            return False

        def search(i: int, j: int, k: int) -> bool:
            if k >= len(word):
                return True

            if not ((0 <= i <= m - 1) and (0 <= j <= n - 1)):
                return False

            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#"
            res = False

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if search(i + di, j + dj, k + 1):
                    res = True
                    break

            board[i][j] = temp
            return res

        for i in range(m):
            for j in range(n):
                if search(i, j, 0):
                    return True

        return False