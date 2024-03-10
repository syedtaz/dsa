from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m, n = len(board), len(board[0])

        def search(i: int, j: int, k: int, word: str) -> bool:
            if k >= len(word):
                return True

            if not (0 <= i <= m - 1 and 0 <= j <= n - 1):
                return False

            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#"
            res = False

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if search(i + di, j + dj, k + 1, word):
                    res = True
                    break

            board[i][j] = temp
            return res

        def search_wrapper(word: str) -> bool:
            for i in range(m):
                for j in range(n):
                    if search(i, j, 0, word):
                        return True
            return False

        return [word for word in words if search_wrapper(word)]