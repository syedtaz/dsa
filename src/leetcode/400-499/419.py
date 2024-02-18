from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        acc, m, n = 0, len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                pos =
